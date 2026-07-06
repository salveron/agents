---
name: systest-pytest
description: System testing with pytest as the harness — the fully assembled system in a production-like environment, end-to-end technical flows and non-functional thresholds. Load when writing system-level tests.
---

# pytest (system level)

## When to use this skill
System tests — the assembled, deployed whole exercised end to end — are being written or run with
pytest as the harness, including for non-Python systems (driven via subprocess, CLI, or HTTP).

## Scope
- **Covers:** System-level pytest: environment fixtures, real-interface driving, non-functional
  measurements, evidence output.
- **Does not cover:** Seams — `inttest-pytest`; requirements-level behavior — `functest-pytest`.

## Core guidance
- **Location & marker:** `tests/system/`, marker `system` in `pyproject.toml`; its own CI stage,
  after integration.
- **The system runs for real.** A session-scoped environment fixture deploys/starts the whole
  system (compose stack, subprocess, installed build), waits until ready, yields, and tears down.
  Nothing inside the system is mocked; the environment should mirror production — flag drift.
- **Drive real interfaces:** `subprocess.run` for CLIs (assert exit codes and output), HTTP
  clients for APIs; assert on observable system behavior.
- **Non-functional criteria are tests:** performance thresholds, restart/recovery, migration and
  upgrade paths, persistence across restarts — each stated criterion gets a measuring test that
  cites its number.
- **Deadlines everywhere:** explicit polling with timeouts; a hanging system test must fail, not
  block the pipeline.

## Steps / patterns
1. Build the environment fixture first; prove start → ready → teardown works twice in a row.
2. Walk the main technical flows end to end; then the ugly paths: kill/restart, full disk, bad
   config.
3. Measure stated thresholds with repeatable load; record the numbers in the test output.
4. Emit `--junitxml` and keep measurements machine-readable — they feed release decisions.

## Pitfalls & anti-patterns
- A "system test" that quietly mocks half the system — say what is real; here, everything is.
- Unrealistic environments (SQLite standing in for Postgres) — a false verdict, flag it.
- Retrying flaky tests instead of fixing the race; flakiness is a defect.
- Asserting timing exactly instead of against thresholds — brittle on shared runners.

## References
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) · [junitxml](https://docs.pytest.org/en/stable/how-to/output.html#creating-junitxml-format-files)
