from datetime import UTC, datetime, timedelta

from permanet_agent.ai.base import AIBackend
from permanet_agent.policy.rate_limits import CooldownLimiter
from permanet_agent.policy.response_policy import ResponsePolicy
from permanet_agent.protocol.message import IncomingMessage
from permanet_agent.routing.router import MeshRouter


class LongAnswerBackend:
    def answer(self, prompt: str) -> str:
        return " ".join([f"step-{index}" for index in range(1, 40)])


class FakeClock:
    def __init__(self) -> None:
        self.now = datetime(2026, 5, 12, 12, 0, tzinfo=UTC)

    def __call__(self) -> datetime:
        return self.now

    def advance(self, seconds: int) -> None:
        self.now += timedelta(seconds=seconds)


def no_cooldown_router(ai_backend: AIBackend | None = None) -> MeshRouter:
    return MeshRouter(
        ai_backend=ai_backend,
        rate_limiter=CooldownLimiter(
            per_node_cooldown_seconds=0,
            per_channel_cooldown_seconds=0,
        ),
    )


def test_router_ignores_unsummoned_message():
    router = no_cooldown_router()
    response = router.route(IncomingMessage(text="normal public chatter"))
    assert response is None


def test_router_replies_to_ping():
    router = no_cooldown_router()
    response = router.route(IncomingMessage(text="@permanet ping", node_id="!abc", channel_index=0))
    assert response is not None
    assert response.text == "pong"
    assert response.channel_index == 0


def test_router_handles_help():
    router = no_cooldown_router()
    response = router.route(IncomingMessage(text="@permanet help"))
    assert response is not None
    assert "Commands:" in response.text


def test_router_handles_ask_with_mock_backend():
    router = no_cooldown_router()
    response = router.route(IncomingMessage(text="@permanet ask wet slope plants"))
    assert response is not None
    assert response.text.startswith("Mock answer:")


def test_long_answer_is_chunked_not_flooded():
    router = MeshRouter(
        ai_backend=LongAnswerBackend(),
        response_policy=ResponsePolicy(max_chars=80),
        rate_limiter=CooldownLimiter(
            per_node_cooldown_seconds=0,
            per_channel_cooldown_seconds=0,
        ),
    )

    response = router.route(IncomingMessage(text="@permanet ask long plan", node_id="!abc"))

    assert response is not None
    assert len(response.text) <= 80
    assert response.text.endswith("Reply MORE for next step.")
    assert router.pagination_cache.has_pending("!abc", 0)


def test_more_returns_next_chunk():
    router = MeshRouter(
        ai_backend=LongAnswerBackend(),
        response_policy=ResponsePolicy(max_chars=80),
        rate_limiter=CooldownLimiter(
            per_node_cooldown_seconds=0,
            per_channel_cooldown_seconds=0,
        ),
    )

    first = router.route(IncomingMessage(text="@permanet ask long plan", node_id="!abc"))
    more = router.route(IncomingMessage(text="@permanet more", node_id="!abc"))

    assert first is not None
    assert more is not None
    assert more.text != first.text
    assert len(more.text) <= 80


def test_more_without_pending_chunk_returns_helpful_message():
    router = no_cooldown_router()

    response = router.route(IncomingMessage(text="@permanet more", node_id="!abc"))

    assert response is not None
    assert response.text == "No pending response. Ask a question first."


def test_pagination_state_is_per_node_and_channel():
    router = MeshRouter(
        ai_backend=LongAnswerBackend(),
        response_policy=ResponsePolicy(max_chars=80),
        rate_limiter=CooldownLimiter(
            per_node_cooldown_seconds=0,
            per_channel_cooldown_seconds=0,
        ),
    )

    first = router.route(
        IncomingMessage(text="@permanet ask long plan", node_id="!abc", channel_index=0)
    )
    wrong_node = router.route(
        IncomingMessage(text="@permanet more", node_id="!other", channel_index=0)
    )
    wrong_channel = router.route(
        IncomingMessage(text="@permanet more", node_id="!abc", channel_index=1)
    )
    right_key = router.route(
        IncomingMessage(text="@permanet more", node_id="!abc", channel_index=0)
    )

    assert first is not None
    assert wrong_node is not None
    assert wrong_node.text == "No pending response. Ask a question first."
    assert wrong_channel is not None
    assert wrong_channel.text == "No pending response. Ask a question first."
    assert right_key is not None
    assert right_key.text != "No pending response. Ask a question first."


def test_router_rate_limits_repeated_summoned_invocation():
    clock = FakeClock()
    router = MeshRouter(
        rate_limiter=CooldownLimiter(
            per_node_cooldown_seconds=30,
            per_channel_cooldown_seconds=0,
            clock=clock,
        )
    )

    first = router.route(IncomingMessage(text="@permanet ping", node_id="!abc"))
    second = router.route(IncomingMessage(text="@permanet ping", node_id="!abc"))

    assert first is not None
    assert first.text == "pong"
    assert second is not None
    assert second.text.startswith("Cooldown active.")

    clock.advance(30)
    third = router.route(IncomingMessage(text="@permanet ping", node_id="!abc"))
    assert third is not None
    assert third.text == "pong"


def test_unsummoned_message_still_ignored_even_with_cooldown_state():
    router = MeshRouter()

    first = router.route(IncomingMessage(text="@permanet ping", node_id="!abc"))
    chatter = router.route(IncomingMessage(text="hello mesh", node_id="!abc"))

    assert first is not None
    assert chatter is None
