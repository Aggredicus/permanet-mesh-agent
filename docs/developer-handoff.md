# Developer Handoff

This document is the fastest path for a senior backend developer to understand the current state of PermaNet Mesh Agent and decide what to build next.

## One-sentence summary

PermaNet Mesh Agent is a mock-first Python service that will become a summon-only Meshtastic chatbot gateway for public mesh channels, private group channels, and admin-controlled field operations.

## Current repository state

The repository now has a completed v0.1 scaffold and is still mock-first, not a live radio bot.

Implemented:

- Python package scaffold under `src/permanet_agent/`.
- Mock radio adapter for hardware-free testing.
- Command parser for `@permanet` and `/permanet` summon phrases.
- Basic handlers for `help`, `ping`, `ask`, and `more`.
- Mock AI backend.
- Router that ignores unsummoned public chatter.
- Unit tests for parser, router, and mock end-to-end flow.
- Example config and environment files.
- Architecture, hardware, roadmap, and channel policy docs.
- GitHub Actions CI workflow.

Not yet implemented:

- Live Meshtastic serial, TCP, or BLE adapter.
- Response chunking and `MORE` pagination state.
- Rate limiting.
- Private group routing.
- Admin command permission layer.
- SQLite persistence.
- Cloud or local LLM integration.

Planning note:

- Issue #2 is complete (initial scaffold/handoff phase).
- Current priority queue is Issue #5 first, then Issue #1.

## Why the repo is mock-first

Meshtastic is bandwidth-constrained and public mesh etiquette matters. The safest path is to prove all behavior with a mock radio before allowing live radio transmission.

The most important invariant is:

```text
Public chatter without @permanet or another configured summon phrase must be ignored.
```

Do not build behavior that automatically replies to every message on a public channel.

## Quick start

```bash
git clone https://github.com/Aggredicus/permanet-mesh-agent.git
cd permanet-mesh-agent
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
```

Expected output:

```text
pong
```

## Current command behavior

| Input | Expected behavior |
|---|---|
| `hello mesh` | ignored |
| `@permanet` | help response |
| `@permanet help` | command list |
| `@permanet ping` | `pong` |
| `@permanet ask wet slope plants` | mock AI response |
| `@permanet more` | placeholder response until pagination is implemented |

## Recommended reading order

1. `README.md` — project identity and quickstart.
2. `AGENTS.md` — safety rules and development boundaries.
3. `docs/architecture.md` — module boundaries and data flow.
4. `docs/channel-policy.md` — public/private/admin channel behavior.
5. `docs/roadmap.md` — milestone sequence.
6. GitHub Issue #1 — v0.2.0 planning issue.

## Immediate next milestone

The next milestone is **v0.2.0: response policy, rate limits, and MORE pagination**.

Build this before live Meshtastic hardware integration.

Primary objectives:

- Add configurable response length limits.
- Add response chunking/truncation.
- Add explicit `MORE` pagination state.
- Add basic per-node cooldown.
- Add tests proving long answers do not auto-flood the mesh.
- Preserve the summon-only public-channel invariant.

## Suggested v0.2 module boundaries

```text
src/permanet_agent/policy/response_policy.py
src/permanet_agent/policy/rate_limits.py
src/permanet_agent/memory/pagination_cache.py
```

The exact filenames can change if the boundaries remain clean.

## What not to build yet

Do not start with:

- A web dashboard.
- A database-heavy architecture.
- Live radio transmission.
- Private group routing.
- A vector database.
- Automatic multi-packet responses.
- A complex agent framework.

Those are valid future directions, but the next step is radio-safe message behavior.

## Recommended first developer task

Start with response policy tests.

Suggested tests:

```text
test_response_policy_limits_public_response_length
test_long_answer_is_chunked_not_flooded
test_more_returns_next_chunk
test_more_without_pending_chunk_returns_helpful_message
test_per_node_cooldown_blocks_repeated_invocation
test_unsummoned_message_still_ignored
```

## Definition of done for v0.2

v0.2 is complete when:

1. `pytest` passes.
2. `ruff check .` passes.
3. `@permanet ping` still returns `pong`.
4. Unsummoned public messages still return no response.
5. Long responses are shortened or chunked.
6. The bot does not automatically send multiple packets.
7. `@permanet more` returns the next chunk only when pending continuation exists.
8. Repeated messages from the same node can be rate-limited.

## After v0.2

Once response safety exists, proceed to **v0.3.0: Meshtastic serial ping bot**.

That milestone should connect a physical Meshtastic node and prove:

```text
@permanet ping -> pong
```

 over live mesh hardware.
