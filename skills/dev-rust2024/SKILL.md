---
name: dev-rust2024
description: Idiomatic Rust, edition 2024 — ownership-first design, Result-based error handling (thiserror/anyhow), traits as seams, cargo project management, rustfmt + clippy as the enforced standard. Load when implementing in Rust.
---

# Rust (edition 2024)

## When to use this skill
The task is implemented in Rust and needs language, style, ownership, or tooling guidance.

## Scope
- **Covers:** Rust edition 2024, ownership/borrowing, error handling, trait-based design, crate
  and module layout, cargo, rustfmt + clippy.
- **Does not cover:** Unit testing — see `unittest-rust`; async and concurrency —
  `dev-rust2024-async`; containers — `dev-docker`; design principles — `dev-oop-design`
  (adapted: traits and modules, not class hierarchies).

## Core guidance
- **Target edition 2024 on the stable toolchain.** Set `edition = "2024"` and `rust-version`
  (MSRV — the stable release the project starts on) in `Cargo.toml`. Stable Rust never breaks
  existing code on compiler upgrades; editions are opt-in per crate, so upgrade toolchains freely
  and treat edition migrations (`cargo fix --edition`) as rare, tool-assisted events.
- **The standard is official and toolchain-enforced:** `cargo fmt` with rustfmt defaults (no
  config file), `cargo clippy -- -D warnings` clean before handoff, the Rust API Guidelines for
  public items. Naming follows compiler conventions — `snake_case` items, `CamelCase` types,
  `SCREAMING_SNAKE_CASE` constants.
- **Ownership first.** Functions borrow (`&T`, `&mut T`) unless they need to own; each piece of
  data has one owner where it lives. When the borrow checker fights back, restructure ownership
  instead of sprinkling `.clone()`. `Box`/`Rc`/`Arc` only where the design genuinely calls for
  heap or shared ownership.
- **Errors are values:** `Result<T, E>` with `?` end to end. Libraries define error enums with
  `thiserror`; binaries may collapse to `anyhow` at the top level. Panics are for bugs (broken
  invariants), never expected failures; `unwrap`/`expect` outside tests only with a message
  stating why failure is impossible.
- **Design with traits and composition.** Traits are the seams — inject dependencies via
  generics by default, `dyn Trait` when runtime choice or compile-time cost demands it. Enums
  with exhaustive `match` model closed sets; newtypes give domain values their own type.
  `dev-oop-design`'s SOLID intent maps to traits and modules — don't emulate inheritance.
- **`#![forbid(unsafe_code)]` at the crate root by default.** A crate that must drop it
  documents the invariant every `unsafe` block upholds.
- **cargo owns the project:** `cargo new/add/build/run/test`; `Cargo.toml` is the single source
  of configuration. Split into a workspace of small crates when the project grows.
- **Visibility is design.** Modules stay private by default; `pub` is a deliberate API decision,
  with the public API re-exported at the crate root. Public items carry `///` docs with runnable
  examples (doctests).

## Steps / patterns
1. From the design, define the types and trait seams first — data as structs/enums, behavior
   contracts as traits.
2. Establish ownership in the signatures — who owns, who borrows — before writing bodies.
3. Decide the error contract per boundary: one error enum per crate or module, `#[from]`
   conversions where they clarify (thiserror).
4. Implement; run `cargo fmt && cargo clippy -- -D warnings` before handing off.

## Pitfalls & anti-patterns
- `.clone()` spray to silence the borrow checker — a sign the ownership design is wrong.
- Stringly-typed errors (`String`, `Box<dyn Error>`) in library APIs — callers can't match.
- `Rc<RefCell<…>>` to dodge ownership design — trades compile-time checks for runtime panics.
- `pub` on everything — the crate loses its API surface; keep visibility minimal.
- Premature `dyn Trait` (boxing where generics do) and premature generics (one instantiation).
- Lifetime parameters leaking into every signature when owning the data would be simpler.

## References
- [The Rust Programming Language](https://doc.rust-lang.org/book/) · [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Edition Guide](https://doc.rust-lang.org/edition-guide/) · [Clippy lint index](https://rust-lang.github.io/rust-clippy/master/)
