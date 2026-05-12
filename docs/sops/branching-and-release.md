# Branching and Release SOP

## Purpose

This SOP protects `permanet-mesh-agent` from unreviewed changes, accidental direct commits to `main`, unsafe public mesh behavior, undocumented AI-assisted modifications, and future hardware deployment risk.

Branch discipline exists to protect:

- the stable state of `main`
- public mesh safety
- reviewability
- traceability
- AI-assisted development quality
- future hardware deployment safety

## Default workflow

Use a lightweight GitHub Flow model with short-lived issue branches:

```text
main
└── feature/<issue-number>-short-name
    └── PR -> main
        └── optional release tag
```

Every meaningful change should start from a GitHub issue, continue on an issue-linked branch, and merge through a pull request after validation evidence is available.

## Main branch rule

`main` represents the stable, reviewed state of the project.

Do not implement feature work directly on `main`.

All meaningful changes should flow through pull requests. CI should pass before merge, and high-risk changes require explicit human review.

High-risk changes include anything that affects:

- live Meshtastic transmission
- public mesh response behavior
- private channel handling
- multi-packet output
- node IDs
- PSKs or encryption keys
- secrets or API keys
- persistence/storage
- AI backend behavior
- safety-critical defaults

## Branch naming conventions

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
hotfix/v1.0.1-public-loop
release/v1.0.0
experiment/mqtt-bridge
```

Use `feature/` for user-facing or runtime functionality, `fix/` for defects, `docs/` for documentation-only work, `quality/` for governance/process/test improvements, `experiment/` for exploratory work, `release/` for stabilization, and `hotfix/` for urgent deployed fixes.

## Issue-first rule

Each meaningful issue should define:

- goal
- scope
- non-goals
- risk level
- acceptance criteria
- likely affected files or modules
- required tests
- rollback plan

If a change begins without an issue, stop and create one before continuing unless the user explicitly authorizes emergency maintenance.

## Pull request rule

Each branch should merge through a PR that includes:

- linked issue
- summary
- scope
- non-goals
- risk level
- safety checklist
- validation evidence
- known limitations
- rollback plan

## Release tags

Use semantic milestone tags for stable checkpoints:

```text
v0.1.0
v0.2.0
v0.3.0
v1.0.0
```

Tag only after the relevant milestone has merged and validation has passed.

## Hotfix branches

Hotfix branches are reserved for urgent safety or deployed-field fixes. They should be small, specific, and based on the affected stable branch or tag.

Example:

```text
hotfix/v1.0.1-public-loop
```

Do not use hotfix branches for normal feature development.

## Accidental direct commits to main

If work accidentally happens on `main`:

1. Stop further work.
2. Document what changed.
3. Create a GitHub issue if one does not exist.
4. Create a corrective branch from current `main` if follow-up work is needed.
5. Open a PR for follow-up fixes or process hardening.
6. Do not rewrite public history unless explicitly approved.

Accidental direct commits should become process-improvement evidence, not blame.

## Branch policy check

Run this before implementation work and before opening a PR:

```bash
python scripts/check_branch_policy.py
```

The script is expected to fail on `main` and pass on valid issue-linked branches such as:

```text
quality/2-branching-ai-quality-workflow
```
