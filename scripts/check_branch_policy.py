#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys

ISSUE_BRANCH_RE = re.compile(r"^(feature|fix|docs|quality)/\d+-[a-z0-9][a-z0-9-]*$")
EXPERIMENT_BRANCH_RE = re.compile(r"^experiment/[a-z0-9][a-z0-9-]*$")
RELEASE_BRANCH_RE = re.compile(r"^release/v\d+\.\d+\.\d+$")
HOTFIX_BRANCH_RE = re.compile(r"^hotfix/v\d+\.\d+\.\d+-[a-z0-9][a-z0-9-]*$")


def get_current_branch() -> str:
    """Return the current Git branch name."""

    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def validate_branch_name(branch: str) -> tuple[bool, str]:
    """Validate a branch name against the repository branching SOP."""

    if branch == "main":
        return (
            False,
            "Do not implement feature work directly on main. "
            "Create an issue-linked branch such as quality/2-branching-ai-quality-workflow.",
        )

    if ISSUE_BRANCH_RE.match(branch):
        return True, "Branch name follows issue-linked branch policy."

    if EXPERIMENT_BRANCH_RE.match(branch):
        return True, "Experiment branch name is valid. Keep experimental work isolated."

    if RELEASE_BRANCH_RE.match(branch):
        return True, "Release branch name is valid."

    if HOTFIX_BRANCH_RE.match(branch):
        return True, "Hotfix branch name is valid. Keep hotfixes small and specific."

    return (
        False,
        "Invalid branch name. Use feature/<issue>-short-name, fix/<issue>-short-name, "
        "docs/<issue>-short-name, quality/<issue>-short-name, experiment/<short-name>, "
        "release/vX.Y.Z, or hotfix/vX.Y.Z-short-name.",
    )


def main() -> int:
    try:
        branch = get_current_branch()
    except subprocess.CalledProcessError as exc:
        print(f"Could not determine current branch: {exc}", file=sys.stderr)
        return 2

    valid, message = validate_branch_name(branch)
    if valid:
        print(f"PASS: {branch} — {message}")
        return 0

    print(f"FAIL: {branch} — {message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
