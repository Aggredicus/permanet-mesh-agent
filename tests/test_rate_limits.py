from datetime import UTC, datetime, timedelta

from permanet_agent.policy.rate_limits import CooldownLimiter, format_cooldown_message


class FakeClock:
    def __init__(self) -> None:
        self.now = datetime(2026, 5, 12, 12, 0, tzinfo=UTC)

    def __call__(self) -> datetime:
        return self.now

    def advance(self, seconds: int) -> None:
        self.now += timedelta(seconds=seconds)


def test_per_node_cooldown_blocks_repeated_invocation():
    clock = FakeClock()
    limiter = CooldownLimiter(
        per_node_cooldown_seconds=30,
        per_channel_cooldown_seconds=0,
        clock=clock,
    )

    assert limiter.check("!node-a", 0).allowed
    blocked = limiter.check("!node-a", 0)
    assert not blocked.allowed
    assert blocked.reason == "node cooldown"
    assert "Cooldown active" in format_cooldown_message(blocked)

    clock.advance(30)
    assert limiter.check("!node-a", 0).allowed


def test_per_channel_cooldown_blocks_public_burst():
    clock = FakeClock()
    limiter = CooldownLimiter(
        per_node_cooldown_seconds=0,
        per_channel_cooldown_seconds=5,
        clock=clock,
    )

    assert limiter.check("!node-a", 0).allowed
    blocked = limiter.check("!node-b", 0)
    assert not blocked.allowed
    assert blocked.reason == "channel cooldown"

    clock.advance(5)
    assert limiter.check("!node-b", 0).allowed


def test_zero_cooldowns_allow_invocations():
    limiter = CooldownLimiter(per_node_cooldown_seconds=0, per_channel_cooldown_seconds=0)

    assert limiter.check("!node", 0).allowed
    assert limiter.check("!node", 0).allowed
