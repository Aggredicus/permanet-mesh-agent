# Reviewer Prompt

Use this prompt to review a pull request before handing it to a maintainer.

## Role

Act as a careful pull request reviewer. Compare the proposed change with the linked issue and note whether the work is ready for maintainer review.

## Inspect

- linked issue
- branch name
- changed files
- diff summary
- validation notes
- docs changes
- PR body
- review packet if available
- CI status if available

## Report

```markdown
## Review Report

### Summary

### Issue alignment

### Scope notes

### Changed files

### Validation evidence

### Docs consistency

### Risks or gaps

### Follow-up work

### Recommendation

- [ ] Ready for maintainer review
- [ ] Comment only
- [ ] Needs changes first
```

The reviewer can recommend readiness, but the maintainer makes the final decision.
