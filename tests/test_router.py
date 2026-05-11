from permanet_agent.protocol.message import IncomingMessage
from permanet_agent.routing.router import MeshRouter


def test_router_ignores_unsummoned_message():
    router = MeshRouter()
    response = router.route(IncomingMessage(text="normal public chatter"))
    assert response is None


def test_router_replies_to_ping():
    router = MeshRouter()
    response = router.route(IncomingMessage(text="@permanet ping", node_id="!abc", channel_index=0))
    assert response is not None
    assert response.text == "pong"
    assert response.channel_index == 0


def test_router_handles_help():
    router = MeshRouter()
    response = router.route(IncomingMessage(text="@permanet help"))
    assert response is not None
    assert "Commands:" in response.text


def test_router_handles_ask_with_mock_backend():
    router = MeshRouter()
    response = router.route(IncomingMessage(text="@permanet ask wet slope plants"))
    assert response is not None
    assert response.text.startswith("Mock answer:")
