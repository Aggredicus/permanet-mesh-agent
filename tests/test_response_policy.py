import pytest

from permanet_agent.policy.response_policy import ResponsePolicy


def test_response_policy_limits_public_response_length():
    policy = ResponsePolicy(max_chars=80)
    chunks = policy.split(" ".join(["wet slope plants"] * 20))

    assert len(chunks) > 1
    assert all(len(chunk) <= 80 for chunk in chunks)
    assert chunks[0].endswith("Reply MORE for next step.")


def test_response_policy_normalizes_whitespace():
    policy = ResponsePolicy(max_chars=180)

    assert policy.split("  wet   slope\n\tplants  ") == ["wet slope plants"]


def test_response_policy_rejects_invalid_limit():
    policy = ResponsePolicy(max_chars=0)

    with pytest.raises(ValueError, match="max_chars"):
        policy.split("hello")
