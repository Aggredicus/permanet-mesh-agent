# Multi-Agent Concurrency SOP

## Purpose

This SOP defines how PermaNet Mesh Agent runs multiple AI-assisted contributors at the same time without creating duplicate pull requests, stale branches, overlapping edits, or unsupported validation claims.

Concurrent agents are useful only when their work is coordinated. The default goal is not maximum parallelism; it is safe, reviewable progress with clear ownership.

## Scope

This SOP covers process and documentation workflow for Codex, Cursor, ChatGPT, and other AI-assisted development tools.

It does not change runtime bot behavior.

For GitHub Project Board setup and operational use, also read:

```text
docs/sops/github-project-orchestration.md
```

## Core rule

Use coordinated concurrency, not independent concurrency.

Preferred model:

```text
1 Coordinator Agent
+
2–4 Worker Agents
+
1 Reviewer Agent
```

Avoid running many independent agents that each choose their own issue, branch, and files.

## Source of truth

Live GitHub state is the source of truth for:

- issue state
- pull request state
- branch existence
- merge state
- labels
- assignees
- CI/check status

Repository planning files such as `docs/planning/priority-ledger.md` are advisory and may lag behind recent merges. If a planning file conflicts with GitHub, GitHub wins and the planning file should be refreshed in a small docs-only PR.

When the GitHub Project Board exists, it is the coordination dashboard but not the factual source of truth. Issues, pull requests, commits, and CI remain factual truth.

## Coordinator Agent

The coordinator decides whether work can safely run in parallel.

The coordinator should not edit files unless explicitly assigned.

Responsibilities:

- inspect open issues
- inspect open PRs
- inspect active branches
- inspect GitHub Project Board assignments when available
- detect duplicate or stale work
- assign one issue per worker
- define allowed files per worker
- define forbidden files per worker
- decide whether related work belongs in one consolidated PR
- sequence work when shared docs or status files overlap
- produce a short assignment table before workers begin

Example assignment table:

```text
Worker A -> #13 -> SECURITY.md only
Worker B -> #18 -> docs/risk-register.md only
Worker C -> #8  -> .github/dependabot.yml only
Reviewer -> inspect all active PRs for freshness, duplication, validation, and safety claims
```

The coordinator must stop and ask for maintainer guidance when ownership, scope, or sequencing is unclear.

## Worker Agent

A worker implements exactly one assigned issue or task slice.

Responsibilities:

- verify the assigned issue is still open
- verify no open PR already targets the same issue
- verify no active branch already targets the same issue
- verify GitHub Project Board assignment when available
- create or use an issue-linked branch
- edit only assigned files
- keep the patch small and reviewable
- preserve non-goals from the issue
- run or request validation
- open a PR with real evidence and rollback plan
- never merge its own work

Workers must not:

- open duplicate PRs for an issue
- expand scope silently
- edit files outside their assigned ownership
- change runtime behavior from a process/docs issue
- mark checks as passed without evidence
- close issues automatically unless explicitly approved
- merge PRs automatically

## Reviewer Agent

The reviewer inspects active PRs and classifies them for maintainers.

Responsibilities:

- check linked issue alignment
- check branch naming policy
- check whether the branch is current with `main`
- check whether another PR already solves the same issue
- check file ownership conflicts
- check Project Board state when available
- check validation evidence
- check safety claims
- check docs consistency when workflow, status, milestone, or check names change
- classify each PR as merge-ready, needs changes, stale, duplicate, blocked, unsafe, or out of scope

The reviewer may recommend closing, superseding, or consolidating PRs, but the human maintainer makes final decisions.

## Required preflight checklist

Every agent must complete this before editing files:

```text
1. What issue am I solving?
2. Is the issue still open?
3. Is there already an open PR for this issue?
4. Is there already an active branch for this issue?
5. What files am I allowed to edit?
6. What files must I not edit?
7. Is my branch based on current main?
8. What validation proves success?
9. Could this conflict with another active PR?
10. Should this be one consolidated PR instead of parallel work?
11. If the Project Board exists, does the board assignment agree?
```

If any answer is unclear, stop and ask for maintainer guidance.

## One active PR per issue

Default rule:

```text
One active implementation PR per issue.
```

Parallel alternatives require explicit maintainer approval.

If an agent finds an existing PR for the issue, it must not open a duplicate PR. It should instead:

- review the existing PR
- comment with findings
- update the existing branch only if authorized
- or stop

## File ownership rules

Agents must declare intended file ownership before editing.

Safe parallel examples:

```text
Worker A -> SECURITY.md
Worker B -> .github/dependabot.yml
Worker C -> docs/risk-register.md
```

Risky parallel examples:

```text
Worker A -> README.md
Worker B -> docs/developer-handoff.md
Worker C -> docs/roadmap.md
Worker D -> CONTRIBUTING.md
```

Shared truth files should usually be changed in one coordinated PR. These include:

```text
README.md
AGENTS.md
CONTRIBUTING.md
docs/developer-handoff.md
docs/roadmap.md
docs/planning/priority-ledger.md
docs/sops/pull-request-quality-gate.md
```

## Branch naming rules

Use repository-approved branch patterns:

```text
feature/<issue-number>-short-description
fix/<issue-number>-short-description
docs/<issue-number>-short-description
quality/<issue-number>-short-description
experiment/<short-description>
release/vX.Y.Z
hotfix/vX.Y.Z-short-name
```

Use `quality/` for governance, process, validation, documentation quality, or agent workflow changes.

Do not work directly on `main` for feature, governance, or process changes.

## Branch freshness rule

Before opening a PR, agents must confirm the branch is current with `main`.

If `main` changed after the branch was created, re-check:

- linked issue state
- open PRs
- active branches
- changed files touched by the branch
- README
- developer handoff
- roadmap
- relevant SOPs
- required check name references

If a major milestone PR merged after the branch was created, assume status docs may be stale until re-read.

## Validation evidence rules

Agents must not mark validation complete unless a command actually ran and passed or GitHub Actions completed successfully.

Valid evidence examples:

```text
python scripts/check_branch_policy.py: passed
pytest: passed
ruff check .: passed
python -m permanet_agent.main --mock --message "@permanet ping": pong
python -m permanet_agent.main --mock --message "hello mesh": no output
test: passed
```

Invalid evidence examples:

```text
[x] pytest
Tests should pass
CI probably passes
Not run, but docs-only
```

When validation is not run because a change is documentation-only, state that clearly and do not imply runtime checks passed.

## CI status interpretation

Only this status counts as passed:

```text
success -> passed
```

These statuses do not count as passed:

```text
failure -> not passed
cancelled -> not passed
skipped -> not passed
pending -> not passed
action_required -> not passed
missing -> not passed
neutral -> not passed
```

Do not merge or recommend merge-ready status when required checks are pending, skipped, missing, blocked, or `action_required`.

## Docs consistency matrix

When changing project truth, review related docs together.

### Milestone or project-status changes

Review:

```text
README.md
docs/developer-handoff.md
docs/roadmap.md
CONTRIBUTING.md
docs/planning/priority-ledger.md
```

### Required-check-name changes

Review:

```text
AGENTS.md
CONTRIBUTING.md
docs/sops/pull-request-quality-gate.md
docs/sops/required-status-check.md
```

### Agent workflow changes

Review:

```text
AGENTS.md
CONTRIBUTING.md
docs/sops/ai-coding-quality-system.md
docs/sops/branching-and-release.md
docs/sops/pull-request-quality-gate.md
docs/sops/multi-agent-concurrency.md
docs/sops/github-project-orchestration.md
```

### Runtime safety behavior changes

Review:

```text
README.md
docs/channel-policy.md
docs/developer-handoff.md
docs/architecture.md
tests/
src/permanet_agent/routing/
src/permanet_agent/policy/
```

Runtime safety changes require tests and explicit human review.

## Safety invariants

All concurrent-agent work must preserve these invariants:

```text
Public mesh chatter without @permanet or /permanet receives no response.
```

```text
The bot never automatically replies to every public mesh message.
```

```text
No automatic multi-packet flooding is introduced.
```

```text
Live radio behavior is not enabled by default.
```

```text
No secrets, PSKs, API keys, private node IDs, private channel data, or client data are committed.
```

## Human authority

Humans remain final authority for:

- merges
- issue closure as completed
- release tags
- branch deletion
- branch protection or ruleset changes
- repository secrets
- security settings
- live radio behavior
- public deployment
- governance changes

Agents may draft, implement, review, and recommend. Agents do not autonomously finalize high-risk or irreversible repository actions.

## Rollback

If this protocol creates too much friction, simplify it to the minimum safe core:

```text
1. One active PR per issue.
2. Explicit file ownership.
3. Branch freshness check.
4. Real validation evidence.
5. Human merge authority.
```

Then reopen a narrower follow-up issue for the remaining coordination rules.
