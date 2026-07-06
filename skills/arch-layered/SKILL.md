---
name: arch-layered
description: Classic layered (n-tier) architecture — presentation, application, domain, infrastructure, with dependencies pointing strictly downward. Load when a straightforward layered design fits better than ports & adapters.
---

# Classic Layered Architecture

## When to use this skill
The design calls for a conventional layered structure — CRUD-heavy applications, small services,
or teams/codebases where the familiar layer stack beats an inverted architecture.

## Scope
- **Covers:** Layer definitions, dependency rules, boundary types, strict vs. relaxed layering.
- **Does not cover:** Ports & adapters — see `arch-hexagonal`.

## Core guidance
- **The stack** (top calls down, never up):
  1. **Presentation** — HTTP handlers, CLI, UI: translate the outside world to application calls.
  2. **Application** — use-case orchestration, transactions, coordination; thin, no business rules.
  3. **Domain** — entities and business logic; the layer that makes the product what it is.
  4. **Infrastructure/data** — persistence, external services, technical detail.
- **Dependency rule:** downward only, no skipping in *strict* layering; *relaxed* layering
  (allowing presentation → domain reads) is a documented, deliberate choice, not an accident.
- **Boundary types:** DTOs between presentation and application; domain objects stay inside;
  database rows stay below. Mapping code is the tax that keeps layers meaningful.
- **Choose layered over hexagonal** when the domain is thin and data-centric — the inversion
  machinery of ports buys little. Choose hexagonal when domain logic is the asset. Say which and
  why in the design (an ADR-worthy call).

## Steps / patterns
1. Name the layers and write down the dependency rule (strict or relaxed) for the repo.
2. Place each new component by asking "who may call it, whom may it call".
3. Keep the application layer thin: orchestration and transactions, not rules.
4. Enforce the direction mechanically where possible (module/package structure, import linting).

## Pitfalls & anti-patterns
- Business logic bleeding into controllers above or repositories below — the classic failure.
- Fat "service" layer with an anemic domain: rules smeared across orchestrators.
- Upward or circular dependencies via "just this one callback".
- Lasagna: layers multiplying (facade → manager → service → helper) without earning their keep.

## References
- Buschmann et al., *POSA Vol. 1* — Layers pattern; Fowler, *PoEAA* — Service Layer, DTO
