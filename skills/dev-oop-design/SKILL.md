---
name: dev-oop-design
description: SOLID principles, modern design principles, and classic design patterns (factory, builder, singleton, adapter, decorator, observer, strategy, iterator, …) with judgment on when not to use them. Load when shaping classes, modules, or interfaces in any OO codebase.
---

# OOP Design (SOLID & patterns)

## When to use this skill
Classes, modules, or interfaces are being designed or restructured — or a review debates whether
a structure is sound — in any object-oriented codebase (C++, Python, …).

## Scope
- **Covers:** SOLID, modern design principles, classic (GoF) patterns with modern notes.
- **Does not cover:** System-level styles — `arch-hexagonal` / `arch-layered`; language idioms —
  the `dev-` language skills.

## Core guidance

### SOLID
- **S**ingle responsibility — a class has one reason to change; name that reason.
- **O**pen/closed — extend behavior by adding types or strategies, not by editing switch-ladders.
- **L**iskov substitution — a subtype honors the base contract: no strengthened preconditions,
  no weakened postconditions, no surprises.
- **I**nterface segregation — many small role-interfaces beat one fat one; clients see only what
  they use.
- **D**ependency inversion — depend on abstractions at the seams; inject dependencies through the
  constructor, never reach out to globals.

### Modern principles
- Composition over inheritance: inherit to *be* substitutable, compose to *reuse*.
- Program to interfaces (abstract classes / `typing.Protocol`); keep concrete types at the edges.
- Abstain until it repeats: introduce an abstraction on the second or third occurrence, not the
  first — YAGNI beats speculative generality.
- Law of Demeter as a smell detector: a long `a.b().c().d()` chain means a missing method.

### Patterns — use when / watch out
| Pattern | Use when | Watch out |
|---------|----------|-----------|
| Factory (method/abstract) | Creation varies by configuration or subtype | Don't wrap a plain constructor |
| Builder | Many optional parts, staged construction | Overkill for ≤ 3 parameters |
| Singleton | Exactly one *process-wide* resource, truly | Hidden global state — prefer one instance, injected |
| Adapter | An existing interface must fit a required one | Adapting in both directions at once |
| Decorator | Stacking optional behavior around a core | Deep stacks obscure order dependence |
| Facade | One simple face over a messy subsystem | The facade growing into a god object |
| Observer | Many reactions to one event source | Lifetimes and unsubscription; cycles |
| Strategy | Interchangeable algorithms behind one contract | An enum + switch is not a strategy |
| Iterator | Traversal decoupled from the container | State the invalidation rules |
| Template method | Fixed skeleton, varying steps | Prefer strategy when the skeleton itself varies |

## Steps / patterns
1. Name each class's single responsibility; if the name needs an "and", split the class.
2. Draw the seams first (interfaces) and inject them; concrete wiring lives at the composition root.
3. Reach for a pattern only when its problem is actually present — then use its name in the code.
4. In review, test the structure against SOLID one letter at a time; cite the letter in findings.

## Pitfalls & anti-patterns
- Pattern-itis: `AbstractSingletonProxyFactoryBean` — patterns are vocabulary, not achievements.
- Singleton as a fancy global variable; inject the instance instead.
- Inheritance for code reuse — it breaks LSP sooner or later; compose.
- Speculative interfaces with a single implementation and nothing else consuming them.
- God classes accreting responsibilities because "they already have the data".

## References
- Gamma, Helm, Johnson, Vlissides — *Design Patterns* (GoF)
- Robert C. Martin — the SOLID principles
- [refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)
