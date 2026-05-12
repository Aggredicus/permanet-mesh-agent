# Issue Prioritization SOP

## Purpose

This SOP defines how `permanet-mesh-agent` prioritizes GitHub issues using priority scores, complexity scores, agent voting, and Eisenhower-style decision categories.

The goal is to keep the growing issue backlog actionable, safety-oriented, and easy for both humans and AI agents to reason about.

## Source of truth

GitHub Issues remain the source of truth for individual work items.

The priority ledger is the source of truth for current ordering and rationale:

```text
docs/planning/priority-ledger.md
```

GitHub Projects and labels may mirror the ledger, but the ledger explains why the priority order exists.

## Structured issue forms

New issues should use the structured GitHub issue forms when practical.

Issue forms improve triage by collecting:

- purpose or current behavior
- scope
- non-goals
- risk level
- PermaNet safety impact
- validation plan
- rollback plan
- acceptance criteria

Use the form data as the first source for priority, complexity, safety impact, quality leverage, and confidence scores.

Blank issues remain enabled for maintainers, but structured forms are preferred for work that will become a branch or PR.

## When to score issues

Score or re-score issues when:

- a new issue is created
- an issue is promoted from the wishlist
- a PR reveals a quality or safety weakness
- an issue blocks another issue
- an issue changes scope
- CI, security, or hardware risk changes
- the AI Reviewer recommends reprioritization
- a human maintainer requests triage

## Required scoring fields

Each prioritized issue should receive:

```text
Priority Score: 1–5
Complexity Score: 1–5
Decision Category
Short rationale
```

Optional supporting fields:

```text
Safety Impact: 1–5
Quality Leverage: 1–5
Dependency Unblock: 1–5
Urgency: 1–5
Confidence: 1–5
Execution Score
```

## Priority scale

```text
1 = nice someday
2 = useful but not urgent
3 = valuable
4 = important
5 = critical / blocking
```

Use higher priority when an issue:

- protects safety invariants
- blocks runtime development
- prevents secrets or private data leaks
- enables reliable CI or branch protection
- improves many future issues or PRs
- removes stale or dangerous instructions

## Complexity scale

```text
1 = tiny
2 = small
3 = moderate
4 = large
5 = complex / multi-system
```

Use higher complexity when an issue:

- spans many files
- affects runtime behavior
- requires GitHub settings or external setup
- needs careful sequencing
- touches hardware or live radio behavior
- requires nontrivial tests or migration steps

## Decision categories

| Category | Rule of thumb | Action |
|---|---|---|
| Do Now | Priority 4–5 and Complexity 1–2 | Execute first |
| Strategic Build | Priority 4–5 and Complexity 3–5 | Plan a focused sprint |
| Batch / Delegate | Priority 1–3 and Complexity 1–2 | Batch with similar work or delegate |
| Defer / Wishlist | Priority 1–3 and Complexity 3–5 | Keep in backlog until needed |

The matrix guides decisions but does not override maintainer judgment.

## Weighted execution score

Use this starting formula when a numeric score is helpful:

```text
Execution Score =
  (Safety Impact × 3)
+ (Quality Leverage × 2)
+ (Dependency Unblock × 2)
+ (Urgency × 2)
+ (Priority × 2)
+ Confidence
- (Complexity × 1.5)
```

This formula gives safety and quality more weight than speed. It may be revised as the project learns.

## Agent voting model

Specialized agents may propose scores and recommendations.

| Agent | Focus |
|---|---|
| Safety Reviewer | Mesh safety, live radio risk, public-channel behavior |
| QA Reviewer | Testability, CI, regression risk, validation evidence |
| Runtime Architect | Code structure, interfaces, maintainability |
| Security Reviewer | Secrets, dependency risk, private data, GitHub security features |
| Product / UX Reviewer | User value, developer experience, clarity |
| Documentation Reviewer | Docs, handoff quality, stale instructions |
| Maintainer | Final sequencing and tie-breaking |

Each agent vote should include:

```text
Priority: 1–5
Complexity: 1–5
Risk: low / medium / high
Recommendation: Do Now / Strategic Build / Batch / Defer
Rationale: 1–3 sentences
```

## Human authority

Agent votes are advisory.

The human maintainer makes the final decision when priorities conflict, when timing constraints change, or when external work depends on a particular issue.

## GitHub label recommendations

When Issue #16 is implemented, labels should mirror prioritization:

```text
priority:P0
priority:P1
priority:P2
priority:P3
priority:P4
risk:low
risk:medium
risk:high
status:ready
status:blocked
status:needs-review
```

## GitHub Project field recommendations

When Issue #15 is implemented, GitHub Project fields should include:

```text
Priority: P0 / P1 / P2 / P3 / P4
Complexity: 1 / 2 / 3 / 5 / 8
Decision Category: Do Now / Strategic Build / Batch / Defer
Safety Impact: Low / Medium / High
Quality Leverage: Low / Medium / High
Agent Score: number
Status: Backlog / Ready / In Progress / Review / Blocked / Done
```

## AI Reviewer feedback loop

The AI Reviewer may recommend reprioritization when it finds repeated quality patterns.

Examples:

```text
Observation: PRs keep changing runtime behavior without adding regression tests.
Recommendation: Raise priority for test harness and AI Reviewer issues.
```

```text
Observation: Multiple issues lack rollback plans.
Recommendation: Raise priority for issue templates and PR template hardening.
```

AI Reviewer recommendations should be recorded in the priority ledger or in a comment on the affected issue.

## Updating the ledger

When updating `docs/planning/priority-ledger.md`:

1. Keep the ranking table sorted by current priority.
2. Preserve rationale for each issue.
3. Note major changes in the PR summary.
4. Do not silently demote safety-critical issues.
5. Prefer short rationale over long debate.
6. Link follow-up issues when priority changes reveal missing work.

## Rollback and simplification

If the scoring system becomes too heavy, simplify to:

```text
Priority
Complexity
Decision Category
Short rationale
```

The system should help development move safely, not become bureaucracy.
