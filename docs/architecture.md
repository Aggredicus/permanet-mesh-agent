# Architecture

PermaNet Mesh Agent is designed as a small, testable Python service with hard separation between radio I/O, command routing, policy, AI backends, and storage.

## Data flow

```text
Radio adapter
  -> IncomingMessage
  -> CommandParser
  -> MeshRouter
  -> policy checks
  -> command handler or AI backend
  -> OutgoingMessage
  -> radio adapter send
```

## MVP architecture

The v0.1 scaffold uses a mock radio and mock AI backend so the full behavior can be tested without hardware.

```text
MockRadio.receive_text()
  -> MeshRouter.route()
  -> CommandParser.parse()
  -> handle_command()
  -> MockAIBackend.answer() when needed
  -> OutgoingMessage
```

## Module boundaries

- `radio/`: adapters for mock radio and future Meshtastic transports.
- `protocol/`: normalized message models independent of Meshtastic packet shape.
- `commands/`: summon parsing and command handlers.
- `routing/`: public/private/admin routing decisions.
- `ai/`: backend protocol and implementations.
- `policy/`: rate limits, permissions, privacy, and mesh etiquette.
- `storage/`: future SQLite persistence.

## Non-negotiable behavior

Public mesh channels must remain summon-only. Normal public chatter without `@permanet` or another configured summon phrase must be ignored.

## Future hardware integration

The first live adapter should support a Meshtastic node connected over serial/USB. TCP, BLE, and meshtasticd support can follow after the ping bot works reliably.
