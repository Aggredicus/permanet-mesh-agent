# GitHub Project Orchestration SOP

## Purpose

This SOP defines how GitHub Projects should be used as the live orchestration console for PermaNet Mesh Agent development.

The GitHub Project Board coordinates:

- issues
- pull requests
- branches
- ownership
- review state
- concurrency boundaries
- validation readiness
- safety readiness
- sprint sequencing
- multi-agent collaboration

The board exists to improve coordination clarity, safety, reviewer visibility, branch discipline, validation quality, concurrency reliability, roadmap execution, and human oversight.

## Related work

Related issues:

```text
#40 Multi-agent concurrency protocol
#43 GitHub Project Board for multi-agent orchestration
```

Related files:

```text
AGENTS.md
CONTRIBUTING.md
docs/sops/multi-agent-concurrency.md
docs/sops/ai-coding-quality-system.md
docs/sops/pull-request-quality-gate.md
docs/sops/branching-and-release.md
docs/planning/priority-ledger.md
docs/templates/agent-assignment-table.md
```

## What the Project Board is

The Project Board is a live coordination system.

It should answer:

```text
What is being worked on?
Who owns it?
What branch is active?
What files are safe to edit?
What files are forbidden?
What validation is complete?
What is blocked?
What is risky?
What requires review?
What is merge-ready?
```

The board is the operational dashboard for maintainers, reviewers, coordinators, Codex agents, Cursor agents, ChatGPT-assisted workflows, and future automation.

## What the Project Board is not

The Project Board is not the factual source of truth.

The board should never replace:

- issues
- pull requests
- commits
- CI results
- repository code
- runtime tests
- GitHub branch state
- maintainer review

## Source-of-truth model

PermaNet uses layered truth:

```text
GitHub Issues / Pull Requests / commits / CI = factual truth
GitHub Project Board = coordination truth
AGENTS.md + SOPs + CONTRIBUTING.md = rule truth
CI + scripts + human review = validation truth
```

If the board conflicts with Issues, PRs, or CI, the Issues, PRs, and CI win. The board should then be updated.

## Canonical Project name

Recommended board name:

```text
PermaNet Mesh Agent — Engineering Console
```

## Field schema

Keep fields intentionally lean. The goal is maximum coordination clarity with minimum maintenance burden.

### Status

Type: single-select

Values:

```text
Triage
Ready
Assigned
In Progress
Review
Blocked
Needs Coordination
Done
```

### Priority

Type: single-select

Values:

```text
P0
P1
P2
P3
```

Definitions:

```text
P0 = critical / blocking
P1 = important
P2 = useful
P3 = low urgency
```

### Risk

Type: single-select

Values:

```text
Low
Medium
High
```

High risk includes runtime safety, live radio, security, storage, mesh routing, public behavior, secret handling, or CI governance.

### Area

Type: single-select

Values:

```text
runtime
docs
process
security
hardware
ci
agent-workflow
```

### Agent Role

Type: single-select

Values:

```text
Coordinator
Worker
Reviewer
Human
```

### Owner

Type: text or GitHub user

Purpose:

```text
Who currently owns execution responsibility.
```

### Branch

Type: text

Examples:

```text
quality/40-multi-agent-concurrency
feature/19-typed-config-loader
```

### Allowed Files

Type: text

Purpose:

```text
Explicit ownership boundaries.
```

### Forbidden Files

Type: text

Purpose:

```text
Prevent overlapping edits.
```

### Concurrency Risk

Type: single-select

Values:

```text
Low
Medium
High
```

High concurrency risk usually includes shared truth files such as:

```text
README.md
AGENTS.md
CONTRIBUTING.md
docs/sops/
docs/roadmap.md
docs/developer-handoff.md
.github/
```

### Validation State

Type: single-select

Values:

```text
Not run
Local passed
CI passed
Blocked
Not applicable
```

### Reviewer Verdict

Type: single-select

Values:

```text
Not reviewed
Merge-ready
Needs changes
Stale
Duplicate
Unsafe
Out of scope
```

### Sprint

Type: iteration

Purpose:

```text
Organize active work windows.
```

### Blocked By

Type: text

Examples:

```text
PR #52
Issue #18
waiting for maintainer review
waiting for CI
```

## Required views

### Coordinator Console

Purpose:

```text
Mission control.
```

Recommended visible fields:

```text
Issue
PR
Status
Priority
Risk
Owner
Agent Role
Branch
Allowed Files
Forbidden Files
Validation State
Concurrency Risk
Reviewer Verdict
```

Recommended grouping:

```text
Status
```

Recommended sorting:

```text
Priority descending
```

### Worker Queue

Purpose:

```text
Work assignment board.
```

Filter:

```text
Status = Ready OR Assigned
```

Recommended visible fields:

```text
Issue
Owner
Branch
Allowed Files
Validation State
```

### Reviewer Queue

Purpose:

```text
Review triage.
```

Filter:

```text
Status = Review
```

Recommended visible fields:

```text
Issue
PR
Reviewer Verdict
Validation State
Risk
Concurrency Risk
```

### Shared Docs Risk

Purpose:

```text
Detect coordination hazards.
```

Filter:

```text
Concurrency Risk = High
```

Recommended visible fields:

```text
Issue
Branch
Owner
Allowed Files
Forbidden Files
```

### Safety Before Hardware

Purpose:

```text
Track readiness before live Meshtastic behavior.
```

Filter:

```text
Risk = High
```

Recommended tracked items:

```text
#18 Risk register
#13 SECURITY.md
#9 Secret scanning
#8 Dependabot
#11 CODEOWNERS
#19 Typed config loader
v0.3 Meshtastic serial ping bot
```

### v0.3 Roadmap

Purpose:

```text
Track progression toward first live hardware milestone.
```

Recommended layout:

```text
Roadmap / timeline
```

### Blocked Work

Purpose:

```text
Show work that needs maintainer action, CI recovery, sequencing, or dependency resolution.
```

Filter:

```text
Status = Blocked
```

## Status flow rules

### Triage

Issue exists but is not prepared.

### Ready

Issue is approved for assignment.

### Assigned

Coordinator assigned ownership.

### In Progress

Work is actively happening.

### Needs Coordination

Issue overlaps shared truth files or overlapping workflows.

### Review

PR is open and awaiting reviewer attention.

### Blocked

Waiting for review, CI, dependency, maintainer decision, or merge sequencing.

### Done

Only valid when:

```text
PR merged
OR
issue closed by maintainer
```

Agents should not move work to Done based solely on local completion.

## Agent workflow

Every fresh agent should follow:

```text
1. Read AGENTS.md.
2. Read docs/sops/multi-agent-concurrency.md.
3. Read docs/sops/github-project-orchestration.md.
4. Open the Project Board when available.
5. Find the assigned issue.
6. Verify branch.
7. Verify allowed files.
8. Verify forbidden files.
9. Verify no duplicate PR exists.
10. Verify branch freshness.
11. Perform narrow scoped work.
12. Record validation evidence.
13. Move item to Review only after a PR is ready for review.
14. Let a human maintainer decide final merge readiness.
```

If the board has not been created yet, agents should fall back to the linked issue, PR template, `docs/templates/agent-assignment-table.md`, and `docs/planning/priority-ledger.md`.

## Coordinator workflow

Coordinator responsibilities:

```text
review open issues
review open PRs
review active branches
assign ownership
prevent overlap
sequence shared-doc work
mark blockers
manage sprint ordering
```

Coordinator should optimize for clarity and safety, not raw parallelism.

## Reviewer workflow

Reviewer responsibilities:

```text
inspect PR quality
inspect overlap
inspect branch freshness
inspect validation evidence
inspect runtime safety claims
inspect docs consistency
classify PR state
```

Reviewer verdicts:

```text
Merge-ready
Needs changes
Stale
Duplicate
Unsafe
Out of scope
```

The reviewer may recommend action, but the human maintainer decides final merge and closure actions.

## Recommended automation strategy

Start small.

### Phase 1 — Manual coordination

Use:

```text
Project Board
SOPs
PR template
Issue templates
agent assignment table
```

No heavy automation yet.

### Phase 2 — Built-in Project automation

Suggested built-in automations:

```text
Issue added -> Triage
PR opened -> Review
PR merged -> Done
Issue closed -> Done
```

### Phase 3 — Lightweight scripts

Suggested future scripts:

```text
scripts/check_project_fields.py
scripts/check_duplicate_prs.py
scripts/check_branch_freshness.py
```

### Phase 4 — GitHub Actions enforcement

Possible future workflow:

```text
.github/workflows/project-orchestration-check.yml
```

Potential checks:

```text
linked issue exists
branch naming valid
required fields present
PR template complete
no duplicate active PR
shared-doc warning
```

Start warning-first. Only hard-fail later if necessary.

## Safety invariants

The board must never weaken repository safety guarantees.

Critical invariants:

```text
Public chatter without summon receives no response.
No automatic multi-packet flooding.
Live radio disabled by default.
No secrets committed.
No autonomous merges.
```

## Human authority

Humans remain final authority for:

```text
merges
issue closure
branch deletion
release tags
rulesets
security settings
hardware activation
public deployment
```

Agents assist. Agents do not govern the repository autonomously.

## Recommended initial board population

Initial tracked issues:

```text
#40 Multi-agent concurrency SOP
#43 GitHub Project Board orchestration
#18 Risk register
#13 SECURITY.md
#9 Secret scanning
#8 Dependabot
#11 CODEOWNERS
#19 Typed config loader
#37 Codex workflow refactor
#36 Progress-report infographic generator
```

## Failure modes to avoid

### Overengineering

Avoid:

```text
50 fields
10 automations
mandatory bureaucracy
```

The board should remain fast, clear, and maintainable.

### Stale orchestration state

If the board diverges from reality:

```text
Issues/PRs/CI win.
```

Update the board.

### Automation lock-in

Do not depend on fragile GraphQL automations, heavy custom integrations, or complex third-party project-management systems.

Prefer simple durable workflows.

## Minimal viable board

If complexity grows too high, reduce to:

```text
Status
Priority
Risk
Owner
Branch
Validation State
```

with these views:

```text
Coordinator Console
Worker Queue
Reviewer Queue
```

That alone solves most coordination failures.

## Rollback plan

If this SOP creates too much process overhead:

1. Keep the source-of-truth model.
2. Reduce board fields to the minimal viable board.
3. Keep only Coordinator Console, Worker Queue, and Reviewer Queue views.
4. Move unused orchestration detail back into issues or PR templates.
5. Reopen a narrower follow-up issue for any automation that proved useful.

## Strategic outcome

This system transforms PermaNet Mesh Agent from ad hoc AI-assisted coding into a structured multi-agent engineering environment with explicit ownership, traceable coordination, reviewer visibility, safety-first governance, branch discipline, validation accountability, scalable orchestration, and human-supervised AI collaboration.
