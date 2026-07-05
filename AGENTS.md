# Agents

A collection of generic, project-agnostic roles (`roles/`) assembled into **rosters** — named
line-ups for a chosen way of working. One roster is active at a time; only its roles take tasks.
Technology-, pattern-, and framework-specific know-how lives in [skills](skills/README.md) loaded
on demand.

## Routing

Each role takes what matches its scope and delegates the rest to the obvious owner; each role
file's **Delegation & escalation** section defines what to hand off, to whom, and when to escalate
to the human. If a referenced role is not in the active roster, route to the nearest roster
member, else to the human.

## Rosters

### Core (default)

Methodology-agnostic; the Project Manager plans and coordinates work that spans several roles.

| Role | File | Owns |
|------|------|------|
| Product Owner | [roles/product-owner.md](roles/product-owner.md) | Requirements, acceptance criteria, backlog priority, scope |
| Project Manager | [roles/project-manager.md](roles/project-manager.md) | Planning, breakdown, tracking, integration |
| Software Architect | [roles/software-architect.md](roles/software-architect.md) | Design, structure, interfaces, standards, decisions |
| Tech Lead | [roles/tech-lead.md](roles/tech-lead.md) | Implementation strategy, technical unblocking, tech debt, conventions |
| Software Developer | [roles/software-developer.md](roles/software-developer.md) | Implementation, bug fixes, refactoring |
| Code Reviewer | [roles/code-reviewer.md](roles/code-reviewer.md) | Change review, standards, approval |
| Unit Tester | [roles/unit-tester.md](roles/unit-tester.md) | Unit testing, mocking, stubbing |

```mermaid
flowchart LR
    subgraph flow [delivery flow]
        PO["Product Owner<br>what / why / what first"] --> SA["Software Architect<br>how / design"]
        SA --> DEV["Software Developer<br>build"]
        DEV --> CR["Code Reviewer<br>approve"]
        DEV --> UT["Unit Tester<br>unit tests"]
        SA -.- TL["Tech Lead<br>implementation strategy,<br>unblocking"]
        TL -.-> DEV
    end
    PM["Project Manager<br>plan, track, integrate"] -.-> flow
```

### Scrum

No Project Manager: the developers own the sprint plan, the Scrum Master owns the process, and the
Engineering Sponsor holds the boundary to the human. Responsibilities tagged **Scrum:** in the
role files apply only while this roster is active.

| Role | File | Owns |
|------|------|------|
| Product Owner | [roles/product-owner.md](roles/product-owner.md) | Backlog & priority, sprint goal, acceptance at sprint review |
| Scrum Master | [roles/scrum-master.md](roles/scrum-master.md) | Process, facilitation, impediments, focus |
| Engineering Sponsor | [roles/engineering-sponsor.md](roles/engineering-sponsor.md) | Escalations, arbitration, resources, boundary to the human |
| Software Architect | [roles/software-architect.md](roles/software-architect.md) | Design, standards; epic/feature-level refinement |
| Software Developer | [roles/software-developer.md](roles/software-developer.md) | Implementation; sprint breakdown & estimation |
| Code Reviewer | [roles/code-reviewer.md](roles/code-reviewer.md) | Change review; Definition of Done |
| Unit Tester | [roles/unit-tester.md](roles/unit-tester.md) | Unit testing, mocking, stubbing |

```mermaid
flowchart LR
    subgraph sprint [sprint loop]
        PO["Product Owner<br>backlog, sprint goal"] --> DEV["Software Developer<br>sprint plan, build"]
        DEV --> CR["Code Reviewer<br>approve, DoD"]
        DEV --> UT["Unit Tester<br>unit tests"]
        CR -->|accept at review| PO
    end
    SA["Software Architect<br>design, epic-level refinement"] -.-> sprint
    SM["Scrum Master<br>process, impediments"] -.-> sprint
    ES["Engineering Sponsor<br>escalations, arbitration"] -.-> sprint
```
