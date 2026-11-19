import asyncio

import pytest
from conftest import fake_model

from pidemo.domain.summarize import PROMPT, EmptyTextError, Summarizer


def test_returns_stripped_summary():
    summarizer = Summarizer(fake_model("  A short summary.  "))
    result = asyncio.run(summarizer.summarize("Some long text."))
    assert result.text == "A short summary."
    assert result.source_chars == len("Some long text.")


def test_rejects_blank_text():
    summarizer = Summarizer(fake_model("unused"))
    with pytest.raises(EmptyTextError):
        asyncio.run(summarizer.summarize("   "))


def test_prompt_carries_text_and_limit():
    messages = PROMPT.format_messages(text="hello world", max_sentences=2)
    assert "at most 2 sentences" in messages[0].content
    assert messages[1].content == "hello world"
