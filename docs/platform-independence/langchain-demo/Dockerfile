# syntax=docker/dockerfile:1
FROM python:3.13-slim-trixie AS build
COPY --from=ghcr.io/astral-sh/uv:0.13.9 /uv /bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0
# Optional provider extra to bake in, e.g. --build-arg EXTRA=openai
ARG EXTRA=""
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-install-project ${EXTRA:+--extra $EXTRA}
COPY README.md ./
COPY src ./src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable ${EXTRA:+--extra $EXTRA}

FROM python:3.13-slim-trixie
RUN useradd --create-home --uid 10001 app \
    && mkdir -p /app/traces && chown app:app /app/traces
COPY --from=build /app/.venv /app/.venv
ENV PATH=/app/.venv/bin:$PATH HOST=0.0.0.0 PORT=8000 TRACE_LOG_PATH=/app/traces/llm.jsonl
WORKDIR /app
USER app
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz')"]
CMD ["pidemo"]
