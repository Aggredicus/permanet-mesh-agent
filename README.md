# PermaNet Mesh Agent

PermaNet Mesh Agent is an off-grid AI chatbot gateway for Meshtastic networks. It listens for short text prompts over a LoRa mesh network, routes them through a safe command and permission layer, optionally generates concise AI responses, and sends replies back over the mesh.

The project is designed for field crews, permaculture designers, local resilience groups, client project teams, and other low-connectivity use cases where lightweight, radio-safe AI assistance would be useful.

## Start here

If you are reviewing this repository for the first time, read these in order:

1. [`docs/developer-handoff.md`](docs/developer-handoff.md) — fastest technical orientation for a backend developer.
2. [`AGENTS.md`](AGENTS.md) — safety rules for human and AI-assisted development.
3. [`docs/architecture.md`](docs/architecture.md) — module boundaries and data flow.
4. [`docs/channel-policy.md`](docs/channel-policy.md) — public, private, and admin channel behavior.
5. [`docs/roadmap.md`](docs/roadmap.md) — completed milestones and next implementation target.

## Current milestone

**v0.2.0 complete:** the repository now has mock-first command routing, response policy, explicit `MORE` pagination, cooldowns, tests, docs, and CI smoke checks.

The project remains mock-first and is **not** live-radio-ready yet. The next implementation milestone is:

```text
v0.3.0 — Meshtastic serial ping bot
```

The first live-hardware milestone is simple:

```text
@permanet ping
```

Expected response:

```text
pong
```

## Core rules

1. Never auto-reply to all public mesh messages.
2. Public channels are summon-only.
3. Keep responses short enough for mesh use.
4. Long responses continue only through explicit `MORE` requests.
5. Private group behavior must be explicitly configured.
6. Admin commands require an allowlisted node identity.
7. Hardware-facing code must be isolated behind radio adapters.

## MVP command set

```text
@permanet help
@permanet ping
@permanet ask <question>
@permanet more
```

## Recommended architecture

```text
Meshtastic node / mock radio
        |
        v
radio adapter
        |
        v
message parser -> router -> policy layer -> command handler / AI backend
        |
        v
response compressor / pagination cache
        |
        v
outgoing mesh message
```

## Repository map

```text
src/permanet_agent/      Python service package
docs/                    Human and developer documentation
docs/sops/               Engineering quality SOPs
.cursor/rules/           Cursor-specific development rules
examples/                Configs, transcripts, and packet examples
tests/                   Unit and integration-style tests
deploy/                  systemd / future deployment assets
scripts/                 Developer helper scripts
```

## Engineering workflow

This repo uses an issue-first, branch-first, PR-reviewed workflow. See:

- [`docs/sops/branching-and-release.md`](docs/sops/branching-and-release.md)
- [`docs/sops/ai-coding-quality-system.md`](docs/sops/ai-coding-quality-system.md)
- [`docs/sops/pull-request-quality-gate.md`](docs/sops/pull-request-quality-gate.md)

## Development quick start

```bash
git clone https://github.com/Aggredicus/permanet-mesh-agent.git
cd permanet-mesh-agent
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected smoke behavior:

```text
@permanet ping -> pong
hello mesh -> no output
```

## Current status

This repository is intentionally mock-first. The mock adapter lets development proceed safely before physical Meshtastic devices are connected.

Implemented:

- mock radio adapter
- command parser
- summon-only router
- mock AI backend
- `help`, `ping`, `ask`, and `more` commands
- response policy for mesh-safe chunking
- in-memory `MORE` pagination cache
- basic per-node and per-channel cooldown guard
- tests for summon-only behavior, response policy, pagination, and cooldowns
- CLI smoke checks for `@permanet ping` and unsummoned public chatter
- architecture, channel policy, hardware, roadmap, and handoff docs
- GitHub Actions CI

Next milestone:

```text
v0.3.0 — Meshtastic serial ping bot
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The most important rule is that public mesh messages must remain summon-only.

## License

This project currently uses a temporary all-rights-reserved notice while the long-term license is being decided. See [`LICENSE.md`](LICENSE.md).
