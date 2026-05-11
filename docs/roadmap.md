# Roadmap

## v0.1.0 — Mock command bot

Goal: prove the full bot behavior without hardware.

- Python package scaffold.
- Mock radio adapter.
- Command parser.
- Router.
- Mock AI backend.
- Tests for summon-only public behavior.

Acceptance test:

```text
python -m permanet_agent.main --mock --message "@permanet ping"
# pong
```

## v0.2.0 — Response policy and pagination

- Response length guard.
- `MORE` pagination state.
- Better command help.
- Basic per-node cooldown.

## v0.3.0 — Meshtastic serial ping bot

- Serial adapter.
- Packet normalization.
- Hardware test checklist.
- Real mesh `@permanet ping` test.

## v0.4.0 — Public summon mode hardening

- Public channel etiquette rules.
- Rate limits.
- Ignore loops/repeated spam.
- Structured logs.

## v0.5.0 — AI backend integration

- Cloud AI backend.
- Local Ollama backend.
- Short-answer prompt templates.
- AI unavailable fallback.

## v0.6.0 — Private group channels

- Channel-index routing.
- Group-specific config.
- Node allowlists.
- Admin-only commands.

## v0.7.0 — Field notes and task logging

- SQLite storage.
- `observe` command.
- `task` command.
- JSONL export.

## v1.0.0 — Field-ready beta

- systemd service.
- Deployment guide.
- Hardware guide.
- Field test report.
- Stable public/private/admin behavior.
