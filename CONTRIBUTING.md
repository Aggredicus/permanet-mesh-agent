# Contributing

Thank you for helping build PermaNet Mesh Agent.

This project is early-stage and intentionally mock-first. The goal is to build a safe, testable Meshtastic chatbot gateway without accidentally creating spammy or unsafe mesh behavior.

## Engineering quality workflow

This repository uses an issue-first, branch-first, PR-reviewed workflow.

Read these SOPs before meaningful implementation work:

- `docs/sops/branching-and-release.md`
- `docs/sops/ai-coding-quality-system.md`
- `docs/sops/pull-request-quality-gate.md`

## Development workflow

1. Start from a GitHub issue.
2. Create an issue-linked branch.
3. Keep changes small and reviewable.
4. Run branch policy, tests, and lint checks before opening a pull request.
5. Update docs when behavior changes.
6. Preserve public-channel summon-only behavior.
7. Open a PR with validation evidence and a rollback plan.

## Branch naming

Allowed branch patterns:

```text
feature/<issue-number>-short-description
fix/<issue-number>-short-description
docs/<issue-number>-short-description
quality/<issue-number>-short-description
hotfix/<version>-short-description
release/<version>
experiment/<short-description>
```

Examples:

```text
feature/1-response-policy-rate-limits
quality/2-branching-ai-workflow
fix/3-ci-ruff-cleanup
docs/4-handoff-polish
experiment/mqtt-bridge
release/v1.0.0
hotfix/v1.0.1-public-loop
```

Do not implement feature work directly on `main`.

## Recommended local checks

```bash
pip install -e .[dev]
python scripts/check_branch_policy.py
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected mock behavior:

```text
@permanet ping -> pong
hello mesh -> no output
```

Note: `python scripts/check_branch_policy.py` is expected to fail on `main`. Create or switch to an issue-linked branch before running it as a pass/fail gate.

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

- [ ] Linked issue is included.
- [ ] `python scripts/check_branch_policy.py` passes on an issue-linked branch.
- [ ] `pytest` passes.
- [ ] `ruff check .` passes.
- [ ] Public chatter without a summon is still ignored.
- [ ] `@permanet ping` still returns `pong`.
- [ ] Docs/config examples are updated if behavior changes.
- [ ] No secrets or private client information were committed.
- [ ] No live radio flood behavior was introduced.
- [ ] Rollback plan is documented.

## Current priority

The next feature milestone is v0.2.0:

- response length guard
- response chunking
- `MORE` pagination
- per-node cooldown
- tests for no automatic flooding

Before continuing v0.2 feature implementation, complete the branching and AI coding quality workflow in GitHub Issue #2.
