from scripts.check_branch_policy import validate_branch_name


def test_valid_issue_linked_branches():
    valid_branches = [
        "feature/1-response-policy-rate-limits",
        "quality/2-branching-workflow",
        "docs/4-handoff-polish",
        "fix/5-ci-ruff-cleanup",
    ]

    for branch in valid_branches:
        valid, message = validate_branch_name(branch)
        assert valid, message


def test_valid_non_issue_branch_types():
    valid_branches = [
        "experiment/mqtt-bridge",
        "release/v1.0.0",
        "hotfix/v1.0.1-public-loop",
    ]

    for branch in valid_branches:
        valid, message = validate_branch_name(branch)
        assert valid, message


def test_invalid_branches():
    invalid_branches = [
        "main",
        "my-changes",
        "stuff",
        "newbranch",
        "feature/response-policy",
        "quality/branching-workflow",
        "docs/handoff-polish",
        "fix/ci-ruff-cleanup",
    ]

    for branch in invalid_branches:
        valid, _ = validate_branch_name(branch)
        assert not valid
