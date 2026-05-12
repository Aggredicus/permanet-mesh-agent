from __future__ import annotations

from permanet_agent.ai.base import AIBackend
from permanet_agent.commands.handlers import handle_command
from permanet_agent.commands.parser import CommandParser
from permanet_agent.memory.pagination_cache import PaginationCache
from permanet_agent.policy.rate_limits import CooldownLimiter, format_cooldown_message
from permanet_agent.policy.response_policy import ResponsePolicy
from permanet_agent.protocol.message import IncomingMessage, OutgoingMessage

NO_PENDING_MORE_TEXT = "No pending response. Ask a question first."


class MeshRouter:
    """Summon-only router for MVP public channel behavior."""

    def __init__(
        self,
        parser: CommandParser | None = None,
        ai_backend: AIBackend | None = None,
        response_policy: ResponsePolicy | None = None,
        pagination_cache: PaginationCache | None = None,
        rate_limiter: CooldownLimiter | None = None,
    ) -> None:
        from permanet_agent.ai.mock_backend import MockAIBackend

        self.parser = parser or CommandParser()
        self.ai_backend = ai_backend or MockAIBackend()
        self.response_policy = response_policy or ResponsePolicy()
        self.pagination_cache = pagination_cache or PaginationCache()
        self.rate_limiter = rate_limiter or CooldownLimiter()

    def route(self, message: IncomingMessage) -> OutgoingMessage | None:
        command = self.parser.parse(message.text)
        if command is None:
            return None

        if command.name == "more":
            response = self.pagination_cache.pop_next(message.node_id, message.channel_index)
            if response is None:
                response = NO_PENDING_MORE_TEXT
            return self._outgoing(message, response)

        rate_limit_decision = self.rate_limiter.check(message.node_id, message.channel_index)
        if not rate_limit_decision.allowed:
            return self._outgoing(message, format_cooldown_message(rate_limit_decision))

        response = handle_command(command, self.ai_backend)
        chunks = self.response_policy.split(response)
        first_chunk = chunks[0]
        self.pagination_cache.store(message.node_id, message.channel_index, chunks[1:])
        return self._outgoing(message, first_chunk)

    @staticmethod
    def _outgoing(message: IncomingMessage, text: str) -> OutgoingMessage:
        return OutgoingMessage(
            text=text,
            destination_node_id=message.node_id if message.is_direct else None,
            channel_index=message.channel_index,
        )
