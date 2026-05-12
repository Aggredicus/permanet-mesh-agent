from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResponsePolicy:
    """Prepare short, mesh-safe responses without automatic flooding."""

    max_chars: int = 180
    more_prompt: str = "Reply MORE for next step."

    def split(self, text: str) -> list[str]:
        normalized = " ".join(text.strip().split())
        if not normalized:
            return [""]

        if len(normalized) <= self.max_chars:
            return [normalized]

        chunks: list[str] = []
        remaining = normalized
        continuation_suffix = " " + self.more_prompt

        while remaining:
            budget = self.max_chars
            suffix = continuation_suffix if len(remaining) > self.max_chars else ""
            if suffix:
                budget = max(1, self.max_chars - len(suffix))

            if len(remaining) <= self.max_chars:
                chunks.append(remaining)
                break

            split_at = remaining.rfind(" ", 0, budget + 1)
            if split_at <= 0:
                split_at = budget

            chunk = remaining[:split_at].strip()
            remaining = remaining[split_at:].strip()

            if remaining:
                chunk = (chunk + suffix).strip()
            chunks.append(chunk[: self.max_chars])

        return chunks
