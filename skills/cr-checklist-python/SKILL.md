---
name: cr-checklist-python
description: Structured checklist for reviewing Python 3.13 changes — typing, OO design, PEP 8/ruff conformance, error handling, resource safety. Load for a systematic review pass over Python code.
---

# Code Review Checklist (Python)

## When to use this skill
A Python change needs a systematic, repeatable review pass.

## Scope
- **Covers:** Review dimensions and an ordered checklist for Python changes (per `dev-python313-pep8` standards).
- **Does not cover:** Security deep dive — see `cr-security-owasp`.

## Core guidance
Review in priority order — correctness first, then design, then style. Cite a location for every
finding and separate must-fix from nice-to-have.

## Steps / patterns
1. **Correctness**
   - Error paths: exceptions caught at the right level, never bare `except:`, context preserved.
   - Resources: files/locks/connections managed with `with`; no leaks on early returns.
   - Mutable default arguments; unintended shared state on class attributes.
   - Behavior matches the acceptance criteria and the stated intent of the change.
2. **Types**
   - Public functions/methods fully annotated; no un-justified `Any`; modern syntax (`X | None`).
   - Interfaces expressed as `Protocol` where the design defines a seam.
3. **Design (OO-first, per repo standard)**
   - New logic lives in cohesive classes, not free-function piles; dataclasses for value types.
   - Dependencies injected, not instantiated inline; I/O kept at the edges.
   - The change is minimal and focused; no drive-by refactoring.
4. **Style** — conformance to `dev-python313-pep8` (that skill owns the exact rules)
   - `ruff format` + `ruff check` clean; naming, typing, and required docstrings all pass.
   - Comments explain *why*, not *what*.
5. **Tests & docs**
   - Unit coverage exists for new logic (authored by the Unit Tester) and exercises error paths.
   - Inline docs updated with the change.

## Pitfalls & anti-patterns
- Approving on style alone — a beautifully formatted wrong change is still wrong.
- Letting `# type: ignore` and `Any` pass without a stated reason.
- Treating missing tests as the author's problem — route the gap to the Unit Tester explicitly.

## References
- `dev-python313-pep8` (the standards this checklist enforces) · [ruff rules](https://docs.astral.sh/ruff/rules/)
