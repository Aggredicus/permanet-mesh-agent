from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Callable

Clock = Callable[[], datetime]


def utc_now() -> datetime:
    """Return the current UTC time."""

    return datetime.now(UTC)


@dataclass(frozen=True)
class RateLimitDecision:
    """Result of a rate-limit check."""

    allowed: bool
    reason: str = ""
    retry_after_seconds: int = 0


@dataclass
class CooldownLimiter:
    """Simple deterministic per-node and per-channel cooldown guard."""

    per_node_cooldown_seconds: int = 30
    per_channel_cooldown_seconds: int = 5
    clock: Clock = utc_now
    _last_node_seen: dict[str, datetime] = field(default_factory=dict)
    _last_channel_seen: dict[int, datetime] = field(default_factory=dict)

    def check(self, node_id: str, channel_index: int) -> RateLimitDecision:
        """Return whether a summoned message may be processed now."""

        now = self.clock()

        node_decision = self._check_key(
            key=node_id,
            seen=self._last_node_seen,
            now=now,
            cooldown_seconds=self.per_node_cooldown_seconds,
            reason="node cooldown",
        )
        if not node_decision.allowed:
            return node_decision

        channel_decision = self._check_key(
            key=channel_index,
            seen=self._last_channel_seen,
            now=now,
            cooldown_seconds=self.per_channel_cooldown_seconds,
            reason="channel cooldown",
        )
        if not channel_decision.allowed:
            return channel_decision

        self._last_node_seen[node_id] = now
        self._last_channel_seen[channel_index] = now
        return RateLimitDecision(allowed=True)

    @staticmethod
    def _check_key(
        key: str | int,
        seen: dict[str, datetime] | dict[int, datetime],
        now: datetime,
        cooldown_seconds: int,
        reason: str,
    ) -> RateLimitDecision:
        if cooldown_seconds <= 0:
            return RateLimitDecision(allowed=True)

        last_seen = seen.get(key)  # type: ignore[arg-type]
        if last_seen is None:
            return RateLimitDecision(allowed=True)

        elapsed = now - last_seen
        cooldown = timedelta(seconds=cooldown_seconds)
        if elapsed >= cooldown:
            return RateLimitDecision(allowed=True)

        retry_after = max(1, int((cooldown - elapsed).total_seconds()))
        return RateLimitDecision(
            allowed=False,
            reason=reason,
            retry_after_seconds=retry_after,
        )


def format_cooldown_message(decision: RateLimitDecision) -> str:
    """Return a short mesh-safe cooldown response."""

    if decision.retry_after_seconds <= 1:
        return "Cooldown active. Try again in 1 second."
    return f"Cooldown active. Try again in {decision.retry_after_seconds} seconds."
