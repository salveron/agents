# Agents

A tool-neutral team of software-development agents. Roles are generic and project-agnostic;
technology-, pattern-, and framework-specific know-how lives in [skills](skills/README.md) loaded
on demand.

## Roster

| Role | File | Owns |
|------|------|------|
| Project Manager | [roles/project-manager.md](roles/project-manager.md) | Intake, breakdown, routing, tracking, integration |
| Business Analyst | [roles/business-analyst.md](roles/business-analyst.md) | Requirements, user stories, acceptance criteria, scope |
| Software Architect | [roles/software-architect.md](roles/software-architect.md) | Design, structure, interfaces, standards, decisions |
| Software Developer | [roles/software-developer.md](roles/software-developer.md) | Implementation, bug fixes, refactoring |
| Code Reviewer | [roles/code-reviewer.md](roles/code-reviewer.md) | Change review, standards, approval |
| Unit Tester | [roles/unit-tester.md](roles/unit-tester.md) | Unit tests only (sole owner) |

## Routing — hybrid

The Project Manager is the default entry point and orchestrator; any agent may also delegate
peer-to-peer to the obvious owner, looping the PM in when scope, priorities, or ownership change.
Each role file's **Delegation & escalation** section defines what to hand off, to whom, and when
to escalate to the human.

```
request ──▶ Project Manager (clarify, break down, sequence)
                │
   ┌────────────┼───────────────┬──────────────┬───────────────┐
   ▼            ▼               ▼              ▼               ▼
Business    Software        Software       Code           Unit
Analyst     Architect       Developer      Reviewer       Tester
(what/why)  (how/design)    (build)        (approve)      (unit tests)

typical peer-to-peer flow:
  BA ──▶ Architect ──▶ Developer ──▶ Reviewer
                          └──▶ Unit Tester
```
