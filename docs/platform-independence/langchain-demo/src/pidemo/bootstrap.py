"""Composition root: the only place that turns configuration into concrete
model and observability implementations."""

from langchain.chat_models import init_chat_model
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.language_models import BaseChatModel

from pidemo.adapters.observability.langsmith import configure_langsmith
from pidemo.adapters.observability.local_log import JsonlTraceHandler
from pidemo.config import Settings
from pidemo.domain.summarize import Summarizer


def build_chat_model(settings: Settings) -> BaseChatModel:
    kwargs = {"temperature": settings.llm_temperature}
    if settings.llm_base_url:
        kwargs["base_url"] = settings.llm_base_url
    return init_chat_model(
        settings.llm_model, model_provider=settings.llm_provider, **kwargs
    )


def build_callbacks(settings: Settings) -> list[BaseCallbackHandler]:
    api_key = settings.langsmith_api_key
    configure_langsmith(
        enabled=settings.tracing == "langsmith",
        api_key=api_key.get_secret_value() if api_key else None,
    )
    if settings.tracing == "local":
        return [JsonlTraceHandler(settings.trace_log_path)]
    return []


def build_summarizer(settings: Settings) -> Summarizer:
    return Summarizer(build_chat_model(settings), callbacks=build_callbacks(settings))
