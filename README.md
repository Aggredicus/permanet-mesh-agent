# PermaNet Mesh Agent

PermaNet Mesh Agent is an off-grid AI chatbot gateway for Meshtastic networks. It listens for short text prompts over a LoRa mesh network, routes them through a safe command and permission layer, optionally generates concise AI responses, and sends replies back over the mesh.

The project is designed for field crews, permaculture designers, local resilience groups, client project teams, and other low-connectivity use cases where lightweight, radio-safe AI assistance would be useful.

## Start here

If you are reviewing this repository for the first time, read these in order:

1. [`docs/developer-handoff.md`](docs/developer-handoff.md) — fastest technical orientation for a backend developer.
2. [`AGENTS.md`](AGENTS.md) — safety rules for human and AI-assisted development.
3. [`docs/architecture.md`](docs/architecture.md) — module boundaries and data flow.
4. [`docs/channel-policy.md`](docs/channel-policy.md) — public, private, and admin channel behavior.
5. [Issue #1](https://github.com/Aggredicus/permanet-mesh-agent/issues/1) — v0.2.0 planning checklist.

## Current phase

The initial v0.1 scaffold is complete and remains mock-first.

Current priority flow:

1. [Issue #5](https://github.com/Aggredicus/permanet-mesh-agent/issues/5) - enforce branch protection and required checks on `main`.
2. [Issue #1](https://github.com/Aggredicus/permanet-mesh-agent/issues/1) - deliver v0.2 response policy, rate limits, and `MORE` pagination.

The first live-hardware milestone remains:

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
4. Private group behavior must be explicitly configured.
5. Admin commands require an allowlisted node identity.
6. Hardware-facing code must be isolated behind radio adapters.

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
response compressor
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
```

Expected output:

```text
pong
```

## Current status

The v0.1 scaffold is complete and intentionally mock-first. The mock adapter lets development proceed before all physical Meshtastic devices are available.

Implemented:

- mock radio adapter
- command parser
- basic router
- mock AI backend
- `help`, `ping`, `ask`, and placeholder `more` commands
- tests for summon-only public behavior
- architecture, channel policy, hardware, roadmap, and handoff docs
- GitHub Actions CI

Next milestone:

```text
v0.2.0 — response policy, rate limits, and MORE pagination
```

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The most important rule is that public mesh messages must remain summon-only.

## License

This project currently uses a temporary all-rights-reserved notice while the long-term license is being decided. See [`LICENSE.md`](LICENSE.md).
