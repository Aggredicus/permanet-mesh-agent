# Governance Invariants

## Purpose

This document turns PermaNet's governance values into concrete repository mechanisms.

The goal is to prevent values language from becoming decorative. A project should not receive credit for words like regenerative, transparent, mutual-aid, or non-extractive unless those values are supported by practices that can be inspected, improved, and repaired.

This roadmap is intentionally repo-native. The active workflow should work through:

```text
GitHub issues
GitHub pull requests
branches
repo documents
issue templates
PR templates
issue comments
assignment tables
local scripts
CI
human review
```

A GitHub Project Board may be used later as an optional aid if it becomes easy to maintain, but it is not required for this invariant roadmap.

## Completion standard

Each invariant should eventually have at least:

```text
1 concrete mechanism
1 recordkeeping practice
1 feedback loop
1 anti-abuse safeguard
```

Definitions:

| Requirement | Meaning |
|---|---|
| Concrete mechanism | A real process, file, template, script, checklist, or rule that changes behavior. |
| Recordkeeping practice | A durable place where decisions, evidence, status, or outcomes are recorded. |
| Feedback loop | A way to review results and improve the system after use. |
| Anti-abuse safeguard | A boundary that prevents harm, hidden authority, overclaiming, extraction, spam, unsafe deployment, or contributor confusion. |

An invariant is not considered strengthened merely because the repo says it values the invariant.

## Invariant types

Some invariants apply primarily to repository governance now. Others become more concrete during live field deployment.

### Repo-governance invariants

These can be strengthened immediately through repository process:

```text
Voluntary association
Mutual aid
Transparent governance
Skill transmission
Open records
Non-extractive economics
Conflict repair
```

### Future field-deployment invariants

These should be planned now and implemented more fully before or during v0.3+ field work:

```text
Ecological regeneration
Respect for place-based knowledge
Real-world beneficial action
```

The field-deployment invariants should not be claimed as achieved until there are actual deployment records or real-world outcomes.

## The 10 invariants

## 1. Ecological regeneration

PermaNet context:

```text
The project should not claim ecological or regenerative impact unless it can point to real deployments, field reports, restoration coordination, community benefit, or ecological evidence.
```

Current status:

```text
Future field-deployment invariant.
```

Possible mechanisms:

- impact ledger
- field-test report template
- deployment outcome records
- evidence categories for planned, tested, and verified impact

Recordkeeping examples:

- `docs/impact-ledger.md`
- `docs/templates/field-test-report.md`
- issue comments linking to field results

Feedback loop examples:

- review field-test lessons before the next live test
- compare claimed benefits against recorded outcomes
- update risk register after field observations

Anti-abuse safeguards:

- no ecological impact claims without evidence
- no public/client claims based only on plans or aesthetics
- protect sensitive field locations and private community data

Recommended follow-up issue:

```text
Strengthen invariant: Ecological regeneration
```

## 2. Voluntary association

PermaNet context:

```text
Contributors, maintainers, collaborators, and agents should have clear ways to accept, decline, pause, transfer, or exit work.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- task acceptance and reassignment rules
- contributor pause/decline workflow
- stale branch and abandoned PR cleanup process
- agent stop rules for unclear scope

Recordkeeping examples:

- issue comments stating assignment and ownership
- PR body concurrency notes
- `docs/templates/agent-assignment-table.md`

Feedback loop examples:

- review abandoned or stale work during sprint cleanup
- update assignment language when contributors become confused

Anti-abuse safeguards:

- no contributor is assumed to own a task forever
- no agent should continue when scope or authority is unclear
- maintainers can reassign stalled work transparently

Recommended follow-up issue:

```text
Strengthen invariant: Voluntary association
```

## 3. Mutual aid

PermaNet context:

```text
The repo should make it easy for blocked contributors or agents to request support instead of silently failing, duplicating work, or abandoning context.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- Help Needed or Needs Support issue comments
- reviewer support path
- maintainer escalation path
- stale PR rescue workflow

Recordkeeping examples:

- issue comments with blocker descriptions
- PR comments requesting reviewer support
- assignment tables that show blocked status

Feedback loop examples:

- identify repeated blockers after failed PRs
- convert common blockers into SOP updates or templates

Anti-abuse safeguards:

- support requests should not pressure unpaid contributors
- maintainers remain final authority for scope and safety
- blocked status should not be treated as failure or blame

Recommended follow-up issue:

```text
Strengthen invariant: Mutual aid
```

## 4. Transparent governance

PermaNet context:

```text
Project decisions, authority boundaries, risk, validation state, and review outcomes should be visible in durable repo-native records.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- documented maintainer authority boundaries
- issue-first, branch-first, PR-reviewed workflow
- PR validation evidence
- governance decision records in issues or docs

Recordkeeping examples:

- GitHub issues
- PR bodies and reviews
- commit history
- SOP updates
- CI results

Feedback loop examples:

- docs consistency review after governance changes
- post-merge issue cleanup
- priority-ledger refresh after major process PRs

Anti-abuse safeguards:

- no hidden authority changes in private chat only
- no claiming checks passed unless CI or command output proves it
- no autonomous merges by agents

Recommended follow-up issue:

```text
Strengthen invariant: Transparent governance
```

## 5. Skill transmission

PermaNet context:

```text
Fresh humans and fresh agents should be able to understand the repo, its safety rules, and its workflow without relying on private chat memory.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- new-agent quickstart
- first 10 minutes in the repo guide
- good issue and good PR examples
- onboarding checklist

Recordkeeping examples:

- `AGENTS.md`
- `CONTRIBUTING.md`
- SOPs
- templates

Feedback loop examples:

- update onboarding when agents make repeated mistakes
- add examples after successful high-quality PRs

Anti-abuse safeguards:

- do not hide required knowledge in private chat
- do not let agents infer authority that is not documented
- require evidence-backed claims in PRs

Recommended follow-up issue:

```text
Strengthen invariant: Skill transmission
```

## 6. Respect for place-based knowledge

PermaNet context:

```text
Future Meshtastic or field deployments should respect local radio norms, terrain, community consent, privacy, legal constraints, and deployment context.
```

Current status:

```text
Future field-deployment invariant.
```

Possible mechanisms:

- hardware field-test SOP
- local deployment context fields
- channel norms checklist
- privacy and consent notes

Recordkeeping examples:

- field-test reports
- risk register entries
- deployment notes that redact sensitive details

Feedback loop examples:

- update test procedures after field observations
- revise channel behavior based on local mesh etiquette

Anti-abuse safeguards:

- no live-radio deployment without mock proof first
- no public channel spam
- no exposure of private node IDs, PSKs, locations, or client data

Recommended follow-up issue:

```text
Strengthen invariant: Respect for place-based knowledge
```

## 7. Open records

PermaNet context:

```text
Important decisions should live in issues, PRs, commits, docs, or CI results instead of only in private chats, private notes, or manually maintained planning surfaces.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- issue-first workflow
- PR summaries with validation evidence
- priority-ledger refreshes
- durable decision records
- repo-native assignment metadata

Recordkeeping examples:

- GitHub issues
- PR bodies
- PR reviews
- commit history
- CI results
- SOPs

Feedback loop examples:

- reconcile priority ledger after major merges
- convert repeated chat decisions into issues or docs

Anti-abuse safeguards:

- private planning surfaces do not override issues, PRs, commits, or CI
- important decisions should not be hidden in chat memory
- GitHub state wins when planning docs conflict with live repo state

Recommended follow-up issue:

```text
Strengthen invariant: Open records
```

## 8. Non-extractive economics

PermaNet context:

```text
Contributor credit, attribution, labor expectations, ownership, and commercialization expectations should be clear before more people contribute or the project becomes commercial.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- contributor credit policy
- attribution norms
- commercialization disclosure expectations
- licensing clarity
- unpaid labor boundaries

Recordkeeping examples:

- `CONTRIBUTING.md`
- future contributor governance SOP
- issue/PR acknowledgements
- release notes or changelog credits

Feedback loop examples:

- review contributor expectations before external recruitment
- update policy before monetization or public service deployment

Anti-abuse safeguards:

- do not imply compensation unless it exists
- do not use vague community language to hide ownership or benefit flows
- do not obscure licensing or commercialization expectations

Recommended follow-up issue:

```text
Strengthen invariant: Non-extractive economics
```

## 9. Conflict repair

PermaNet context:

```text
The repo should have a lightweight process for disagreements, PR disputes, harmful behavior, appeals, and maintainer intervention.
```

Current status:

```text
Repo-governance invariant.
```

Possible mechanisms:

- code of conduct
- contributor governance SOP
- PR/review dispute path
- second-review or appeal path
- anti-retaliation expectation
- emergency maintainer authority

Recordkeeping examples:

- issue or PR comments where appropriate
- maintainer decision notes
- conduct document updates

Feedback loop examples:

- convert repeated disputes into clearer contribution rules
- review unresolved conflicts during governance cleanup

Anti-abuse safeguards:

- no harassment or retaliation
- no unreviewable authority changes
- emergency maintainer authority should be bounded by safety and documented after use where appropriate

Recommended follow-up issue:

```text
Strengthen invariant: Conflict repair
```

## 10. Real-world beneficial action

PermaNet context:

```text
The project should distinguish useful completed outcomes from plans, aesthetics, demos, or claims.
```

Current status:

```text
Future field-deployment invariant.
```

Possible mechanisms:

- field-test report template
- deployment records
- practical benefit evidence
- beneficiary/context notes
- lessons learned

Recordkeeping examples:

- field-test reports
- impact ledger
- roadmap updates
- issue comments linking to evidence

Feedback loop examples:

- review what worked before next deployment
- update risk register after practical failures
- separate planned, tested, and verified outcomes

Anti-abuse safeguards:

- no real-world benefit claims without evidence
- no live-radio behavior without mock-first proof
- no exposing private field data or community-sensitive context

Recommended follow-up issue:

```text
Strengthen invariant: Real-world beneficial action
```

## Recommended phases

## Phase 1 — Governance integrity

Prioritize before or alongside v0.3 planning:

```text
Open records
Transparent governance
Conflict repair
Voluntary association
Non-extractive economics
```

Purpose:

```text
Stabilize how people and agents coordinate, decide, review, record, and repair work.
```

## Phase 2 — Contributor support and learning

Prioritize as collaboration expands:

```text
Skill transmission
Mutual aid
```

Purpose:

```text
Make the repo easier to join, learn, support, and rescue when work gets blocked.
```

## Phase 3 — Field deployment integrity

Prioritize before or during v0.3+ live field work:

```text
Real-world beneficial action
Respect for place-based knowledge
Ecological regeneration
```

Purpose:

```text
Ensure future deployment claims are grounded in context, evidence, and real benefit.
```

## Cross-invariant dependencies

```text
Open records -> transparent governance
Conflict repair -> voluntary association
Non-extractive economics -> mutual aid
Skill transmission -> voluntary association
Respect for place-based knowledge -> real-world beneficial action
Real-world beneficial action -> ecological regeneration
```

Use these dependencies when deciding implementation order.

## Follow-up issue plan

Create or track one focused issue for each invariant using this naming pattern:

```text
Strengthen invariant: Ecological regeneration
Strengthen invariant: Voluntary association
Strengthen invariant: Mutual aid
Strengthen invariant: Transparent governance
Strengthen invariant: Skill transmission
Strengthen invariant: Respect for place-based knowledge
Strengthen invariant: Open records
Strengthen invariant: Non-extractive economics
Strengthen invariant: Conflict repair
Strengthen invariant: Real-world beneficial action
```

Each follow-up issue should include:

```text
Invariant:
Current status:
Concrete mechanism:
Recordkeeping practice:
Feedback loop:
Anti-abuse safeguard:
Likely files:
Non-goals:
Validation plan:
Rollback plan:
```

## Repo-native tracking guidance

Because the active workflow is repo-native, invariant work should be tracked through ordinary GitHub surfaces:

```text
issue title
issue body
labels when useful
PR body
PR review
commit history
SOP updates
CI results
```

Recommended issue metadata block:

```text
Invariant:
Phase:
Mechanism:
Recordkeeping:
Feedback loop:
Anti-abuse safeguard:
```

Optional future labels:

```text
invariant:ecological-regeneration
invariant:voluntary-association
invariant:mutual-aid
invariant:transparent-governance
invariant:skill-transmission
invariant:place-based-knowledge
invariant:open-records
invariant:non-extractive-economics
invariant:conflict-repair
invariant:real-world-benefit
```

Do not require a GitHub Project Board for invariant tracking. If a Project Board is used later, it should remain an optional coordination aid and must not replace issues, PRs, commits, docs, or CI as durable records.

## Non-goals

This roadmap does not:

- change runtime bot behavior
- enable live Meshtastic behavior
- change branch protection or repository rulesets
- require external project-management tools
- create compensation promises
- claim ecological impact without evidence
- require all 10 invariant follow-ups before v0.3 unless safety-critical
- replace human maintainer authority

## Validation for invariant work

For documentation/process-only invariant work, use:

```bash
python scripts/check_branch_policy.py
python scripts/check_concurrency_preflight.py
```

For runtime, hardware, or field-test related invariant work, also use:

```bash
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected smoke behavior must remain:

```text
@permanet ping -> pong
hello mesh -> no output
```

## Rollback guidance

If this roadmap creates too much overhead:

1. Keep this document as a short reference.
2. Preserve the highest-leverage follow-ups:
   - Open records
   - Transparent governance
   - Conflict repair
   - Voluntary association
   - Non-extractive economics
3. Defer field-deployment invariants until v0.3 hardware work begins.
4. Avoid adding mandatory tracking surfaces beyond issues, PRs, docs, scripts, and CI.

## Strategic outcome

This roadmap upgrades PermaNet from a technically safe AI-assisted repository into a more socially durable, human-supervised, repairable multi-agent engineering environment.

The aim is to make PermaNet safer not only against mesh spam and bad automation, but also against stale coordination state, hidden authority, unsupported claims, contributor confusion, conflict avoidance, and extractive collaboration patterns.
