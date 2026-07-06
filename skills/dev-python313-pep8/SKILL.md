---
name: dev-python313-pep8
description: Idiomatic Python 3.13 — PEP 8, full typing, Sphinx docstrings, uv for project management, ruff for lint & format, object-oriented design via classes. Load when implementing in Python.
---

# Python 3.13 (PEP 8)

## When to use this skill
The task is implemented in Python and needs language, layout, or tooling guidance.

## Scope
- **Covers:** Python 3.13, PEP 8 + typing, Sphinx docstrings, uv, ruff, project layout, OO design.
- **Does not cover:** Unit-test framework specifics — see `unittest-pytest`; higher test levels —
  `inttest-pytest` / `systest-pytest` / `functest-pytest`; containers — `dev-docker`.

## Core guidance
- **Target Python 3.13.** Modern syntax is expected: `list[str]`, `X | None`, `type` aliases,
  structural pattern matching where it clarifies, f-strings everywhere.
- **Type everything public.** Full annotations on public functions, methods, and attributes;
  `typing.Protocol` for interfaces (ports); avoid `Any` — reach for generics or unions first.
- **Document with Sphinx-style docstrings.** Every module, class, and public function/method
  carries a docstring using reST fields — `:param x:`, `:returns:`, `:raises:`. Only empty
  `__init__.py` files are exempt.
- **Design object-oriented.** Model the domain in classes, not sprawling module-private free
  functions. Use `@dataclass` (often `frozen=True`) for value-like types, regular classes for
  behavior, `Protocol` for seams. A module is a namespace for related classes, not a bag of helpers.
- **uv owns the project.** `uv init`, `uv add`, `uv sync`, `uv run <cmd>`; `pyproject.toml` is the
  single source of configuration; no `requirements.txt`, no manual venv management.
- **ruff owns style.** `uv run ruff format` + `uv run ruff check`. Enabled rule sets for now —
  extend later as needed:
  `E`,`W` (pycodestyle) · `F` (pyflakes) · `I` (isort) · `UP` (pyupgrade) · `B` (bugbear) ·
  `D` (pydocstyle — docstring presence and form). Exempt package inits from the module-docstring
  rule via `[tool.ruff.lint.per-file-ignores]` `"__init__.py" = ["D104"]`; non-empty inits should
  still carry one by convention.
- **Layout:** `src/<package>/` layout, tests in `tests/`, one class hierarchy per module where
  natural, `__init__.py` exports the public API explicitly.

## Steps / patterns
1. Start from the design's interfaces: define `Protocol`s and dataclasses first.
2. Implement behavior classes against those protocols; inject dependencies via `__init__`.
3. Keep I/O at the edges; pure logic in methods that are trivially unit-testable.
4. Run `uv run ruff format && uv run ruff check --fix` before handing off.

## Pitfalls & anti-patterns
- Mutable default arguments; class attributes shared as instance state.
- Bags of free functions passing the same three parameters around — that's a class.
- Side effects at import time or in `__init__.py`.
- Bare `except:`; swallowing exceptions without context — re-raise or add context.
- Circular imports — usually a missing seam; introduce a protocol.

## References
- [PEP 8](https://peps.python.org/pep-0008/) · [typing docs](https://docs.python.org/3.13/library/typing.html)
- [Sphinx docstring fields](https://www.sphinx-doc.org/en/master/usage/domains/python.html#info-field-lists)
- [uv docs](https://docs.astral.sh/uv/) · [ruff rules](https://docs.astral.sh/ruff/rules/)
