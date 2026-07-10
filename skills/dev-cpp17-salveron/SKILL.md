---
name: dev-cpp17-salveron
description: C++17 in the Salveron style — Google C++ Style Guide as the base with house deviations (snake_case functions, m_ members, CAPITAL_CASE constants, .cpp/.hpp files, exceptions enabled, OOP-first design), ownership via RAII. Load when implementing in C++.
---

# C++17 (Salveron style)

## When to use this skill
The task is implemented in C++ and needs language, style, or ownership guidance.

## Scope
- **Covers:** C++17, Salveron style (Google-based, deviations noted), RAII/ownership, exception
  handling, header discipline.
- **Does not cover:** Unit testing — see `unittest-gtest`; plain C — see `dev-c17-linux`;
  SOLID and design patterns — see `dev-oop-design`; threading — `dev-cpp17-concurrency`;
  builds — `dev-cmake322`.

## Core guidance
- **Target C++17**: structured bindings, `std::optional`, `std::variant`, `std::string_view`,
  if-with-initializer — use them where they clarify.
- **Style: Google C++ Style Guide as the base**, with these house deviations — types `CamelCase`,
  functions and methods `snake_case`, variables `snake_case`, data members `m_snake_case` (`m_`
  prefix, no trailing underscore), constants `CAPITAL_CASE`; files `snake_case.cpp` /
  `snake_case.hpp` with include guards; include what you use, in the prescribed order.
- **Exceptions are enabled** (deviation from Google): throw for genuinely exceptional failures,
  derived from `std::exception`; catch by `const&` at the level that can actually handle or
  translate the error; mark what cannot throw `noexcept` (moves, swaps, destructors). Exceptions
  are not control flow — expected outcomes use return types (`std::optional`, result-like types).
- **Design object-oriented.** Model the domain in classes with clear responsibilities; free
  functions only for small, pure utilities. Interfaces are abstract classes at the seams; shape
  them with `dev-oop-design` (SOLID, patterns).
- **Ownership via RAII.** `std::unique_ptr` is the default owner; raw pointers and references are
  non-owning observers; `std::shared_ptr` only for genuinely shared lifetime. No naked
  `new`/`delete` in application code. RAII is also what makes stack unwinding safe.
- **Rule of zero** first; if a destructor is needed, define/`delete` the full set of five.
- Mark single-argument constructors `explicit`; initialize members in-class; `const` by default.

## Steps / patterns
1. Define interfaces as abstract classes at the seams from the design; shape them with
   `dev-oop-design`.
2. Establish ownership in the type signatures — who owns, who borrows — before writing bodies.
3. Decide the error contract per boundary — what throws, what returns `optional`/result — and
   document it in the header.
4. Keep headers minimal: forward-declare where possible, implement in `.cpp`.
5. Build with `-Wall -Wextra -Werror`; treat clang-tidy findings as review input.

## Pitfalls & anti-patterns
- Throwing from destructors or moves; catching by value (slices) — catch by `const&`.
- Swallowing errors with bare `catch (...)` — translate or rethrow with context.
- Dangling `std::string_view`/references escaping the lifetime of what they view.
- Implicit conversions from non-`explicit` constructors; object slicing in by-value passes.
- `shared_ptr` as a default — it hides ownership design instead of expressing it.
- Uninitialized members; initialization-order dependencies across translation units.

## References
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) — the base; house
  deviations above take precedence
- [C++ Core Guidelines — error handling](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-errors)
- ISO/IEC 14882:2017 (C++17)
