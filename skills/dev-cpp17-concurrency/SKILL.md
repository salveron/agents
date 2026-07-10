---
name: dev-cpp17-concurrency
description: C++17 concurrency — std::thread with RAII joining, mutexes and scoped locks, condition variables, atomics used sparingly, documented synchronization per shared state. Load when C++ code goes multithreaded.
---

# C++17 Concurrency

## When to use this skill
C++ code is becoming multithreaded: worker threads, shared state, synchronization decisions —
or the question is whether it should.

## Scope
- **Covers:** C++17 threading: `std::thread`, mutexes/locks, condition variables, atomics,
  futures, data-race discipline.
- **Does not cover:** General C++ style and ownership — `dev-cpp17-salveron`; lock-free algorithm
  design (out of scope on purpose — don't hand-roll it).

## Core guidance
- **Concurrency must earn its complexity.** Default to single-threaded; parallelize a measured
  bottleneck, not a suspicion.
- **Threads have owners.** C++17 has no `jthread`: every `std::thread` is joined on every path —
  wrap it in a RAII guard class (join in the destructor); a detached thread touching objects
  with shorter lifetimes is a latent crash.
- **State and its mutex live together** (house OO rule): encapsulate the data, the `std::mutex`,
  and the operations in one class; lock with `std::lock_guard` / `std::scoped_lock` (the latter
  for multiple mutexes — deadlock-free ordering for free). Document each class's synchronization
  strategy in its header.
- **Condition variables always wait on a predicate:**
  `cv.wait(lock, [&]{ return m_ready; })` — spurious wakeups are the norm, not the exception.
- **Atomics for flags and counters only**, `std::memory_order_seq_cst` until a measurement says
  otherwise; atomics are not a substitute for a lock around compound state.
- **Move data, don't share it,** where possible: pass by value/move into the thread; return
  one-shot results via `std::future`/`std::promise` or `std::async`.
- **Exceptions cross threads badly:** an exception escaping a thread function calls
  `std::terminate` — catch at the thread boundary and hand it over via the future/promise.

## Steps / patterns
1. Name the shared state; everything not on that list stays thread-confined.
2. Choose per item: confine it, move it, or lock it — in that order of preference.
3. Establish one lock-ordering rule and write it down; `std::scoped_lock` where two locks meet.
4. Verify with ThreadSanitizer in tests before trusting any of it.

## Pitfalls & anti-patterns
- Capturing locals by reference in a thread lambda that outlives the scope.
- Detached threads — ownership by wishful thinking.
- Inconsistent lock order between two paths; the deadlock arrives in production.
- `condition_variable::wait` without a predicate; notify before the waiter locks.
- Sprinkling atomics over a struct and calling it thread-safe.

## References
- [cppreference — thread support library](https://en.cppreference.com/w/cpp/thread)
- Anthony Williams — *C++ Concurrency in Action* (2nd ed.)
