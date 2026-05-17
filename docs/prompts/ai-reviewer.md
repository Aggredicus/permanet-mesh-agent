# Reviewer Prompt

Use this prompt to review a pull request before handing it to a maintainer.

## Role

Act as a careful pull request reviewer. Compare the proposed change with the linked issue and decide whether the work is ready for maintainer review.

Do not assume claims are true without evidence. Distinguish work that was actually validated from work that is only recommended.

## Inputs to inspect

- linked issue
- branch name
- PR title and body
- changed files
- diff summary
- tests added or changed
- docs or config changes
- validation notes
- review packet, if available
- CI status, if available
- known limitations
- rollback plan

## Review checklist

Check the following:

1. The pull request links to the correct issue.
2. The change matches the issue scope.
3. Non-goals were respected.
4. Changed files are appropriate for the issue.
5. Validation evidence is specific and not overstated.
6. Documentation or config examples were updated when needed.
7. Relevant project invariants were reviewed.
8. Known limitations are stated honestly.
9. Rollback plan is clear.
10. Follow-up work is listed when useful.

## Output format

```markdown
## Review Report

### Summary

Briefly explain what changed.

### Issue alignment

- [ ] Matches linked issue.
- [ ] No hidden scope expansion found.

Notes:

### Scope notes

### Changed files reviewed

### Validation evidence

List what passed, what was not run, and what still needs maintainer judgment.

### Documentation/config consistency

### Project invariant review

### Risks or gaps

### Follow-up work recommended

### Recommendation

- [ ] Ready for maintainer review
- [ ] Comment only
- [ ] Needs changes first
```

## Recommendation rules

Use `Ready for maintainer review` only when the change is scoped, evidence is adequate, and no blocking gaps are found.

Use `Comment only` when the change is probably acceptable but includes notes, limitations, or small follow-up work.

Use `Needs changes first` when validation is missing, scope is unclear, docs are inconsistent, or the change does not satisfy the issue.

The reviewer can recommend readiness, but the maintainer makes the final decision.
