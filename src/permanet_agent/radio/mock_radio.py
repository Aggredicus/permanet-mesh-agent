from __future__ import annotations

from dataclasses import dataclass, field

from permanet_agent.protocol.message import IncomingMessage, OutgoingMessage


@dataclass
class MockRadio:
    """In-memory radio adapter for tests and local development."""

    sent_messages: list[OutgoingMessage] = field(default_factory=list)

    def receive_text(self, text: str, node_id: str = "!mock", channel_index: int = 0) -> IncomingMessage:
        return IncomingMessage(text=text, node_id=node_id, channel_index=channel_index)

    def send(self, message: OutgoingMessage) -> None:
        self.sent_messages.append(message)
