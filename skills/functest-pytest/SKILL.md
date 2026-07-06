---
name: functest-pytest
description: Functional testing with pytest as the harness — user flows derived from acceptance criteria, exploratory findings captured as tests, results doubling as acceptance evidence. Load when writing functional tests.
---

# pytest (functional level)

## When to use this skill
Functional tests — behavior validated against the requirements from the user's perspective — are
being written or run with pytest as the harness.

## Scope
- **Covers:** Functional-level pytest: criteria-driven scenarios, evidence mapping, exploratory
  capture, regression of user-visible behavior.
- **Does not cover:** Seams — `inttest-pytest`; technical system qualities — `systest-pytest`.

## Core guidance
- **Location & marker:** `tests/functional/`, marker `functional` in `pyproject.toml`; its own CI
  stage — the last gate before acceptance.
- **One criterion, one test (at least):** name the test after the acceptance criterion it
  verifies and cite the criterion id in the docstring — the JUnit report then doubles as the
  Product Owner's acceptance evidence.
- **Take the user's seat:** drive the product through its real interfaces (CLI, API, UI harness)
  in realistic scenarios; assert on what the user observes, not on internals.
- **Exploratory findings become tests:** every surprising behavior found while exploring is
  captured as a new test (passing or failing) so it stays found.
- **Regression:** changed user-visible behavior re-runs its criterion tests; a changed criterion
  changes its test first.

## Steps / patterns
1. List the acceptance criteria; map each to scenario(s) — happy path plus the stated edge cases.
2. Reuse the environment fixtures of the system suite where possible; functional tests need a
   running product, not their own bespoke deployment logic.
3. Write scenarios as user flows: setup → user actions → observable outcome.
4. Emit `--junitxml`; hand the criteria-to-result mapping to the Product Owner.

## Pitfalls & anti-patterns
- Testing implementation details — functional tests break only when *behavior* breaks.
- Criteria drift: the criterion changed but the test still passes the old expectation.
- Scenarios only an engineer would run; flows must mirror actual usage.
- Burying the criterion mapping — evidence nobody can trace is not evidence.

## References
- [pytest markers](https://docs.pytest.org/en/stable/how-to/mark.html) · [junitxml](https://docs.pytest.org/en/stable/how-to/output.html#creating-junitxml-format-files)
