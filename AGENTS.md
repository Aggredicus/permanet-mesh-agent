# AGENTS.md

This file defines how human developers and AI coding agents should work in the PermaNet Mesh Agent repository.

## Project mission

PermaNet Mesh Agent is a summon-only Meshtastic chatbot gateway. It should listen for short prompts over a LoRa mesh, route them through a safe command and permission layer, optionally generate concise AI responses, and send short replies back over the mesh.

## Core mesh safety rule

Never implement behavior that automatically replies to all public Meshtastic messages.

The bot must only respond on public channels when explicitly invoked with an approved summon phrase such as `@permanet` or `/permanet`.

## Development priorities

1. Mock-first correctness before hardware integration.
2. Radio adapters isolated from business logic.
3. Public summon-only behavior preserved by tests.
4. Private channel behavior explicitly configured.
5. Admin commands protected by allowlisted node identities.
6. Short, radio-safe responses by default.

## Repository map

```text
src/permanet_agent/commands/   command parsing and handlers
src/permanet_agent/routing/    message routing decisions
src/permanet_agent/radio/      radio adapters and mock radio
src/permanet_agent/protocol/   normalized message models
src/permanet_agent/ai/         AI backend interfaces and implementations
tests/                         quality gates for command and routing behavior
docs/                          project, architecture, hardware, and deployment notes
examples/                      sample configs and transcripts
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

## Coding style

- Prefer small, testable modules.
- Keep hardware-specific code behind radio adapters.
- Keep AI backend calls behind a protocol/interface.
- Do not hardcode private channel names, PSKs, node IDs, API keys, or client information.
- Use examples and `.env.example` for configuration templates.

## MVP target

The first success condition is:

```text
Input:  @permanet ping
Output: pong
```

The first milestone must work with mock radio before live hardware.
