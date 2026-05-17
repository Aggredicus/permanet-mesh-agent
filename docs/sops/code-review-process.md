# Standardized Code Review Process

## Purpose

This SOP defines a repeatable pull request review process for contributors.

The goal is to make every contribution easy to understand, verify, reverse, and hand to a maintainer for a final decision.

## Contribution loop

Use this pattern for issue-based work:

```text
find or receive an issue
create an issue-linked branch
make a focused change
run validation
generate or explain a review packet
complete the review checklist
open a pull request with evidence
leave the pull request ready for maintainer review
```

## Decision boundary

Contributors may prepare evidence, recommend an outcome, and open pull requests.

Maintainers make the final decision about whether a pull request is accepted.

## When to run this process

Run this process before opening a pull request whenever practical.

Run it again after meaningful updates to the pull request branch.

For small documentation-only changes, the review can be brief, but the pull request should still explain what changed and how it was checked.

## Required review sequence

1. Confirm the linked issue.
2. Confirm the branch name follows repository policy.
3. Confirm the branch is current enough for review, or note uncertainty.
4. Inspect the changed files.
5. Confirm the scope matches the linked issue.
6. Confirm non-goals were respected.
7. Check validation evidence.
8. Check documentation and configuration consistency.
9. Check project invariants relevant to the change.
10. Record known limitations honestly.
11. Record rollback plan.
12. Generate or explain the review packet.
13. Leave standardized review evidence in the PR body or a PR comment.

## Review packet

Generate a local review packet when possible:

```bash
python scripts/generate_review_packet.py
```

Default output:

```text
.review/review-packet.md
```

The packet is a generated local aid. It should not be committed unless a maintainer explicitly asks for a permanent artifact.

If the packet cannot be generated, explain why in the pull request.

## Required pull request evidence

Every pull request should include or explain:

- linked issue
- summary
- scope
- non-goals
- changed files reviewed
- validation evidence
- documentation or configuration updates
- known limitations
- rollback plan
- follow-up work, if any
- final recommendation for maintainer review

## Review outcomes

Use one of these outcomes:

```text
Ready for maintainer review
Comment only
Needs changes first
```

`Ready for maintainer review` means the contributor believes the work is prepared for a maintainer. It does not mean the pull request is accepted.

## Maintainer return workflow

When a maintainer returns to queued pull requests, each PR should make these questions easy to answer:

- What issue does this solve?
- What files changed?
- What validation ran?
- What still needs judgment?
- What would rollback look like?
- Is the contributor recommending ready, comment only, or changes first?

## Merge blockers

Do not recommend acceptance when:

- required checks are failing, missing, or not yet complete
- validation evidence is missing or overstated
- the change is larger than the issue describes without explanation
- behavior changed without matching tests or docs
- docs or examples no longer match the implementation
- relevant project invariants were not reviewed
- the rollback path is unclear

## Follow-up work

Small non-blocking improvements may become follow-up issues when the current pull request remains clear, focused, and verifiable.

Do not defer core validation or unclear behavior to follow-up work.

## Related files

Use this SOP with:

- `.github/pull_request_template.md`
- `docs/prompts/ai-reviewer.md`
- `docs/sops/pull-request-quality-gate.md`
- `docs/sops/multi-agent-concurrency.md`
- `scripts/generate_review_packet.py`
