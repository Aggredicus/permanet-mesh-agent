# Contributing

Thank you for helping build PermaNet Mesh Agent.

This project is early-stage and intentionally mock-first. The goal is to build a safe, testable Meshtastic chatbot gateway without accidentally creating spammy or unsafe mesh behavior.

## Engineering quality workflow

This repository uses an issue-first, branch-first, PR-reviewed workflow.

Read these SOPs before meaningful implementation work:

- `docs/sops/branching-and-release.md`
- `docs/sops/ai-coding-quality-system.md`
- `docs/sops/pull-request-quality-gate.md`
- `docs/sops/issue-prioritization.md`

Use this planning artifact when selecting or reordering work:

- `docs/planning/priority-ledger.md`

## Protected main workflow

`main` is the stable reviewed branch. Meaningful changes should be made on issue-linked branches and merged through pull requests.

The intended GitHub protection for `main` is:

```text
Pull requests required before merge
test required before merge
Force pushes blocked
Branch deletion blocked
Conversation resolution required if available
Administrator enforcement enabled if practical
```

If branch protection is not yet active in GitHub settings, contributors should still follow this workflow manually. Once Issue #5 is completed, GitHub should enforce these rules directly.

## Issue forms

Use the structured GitHub issue forms when opening new work:

| Template | Use when |
|---|---|
| Feature request | Proposing normal product, runtime, or developer-facing feature work. |
| Bug report | Reporting broken behavior, regressions, or unexpected output. |
| Quality improvement | Improving CI, tests, linting, branch policy, AI review, scoring, or repo hygiene. |
| Hardware safety / live radio work | Planning Meshtastic hardware, live radio adapters, field tests, or transmission behavior. |
| Security or secrets concern | Reporting secret hygiene, API keys, PSKs, node IDs, private channel risk, or dependency security concerns. |
| Documentation update | Improving README, SOPs, handoff docs, AGENTS, CONTRIBUTING, diagrams, or tutorials. |
| Experiment / research spike | Exploring uncertain ideas without silently turning them into production behavior. |

Blank issues remain enabled for maintainers, but contributors and agents should prefer the structured forms because they capture scope, non-goals, validation, rollback, and acceptance criteria.

## Development workflow

1. Start from a GitHub issue.
2. Check whether the issue is prioritized in `docs/planning/priority-ledger.md`.
3. Create an issue-linked branch.
4. Keep changes small and reviewable.
5. Run branch policy, tests, and lint checks before opening a pull request.
6. Update docs when behavior changes.
7. Preserve public-channel summon-only behavior.
8. Open a PR with validation evidence and a rollback plan.
9. Merge only after required checks pass.

## Issue prioritization

Issues may be scored by priority, complexity, safety impact, quality leverage, dependency unblock, urgency, and confidence.

Decision categories:

```text
Do Now
Strategic Build
Batch / Delegate
Defer / Wishlist
```

Agent votes are advisory. Human maintainers make final priority decisions.

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
- [ ] Priority ledger is updated if the PR changes issue ordering or triage rules.

## Current priority

Use `docs/planning/priority-ledger.md` for the current ranked issue order.

The next feature milestone remains v0.2.0:

- response length guard
- response chunking
- `MORE` pagination
- per-node cooldown
- tests for no automatic flooding

Issue #1 tracks the detailed v0.2 planning checklist.
