---
name: cr-checklist-c
description: Structured checklist for reviewing C17 changes — memory ownership, bounds and integer safety, error-path completeness, kernel-style conformance. Load for a systematic review pass over C code.
---

# Code Review Checklist (C)

## When to use this skill
A C change needs a systematic, repeatable review pass.

## Scope
- **Covers:** Review dimensions and an ordered checklist for C changes (per `dev-c17-linux` standards).
- **Does not cover:** Security deep dive — see `cr-security-owasp` (memory findings overlap; report both).

## Core guidance
In C, memory and error-path findings are correctness *and* security findings — they outrank
everything else in the review. Cite a location for every finding.

## Steps / patterns
1. **Memory ownership**
   - Every allocation has one owner and a free on every path (including error paths).
   - No use-after-free, double-free, or ownership transfer without a comment saying so.
   - `sizeof(*ptr)` idiom; allocation results checked for `NULL`.
2. **Bounds & integers**
   - Every buffer write is bounded (`snprintf`, explicit length checks); no off-by-one at limits.
   - Size arithmetic checked for overflow *before* allocating or indexing.
   - Signed/unsigned comparisons and implicit promotions inspected.
3. **Error paths**
   - Every fallible call's return value checked; failures propagate consistently
     (0/negative-errno or the project's documented convention).
   - `goto out` cleanup chains release everything acquired, in reverse order.
4. **Concurrency** (when applicable)
   - Shared state identified; locking order documented; no data races on flags or counters.
5. **Style & API** — conformance to `dev-c17-linux` (that skill owns the style rules)
   - Kernel style followed (naming, braces, flat functions, early returns); check against that skill.
   - `const` correctness; `NULL`-handling of parameters documented in the function comment.

## Pitfalls & anti-patterns
- Reviewing the happy path only — most C defects live in the error path.
- Trusting the caller's buffer size claim without seeing the length passed alongside.
- Style nitpicks drowning out a missed `free()` — order findings by severity.

## References
- `dev-c17-linux` (the standards this checklist enforces)
- [Linux kernel coding style](https://www.kernel.org/doc/html/latest/process/coding-style.html)
