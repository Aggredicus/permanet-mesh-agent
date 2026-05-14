# Agent Assignment Table

Use this template before running multiple AI-assisted contributors concurrently.

Purpose:

- prevent duplicate PRs
- prevent overlapping edits
- define ownership clearly
- coordinate reviewer expectations
- improve branch freshness discipline
- keep shared truth files synchronized

## Rules

- One active implementation PR per issue unless explicitly approved.
- Shared truth files should usually be edited in one coordinated PR.
- Every worker must verify live GitHub state before starting.
- Reviewer agents should inspect all active PRs before merge recommendations.
- Human maintainers remain final authority.

## Sprint coordination table

| Agent | Role | Issue | Branch | Allowed files | Forbidden files | Validation owner | Status |
|---|---|---|---|---|---|---|---|
| Coordinator | Coordination | # | quality/... | planning only | runtime files unless assigned | reviewer | active |
| Worker A | Implementation | # | feature/... | assigned files only | shared truth docs | self | pending |
| Worker B | Implementation | # | docs/... | assigned docs only | runtime files | self | pending |
| Reviewer | Review | all active PRs | none | comments/reviews only | implementation edits unless approved | reviewer | active |

## Shared truth files

These files should be treated as high-coordination surfaces:

```text
README.md
AGENTS.md
CONTRIBUTING.md
docs/developer-handoff.md
docs/roadmap.md
docs/planning/priority-ledger.md
docs/sops/
.github/
```

If multiple workers need to touch these files simultaneously, the coordinator should usually consolidate the work into a single PR.

## Recommended workflow

```text
1. Coordinator reviews open issues/PRs/branches.
2. Coordinator assigns ownership.
3. Workers verify branch freshness.
4. Workers implement narrow scoped changes.
5. Reviewer checks overlap, freshness, validation, and safety.
6. Human maintainer decides merge order.
```

## Example

| Agent | Role | Issue | Branch | Allowed files | Forbidden files | Validation owner | Status |
|---|---|---|---|---|---|---|---|
| Coordinator | Coordination | #40 | quality/40-multi-agent-concurrency | planning + SOPs | runtime | Reviewer | active |
| Worker A | Docs | #13 | docs/13-security-policy | SECURITY.md | src/ | Worker A | active |
| Worker B | CI | #8 | quality/8-dependabot | .github/dependabot.yml | docs/sops/ | Worker B | pending |
| Reviewer | Review | all | none | reviews/comments | implementation edits | Reviewer | active |
