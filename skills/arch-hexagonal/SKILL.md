---
name: arch-hexagonal
description: Ports & adapters — a domain core isolated from I/O behind explicit interfaces, adapters at the edges, dependencies pointing inward. Load when designing a system around an isolated domain core.
---

# Hexagonal Architecture (Ports & Adapters)

## When to use this skill
The design calls for a domain core isolated from I/O — business logic worth protecting from
frameworks, databases, and transport, or a system that must be testable without infrastructure.

## Scope
- **Covers:** Ports (interfaces), driving/driven adapters, dependency direction, composition.
- **Does not cover:** Classic layered style — see `arch-layered`.

## Core guidance
- **The core** holds domain logic and knows nothing of the outside: no framework, ORM, transport,
  or clock dependencies. Everything it needs arrives through interfaces it owns.
- **Ports are owned by the core.** *Driving* ports = the use cases the core offers (called by the
  outside); *driven* ports = the capabilities it requires (repositories, notifiers, clocks).
- **Adapters live at the edge.** Driving adapters translate the outside in (HTTP handler, CLI,
  scheduler → use case); driven adapters implement the required capabilities (Postgres repository,
  SMTP notifier). Adapters depend on ports — never the reverse.
- **Dependency rule:** all source dependencies point inward. Domain types cross ports; ORM rows,
  request objects, and framework types do not.
- **Composition root** wires adapters to ports at startup — the only place that knows everything.
- In Python, ports are `typing.Protocol`s and adapters are classes (see `dev-python313-pep8`); in
  C++, ports are abstract interfaces (see `dev-cpp17-salveron`). The payoff: the core unit-tests
  without mocks of infrastructure — fakes of ports suffice.

## Steps / patterns
1. List the use cases → define driving ports (one per capability, not per entity).
2. Ask what the core must reach for → define driven ports, named for the *need* ("ArticleStore"),
   not the technology ("PostgresClient").
3. Implement the core against the ports; unit-test it with in-memory fakes.
4. Implement adapters last; integration-test them against the real technology (the seam the
   Integration Tester verifies).

## Pitfalls & anti-patterns
- Anemic core: all logic drifts into adapters or "service" glue — the hexagon protects nothing.
- Leaky ports: ORM entities or HTTP types in port signatures re-couple the core to the edge.
- Port-per-entity CRUD explosion instead of capability-shaped ports.
- Skipping the composition root — adapters instantiating each other ad hoc.

## References
- Alistair Cockburn, [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
