# PermaNet Mesh Agent

PermaNet Mesh Agent is an off-grid AI chatbot gateway for Meshtastic networks. It listens for short text prompts over a LoRa mesh network, routes them through a safe command and permission layer, optionally generates concise AI responses, and sends replies back over the mesh.

The project is designed for field crews, permaculture designers, local resilience groups, client project teams, and other low-connectivity use cases where lightweight, radio-safe AI assistance would be useful.

## Current milestone

**v0.1.0 target:** build and test a mock-radio command bot before connecting to physical Meshtastic hardware.

The first hardware milestone is simple:

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
examples/                Configs, transcripts, and packet examples
tests/                   Unit and integration-style tests
deploy/                  systemd / future deployment assets
scripts/                 Developer helper scripts
```

## Development quick start

```bash
git clone https://github.com/Aggredicus/permanet-mesh-agent.git
cd permanet-mesh-agent
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m permanet_agent.main --mock --message "@permanet ping"
pytest
```

## Status

This repository is intentionally scaffolded around a mock-first workflow. The mock adapter lets development proceed before all physical Meshtastic devices are available.

## License

License TBD by project owner before public reuse, packaging, or commercial distribution.
