## Linked issue

Closes #

## Summary

## Scope

## Non-goals

## Risk level

- [ ] Low
- [ ] Medium
- [ ] High: hardware / radio / secrets / security / storage / public mesh behavior

## Multi-agent concurrency check

- [ ] I checked for existing open PRs for this issue.
- [ ] I checked for active branches for this issue.
- [ ] I checked that this branch is current with `main`.
- [ ] I declared or respected file ownership for this work.
- [ ] This PR does not duplicate, supersede, or conflict with another active PR unless explicitly explained below.
- [ ] Shared status/workflow docs were updated together or intentionally left unchanged.

Concurrency notes:

```text
Existing PRs checked:
Active branches checked:
Allowed files:
Forbidden files:
Coordinator/reviewer notes:
```

## Safety checklist

- [ ] Public chatter without summon remains ignored.
- [ ] No automatic multi-packet flooding was introduced.
- [ ] Live radio behavior is not enabled by default.
- [ ] No secrets, PSKs, node IDs, API keys, or private client data were committed.
- [ ] Config defaults remain safe.
- [ ] High-risk behavior has human-review notes if applicable.

## Validation evidence

- [ ] `python scripts/check_branch_policy.py`
- [ ] `pytest`
- [ ] `ruff check .`
- [ ] `python -m permanet_agent.main --mock --message "@permanet ping"`
- [ ] `python -m permanet_agent.main --mock --message "hello mesh"`

If a validation step was not run, explain why without implying it passed.

## Documentation updated

- [ ] README / docs updated if behavior changed.
- [ ] config examples updated if settings changed.
- [ ] New SOPs/rules added if workflow changed.
- [ ] `docs/planning/priority-ledger.md` updated if issue ordering or triage rules changed.

## Known limitations

## Rollback plan
