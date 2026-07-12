---
name: unittest-rust
description: Unit testing Rust with the built-in harness — #[cfg(test)] modules, assert macros, Result-returning tests, doctests, mockall for trait seams, cargo test. Load when authoring or running Rust tests.
---

# Rust built-in tests (unit level)

## When to use this skill
Rust tests are being written or run with the built-in harness (`cargo test`).

## Scope
- **Covers:** `#[cfg(test)]` unit tests, doctests, `mockall`, running via cargo; plus the cargo
  `tests/` directory as the Rust-native way to test a *library crate's public API* in-language.
- **Does not cover:** Language idioms — see `dev-rust2024`; black-box integration/system/
  functional testing of a Rust binary or service — that is `inttest-pytest` / `systest-pytest` /
  `functest-pytest` (pytest drives non-Rust artifacts via subprocess/CLI/HTTP), same as C/C++.

## Core guidance
- **Structure:** unit tests live in a `#[cfg(test)] mod tests` beside the code under test (with
  access to private items); one `#[test]` per behavior, named for the behavior.
- **Assertions:** `assert!` / `assert_eq!` / `assert_ne!`, with a context message wherever the
  values alone won't explain a failure. Tests may return `Result<(), E>` so `?` replaces
  unwrap chains.
- **Panics:** `#[should_panic(expected = "…")]` only for contracts that promise a panic;
  error-path tests assert on the returned `Err` variant instead.
- **Doctests:** examples in `///` docs compile and run with the suite — keep each the smallest
  true usage of its item; they are the public contract's examples.
- **Mocking:** `mockall` (`#[cfg_attr(test, automock)]` or `mock!`) on the trait seams the
  design defines; mock only the seam, never value types. Expect the interactions that are the
  contract, not every call.
- **Async units:** annotate with `#[tokio::test]`; drive time with `tokio::time::pause` instead
  of sleeping.
- **Library-API integration (Rust-native):** the cargo `tests/` directory builds the crate as an
  external dependency and exercises only its public API — the right tool only when the seam under
  test *is* a Rust API (a pure library crate). A Rust binary or service is integration-tested
  black-box via `inttest-pytest` & co., which drive the built artifact like any other language.
- **Running:** `cargo test` runs unit, integration, and doctests; filter by name substring
  (`cargo test parse`); show captured output with `-- --nocapture`.

## Steps / patterns
1. From the contract, list behaviors, boundaries, and error paths; one `#[test]` per behavior.
2. Arrange with plain constructors or builders; inject `mockall` mocks at designed seams only.
3. For error paths, drive the mock to return `Err` and assert the unit's documented response.
4. Verify fixes by the previously failing test; keep tests deterministic — no real I/O, clocks,
   or thread timing in unit scope.

## Pitfalls & anti-patterns
- Widening visibility (`pub(crate)` creep) just to reach internals — test through the contract;
  if it's untestable, that's a design finding, not a visibility problem.
- Over-mocking: mocks for types with no I/O or side effects — construct the real value.
- Shared mutable state via `static` — cargo runs tests in parallel by default.
- Sleeps or wall-clock time in tests — inject a clock seam or pause tokio time.
- `unwrap` chains where a `Result`-returning test with `?` reads cleaner.

## References
- [The Book — testing](https://doc.rust-lang.org/book/ch11-00-testing.html) · [mockall docs](https://docs.rs/mockall/)
