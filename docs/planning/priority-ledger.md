# Agent Priority Ledger

This ledger records the current prioritized issue order for `permanet-mesh-agent`.

It is intended to be readable by humans, Cursor, Codex, ChatGPT, and future AI reviewer agents. The ledger is not a replacement for GitHub Issues or GitHub Projects. It is a repo-owned planning artifact that explains why work is prioritized.

## Scoring scale

### Priority

```text
1 = nice someday
2 = useful but not urgent
3 = valuable
4 = important
5 = critical / blocking
```

### Complexity

```text
1 = tiny
2 = small
3 = moderate
4 = large
5 = complex / multi-system
```

### Supporting scores

Optional supporting scores use the same 1–5 scale:

```text
Safety Impact
Quality Leverage
Dependency Unblock
Urgency
Confidence
```

## Weighted execution score

Initial formula:

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

This formula intentionally gives safety and quality more weight than speed. It is a guide, not an automatic command.

## Decision categories

| Category | Rule of thumb | Action |
|---|---|---|
| Do Now | Priority 4–5 and Complexity 1–2 | Execute first |
| Strategic Build | Priority 4–5 and Complexity 3–5 | Plan sprint carefully |
| Batch / Delegate | Priority 1–3 and Complexity 1–2 | Batch or delegate |
| Defer / Wishlist | Priority 1–3 and Complexity 3–5 | Keep in backlog |

## Agent voting roles

Specialized agents may recommend scores using this role set:

| Agent | Focus |
|---|---|
| Safety Reviewer | Mesh safety, live radio risk, public-channel behavior |
| QA Reviewer | Testability, CI, regression risk, validation evidence |
| Runtime Architect | Code structure, interfaces, maintainability |
| Security Reviewer | Secrets, dependency risk, private data, GitHub security features |
| Product / UX Reviewer | User value, developer experience, clarity |
| Documentation Reviewer | Docs, handoff quality, stale instructions |
| Maintainer | Final tie-breaking, sequencing, human judgment |

Each vote should include:

```text
Priority: 1–5
Complexity: 1–5
Risk: low / medium / high
Recommendation: Do Now / Strategic Build / Batch / Defer
Rationale: 1–3 sentences
```

## Current ranked issues

This initial ranking was created after Issue #21 was opened and before the next implementation sprint. Scores should be updated as new information arrives.

| Rank | Issue | Title | Priority | Complexity | Category | Rationale |
|---:|---:|---|---:|---:|---|---|
| 1 | #5 | Enable main branch protection and required CI checks | 5 | 2 | Do Now | Turns documented quality rules into enforced GitHub behavior before more runtime work. |
| 2 | #17 | Clean up stale milestone wording in README and CONTRIBUTING | 3 | 1 | Batch / Delegate | Quick cleanup that prevents humans and agents from following outdated Issue #2 sequencing. |
| 3 | #7 | Add GitHub issue templates | 4 | 2 | Do Now | Improves every future issue by collecting scope, risk, tests, and rollback data up front. |
| 4 | #12 | Split CI into separate test, lint, branch policy, and format checks | 4 | 3 | Strategic Build | Makes branch protection and future quality gates more precise. |
| 5 | #9 | Enable and document secret scanning and push protection | 5 | 2 | Do Now | Reduces risk of leaking API keys, PSKs, node IDs, and private data before hardware/API work. |
| 6 | #13 | Add SECURITY.md and vulnerability reporting policy | 4 | 2 | Do Now | Provides a clear path for reporting secret leaks, public mesh spam, and security issues. |
| 7 | #8 | Add Dependabot configuration | 3 | 2 | Batch / Delegate | Improves dependency hygiene with low implementation complexity. |
| 8 | #18 | Add project risk register | 4 | 2 | Do Now | Captures safety, AI, hardware, and operational risks before live Meshtastic work. |
| 9 | #21 | Add agent-prioritized Eisenhower scoring system | 4 | 2 | Do Now | Creates the triage system that keeps the growing backlog orderly and agent-readable. |
| 10 | #19 | Add typed config loader and validation | 4 | 3 | Strategic Build | Converts safe config expectations into validated behavior before real adapters depend on config. |
| 11 | #1 | v0.2 response policy, rate limits, and MORE pagination | 5 | 4 | Strategic Build | Core runtime safety milestone; should proceed after the most important quality gates are in place. |
| 12 | #6 | Add recursive AI reviewer workflow | 4 | 3 | Strategic Build | Establishes recursive self-reflection for future PRs, but works best after issue templates and CI are stronger. |
| 13 | #10 | Enable CodeQL code scanning | 3 | 2 | Batch / Delegate | Adds security scanning with low runtime risk. |
| 14 | #11 | Add CODEOWNERS | 3 | 2 | Batch / Delegate | Helps route review once collaborator ownership is clearer. |
| 15 | #14 | Add CHANGELOG and release tagging workflow | 3 | 2 | Batch / Delegate | Improves release traceability before more milestones are completed. |
| 16 | #15 | Create GitHub milestones and project board | 3 | 3 | Defer / Wishlist | Useful for roadmap clarity, but not as urgent as enforcement, safety, and CI. |
| 17 | #16 | Define repository label taxonomy | 3 | 2 | Batch / Delegate | Useful for triage and search, especially after issue templates exist. |
| 18 | #20 | Add structured logging | 4 | 3 | Strategic Build | Important before field testing, but should follow config, policy, and risk-register work. |
| 19 | #4 | Feature wishlist backlog | 2 | 1 | Batch / Delegate | Living backlog; maintain continuously rather than completing as a sprint. |

## Current recommended sprint order

```text
#5  Branch protection / required CI
#17 Stale docs cleanup
#7  Issue templates
#12 Split CI checks
#9  Secret scanning and push protection
#13 SECURITY.md
#8  Dependabot
#18 Risk register
#19 Typed config validation
#1  v0.2 response policy, rate limits, and MORE
```

## Reprioritization triggers

Re-score issues when:

- a PR fails CI unexpectedly
- a security or secret risk is discovered
- a live-radio task becomes imminent
- a user or collaborator is blocked
- the AI Reviewer identifies a repeated process weakness
- an issue expands in scope or complexity
- a dependency becomes required by another issue

## AI Reviewer feedback loop

AI Reviewer reports may propose changes to this ledger when they identify repeated quality patterns.

Example:

```text
Observation: PRs keep changing docs without updating related SOPs.
Recommendation: Increase priority for issue-template and AI-reviewer workflow tasks.
```

Human maintainers retain final priority authority.
