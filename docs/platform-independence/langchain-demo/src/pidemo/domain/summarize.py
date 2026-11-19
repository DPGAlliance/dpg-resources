"""Summarization use case. Depends only on langchain-core abstractions."""

from collections.abc import Sequence
from dataclasses import dataclass

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableConfig

PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are a precise summarizer. Summarize the user's text in at "
                "most {max_sentences} sentences. Reply with the summary only."
            ),
        ),
        ("human", "{text}"),
    ]
)


class EmptyTextError(ValueError):
    pass


@dataclass(frozen=True)
class Summary:
    text: str
    source_chars: int


class Summarizer:
    def __init__(
        self, model: BaseChatModel, callbacks: Sequence[BaseCallbackHandler] = ()
    ) -> None:
        self._chain = PROMPT | model | StrOutputParser()
        self._config = RunnableConfig(run_name="summarize", callbacks=list(callbacks))

    async def summarize(self, text: str, max_sentences: int = 3) -> Summary:
        if not text.strip():
            raise EmptyTextError("text must not be blank")
        output = await self._chain.ainvoke(
            {"text": text, "max_sentences": max_sentences}, config=self._config
        )
        return Summary(text=output.strip(), source_chars=len(text))
