# pidemo: a platform-independent LangChain service

A small HTTP service that summarizes text with an LLM. It is built so that no
proprietary service is required to run it, and swapping the model provider or
the tracing backend is a configuration change, not a code change.

- Model: self-hosted [Ollama](https://ollama.com) by default (runs in compose).
- Tracing: a project-owned JSONL callback handler by default. Hosted LangSmith
  is opt-in.
- Domain and API code import only `langchain-core` (MIT). Vendor integrations
  are resolved in one composition root (`src/pidemo/bootstrap.py`).

## Layout

```
src/pidemo/
  config.py                         Settings from env / .env
  bootstrap.py                      composition root: config -> model + callbacks
  domain/summarize.py               use case, typed against BaseChatModel
  adapters/observability/local_log.py   JSONL tracing (default)
  adapters/observability/langsmith.py   hosted tracing (opt-in)
  api.py                            FastAPI: POST /summarize, GET /healthz
tests/                              fake chat model, no network
```

## Run with docker compose

```sh
cp .env.example .env        # optional; defaults are the same
docker compose up -d        # ollama, one-shot model pull, app
curl -s localhost:8000/summarize -H 'content-type: application/json' \
  -d '{"text": "Long text to summarize...", "max_sentences": 2}'
docker compose exec app cat /app/traces/llm.jsonl
```

The first start pulls the model (`llama3.2:1b`, about 1.3 GB) into the
`ollama` volume. CPU-only is fine.

## Run locally

```sh
uv sync
uv run pytest
LLM_BASE_URL=http://localhost:11434 uv run pidemo   # needs a reachable Ollama
```

## Configuration

| Variable            | Default            | Notes                                         |
|---------------------|--------------------|-----------------------------------------------|
| `LLM_PROVIDER`      | `ollama`           | any `init_chat_model` provider whose package is installed |
| `LLM_MODEL`         | `llama3.2:1b`      | also the model pulled by `ollama-pull`        |
| `LLM_BASE_URL`      | compose: `http://ollama:11434` | set empty for a provider's own default |
| `LLM_TEMPERATURE`   | `0.0`              |                                               |
| `TRACING`           | `local`            | `none`, `local`, or `langsmith`               |
| `TRACE_LOG_PATH`    | `traces/llm.jsonl` | compose: `/app/traces/llm.jsonl` (volume)     |
| `LANGSMITH_API_KEY` | unset              | required only for `TRACING=langsmith`         |
| `EXTRA`             | unset              | build arg: provider extra to install (`openai`, `anthropic`) |

The JSONL trace records provider, model, latency, token counts and sizes. It
never records prompt or completion text.

## Switching the model provider

Proprietary integrations are uv extras, not default dependencies. Switching is
"install the extra + set env vars":

```sh
# .env
EXTRA=openai
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini
LLM_BASE_URL=
OPENAI_API_KEY=sk-...

docker compose up -d --build
```

Locally: `uv sync --extra openai` (or `--extra anthropic` with
`LLM_PROVIDER=anthropic` and `ANTHROPIC_API_KEY`). The compose file still
starts Ollama; use `docker compose up app --no-deps` to skip it.

Ollama also serves an OpenAI-compatible API, so you can exercise the `openai`
integration with no external account:
`LLM_PROVIDER=openai LLM_BASE_URL=http://ollama:11434/v1 OPENAI_API_KEY=unused`.

## Enabling LangSmith (optional)

```sh
TRACING=langsmith
LANGSMITH_API_KEY=lsv2_...
# LANGSMITH_ENDPOINT / LANGSMITH_PROJECT are honored if set
```

`TRACING` is the only switch. At startup the app calls
`langsmith.configure(enabled=...)`, which overrides the `LANGSMITH_TRACING`
environment variable. A stray `LANGSMITH_TRACING=true` therefore does not send
anything to LangSmith unless `TRACING=langsmith`.

### Why `langsmith` is still in `uv.lock`

`langchain-core` has a hard dependency on the `langsmith` SDK (MIT), so the
package cannot be excluded. Installing the SDK does not contact the hosted
service. Network calls happen only when tracing is enabled, which this app
does only when `TRACING=langsmith`. The hosted LangSmith service is
proprietary. The SDK is open source.
