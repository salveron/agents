---
name: inttest-pytest
description: Integration testing with pytest as the harness — verifying seams and contracts between real components, deliberate use of test doubles at outer boundaries. Load when writing integration tests.
---

# pytest (integration level)

## When to use this skill
Integration tests — component-to-component or system-to-external-service seams — are being
written or run with pytest as the harness, including against non-Python components.

## Scope
- **Covers:** Integration-level pytest: suite organization, fixtures that bring real parts
  together, contract assertions, doubles at outer boundaries.
- **Does not cover:** Unit level — `unittest-pytest`; whole-system — `systest-pytest`;
  requirements-level — `functest-pytest`.

## Core guidance
- **Location & marker:** `tests/integration/`, marker `integration` registered in
  `pyproject.toml`; runnable alone (`uv run pytest -m integration`) as its own CI stage.
- **Test the pair for real.** The two sides of the seam under test are real; doubles are allowed
  only *outside* the pair (e.g. fake the payment provider while testing service ↔ database).
  State in the test what is real and what is faked.
- **Pin the contract:** request/response shapes, error propagation, timeouts, retries — assert
  what crosses the seam, not the internals of either side.
- **Fixtures own resources:** module/session-scoped fixtures start what the seam needs (temp
  database, subprocess server, container) with `yield` + guaranteed teardown; tests only use them.
- **Timeouts** on everything awaited; explicit readiness polling with deadlines, never bare sleeps.

## Steps / patterns
1. From the documented interface contract, list the interactions: happy path, each error, each
   boundary.
2. Build the resource fixture (start, wait-until-ready, yield, tear down) before any test.
3. One interaction per test, named after the contract clause it pins.
4. Emit `--junitxml` results so the seam's status is visible in the pipeline.

## Pitfalls & anti-patterns
- Mocking one side of the seam under test — that's a unit test wearing a costume.
- Contract drift: the test pins yesterday's shape; regenerate against the documented contract.
- Shared state between tests via the common resource — reset or isolate per test.
- Fixtures without teardown; orphaned processes poison later runs.

## References
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [markers](https://docs.pytest.org/en/stable/how-to/mark.html)
