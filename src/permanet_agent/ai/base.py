from __future__ import annotations

from typing import Protocol


class AIBackend(Protocol):
    """Backend interface for short mesh-safe answers."""

    def answer(self, prompt: str) -> str:
        """Return a concise answer suitable for mesh transmission."""
