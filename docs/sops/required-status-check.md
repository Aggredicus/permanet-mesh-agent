# Required Status Check

## Purpose

This note records the verified GitHub ruleset status-check name for protected merges into `main`.

## Verified required check

The active `Protect main` ruleset requires this check before merge:

```text
test
```

## Verification history

During PR #27, the imported ruleset originally expected:

```text
CI / test
```

GitHub did not recognize that value as satisfying the required check. After the ruleset was changed to require:

```text
test
```

PR #27 merged successfully.

## Current rule

Use `test` as the required status check name in branch protection and ruleset configuration.

If the CI workflow is later split into separate jobs, update this note and the GitHub ruleset together.

## Related issues

- #5 — Enable main branch protection and required CI checks
- #28 — Update branch protection docs to use verified required check name
