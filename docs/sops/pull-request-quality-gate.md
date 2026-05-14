# Pull Request Quality Gate

## Purpose

Every pull request should make a proposed change reviewable, testable, reversible, and linked to an issue.

The PR quality gate protects the project from undocumented assumptions, unsafe behavior changes, accidental public mesh spam, and unverified AI-generated code.

## Required PR fields

Each PR should include:

- linked issue
- summary
- scope
- non-goals
- risk level
- safety checklist
- validation evidence
- documentation updates
- known limitations
- rollback plan

## Risk levels

### Low

Documentation, comments, formatting, or small tests with no runtime behavior change.

### Medium

Internal behavior, config, tests, CLI changes, or non-hardware code paths.

### High

Anything involving radio behavior, public mesh behavior, secrets, storage, AI backends, private channels, live transmission, or safety-critical defaults.

High-risk PRs require explicit human-review notes before merge.

## Required validation

At minimum, run:

```bash
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected behavior:

```text
@permanet ping -> pong
hello mesh -> no output
```

If a command cannot be run, state why and do not imply it passed.

## Required GitHub checks

Pull requests into `main` should require GitHub Actions CI to pass before merge.

Verified required check target:

```text
test
```

If GitHub exposes a slightly different required-check name, use the closest equivalent and document the exact name in the PR or linked issue.

Do not merge PRs into `main` when required checks are failing, pending, skipped unexpectedly, or missing.

If CI fails for a reason unrelated to the PR, document the evidence, create a follow-up issue if needed, and avoid merging until the maintainer explicitly approves the exception.

## Safety checklist

Every PR should verify:

- public chatter without summon remains ignored
- no automatic multi-packet flooding was introduced
- live radio behavior is not enabled by default
- no secrets, PSKs, node IDs, API keys, or private client data were committed
- config defaults remain safe
- high-risk behavior has human-review notes if applicable

## Documentation updates

Update README, docs, SOPs, config examples, or agent rules when behavior or workflow changes.

## Rollback plan

Every PR should include a simple rollback statement. Examples:

```text
Revert this PR to remove the workflow documentation changes.
```

```text
Revert this PR to restore the previous routing behavior.
```

## Merge guidance

Do not merge if:

- tests are failing
- required GitHub checks are failing or missing
- validation evidence is missing
- the PR changes public mesh behavior without explicit review
- the PR enables live radio behavior by default
- secrets or private identifiers are present
- scope expanded beyond the linked issue without explanation

## Branch protection exception guidance

If branch protection blocks urgent maintenance:

1. Document why the exception is needed.
2. Adjust the narrowest setting possible.
3. Complete the fix through a PR if possible.
4. Restore protection immediately after the urgent work.
5. Add a follow-up issue if the workflow itself needs improvement.

Exceptions should be rare and explicit.
