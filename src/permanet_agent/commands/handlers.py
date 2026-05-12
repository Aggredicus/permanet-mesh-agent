from __future__ import annotations

from permanet_agent.ai.base import AIBackend
from permanet_agent.commands.parser import ParsedCommand

HELP_TEXT = "Commands: help, ping, ask <q>, more. Public mode replies only when summoned."


def handle_command(command: ParsedCommand, ai_backend: AIBackend) -> str:
    """Return a short mesh-safe response for a parsed command."""

    match command.name:
        case "help":
            return HELP_TEXT
        case "ping":
            return "pong"
        case "ask":
            if not command.args:
                return "Ask usage: @permanet ask <short question>"
            return ai_backend.answer(command.args)
        case "more":
            return "No pending response. Ask a question first."
        case _:
            return "Unknown command. Try: @permanet help"
