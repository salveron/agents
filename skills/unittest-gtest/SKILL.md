---
name: unittest-gtest
description: Unit testing C and C++ with GoogleTest/gMock — suites, fixtures, matchers, parametrized tests, CMake integration. Load when authoring or running C/C++ unit tests.
---

# GoogleTest (unit level)

## When to use this skill
C or C++ unit tests are being written or run with GoogleTest.

## Scope
- **Covers:** GoogleTest + gMock for C++17 (and C code tested through C++ test files).
- **Does not cover:** Language idioms — see `dev-cpp17-salveron` / `dev-c17-linux`; higher test
  levels — `inttest-pytest` / `systest-pytest` / `functest-pytest`.

## Core guidance
- **Structure:** `TEST(SuiteName, BehaviorName)` for free cases; `TEST_F` with a fixture class
  (`SetUp`/`TearDown`) for shared arrangement; suite = the unit, test = the behavior.
- **Assertions:** `EXPECT_*` to record and continue, `ASSERT_*` only when continuing is
  meaningless (e.g. a null that would crash the test). Prefer `EXPECT_THAT(value, matcher)` with
  gMock matchers for readable failures.
- **Parametrize** case tables with `TEST_P` + `INSTANTIATE_TEST_SUITE_P`; name the instantiations.
- **gMock:** `MOCK_METHOD` on the seam interface (abstract class from the design); default to
  `NiceMock` and assert only the interactions that are the contract — `StrictMock` invites
  brittle tests.
- **Build:** wired through CMake/ctest — `dev-cmake322` owns the setup; tests build with the same
  warnings-as-errors as production code.
- Testing C: compile the C unit into the C++ test target; wrap the header in `extern "C"`.

## Steps / patterns
1. From the contract, list behaviors, boundaries, error returns; one `TEST` per behavior.
2. Fixtures own lifetime: acquire in `SetUp`, release in `TearDown` — RAII members preferred.
3. For error paths, drive the injected mock to fail and assert the unit's documented response.
4. Verify fixes by the previously failing test; keep tests deterministic (no sleeps, no real I/O).

## Pitfalls & anti-patterns
- `ASSERT_*` everywhere — one failure hides the rest of the diagnostics.
- Mocking value types or internals instead of the designed seam.
- Shared mutable state across tests via static/global fixtures — order-dependent suites.
- Death tests and real threads where a matcher would do — slow and flaky.

## References
- [GoogleTest user's guide](https://google.github.io/googletest/) · [gMock cookbook](https://google.github.io/googletest/gmock_cook_book.html)
