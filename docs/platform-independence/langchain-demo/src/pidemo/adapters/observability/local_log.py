"""Vendor-neutral tracing: one JSON line per chat model call.

Records metadata only (provider, model, latency, token counts, sizes), never
prompt or completion text.
"""

import json
import threading
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import LLMResult


class JsonlTraceHandler(BaseCallbackHandler):
    def __init__(self, path: Path) -> None:
        self._path = path
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._runs: dict[UUID, dict[str, Any]] = {}

    def on_chat_model_start(
        self,
        serialized: dict[str, Any],
        messages: list[list[BaseMessage]],
        *,
        run_id: UUID,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        metadata = metadata or {}
        self._runs[run_id] = {
            "start": time.perf_counter(),
            "provider": metadata.get("ls_provider"),
            "model": metadata.get("ls_model_name"),
            "input_chars": sum(len(m.text) for batch in messages for m in batch),
        }

    def on_llm_end(self, response: LLMResult, *, run_id: UUID, **kwargs: Any) -> None:
        run = self._runs.pop(run_id, None)
        if run is None:
            return
        generation = response.generations[0][0] if response.generations else None
        message = getattr(generation, "message", None)
        usage = getattr(message, "usage_metadata", None) or {}
        self._write(
            run,
            run_id,
            status="ok",
            output_chars=len(generation.text) if generation else 0,
            input_tokens=usage.get("input_tokens"),
            output_tokens=usage.get("output_tokens"),
        )

    def on_llm_error(
        self, error: BaseException, *, run_id: UUID, **kwargs: Any
    ) -> None:
        run = self._runs.pop(run_id, None)
        if run is None:
            return
        self._write(run, run_id, status="error", error=type(error).__name__)

    def _write(self, run: dict[str, Any], run_id: UUID, **fields: Any) -> None:
        record = {
            "ts": datetime.now(UTC).isoformat(),
            "run_id": str(run_id),
            "provider": run["provider"],
            "model": run["model"],
            "latency_ms": round((time.perf_counter() - run["start"]) * 1000, 1),
            "input_chars": run["input_chars"],
            **fields,
        }
        line = json.dumps(record) + "\n"
        with self._lock, self._path.open("a", encoding="utf-8") as f:
            f.write(line)
