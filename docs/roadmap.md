# Roadmap

## Completed milestones

### v0.1.0 — Mock command bot

Goal: prove the full bot behavior without hardware.

Completed:

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

### v0.2.0 — Response policy and pagination

Goal: prevent public mesh flooding while allowing explicit continuation.

Completed:

- Response length guard.
- Mesh-safe response chunking.
- Explicit `MORE` pagination state.
- Better command help.
- Basic per-node cooldown.
- Basic per-channel cooldown.
- CLI smoke checks for `@permanet ping` and unsummoned public chatter.

## Next milestone

### v0.3.0 — Meshtastic serial ping bot

Goal: prove the existing summon-only mock behavior over a real Meshtastic serial adapter.

Planned:

- Serial adapter.
- Packet normalization.
- Hardware test checklist.
- Real mesh `@permanet ping` test.
- Preserve `hello mesh -> no output` on public channels.

## Future milestones

### v0.4.0 — Public summon mode hardening

- Public channel etiquette rules.
- Rate limits.
- Ignore loops/repeated spam.
- Structured logs.

### v0.5.0 — AI backend integration

- Cloud AI backend.
- Local Ollama backend.
- Short-answer prompt templates.
- AI unavailable fallback.

### v0.6.0 — Private group channels

- Channel-index routing.
- Group-specific config.
- Node allowlists.
- Admin-only commands.

### v0.7.0 — Field notes and task logging

- SQLite storage.
- `observe` command.
- `task` command.
- JSONL export.

### v1.0.0 — Field-ready beta

- systemd service.
- Deployment guide.
- Hardware guide.
- Field test report.
- Stable public/private/admin behavior.
