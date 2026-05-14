# Agent Priority Ledger

This ledger records the current prioritized issue order for `permanet-mesh-agent`.

It is intended to be readable by humans, Cursor, Codex, ChatGPT, and future AI reviewer agents. The ledger is not a replacement for GitHub Issues or GitHub Projects. GitHub Issues and Pull Requests remain the live source of truth for issue state, PR state, merge state, branch activity, labels, and assignees.

## Source-of-truth rule

Before starting work, humans and AI agents must verify live GitHub state instead of trusting this ledger alone.

Check:

```text
1. Is the issue still open?
2. Is there already an open PR for the issue?
3. Is there already an active branch for the issue?
4. Has main changed since this ledger was updated?
5. Has a milestone PR recently merged that changes status docs?
6. Are the labels, status, and acceptance criteria still current?
```

If this ledger conflicts with GitHub, GitHub wins and the ledger should be refreshed in a small docs-only PR.

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

## Current status snapshot

This ledger was refreshed after PR #39 merged the stale-agent-PR documentation cleanup.

Known completed or superseded work should not be selected as active sprint work:

```text
#1  v0.2 response policy, cooldowns, and MORE pagination — completed by PR #35
#7  GitHub issue templates — completed/superseded by #24 and PR #25
#17 stale milestone wording cleanup — completed by PR #39
#30 required-check wording cleanup — completed by PR #39
#38 stale agent PR consolidation — completed by PR #39
```

The current implementation milestone is:

```text
v0.3.0 — Meshtastic serial ping bot
```

The project remains mock-first and not live-radio-ready until that milestone is implemented and verified.

## Current ranked active issues

| Rank | Issue | Title | Priority | Complexity | Category | Rationale |
|---:|---:|---|---:|---:|---|---|
| 1 | #40 | Add multi-agent concurrency protocol for coordinated Codex and AI-assisted development | 5 | 2 | Do Now | Directly addresses the duplicate/stale PR failure mode from the recent multi-agent run and should be in place before running many agents again. |
| 2 | #18 | Add project risk register for mesh safety and AI-assisted development | 5 | 2 | Do Now | Captures live-radio, public-mesh, secret, AI, and operational risks before v0.3 hardware work. |
| 3 | #13 | Add SECURITY.md and vulnerability reporting policy | 4 | 2 | Do Now | Establishes responsible disclosure and security expectations before secrets, PSKs, hardware, or AI provider keys become more relevant. |
| 4 | #9 | Enable and document secret scanning and push protection | 5 | 3 | Strategic Build | High safety value, but may require GitHub settings verification in addition to docs, so it should be coordinated carefully. |
| 5 | #8 | Add Dependabot configuration for Python dependencies and GitHub Actions | 3 | 2 | Batch / Delegate | Low-risk dependency hygiene improvement that can run safely in parallel if file ownership is clear. |
| 6 | #11 | Add CODEOWNERS for review ownership and high-risk areas | 3 | 2 | Batch / Delegate | Helps review routing and supports future coordinated-agent work once ownership expectations are agreed. |
| 7 | #19 | Add typed config loader and validation for safe defaults | 4 | 3 | Strategic Build | Turns documented safe defaults into validated runtime behavior before live adapters depend on config. |
| 8 | #37 | Refactor repository workflows and docs from Cursor-centric to Codex-optimized performance and quality model | 4 | 3 | Strategic Build | Useful after #40, because the concurrency protocol should define the coordination baseline for broader Codex workflow refactoring. |
| 9 | #12 | Split CI into separate test, lint, branch policy, and format checks | 4 | 3 | Strategic Build | Improves check clarity, but changes required-check names and branch-policy behavior, so it should follow the concurrency SOP and docs consistency rules. |
| 10 | #20 | Add structured logging for command routing and mesh safety events | 4 | 3 | Strategic Build | Important before field testing, but should follow risk/config work so logging avoids sensitive data and has clear safety requirements. |
| 11 | #10 | Enable CodeQL code scanning for Python security and quality checks | 3 | 2 | Batch / Delegate | Adds security scanning with low runtime risk after the security workflow is clarified. |
| 12 | #14 | Add CHANGELOG and release tagging workflow | 3 | 2 | Batch / Delegate | Improves milestone traceability before more releases are tagged. |
| 13 | #16 | Define repository label taxonomy for type, area, risk, and status | 3 | 2 | Batch / Delegate | Useful for triage and project hygiene, especially after the concurrency SOP formalizes agent roles. |
| 14 | #15 | Create GitHub milestones and project board for roadmap tracking | 3 | 3 | Defer / Wishlist | Valuable, but not as urgent as safety, security, config, and concurrency controls. |
| 15 | #36 | Add progress-report infographic generator from YAML project state | 3 | 3 | Defer / Wishlist | Helpful deterministic reporting artifact, but less urgent than safety/process foundations and v0.3 readiness. |
| 16 | #4 | Feature wishlist backlog | 2 | 1 | Batch / Delegate | Living idea bank; maintain continuously rather than completing as a single sprint. |

## Current recommended sprint order

```text
#40 Multi-agent concurrency SOP
#18 Risk register
#13 SECURITY.md
#9  Secret scanning and push protection
#8  Dependabot
#11 CODEOWNERS
#19 Typed config validation
v0.3 Meshtastic serial ping bot
#37 Codex workflow refactor
```

## Parallelization guidance

Safe concurrent work requires explicit coordination.

Safer parallel examples:

```text
Worker A -> #13 SECURITY.md only
Worker B -> #8 .github/dependabot.yml only
Worker C -> #18 docs/risk-register.md only
Reviewer -> review all PRs for branch freshness, duplicate issue work, and validation evidence
```

Risky parallel examples:

```text
Worker A -> AGENTS.md
Worker B -> CONTRIBUTING.md
Worker C -> docs/sops/pull-request-quality-gate.md
Worker D -> docs/roadmap.md
```

Shared status, workflow, and milestone docs should usually be changed in one coordinated PR.

## Reprioritization triggers

Re-score issues when:

- a PR fails CI unexpectedly
- a security or secret risk is discovered
- a live-radio task becomes imminent
- a user or collaborator is blocked
- the AI Reviewer identifies a repeated process weakness
- an issue expands in scope or complexity
- a dependency becomes required by another issue
- a PR merges that completes, supersedes, or changes the scope of a ranked issue

## AI Reviewer feedback loop

AI Reviewer reports may propose changes to this ledger when they identify repeated quality patterns.

Example:

```text
Observation: Multiple agents opened duplicate or stale PRs for the same issues.
Recommendation: Increase priority for #40 and require live issue/PR/branch preflight before edits.
```

Human maintainers retain final priority authority.
