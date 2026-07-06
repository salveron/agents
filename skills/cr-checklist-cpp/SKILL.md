---
name: cr-checklist-cpp
description: Structured checklist for reviewing C++17 changes — ownership/RAII, lifetimes, rule of zero/five, Salveron-style conformance, no-exceptions discipline. Load for a systematic review pass over C++ code.
---

# Code Review Checklist (C++)

## When to use this skill
A C++ change needs a systematic, repeatable review pass.

## Scope
- **Covers:** Review dimensions and an ordered checklist for C++ changes (per `dev-cpp17-salveron` standards).
- **Does not cover:** Security deep dive — see `cr-security-owasp`.

## Core guidance
Ownership and lifetime findings first — they are where C++ changes fail silently. Cite a location
for every finding; separate must-fix from nice-to-have.

## Steps / patterns
1. **Ownership & RAII**
   - `unique_ptr` for owners, raw pointers/references only as observers; `shared_ptr` justified.
   - No naked `new`/`delete`; resources wrapped in RAII types.
   - Rule of zero holds — or all five special members are handled deliberately.
2. **Lifetimes**
   - No `string_view`, spans, references, or iterators outliving what they view.
   - Lambda captures don't dangle (`&` captures on deferred execution inspected).
3. **Correctness**
   - Members initialized in-class or in every constructor; no init-order surprises.
   - Single-argument constructors `explicit`; no object slicing (by-value polymorphic passes).
   - Error handling follows the no-exceptions convention: status/expected returns checked.
4. **Style** — conformance to `dev-cpp17-salveron` (that skill owns the naming/layout rules)
   - Naming, file names, include order, and header guards all follow that skill.
   - `const` correctness on methods and parameters.
5. **Tests & scope**
   - Unit coverage for new logic (authored by the Unit Tester), including failure returns.
   - The change is minimal; no unrelated reformatting mixed in.

## Pitfalls & anti-patterns
- Waving through `auto` where the type carries ownership semantics the reader needs to see.
- Accepting `shared_ptr` "to be safe" — it usually hides an undesigned lifetime.
- Missing that a "small" header change recompiles the world — flag include-graph growth.

## References
- `dev-cpp17-salveron` (the standards this checklist enforces)
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) — the base style
