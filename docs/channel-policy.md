# Channel Policy

PermaNet Mesh Agent supports three conceptual channel modes.

## 1. Public summon mode

Public channels are summon-only. The bot ignores all messages unless they begin with a configured summon phrase.

Examples:

```text
@permanet ping
@permanet help
@permanet ask how do I stabilize a wet slope?
```

Ignored:

```text
hello everyone
anyone around?
what plants work here?
```

## 2. Private group mode

Private group mode is intended for crews, clients, and project teams. Each group should have explicit configuration.

Example future config:

```yaml
private_groups:
  - name: field_crew
    index: 1
    allowed_nodes:
      - "!example"
```

## 3. Admin mode

Admin commands must only work for allowlisted node identities.

Examples of future admin commands:

```text
@permanet status
@permanet reload config
@permanet export logs
```

## Mesh etiquette

- Do not respond to unsummoned public chatter.
- Do not send automatic multi-packet floods.
- Keep answers short.
- Prefer `MORE` for continuation.
- Avoid sharing private group details on public channels.
