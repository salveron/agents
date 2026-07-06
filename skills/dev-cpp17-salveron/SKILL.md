---
name: dev-cpp17-salveron
description: C++17 in the Salveron style — Google C++ Style Guide as the base with naming deviations (m_ members, CAPITAL_CASE constants, .cpp/.hpp files), ownership via RAII, no exceptions. Load when implementing in C++.
---

# C++17 (Salveron style)

## When to use this skill
The task is implemented in C++ and needs language, style, or ownership guidance.

## Scope
- **Covers:** C++17, Salveron style (Google-based, deviations noted), RAII/ownership, header
  discipline.
- **Does not cover:** Unit testing — see `unittest-gtest`; plain C — see `dev-c17-linux`.

## Core guidance
- **Target C++17**: structured bindings, `std::optional`, `std::variant`, `std::string_view`,
  if-with-initializer — use them where they clarify.
- **Style: Google C++ Style Guide as the base**, with these house deviations — types `CamelCase`,
  functions `CamelCase`, variables `snake_case`, data members `m_snake_case` (`m_` prefix, no
  trailing underscore), constants `CAPITAL_CASE`; files `snake_case.cpp` / `snake_case.hpp` with
  include guards; include what you use, in the prescribed order.
- **No exceptions** (Google rule, kept): report errors via status/expected-style return types or
  documented error codes; never throw across module boundaries.
- **Ownership via RAII.** `std::unique_ptr` is the default owner; raw pointers and references are
  non-owning observers; `std::shared_ptr` only for genuinely shared lifetime. No naked
  `new`/`delete` in application code.
- **Rule of zero** first; if a destructor is needed, define/`delete` the full set of five.
- Mark single-argument constructors `explicit`; initialize members in-class; `const` by default.

## Steps / patterns
1. Define interfaces as abstract classes (pure virtual) or templates at the seams from the design.
2. Establish ownership in the type signatures — who owns, who borrows — before writing bodies.
3. Keep headers minimal: forward-declare where possible, implement in `.cpp`.
4. Build with `-Wall -Wextra -Werror`; treat clang-tidy findings as review input.

## Pitfalls & anti-patterns
- Dangling `std::string_view`/references escaping the lifetime of what they view.
- Object slicing when passing derived types by value; pass by reference or pointer.
- Implicit conversions from non-`explicit` constructors.
- `shared_ptr` as a default — it hides ownership design instead of expressing it.
- Uninitialized members; initialization-order dependencies across translation units.

## References
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) — the base; house
  deviations above take precedence
- ISO/IEC 14882:2017 (C++17)
