import asyncio
import json

import pytest
from conftest import fake_model

from pidemo.adapters.observability.local_log import JsonlTraceHandler
from pidemo.domain.summarize import Summarizer


def test_writes_one_metadata_line_per_call(tmp_path):
    path = tmp_path / "nested" / "llm.jsonl"
    summarizer = Summarizer(
        fake_model("first", "second"), callbacks=[JsonlTraceHandler(path)]
    )
    asyncio.run(summarizer.summarize("secret input one"))
    asyncio.run(summarizer.summarize("secret input two"))

    lines = path.read_text().splitlines()
    assert len(lines) == 2
    record = json.loads(lines[0])
    assert record["status"] == "ok"
    assert record["output_chars"] == len("first")
    assert record["input_tokens"] == 7
    assert record["output_tokens"] == 3
    assert record["latency_ms"] >= 0
    assert {"ts", "run_id", "provider", "model", "input_chars"} <= record.keys()
    # Only metadata is logged, never content.
    assert "secret input" not in path.read_text()


def test_writes_error_line(tmp_path):
    path = tmp_path / "llm.jsonl"
    summarizer = Summarizer(fake_model(), callbacks=[JsonlTraceHandler(path)])
    # The fake model has no replies, so the call fails.
    with pytest.raises(RuntimeError):
        asyncio.run(summarizer.summarize("text"))
    record = json.loads(path.read_text().splitlines()[0])
    assert record["status"] == "error"
    assert record["error"]
