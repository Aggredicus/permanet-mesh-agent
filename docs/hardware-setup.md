# Hardware Setup

This project should begin with a small, reliable test kit rather than a large fleet.

## Minimum prototype kit

- 3 Meshtastic-compatible LoRa nodes.
- 1 always-on Linux host such as a Raspberry Pi, mini PC, or laptop.
- USB data cables for gateway-node development.
- Region-appropriate antennas.
- Battery packs or USB power supplies.
- Optional weather-resistant enclosure for later field deployment.

## Recommended first topology

```text
Phone + handheld node
        |
        | LoRa mesh
        v
Gateway Meshtastic node -- USB --> Linux host running PermaNet Mesh Agent
        ^
        |
Spare/test node
```

## Development sequence

1. Verify phone-to-node Meshtastic messaging.
2. Verify node-to-node messaging.
3. Connect one node to the Linux host.
4. Run the Python mock bot locally.
5. Add a serial Meshtastic adapter.
6. Test `@permanet ping` over the real mesh.

## Hardware testing rule

No live radio behavior should be added until the same flow passes through `MockRadio` tests first.
