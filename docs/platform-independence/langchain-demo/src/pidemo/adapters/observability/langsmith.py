"""Opt-in hosted tracing via LangSmith (proprietary service).

langchain-core always installs the langsmith SDK and enables tracing whenever
LANGSMITH_TRACING=true is in the environment. This adapter overrides that
globally so the application's TRACING setting is the only switch.
"""

import langsmith


def configure_langsmith(enabled: bool, api_key: str | None = None) -> None:
    if not enabled:
        langsmith.configure(enabled=False)
        return
    if not api_key:
        raise ValueError("TRACING=langsmith requires LANGSMITH_API_KEY")
    langsmith.configure(enabled=True, client=langsmith.Client(api_key=api_key))
