# Baseline Release Readiness Review

Issue: #50

## Purpose

This review inspects the repository from the viewpoint of a new person who clones or forks the project today.

The goal is to make PermaNet Mesh Agent easier to understand, run, evaluate, and build on before the next implementation sprint.

## Review questions

- Can a new person understand what works today?
- Can they install and run the current demo quickly?
- Is the README clear about current capability versus planned work?
- Is the codebase organized well enough for outside contributors?
- Is the license plan clear enough before more reuse happens?
- What cleanup should happen before the next implementation sprint?

## Current strengths

- The project has a clear mock-first command path.
- The README states the current milestone and the next planned milestone.
- The documented smoke checks are simple and valuable.
- The public summon-only behavior is protected by tests and CI.
- Agent and contributor workflow docs are now much more coherent.
- The repository has a governance invariant roadmap for future process decisions.

## Current gaps

- The repo still uses a temporary license notice.
- A new fork owner may not immediately know whether to use GPLv3, AGPLv3, or another license path.
- The README is useful but could become more fork-oriented at the top.
- There is no short fork quickstart page yet.
- The path from mock demo to the next real traffic milestone could be made more explicit.
- Security and release-readiness follow-up issues should be completed before broader public use.

## License review notes

The current license file is temporary and all-rights-reserved. That protects the project while the final licensing path is undecided, but it is not ideal once people are already forking the repository.

Recommended next step: create a dedicated licensing PR or follow-up issue that compares GPLv3 and AGPLv3 for this project.

Decision points:

- GPLv3 is strong copyleft for copied, modified, and distributed versions.
- AGPLv3 may be a better fit if future modified gateway services are offered over a network.
- The final license should be reflected in the license file, README, contributor docs, and source file notices if adopted.
- Project name and branding expectations may need a separate trademark or naming policy.

## Recommended follow-up work

1. Add a short fork quickstart document.
2. Refactor the README top section around first-time clone/run/evaluate flow.
3. Create a license decision issue for GPLv3 versus AGPLv3.
4. Add a public release checklist.
5. Review whether examples and configuration files are sufficient for new contributors.
6. Keep the next implementation sprint focused on typed config, risk register, and the real traffic milestone path.

## Acceptance check

This PR should not change runtime behavior. It only records the baseline review and creates a surface for GitHub code review comments.

Before merge, confirm:

```bash
pytest
ruff check .
python -m permanet_agent.main --mock --message "@permanet ping"
python -m permanet_agent.main --mock --message "hello mesh"
```

Expected smoke behavior:

```text
@permanet ping -> pong
hello mesh -> no output
```
