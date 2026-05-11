from permanet_agent.main import run_mock_message


def test_mock_ping_flow():
    assert run_mock_message("@permanet ping") == "pong"


def test_mock_ignores_unsummoned_flow():
    assert run_mock_message("hello everyone") == ""


def test_mock_help_flow():
    assert "Commands:" in run_mock_message("@permanet help")
