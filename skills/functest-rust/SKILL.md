---
name: functest-rust
description: Functional testing of Rust binaries with cargo's tests/ directory — acceptance-criteria-driven flows through the built binary (assert_cmd, pty for interactive modes), shared plumbing in one common module. Load when writing functional tests for a Rust binary.
---

# cargo tests/ (functional level)

## When to use this skill
Functional tests — behavior validated against the requirements from the user's perspective — are
being written or run for a Rust binary, with cargo's `tests/` directory as the harness.

## Scope
- **Covers:** Criteria-driven scenarios driving the built binary (CLI one-shots, stdin, files,
  interactive REPLs), test-crate layout, shared test plumbing.
- **Does not cover:** In-crate unit tests and doctests — `unittest-rust`; pytest-harnessed
  functional/integration/system testing of non-Rust or service artifacts — `functest-pytest` & co.

## Core guidance
- **Layout:** each `tests/*.rs` file is its own crate compiled against the package; group files
  by user-facing flow (one-shot, REPL, file loading, errors), named for what they validate.
- **One common module:** shared plumbing — process spawning, output capture, exit and output
  assertions — lives in `tests/common/mod.rs` (declared `mod common;` in each
  test file), the single home for what the test crates share. Promote a helper there the moment
  a second file wants it. Test crates cannot see `#[cfg(test)]` unit helpers — separate
  compilation units, one home per layer.
- **Drive the real binary:** `assert_cmd` locates and runs the built binary; assert on what the
  user observes — stdout, stderr, exit status — never on internals.
- **Interactive flows:** drive REPLs through a pty (e.g. `portable-pty`) when behavior depends
  on a terminal; the pty driver belongs in the common module.
- **One criterion, one test (at least):** name tests after the acceptance criterion or user flow
  they verify; results double as acceptance evidence.
- **Exploratory findings become tests:** every surprising behavior found while exploring is
  captured as a test so it stays found.

## Steps / patterns
1. List the acceptance criteria; map each to scenario(s) — happy path plus the stated edge cases.
2. Write scenarios as user flows: invocation → input → observable output and exit status.
3. Reach for the common module first; extend it rather than growing per-file helpers.
4. Iterate with `cargo test --test <file>`; the full `cargo test` gates the change.

## Pitfalls & anti-patterns
- Testing implementation details — functional tests break only when *behavior* breaks.
- Per-file copies of spawning or assertion plumbing growing beside an underused common module.
- Asserting on incidental output (formatting, ordering) the requirements don't promise.
- Scenarios only an engineer would run; flows must mirror actual usage.

## References
- [assert_cmd](https://docs.rs/assert_cmd/) · [test organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests)
