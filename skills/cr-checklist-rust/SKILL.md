---
name: cr-checklist-rust
description: Structured checklist for reviewing Rust changes — unsafe and panic discipline, ownership in APIs, error propagation, exhaustive matching, clippy conformance. Load for a systematic review pass over Rust code.
---

# Code Review Checklist (Rust)

## When to use this skill
A Rust change needs a systematic, repeatable review pass.

## Scope
- **Covers:** Review dimensions and an ordered checklist for Rust changes (per `dev-rust2024`
  standards).
- **Does not cover:** Security deep dive — see `cr-security-owasp`; performance lens —
  `cr-performance`.

## Core guidance
The compiler already proves memory safety in safe code — spend review attention where it can't
look: `unsafe` blocks, panic paths, API ownership decisions, and error contracts. Cite a
location for every finding; separate must-fix from nice-to-have.

## Steps / patterns
1. **Unsafe & panics**
   - Every `unsafe` block carries its documented invariant — or shouldn't exist at all where
     `#![forbid(unsafe_code)]` is the policy (per `dev-rust2024`).
   - `unwrap`/`expect`/`panic!`/indexing on production paths follow the panic discipline in
     `dev-rust2024` — check against that skill, not from memory.
2. **Ownership & API**
   - Signatures borrow vs. own deliberately; no `.clone()` inserted to satisfy the borrow
     checker.
   - `Rc<RefCell<…>>` / `Arc<Mutex<…>>` appearances justified by the design, not convenience.
   - New `pub` items are intentional API and carry docs.
3. **Errors**
   - Every `Result` propagated or handled — no `let _ =` swallowing, no `.ok()` discarding.
   - Error types follow `dev-rust2024` (library error enums vs. binary-level `anyhow`).
4. **Correctness**
   - `match` arms exhaustive; wildcard `_` arms don't silently absorb future enum variants.
   - Integer overflow assumptions explicit (`checked_*` / `saturating_*` where overflow is
     reachable).
   - No blocking calls inside async contexts (per `dev-rust2024-async`).
5. **Style & tooling** — `cargo fmt` and `cargo clippy -- -D warnings` clean; naming, layout,
   and visibility per `dev-rust2024` (that skill owns the rules); comment density (`///` docs
   included) within the working-agreement cap.
6. **Tests & scope**
   - Unit coverage for new logic including `Err` paths; doctests still true.
   - The change is minimal; no unrelated reformatting mixed in.

## Pitfalls & anti-patterns
- Waving through `unsafe` because "it compiles" — the compiler checks nothing inside it.
- Accepting `clone`/`Arc` as harmless — they often paper over an ownership design flaw.
- Trusting a wildcard match arm — it's where the next variant's bug will hide.
- Reviewing macro-generated code as if hand-written — review the macro and its inputs instead.

## References
- `dev-rust2024` (the standards this checklist enforces)
- [Rustonomicon](https://doc.rust-lang.org/nomicon/) — what `unsafe` code must uphold
