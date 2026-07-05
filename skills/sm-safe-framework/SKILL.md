---
name: sm-safe-framework
description: Scaled Agile Framework (SAFe) — PI planning, Agile Release Trains, program-level cadence and roles. Load when the team operates within a SAFe environment.
---

# SAFe (Scaled Agile Framework)

## When to use this skill
- The team belongs to an Agile Release Train: PI planning, ART syncs, system demos, Inspect & Adapt.
- Work arrives as Features from an ART backlog, or priorities are argued with WSJF.
- Cross-team dependencies, program cadence, or SAFe roles (RTE, Product Management, Business
  Owners) shape how the team plans and delivers.

## Scope
- **Covers:** SAFe 6.0 structure — Agile Release Trains, Planning Intervals, PI planning,
  program-level events and roles, and how they map to this collection's roles.
- **Does not cover:** Single-team Scrum mechanics.

## Core guidance

### Structure
- **Configurations:** Essential → Large Solution → Portfolio → Full. Start from Essential; add a
  level only when it demonstrably pays for its coordination cost.
- **Agile Release Train (ART):** a long-lived team of 5–12 agile teams (~50–125 people) aligned to
  a value stream, planning and delivering on one synchronized cadence.
- **Planning Interval (PI):** 8–12 weeks, typically 5 iterations — 4 delivery + 1 **Innovation &
  Planning (IP)** iteration. (Until SAFe 6.0 "PI" meant *Program Increment*; same cadence, new name.)
- **Backlog hierarchy:** Portfolio Epics → ART Features (benefit hypothesis + acceptance criteria)
  → team Stories.
- **WSJF prioritization:** weighted shortest job first = cost of delay ÷ job size, where cost of
  delay = user/business value + time criticality + risk reduction/opportunity enablement.

### SAFe roles mapped to this collection
| SAFe role | Closest role here | Difference at scale |
|-----------|-------------------|---------------------|
| Release Train Engineer (RTE) | Scrum Master | Scrum Master of the whole train: facilitates PI planning and ART sync, tracks program risks |
| Product Management | Product Owner | Owns the ART backlog of Features and the roadmap; the team-level PO owns Stories |
| System Architect | Software Architect | Designs at ART level: intentional architecture, runway, cross-team seams |
| Business Owners | Engineering Sponsor | Approve PI objectives, assign business value, hold the budget |
| Scrum Master / Team Coach | Scrum Master | Team level; also represents the team at the coach sync |

### Cadence of events
- **PI planning** (2 days, whole ART): business context and vision briefings → team breakouts
  (draft plans, risks, dependencies) → management review → final plans → **confidence vote**
  (below 3 of 5 → rework the plan). Outputs: team PI objectives (committed + uncommitted) and the
  **ART planning board** of dependencies and milestones.
- **During the PI:** teams run their usual iteration events; **ART sync** (RTE, Scrum Masters,
  POs) tracks progress and risks; the **system demo** shows integrated work of all teams every
  iteration.
- **Inspect & Adapt** (PI end): PI system demo → quantitative review (planned vs. delivered
  business value, predictability) → problem-solving workshop feeding improvement items into the
  next PI backlog.
- **IP iteration:** slack for innovation, PI-planning preparation, and finishing — never planned
  full of feature work.

## Steps / patterns
Operating as Scrum Master inside SAFe:
1. **Before PI planning:** refine the team backlog against the candidate Features; pre-spot
   cross-team dependencies; know the team's realistic capacity.
2. **During PI planning:** facilitate the team breakout; put every dependency on the ART planning
   board; keep committed objectives within capacity — stretch goes to uncommitted.
3. **During the PI:** raise risks and dependency slips at ART sync early; **ROAM** program risks
   (Resolved, Owned, Accepted, Mitigated); protect the team from mid-PI scope injection.
4. **At Inspect & Adapt:** bring data (predictability, flow metrics), not impressions; turn the
   top problems into concrete items for the next PI.

## Pitfalls & anti-patterns
- **Waterfall in agile clothing:** treating the PI plan as a fixed contract. It commits to
  objectives, not to a Gantt chart — replan when learning demands it.
- **100% capacity loading:** no uncommitted objectives and a feature-stuffed IP iteration;
  predictability collapses at the first surprise.
- **Cargo-culting levels:** adopting Portfolio/Full when Essential (or plain Scrum) suffices —
  every layer must earn its coordination cost.
- **Dependency management as a lifestyle:** the same dependencies recurring every PI mean the team
  boundaries are wrong; restructure toward value streams instead of tracking harder.
- **Gamed WSJF:** inflated business-value scores turn prioritization into politics; keep sizing
  relative and revisit stale estimates.
- **Confidence-vote theater:** a pressured 4-of-5 hides risk; a low vote is information — act on it.

## References
- [SAFe knowledge base](https://framework.scaledagile.com/) — official framework site (SAFe 6.0)
- [PI Planning](https://framework.scaledagile.com/pi-planning) — event agenda, inputs, outputs
- Related articles there: Agile Release Train, Planning Interval, WSJF, Inspect & Adapt,
  Innovation and Planning Iteration
