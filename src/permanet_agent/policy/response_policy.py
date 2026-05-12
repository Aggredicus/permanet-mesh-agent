from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResponsePolicy:
    """Prepare short, mesh-safe responses without automatic flooding."""

    max_chars: int = 180
    more_prompt: str = "Reply MORE for next step."

    def split(self, text: str) -> list[str]:
        """Split text into mesh-safe chunks.

        This method returns all chunks so the router can cache continuations, but
        it never sends multiple packets by itself. Non-final chunks include the
        MORE hint when it fits within the configured character budget.
        """

        if self.max_chars < 1:
            raise ValueError("max_chars must be at least 1")

        normalized = " ".join(text.strip().split())
        if not normalized:
            return [""]

        if len(normalized) <= self.max_chars:
            return [normalized]

        chunks: list[str] = []
        remaining = normalized
        continuation_suffix = " " + self.more_prompt

        while remaining:
            if len(remaining) <= self.max_chars:
                chunks.append(remaining)
                break

            budget = self.max_chars - len(continuation_suffix)
            if budget < 1:
                budget = self.max_chars

            split_at = remaining.rfind(" ", 0, budget + 1)
            if split_at <= 0:
                split_at = budget

            chunk = remaining[:split_at].strip()
            remaining = remaining[split_at:].strip()

            if remaining and len(chunk) + len(continuation_suffix) <= self.max_chars:
                chunk = f"{chunk}{continuation_suffix}"

            chunks.append(chunk[: self.max_chars])

        return chunks
