from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(frozen=True)
class IncomingMessage:
    """Normalized incoming message from a radio adapter."""

    text: str
    node_id: str = "!mock"
    channel_index: int = 0
    is_direct: bool = False
    received_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass(frozen=True)
class OutgoingMessage:
    """Normalized outgoing message ready for a radio adapter."""

    text: str
    destination_node_id: str | None = None
    channel_index: int = 0
