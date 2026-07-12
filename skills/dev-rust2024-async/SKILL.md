---
name: dev-rust2024-async
description: Async Rust on tokio — when async pays off vs. threads/rayon, task spawning and JoinSet, cancellation and timeouts, the sync/async boundary. Load when Rust code goes concurrent or async.
---

# Async Rust (tokio)

## When to use this skill
Rust code is going asynchronous or concurrent and needs runtime, task, or boundary guidance.

## Scope
- **Covers:** tokio, async/await idioms, task lifecycle, cancellation, channels, the sync/async
  boundary, choosing async vs. threads.
- **Does not cover:** Language, style, ownership — see `dev-rust2024`; testing async code —
  `unittest-rust` (with `#[tokio::test]`).

## Core guidance
- **Async is for many concurrent I/O-bound tasks** (network services, timers, fan-out calls).
  CPU-bound work belongs on threads — `std::thread`, scoped threads, or `rayon` — and a mostly
  synchronous program with one blocking call doesn't justify an async rewrite.
- **tokio is the runtime:** `#[tokio::main]`, multi-threaded scheduler by default, one runtime
  per process. Library crates take a runtime as given rather than starting their own.
- **Structured concurrency:** spawn related tasks into a `JoinSet` and join them all — no
  detached fire-and-forget `tokio::spawn`; every task's `Result` is observed somewhere.
- **Cancellation is dropping the future.** Enforce deadlines with `tokio::time::timeout` at the
  boundary that knows them; in `select!`, every arm must be cancellation-safe or its work moved
  into a spawned task.
- **The sync/async boundary is explicit:** blocking calls (sync clients, heavy files, CPU
  bursts) go through `spawn_blocking`; never `block_on` from inside the runtime.
- **Prefer message passing to shared state:** `mpsc` for pipelines, `oneshot` for replies,
  `watch` for latest-value state. Where state must be shared, `std::sync::Mutex` for short
  critical sections that never hold the guard across `.await`; `tokio::sync::Mutex` only when
  holding across one is unavoidable.
- **Async in traits:** native `async fn` in traits by default; the `async-trait` crate only when
  `dyn` dispatch is required. Values held across `.await` in spawned tasks must be `Send`.

## Steps / patterns
1. Decide per component: async (concurrent I/O), threads/rayon (CPU), or plain sync.
2. Design the task topology and channels first — who spawns, who joins, what crosses which
   channel — and document it like any other shared-state decision.
3. Wrap external await points in timeouts at the boundary where the deadline is known.
4. Push blocking work behind `spawn_blocking` at the edges; keep the async core non-blocking.

## Pitfalls & anti-patterns
- Blocking inside async — sync I/O, heavy compute, `std::thread::sleep` — stalls the executor.
- Holding a `std::sync::Mutex` guard across `.await` — deadlock-prone and blocks the worker.
- Cancellation-unsafe `select!` arms silently losing partially completed work.
- Dropping a `JoinHandle` without joining — the task's panic or `Err` vanishes.
- Boxing every trait through `async-trait` out of habit when native `async fn` works.

## References
- [tokio tutorial](https://tokio.rs/tokio/tutorial) · [tokio API docs](https://docs.rs/tokio/)
- [Async Book](https://rust-lang.github.io/async-book/)
