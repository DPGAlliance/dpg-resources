"""HTTP interface. Knows the use case, not the model behind it."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from pidemo.bootstrap import build_summarizer
from pidemo.config import Settings
from pidemo.domain.summarize import EmptyTextError, Summarizer

logger = logging.getLogger(__name__)


class SummarizeRequest(BaseModel):
    text: str = Field(min_length=1, max_length=50_000)
    max_sentences: int = Field(default=3, ge=1, le=10)


class SummarizeResponse(BaseModel):
    summary: str
    source_chars: int


def create_app(summarizer: Summarizer | None = None) -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        app.state.summarizer = summarizer or build_summarizer(Settings())
        yield

    app = FastAPI(title="pidemo", lifespan=lifespan)

    @app.get("/healthz")
    async def healthz() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/summarize")
    async def summarize(body: SummarizeRequest, request: Request) -> SummarizeResponse:
        try:
            result = await request.app.state.summarizer.summarize(
                body.text, max_sentences=body.max_sentences
            )
        except EmptyTextError as e:
            raise HTTPException(status_code=422, detail=str(e)) from e
        except Exception as e:
            logger.exception("model call failed")
            raise HTTPException(status_code=502, detail="model call failed") from e
        return SummarizeResponse(summary=result.text, source_chars=result.source_chars)

    return app


app = create_app()


def main() -> None:
    settings = Settings()
    uvicorn.run("pidemo.api:app", host=settings.host, port=settings.port)
