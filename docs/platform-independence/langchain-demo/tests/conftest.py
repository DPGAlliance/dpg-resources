import langsmith
import pytest
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage

from pidemo.config import Settings


def fake_model(*replies: str) -> GenericFakeChatModel:
    return GenericFakeChatModel(
        messages=iter(
            AIMessage(
                content=r,
                usage_metadata={
                    "input_tokens": 7,
                    "output_tokens": 3,
                    "total_tokens": 10,
                },
            )
            for r in replies
        )
    )


def make_settings(**overrides) -> Settings:
    # Ignore any developer .env so tests are hermetic.
    return Settings(_env_file=None, **overrides)


@pytest.fixture(autouse=True)
def reset_langsmith_global():
    yield
    langsmith.configure(enabled=None, client=None)
