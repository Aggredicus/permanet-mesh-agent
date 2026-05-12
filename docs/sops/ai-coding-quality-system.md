# AI Coding Quality System

## Purpose

This SOP defines the PermaNet Engineering Quality System for human and AI-assisted software development.

The goal is to reduce hallucinated assumptions, unsafe automation, unreviewed behavior changes, and quality drift while preserving rapid iteration.

## Core principles

1. Safety before speed.
2. Evidence before confidence.
3. Small changes before large rewrites.
4. Mock-first before hardware.
5. Issue-first before implementation.
6. Branch-first before edits.
7. Tests before merge.
8. Human review before high-risk automation.
9. Documentation updated with behavior.
10. Every defect becomes a process improvement.

## AI agent responsibilities

AI coding agents must:

- inspect the repository before editing
- identify the linked issue
- create or use an issue-linked branch
- state assumptions clearly
- avoid hidden scope expansion
- modify the smallest practical file set
- add or update tests when behavior changes
- update documentation when behavior changes
- distinguish tests actually run from tests merely recommended
- never claim tests passed unless they were actually run
- stop before high-risk changes requiring human review

## Prohibited AI behavior

AI agents must not:

- invent APIs, files, modules, or repo state without checking
- claim tests passed without execution evidence
- enable live radio behavior by default
- auto-reply to public mesh chatter
- introduce automatic multi-packet flooding
- commit secrets, PSKs, node IDs, API keys, or private client information
- expand scope beyond the issue without calling it out
- delete safety checks without review
- hide uncertainty or known limitations

## High-risk change categories

The following changes require extra caution and explicit human-review notes:

- live Meshtastic transmission
- public mesh behavior
- multi-packet replies
- private channels
- node IDs
- PSKs or encryption keys
- API keys or secrets
- persistence/storage
- AI backend behavior
- safety-critical defaults

## Safety invariants

These invariants must remain true across development:

```text
Public mesh chatter without @permanet or another configured summon phrase is ignored.
```

```text
The bot must never automatically reply to every public mesh message.
```

```text
Live radio transmission must not be enabled by default.
```

```text
No secrets, PSKs, private node IDs, API keys, or client information may be committed.
```

```text
AI-generated code must not be merged without tests, documented assumptions, and validation evidence.
```

## Continuous improvement loop

Use a Plan -> Do -> Check -> Act cycle.

### Plan

Create or use a GitHub issue. Define goal, scope, non-goals, risks, acceptance criteria, required tests, and rollback plan.

### Do

Create or use an issue-linked branch. Implement the smallest useful slice. Avoid hidden scope expansion.

### Check

Run tests, linting, branch policy checks, and relevant manual smoke checks. Open a PR with validation evidence.

### Act

Merge only after review and passing evidence. Tag releases when appropriate. Convert defects or process gaps into follow-up issues.

## Evidence standard

Final summaries and PR descriptions must say exactly what was run.

Acceptable:

```text
Ran pytest: passed.
Ran ruff check .: passed.
Could not run hardware test because no Meshtastic device was connected.
```

Unacceptable:

```text
Everything should work.
Tests are probably fine.
```

## Mock-first before hardware

No live radio adapter should be enabled until equivalent behavior is proven through mock-radio tests. Hardware code must remain isolated behind radio adapters and disabled by safe defaults.
