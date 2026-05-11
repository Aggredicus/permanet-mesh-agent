from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ParsedCommand:
    name: str
    args: str = ""


class CommandParser:
    """Parse summon-only PermaNet commands from mesh text."""

    def __init__(self, summons: tuple[str, ...] = ("@permanet", "/permanet")) -> None:
        self.summons = tuple(s.lower() for s in summons)

    def parse(self, text: str) -> ParsedCommand | None:
        normalized = text.strip()
        if not normalized:
            return None

        lowered = normalized.lower()
        matched = next((summon for summon in self.summons if lowered.startswith(summon)), None)
        if matched is None:
            return None

        remainder = normalized[len(matched) :].strip()
        if not remainder:
            return ParsedCommand(name="help")

        parts = remainder.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1].strip() if len(parts) > 1 else ""

        if command == "?":
            return ParsedCommand(name="help")

        return ParsedCommand(name=command, args=args)
