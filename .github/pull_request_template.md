## Linked issue

Closes #

## Summary

## Scope

## Non-goals

## Risk level

- [ ] Low
- [ ] Medium
- [ ] High: hardware / radio / secrets / security / storage / public mesh behavior

## Safety checklist

- [ ] Public chatter without summon remains ignored.
- [ ] No automatic multi-packet flooding was introduced.
- [ ] Live radio behavior is not enabled by default.
- [ ] No secrets, PSKs, node IDs, API keys, or private client data were committed.
- [ ] Config defaults remain safe.
- [ ] High-risk behavior has human-review notes if applicable.

## Validation evidence

- [ ] `pytest`
- [ ] `ruff check .`
- [ ] `python -m permanet_agent.main --mock --message "@permanet ping"`
- [ ] `python -m permanet_agent.main --mock --message "hello mesh"`

## Documentation updated

- [ ] README / docs updated if behavior changed.
- [ ] config examples updated if settings changed.
- [ ] New SOPs/rules added if workflow changed.

## Known limitations

## Rollback plan
