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

## Public response limits and MORE

Public responses must stay short enough for mesh etiquette and bandwidth constraints.

When a generated answer is longer than the configured response limit, the router returns only the first chunk and stores the remaining chunks in memory. The bot does not automatically send every chunk.

If more content is available, the first chunk may end with:

```text
Reply MORE for next step.
```

The user can then request exactly one continuation chunk with:

```text
@permanet more
```

If no continuation is pending, the bot returns:

```text
No pending response. Ask a question first.
```

Continuation state is keyed by node ID and channel index so one user or channel does not accidentally receive another user's pending answer.

## Cooldowns

Summoned public commands can be rate-limited by node and channel to reduce spam, loops, and accidental repeated invocations.

Cooldown messages should be short, for example:

```text
Cooldown active. Try again in 30 seconds.
```

Unsummoned public chatter is still ignored and should not produce cooldown replies.

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
