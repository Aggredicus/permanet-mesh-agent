# Developer Handoff

This document is the fastest path for a senior backend developer to understand the current state of PermaNet Mesh Agent and decide what to build next.

## One-sentence summary

PermaNet Mesh Agent is a mock-first Python service that will become a summon-only Meshtastic chatbot gateway for public mesh channels, private group channels, and admin-controlled field operations.

## Current repository state

The repository currently contains a working mock-first command bot with v0.2 response-safety behavior implemented. It is still not a live radio bot.

Implemented:

- Python package scaffold under `src/permanet_agent/`.
- Mock radio adapter for hardware-free testing.
- Command parser for `@permanet` and `/permanet` summon phrases.
- Basic handlers for `help`, `ping`, `ask`, and `more`.
- Mock AI backend.
- Router that ignores unsummoned public chatter.
- Response policy for mesh-safe chunking.
- In-memory `MORE` pagination cache keyed by node and channel.
- Basic per-node and per-channel cooldown guard.
- Unit tests for parser, router, policy, pagination, cooldown, and mock end-to-end flow.
- CLI smoke checks for `@permanet ping` and unsummoned public chatter.
- Example config and environment files.
- Architecture, hardware, roadmap, and channel policy docs.
- GitHub Actions CI workflow.

Not yet implemented:

- Live Meshtastic serial, TCP, or BLE adapter.
- Private group routing.
- Admin command permission layer.
- SQLite persistence.
- Cloud or local LLM integration.

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
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected smoke behavior:

```text
@permanet ping -> pong
hello mesh -> no output
```

## Current command behavior

| Input | Expected behavior |
|---|---|
| `hello mesh` | ignored |
| `@permanet` | help response |
| `@permanet help` | command list |
| `@permanet ping` | `pong` |
| `@permanet ask wet slope plants` | mock AI response, chunked if long |
| `@permanet more` | next pending chunk, or a short no-pending message |

## MORE pagination behavior

Long answers are split into mesh-safe chunks. The router sends only the first chunk immediately and stores remaining chunks in memory.

The bot does not automatically send multiple packets.

A user must explicitly request the next continuation with:

```text
@permanet more
```

Continuation state is keyed by node ID and channel index.

## Recommended reading order

1. `README.md` — project identity and quickstart.
2. `AGENTS.md` — safety rules and development boundaries.
3. `docs/architecture.md` — module boundaries and data flow.
4. `docs/channel-policy.md` — public/private/admin channel behavior.
5. `docs/roadmap.md` — completed milestones and next implementation target.
6. GitHub Issue #38 — current handoff/status documentation consolidation issue, if still open.

## Current milestone

The current implementation milestone is **v0.3.0: Meshtastic serial ping bot**.

Build and verify v0.3 only after preserving the current mock behavior and safety tests.

Primary v0.3 objectives:

- Add a live Meshtastic serial adapter behind a radio interface.
- Normalize incoming and outgoing packet data without changing router behavior.
- Prove `@permanet ping -> pong` on real hardware.
- Preserve `hello mesh -> no output` on public channels.
- Keep live radio behavior disabled unless explicitly configured.

## v0.2 module boundaries now in place

```text
src/permanet_agent/policy/response_policy.py
src/permanet_agent/policy/rate_limits.py
src/permanet_agent/memory/pagination_cache.py
```

## What not to build yet

Do not start with:

- A web dashboard.
- A database-heavy architecture.
- Private group routing.
- A vector database.
- Automatic multi-packet responses.
- A complex agent framework.

Those are valid future directions, but the next step is a small hardware-safe serial ping milestone.

## Definition of done for v0.3

v0.3 is complete when:

1. `pytest` passes.
2. `ruff check .` passes.
3. Mock `@permanet ping` still returns `pong`.
4. Unsummoned public messages still return no response.
5. A serial adapter can prove real mesh `@permanet ping -> pong` behavior.
6. Live transmission is isolated behind adapter/config boundaries.
7. Documentation explains hardware setup and rollback/disable steps.

## After v0.3

Once the serial ping bot works safely, proceed to **v0.4.0: public summon mode hardening**.
