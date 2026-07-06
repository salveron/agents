---
name: dev-c17-linux
description: C17 with Linux kernel coding style — naming, layout, memory ownership, error-path discipline. Load when implementing in C.
---

# C17 (Linux kernel style)

## When to use this skill
The task is implemented in C and needs language, style, or memory-discipline guidance.

## Scope
- **Covers:** C17, Linux kernel coding style, memory ownership, error handling patterns.
- **Does not cover:** Unit testing — see `unittest-gtest`; C++ — see `dev-cpp17-salveron`.

## Core guidance
- **Target C17**, portable; avoid compiler extensions unless the project already commits to them.
- **Kernel style:** tabs (8 wide), K&R braces (opening brace on the same line, except functions),
  `lowercase_with_underscores` naming, ~80-column guidance, `/* ... */` comments, no CamelCase,
  no typedefs for plain structs (`struct foo`, not `foo_t`).
- **Memory ownership is explicit.** Every allocation has one named owner and one free path;
  document transfer of ownership in the function comment. `sizeof(*ptr)` over `sizeof(type)`.
- **Error handling:** return `0`/negative-errno style (or a documented equivalent) consistently;
  check every return value that can fail; centralize cleanup with `goto out`-style error paths —
  idiomatic, not a smell.
- **Const-correctness** on pointers that don't mutate; keep functions short and single-purpose.

## Steps / patterns
1. Define the structs and their ownership rules first; who allocates, who frees.
2. Write the error path with the success path: every early exit releases what it took.
3. Prefer `snprintf`/`strscpy`-style bounded operations over unbounded string functions.
4. Build with warnings as errors (`-Wall -Wextra -Werror`) from the first commit.

## Pitfalls & anti-patterns
- Use-after-free and double-free — the free path must be as designed as the happy path.
- Integer promotion and overflow surprises in size arithmetic; check before, not after.
- Off-by-one on buffer bounds; unbounded `strcpy`/`sprintf`.
- Uninitialized memory reads; missing `NULL` checks on every allocation.
- Deep nesting — invert conditions and return early (kernel style favors flat functions).

## References
- [Linux kernel coding style](https://www.kernel.org/doc/html/latest/process/coding-style.html)
- ISO/IEC 9899:2018 (C17)
