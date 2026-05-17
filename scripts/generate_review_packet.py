#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def run_git(*args: str) -> tuple[int, str, str]:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def git_text(*args: str, fallback: str = "Unavailable") -> str:
    code, stdout, stderr = run_git(*args)
    if code == 0:
        return stdout or "None"
    return f"{fallback}: {stderr or stdout}"


def ensure_git_repo() -> None:
    code, _, _ = run_git("rev-parse", "--is-inside-work-tree")
    if code != 0:
        raise SystemExit("ERROR: generate_review_packet.py must be run inside a Git repository.")


def build_packet(base: str) -> str:
    branch = git_text("branch", "--show-current")
    head = git_text("rev-parse", "--short", "HEAD")
    status = git_text("status", "--short")
    changed = git_text("diff", "--name-only", f"{base}...")
    stat = git_text("diff", "--stat", f"{base}...")
    commits = git_text("log", "--oneline", f"{base}..HEAD")

    return f"""# Pull Request Review Packet

## Branch

```text
{branch}
```

## Head

```text
{head}
```

## Base

```text
{base}
```

## Commits since base

```text
{commits}
```

## Changed files

```text
{changed}
```

## Diff stat

```text
{stat}
```

## Local git status

```text
{status}
```

## Validation checklist

- [ ] Branch policy checked.
- [ ] Concurrency preflight checked.
- [ ] Tests run or explained.
- [ ] Lint run or explained.
- [ ] Smoke checks run or explained.

## Review checklist

- [ ] Linked issue reviewed.
- [ ] Scope reviewed.
- [ ] Non-goals reviewed.
- [ ] Changed files reviewed.
- [ ] Docs/config consistency reviewed.
- [ ] Known limitations recorded.
- [ ] Rollback plan recorded.

## Follow-up work

- None recorded yet.

## Reviewer recommendation

- [ ] Ready for maintainer review.
- [ ] Comment only.
- [ ] Needs changes first.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a local PR review packet.")
    parser.add_argument("--base", default="main", help="Base branch or ref to compare against.")
    parser.add_argument("--out", default=".review/review-packet.md", help="Output Markdown path.")
    args = parser.parse_args()

    ensure_git_repo()
    packet = build_packet(args.base)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(packet, encoding="utf-8")
    print(f"Wrote review packet to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
