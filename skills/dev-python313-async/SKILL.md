---
name: dev-python313-async
description: asyncio in Python 3.13 — when async pays off, structured concurrency with TaskGroup, cancellation and timeouts, clean sync/async boundaries. Load when implementing asynchronous Python.
---

# Python 3.13 asyncio

## When to use this skill
The task involves asynchronous Python: concurrent I/O, `async def` code paths, or deciding
whether async is warranted at all.

## Scope
- **Covers:** asyncio on Python 3.13 — structure, cancellation, timeouts, boundaries.
- **Does not cover:** General Python idioms — `dev-python313-pep8`; unit testing — `unittest-pytest`.

## Core guidance
- **Async pays for I/O-bound concurrency only.** Waiting on sockets, subprocesses, many slow
  calls at once — yes. CPU-bound work — no (the GIL; use processes). One slow call after another
  with no fan-out — plain sync is simpler and just as fast.
- **Structured concurrency:** `asyncio.TaskGroup` is the default fan-out tool — children are
  awaited together and cancelled together on failure. Bare `create_task` without a kept reference
  is a bug (tasks can be garbage-collected mid-flight).
- **Cancellation is normal control flow:** `asyncio.CancelledError` must never be swallowed —
  clean up (`finally`, async context managers) and let it propagate.
- **Deadlines at the boundaries:** `async with asyncio.timeout(…)` around anything that talks to
  the outside world; no unbounded awaits.
- **One loop, explicit edges:** `asyncio.run(main())` at the top; blocking calls inside coroutines
  go through `asyncio.to_thread(...)`; never call blocking I/O (`requests`, `time.sleep`) in a
  coroutine.
- **Async stays object-oriented** (house rule): async methods on classes, `async with` for
  resource lifetimes, `AsyncIterator` for streams; type hints throughout (`Awaitable`,
  `AsyncIterator`).

## Steps / patterns
1. Identify the genuinely I/O-bound seams; keep everything else synchronous.
2. Define the async boundary as a Protocol; the core stays testable with fakes.
3. Fan out with a `TaskGroup` per logical batch; put a `timeout` on the group's boundary.
4. Prove cancellation: killing the entry task must release every resource.

## Pitfalls & anti-patterns
- Blocking calls hidden inside coroutines — one `requests.get` stalls the whole loop.
- Fire-and-forget tasks with no owner; use TaskGroup or keep and await the handle.
- `except Exception` that also eats `CancelledError` (it's `BaseException` in modern Python —
  but broad handlers around awaits still cause misbehavior; re-raise).
- Async creep: making everything `async def` when only the edges wait on I/O.
- Mixing threads and the loop without `to_thread` / `run_coroutine_threadsafe`.

## References
- [asyncio documentation](https://docs.python.org/3.13/library/asyncio.html) ·
  [TaskGroup](https://docs.python.org/3.13/library/asyncio-task.html#task-groups)
