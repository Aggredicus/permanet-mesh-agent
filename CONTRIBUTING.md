# Contributing

Thank you for helping build PermaNet Mesh Agent.

This project is early-stage and intentionally mock-first. The goal is to build a safe, testable Meshtastic chatbot gateway without accidentally creating spammy or unsafe mesh behavior.

## Development workflow

1. Create a branch for each meaningful change.
2. Keep changes small and reviewable.
3. Run tests before opening a pull request.
4. Update docs when behavior changes.
5. Preserve public-channel summon-only behavior.

Recommended local checks:

```bash
pip install -e .[dev]
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
```

Expected mock output:

```text
pong
```

## Safety rules

Do not implement any behavior that replies to all public Meshtastic messages.

Public channel responses must require an explicit summon phrase such as:

```text
@permanet
/permanet
```

Do not add automatic multi-packet replies. Long answers should be shortened or continued only when the user explicitly requests `MORE`.

Do not hardcode private channel names, PSKs, node IDs, API keys, client names, or other sensitive information.

## Hardware rule

All live radio behavior must be backed by mock-radio tests first.

Before adding a Meshtastic serial, TCP, BLE, or meshtasticd adapter, prove the same behavior through `MockRadio`.

## Pull request checklist

- [ ] `pytest` passes.
- [ ] `ruff check .` passes.
- [ ] Public chatter without a summon is still ignored.
- [ ] `@permanet ping` still returns `pong`.
- [ ] Docs/config examples are updated if behavior changes.
- [ ] No secrets or private client information were committed.
- [ ] No live radio flood behavior was introduced.

## Current priority

The next milestone is v0.2.0:

- response length guard
- response chunking
- `MORE` pagination
- per-node cooldown
- tests for no automatic flooding

See GitHub Issue #1 for the detailed planning checklist.
