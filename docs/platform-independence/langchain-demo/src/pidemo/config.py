"""Runtime configuration, read from environment variables (and an optional .env)."""

from pathlib import Path
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Any provider known to langchain's init_chat_model, as long as its
    # integration package is installed (see the optional extras in pyproject).
    llm_provider: str = "ollama"
    llm_model: str = "llama3.2:1b"
    llm_base_url: str | None = None
    llm_temperature: float = 0.0

    # none: no tracing. local: JSONL file. langsmith: hosted LangSmith (opt-in).
    tracing: Literal["none", "local", "langsmith"] = "local"
    trace_log_path: Path = Path("traces/llm.jsonl")
    langsmith_api_key: SecretStr | None = None

    host: str = "127.0.0.1"
    port: int = 8000
