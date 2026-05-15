#!/usr/bin/env python3
"""Lightweight concurrency preflight checks for PermaNet Mesh Agent.

Purpose:
- reinforce multi-agent coordination rules
- encourage branch freshness discipline
- encourage issue-linked workflow
- encourage PR checklist completion
- reduce duplicate/stale PR incidents

This script is intentionally lightweight.
It warns aggressively before adding hard enforcement.
"""

from __future__ import annotations

import re
import subprocess
import sys


ALLOWED_BRANCH_PATTERNS = [
    r"^feature/\d+-[a-z0-9-]+$",
    r"^fix/\d+-[a-z0-9-]+$",
    r"^docs/\d+-[a-z0-9-]+$",
    r"^quality/\d+-[a-z0-9-]+$",
    r"^experiment/[a-z0-9-]+$",
    r"^release/v\d+\.\d+\.\d+$",
    r"^hotfix/v\d+\.\d+\.\d+-[a-z0-9-]+$",
]


SHARED_TRUTH_FILES = {
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "docs/developer-handoff.md",
    "docs/roadmap.md",
    "docs/planning/priority-ledger.md",
}


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def current_branch() -> str:
    return run_git("branch", "--show-current")


def branch_name_valid(branch: str) -> bool:
    return any(re.match(pattern, branch) for pattern in ALLOWED_BRANCH_PATTERNS)


def changed_files() -> list[str]:
    output = run_git("diff", "--name-only", "origin/main...")
    return [line.strip() for line in output.splitlines() if line.strip()]


def main() -> int:
    print("== PermaNet concurrency preflight ==")

    branch = current_branch()
    print(f"Branch: {branch}")

    if not branch_name_valid(branch):
        print("WARNING: Branch name does not match approved patterns.")
        print("See docs/sops/branching-and-release.md")

    files = changed_files()

    if not files:
        print("WARNING: No changed files detected relative to origin/main")

    shared = [f for f in files if f in SHARED_TRUTH_FILES]

    if shared:
        print("WARNING: Shared truth files modified:")
        for file in shared:
            print(f"  - {file}")

        print(
            "Consider whether this work overlaps with another active PR or should be consolidated."
        )

    print("Preflight complete.")
    print("Human review and live GitHub verification are still required.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
