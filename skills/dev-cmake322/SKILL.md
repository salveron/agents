---
name: dev-cmake322
description: CMake 3.22 for C/C++ projects — target-based, idiomatic and deliberately simple: targets and properties, visibility keywords, FetchContent, ctest wiring. Load when creating or maintaining CMake builds.
---

# CMake 3.22 (target-based, simple)

## When to use this skill
A C or C++ project's build configuration is being created, extended, or debugged with CMake.

## Scope
- **Covers:** Target-based CMake at the 3.22 baseline: project layout, targets, visibility,
  dependencies, test wiring.
- **Does not cover:** Compiler warning policy — the `dev-c17-linux` / `dev-cpp17-salveron` skills
  own it; pipelines — `ops-gitlab-ci` / `ops-jenkins`; GoogleTest usage — `unittest-gtest`.

## Core guidance
- **Pin the baseline:** `cmake_minimum_required(VERSION 3.22)`; one `project(<name> LANGUAGES CXX)`
  (and/or `C`) at the top.
- **Everything is a target.** `add_library` / `add_executable`, configured only through
  `target_*` commands: `target_include_directories`, `target_link_libraries`,
  `target_compile_features(<t> PUBLIC cxx_std_17)`, `target_compile_options`. No global
  `include_directories`, no `CMAKE_CXX_FLAGS` mutation.
- **Visibility keywords carry the design:** `PRIVATE` = needed to build the target only,
  `PUBLIC` = needed by the target *and* its consumers, `INTERFACE` = consumers only. Getting
  these right is most of "modern CMake".
- **Dependencies:** `find_package` for system/installed libraries; `FetchContent` for small
  vendored ones (e.g. googletest). Declare in one place, link by target name
  (`GTest::gtest_main`), never by path.
- **Tests:** `enable_testing()` at the top level; register with ctest (`gtest_discover_tests`
  for GoogleTest); `ctest --test-dir build` is the runner.
- **Keep it boring.** Out-of-source builds only (`cmake -S . -B build`); list source files
  explicitly; no custom functions/macros until the same pattern repeats three times; generator
  expressions only when nothing simpler works.

## Steps / patterns
1. Skeleton: a library target with the real code, a thin executable target linking it, a
   `tests/` directory with a test target — three targets, clear edges.
2. Declare targets and their `PUBLIC`/`PRIVATE` surfaces first; the dependency graph is the design.
3. Wire third-party dependencies via `FetchContent_Declare` + `FetchContent_MakeAvailable`.
4. Configure, build, test: `cmake -S . -B build && cmake --build build && ctest --test-dir build`.

## Pitfalls & anti-patterns
- `file(GLOB …)` for sources — new files silently missing from the build; list them.
- Global flags and directories — they leak into every target and FetchContent'd dependency.
- In-source builds polluting the tree; `build/` is disposable and git-ignored.
- Variables where targets belong — passing include paths in variables instead of linking a target.
- Copy-pasted "modern CMake" boilerplate nobody on the team can explain — simpler is maintainable.

## References
- [CMake 3.22 documentation](https://cmake.org/cmake/help/v3.22/)
- [An Introduction to Modern CMake](https://cliutils.gitlab.io/modern-cmake/)
