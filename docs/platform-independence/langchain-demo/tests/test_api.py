from conftest import fake_model
from fastapi.testclient import TestClient

from pidemo.api import create_app
from pidemo.domain.summarize import Summarizer


class FailingSummarizer:
    async def summarize(self, text, max_sentences=3):
        raise ConnectionError("model unreachable")


def test_healthz():
    with TestClient(create_app(Summarizer(fake_model()))) as client:
        assert client.get("/healthz").json() == {"status": "ok"}


def test_summarize():
    with TestClient(create_app(Summarizer(fake_model("Short.")))) as client:
        resp = client.post(
            "/summarize", json={"text": "Long text.", "max_sentences": 1}
        )
    assert resp.status_code == 200
    assert resp.json() == {"summary": "Short.", "source_chars": 10}


def test_blank_text_is_422():
    with TestClient(create_app(Summarizer(fake_model()))) as client:
        assert client.post("/summarize", json={"text": "  "}).status_code == 422


def test_model_failure_is_502():
    with TestClient(create_app(FailingSummarizer())) as client:
        resp = client.post("/summarize", json={"text": "x"})
    assert resp.status_code == 502
    assert "unreachable" not in resp.text
