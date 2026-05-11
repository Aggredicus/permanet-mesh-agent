from __future__ import annotations

from permanet_agent.ai.base import AIBackend
from permanet_agent.commands.handlers import handle_command
from permanet_agent.commands.parser import CommandParser
from permanet_agent.protocol.message import IncomingMessage, OutgoingMessage


class MeshRouter:
    """Summon-only router for MVP public channel behavior."""

    def __init__(self, parser: CommandParser | None = None, ai_backend: AIBackend | None = None) -> None:
        from permanet_agent.ai.mock_backend import MockAIBackend

        self.parser = parser or CommandParser()
        self.ai_backend = ai_backend or MockAIBackend()

    def route(self, message: IncomingMessage) -> OutgoingMessage | None:
        command = self.parser.parse(message.text)
        if command is None:
            return None

        response = handle_command(command, self.ai_backend)
        return OutgoingMessage(
            text=response,
            destination_node_id=message.node_id if message.is_direct else None,
            channel_index=message.channel_index,
        )
