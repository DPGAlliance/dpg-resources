import pytest
from conftest import make_settings
from langchain_ollama import ChatOllama
from langsmith.utils import tracing_is_enabled

from pidemo.adapters.observability.local_log import JsonlTraceHandler
from pidemo.bootstrap import build_callbacks, build_chat_model


def test_defaults_to_self_hosted_ollama():
    settings = make_settings()
    assert settings.llm_provider == "ollama"
    assert settings.tracing == "local"


def test_builds_provider_from_config():
    model = build_chat_model(
        make_settings(llm_model="qwen2.5:0.5b", llm_base_url="http://ollama:11434")
    )
    assert isinstance(model, ChatOllama)
    assert model.model == "qwen2.5:0.5b"
    assert model.base_url == "http://ollama:11434"


def test_unknown_provider_is_rejected():
    with pytest.raises(ValueError):
        build_chat_model(make_settings(llm_provider="no-such-vendor"))


def test_local_tracing_uses_jsonl_and_keeps_langsmith_off(tmp_path, monkeypatch):
    # Even a stray LANGSMITH_TRACING=true must not enable hosted tracing.
    monkeypatch.setenv("LANGSMITH_TRACING", "true")
    callbacks = build_callbacks(make_settings(trace_log_path=tmp_path / "t.jsonl"))
    assert [type(c) for c in callbacks] == [JsonlTraceHandler]
    assert not tracing_is_enabled()


def test_no_tracing():
    assert build_callbacks(make_settings(tracing="none")) == []
    assert not tracing_is_enabled()


def test_langsmith_requires_api_key():
    with pytest.raises(ValueError, match="LANGSMITH_API_KEY"):
        build_callbacks(make_settings(tracing="langsmith"))


def test_langsmith_opt_in_enables_tracing(monkeypatch):
    monkeypatch.delenv("LANGSMITH_TRACING", raising=False)
    callbacks = build_callbacks(
        make_settings(tracing="langsmith", langsmith_api_key="lsv2-test")
    )
    assert callbacks == []
    assert tracing_is_enabled()
