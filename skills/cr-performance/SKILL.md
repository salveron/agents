---
name: cr-performance
description: Performance review lens — algorithmic complexity, allocations and copies in hot paths, I/O patterns, measurement-before-optimization guardrails. Load when a change touches hot paths or performance-sensitive code.
---

# Performance Review

## When to use this skill
A change touches hot paths, loops over large data, or I/O-heavy code — or the review explicitly
asks for a performance pass.

## Scope
- **Covers:** A language-agnostic performance review pass, with C/C++/Python notes.
- **Does not cover:** Writing benchmarks or profiling sessions (the author's/Developer's job);
  system-level performance testing — `systest-pytest`.

## Core guidance
A performance finding names **the cost and the scale at which it hurts** ("O(n²) over the order
list — fine at 100, minutes at 100k"). Speculation cuts both ways: demand measurement before
accepting perf-motivated complexity, and before rejecting clear code as "too slow".

## Steps / patterns
1. **Complexity first** — it dwarfs everything else:
   - Nested loops over the same collection (hidden O(n²)); membership tests on lists where a
     set/map belongs; recomputation inside loops that could hoist or cache.
2. **Allocations & copies in hot paths:**
   - C++: missing `reserve`, temporary strings, by-value passes of heavy objects where
     `const&`/`string_view` serves; churn from repeated small `new`s.
   - Python: string concatenation in loops (use `join`), needless `list()` materialization of
     iterators, per-iteration object creation in tight loops.
3. **I/O patterns:** N+1 round trips where one batched call serves; unbuffered or per-record
   writes; synchronous calls serialized where they could overlap; missing streaming for large data.
4. **The guardrail, both directions:** perf-motivated complexity without a measurement →
   request the number (profile, `timeit`, benchmark); "this looks slow" without scale analysis →
   don't block the change on it.

## Pitfalls & anti-patterns
- Micro-optimizing cold code while an O(n²) sails through in the same diff.
- Accepting "it's faster this way" with no numbers — or demanding numbers for obviously-free wins.
- Trading correctness or clarity for speed before correctness has even settled.
- Benchmark-in-a-vacuum claims: measured on toy data, deployed on real data.

## References
- [Python profiling — cProfile](https://docs.python.org/3.13/library/profile.html) ·
  [perf wiki](https://perfwiki.github.io/main/)
