# AGENTS.md

This file defines how human developers and AI coding agents should work in the PermaNet Mesh Agent repository.

## Project mission

PermaNet Mesh Agent is a summon-only Meshtastic chatbot gateway. It should listen for short prompts over a LoRa mesh, route them through a safe command and permission layer, optionally generate concise AI responses, and send short replies back over the mesh.

## Core mesh safety rule

Never implement behavior that automatically replies to all public Meshtastic messages.

The bot must only respond on public channels when explicitly invoked with an approved summon phrase such as `@permanet` or `/permanet`.

## Branching and quality workflow

All human and AI-assisted implementation work should follow:

- `docs/sops/branching-and-release.md`
- `docs/sops/ai-coding-quality-system.md`
- `docs/sops/pull-request-quality-gate.md`
- `docs/sops/issue-prioritization.md`
- `docs/sops/multi-agent-concurrency.md`

Cursor-specific behavior is defined in:

- `.cursor/rules/branching.mdc`
- `.cursor/rules/quality-gates.mdc`

Planning and prioritization are tracked in:

- `docs/planning/priority-ledger.md`

Active coordination should remain repo-native and app-functional. Use issues, pull requests, branches, PR template fields, issue comments, assignment tables, local scripts, and CI as the canonical workflow surfaces. A GitHub Project Board may be used later as an optional aid if it is actively maintained, but it is not required for normal work.

Rules:

- Do not implement feature work directly on `main`.
- Create or use an issue-linked branch before editing code.
- Preserve public summon-only behavior.
- Do not claim tests passed unless they were actually run.
- Stop before high-risk behavior changes.
- PR summaries must include validation evidence and a rollback plan.
- Use the priority ledger and prioritization SOP when selecting or reordering work.
- Use the multi-agent concurrency SOP before coordinated AI-agent work.
- Treat required GitHub checks as merge-blocking once branch protection is active.

## Protected main expectations

`main` is intended to be protected by GitHub branch protection or repository rulesets.

Agents should assume these expectations apply even if GitHub settings are still being configured:

```text
Pull requests are required before merge.
test must pass before merge.
Force pushes to main are not allowed.
Deleting main is not allowed.
Conversation resolution is required if available.
```

Agents must not bypass, weaken, or claim completion of branch protection settings unless the settings were explicitly verified in GitHub.

## Development priorities

1. Mock-first correctness before hardware integration.
2. Radio adapters isolated from business logic.
3. Public summon-only behavior preserved by tests.
4. Private channel behavior explicitly configured.
5. Admin commands protected by allowlisted node identities.
6. Short, radio-safe responses by default.
7. Issue-first, branch-first, evidence-backed changes.
8. Priority/complexity scoring before large backlog reordering.
9. Coordinated multi-agent work before parallel execution.
10. Repo-native assignment metadata before agents edit assigned work.

## Repository map

```text
src/permanet_agent/commands/   command parsing and handlers
src/permanet_agent/routing/    message routing decisions
src/permanet_agent/radio/      radio adapters and mock radio
src/permanet_agent/protocol/   normalized message models
src/permanet_agent/ai/         AI backend interfaces and implementations
tests/                         quality gates for command and routing behavior
docs/                          project, architecture, hardware, and deployment notes
docs/sops/                     engineering quality SOPs
docs/planning/                 roadmap and priority planning artifacts
docs/templates/                reusable coordination and planning templates
.cursor/rules/                 Cursor-specific development rules
```

## Required behavior tests

Every change that affects message routing must preserve these behaviors:

- Public chatter without a summon phrase is ignored.
- `@permanet ping` returns `pong`.
- `@permanet help` returns the command list.
- `@permanet ask <question>` routes to the configured AI backend.
- Unknown commands return a short help-oriented response.

## Stop rules for agents

Stop and ask for human review before:

- Adding behavior that sends multiple packets automatically.
- Adding admin commands that affect configuration, logs, storage, keys, or channel state.
- Adding live Meshtastic transmission behavior that has not been tested with a mock adapter.
- Adding dependency-heavy services such as dashboards, brokers, vector databases, or cloud infrastructure.
- Changing public-channel summon behavior.
- Working directly on `main` for feature or governance work.
- Claiming validation success without command output or explicit evidence.
- Reordering high-priority safety work without updating the priority ledger rationale.
- Starting parallel agent work without checking active issues, PRs, branches, file ownership, and assignment metadata.
- Merging while required GitHub checks are failing, pending, or missing.
- Claiming branch protection is enabled without verified GitHub settings evidence.

## Coding style

- Prefer small, testable modules.
- Keep hardware-specific code behind radio adapters.
- Keep AI backend calls behind a protocol/interface.
- Do not hardcode private channel names, PSKs, node IDs, API keys, or client information.
- Use examples and `.env.example` for configuration templates.
- Keep implementation scoped to the linked issue.

## Current milestone

The project has completed the mock-first v0.2 response-safety milestone. The next implementation milestone is:

```text
v0.3.0 — Meshtastic serial ping bot
```

The first live-hardware success condition is:

```text
Input:  @permanet ping
Output: pong
```

This must continue to work with mock radio before and after live hardware support is added.
