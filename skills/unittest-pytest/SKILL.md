---
name: unittest-pytest
description: Unit testing Python with pytest — layout, fixtures, parametrization, isolation with monkeypatch/mocks, running via uv. Load when authoring or running Python unit tests.
---

# pytest (unit level)

## When to use this skill
Python unit tests are being written or run with pytest.

## Scope
- **Covers:** Unit-level pytest: layout, fixtures, parametrization, isolation, assertions.
- **Does not cover:** Higher test levels — see `inttest-pytest` / `systest-pytest` /
  `functest-pytest`; Python idioms — `dev-python313-pep8`.

## Core guidance
- **Layout:** `tests/` mirrors `src/`; files `test_<module>.py`; test names state behavior:
  `test_<unit>_<behavior>[_when_<condition>]`.
- **Structure:** Arrange–Act–Assert, one behavior per test; plain `assert` (pytest introspection
  beats assertion helpers).
- **Fixtures:** shared setup in `conftest.py`; default `function` scope for isolation — wider
  scopes only for genuinely immutable fixtures.
- **Parametrize** boundaries and case tables with `@pytest.mark.parametrize`; give cases `id=`s.
- **Isolate:** `monkeypatch` for env/attributes; `unittest.mock` for injected dependencies —
  mock the seam (the Protocol), never the internals of the unit under test.
- **Run:** `uv run pytest` (quiet, fast, offline); `-k` to select, `--lf` to re-run failures;
  coverage via `pytest-cov` when asked.

## Steps / patterns
1. Read the unit's contract and the acceptance criteria; list behaviors, boundaries, error paths.
2. Write the case table first (parametrize ids), then the tests.
3. One failing behavior → one failing test with a diagnostic that names expected vs. actual.
4. Verify a fix by the previously failing test — never by deleting or loosening it.

## Pitfalls & anti-patterns
- Tests coupled to implementation details — they break on refactor, not on defect.
- Time, randomness, network, or filesystem reliance — inject or fake them; flaky = defect.
- Over-mocking: if everything is mocked, nothing is tested.
- Asserting only the happy path; error paths are half the contract.

## References
- [pytest docs](https://docs.pytest.org/) · [unittest.mock](https://docs.python.org/3.13/library/unittest.mock.html)
