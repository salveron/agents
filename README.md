# Agents

A tool-neutral collection of software-development **roles** for AI agents, assembled into
**rosters** (line-ups for a chosen way of working) and backed by on-demand **skills**
(technology-, pattern-, and methodology-specific knowledge). Given a project vision and a
technology stack, a roster of these agents takes software from requirements to verified,
releasable increments — with the human holding final authority over value, scope, and anything
irreversible.

## How it works

- **Roles** ([agents/](agents/)) are generic and project-agnostic. Each file is a complete agent
  prompt: identity, responsibilities, delegation & escalation rules, skills to load, and working
  principles. Every role decides for itself whether a task is theirs or belongs to another role.
- **Rosters** ([AGENTS.md](AGENTS.md)) pick which roles are active. AGENTS.md is the single home
  for their line-ups, routing rules, and the roster-specific tagged duties that apply only within
  a given roster.
- **Skills** ([skills/](skills/README.md)) keep the roles technology-free: one folder per skill,
  prefixed by area, loaded only when a task needs it.

## Using the roles as agents

- **Claude Code** — every role is a subagent in [.claude/agents/](.claude/agents/)
  (e.g. "use the software-developer subagent").
- **GitHub Copilot** — every role is an agent in [.github/agents/](.github/agents/).

Both `.claude/agents` and `.github/agents` are **directory symlinks to [agents/](agents/)**, and the
role files are named `*.agent.md`. So `agents/` is the single, literal source of truth: edit a role
and every tool sees it immediately; **add a role by dropping a new `agents/<name>.agent.md` — it
appears in both tools automatically, with no new links to create**.

> **Windows note:** git materializes symlinks as real links only when `core.symlinks=true` (needs
> Developer Mode or an elevated shell). Without it, `.claude/agents` and `.github/agents` are
> checked out as small text files containing the target path and the agents won't resolve. On
> Windows, enable symlinks — or replace each with a real directory of copies of the role files.

### Kickoff template

```text
Roster: lightweight
Vision: <what to build and why>
Stack: <e.g. Python 3.13 + uv, or C++17 + CMake>
Constraints: <deadlines, non-goals, quality bars>
```

Hand this to the roster; the Product Owner and Software Architect pick it up first, and routing
takes it from there.

## Decided standards (current skillset)

| Area | Standard |
|------|----------|
| Python | 3.13 · PEP 8 + full typing · Sphinx docstrings · uv · ruff (E, W, F, I, UP, B, D) · OO-first design |
| C | C17 · Linux kernel coding style |
| C++ | C++17 · Salveron style: Google-based, `m_` members, `CAPITAL_CASE` constants, `.cpp`/`.hpp` (no exceptions) |
| Containers | Docker — dev environments (`dev-docker`) & CI (`ops-docker`) |
| Unit testing | pytest (Python) · GoogleTest/gMock (C/C++) |
| Integration / system / functional | pytest as the harness |
| Architecture | Hexagonal (ports & adapters) · Classic layered |
| Process at scale | SAFe 6.0 (via the Scrum Master) |
| CI/CD | GitLab CI · Jenkins |
| Security review | OWASP lens |
