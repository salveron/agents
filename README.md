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
  for their line-ups, routing rules, the always-on working agreements, and the roster-specific
  tagged duties that apply only within a given roster.
- **Skills** ([skills/](skills/README.md)) keep the roles technology-free: one folder per skill,
  prefixed by area, loaded only when a task needs it.

## Using the roles as agents

Two setup scripts symlink each role and skill into the directory a tool reads. `agents/` and
`skills/` stay the single source of truth: **add a role by dropping a new `agents/<name>.agent.md`,
or a skill as `skills/<name>/SKILL.md`, then re-run the relevant script** — the new entry is picked
up with no manual linking. Both scripts are idempotent and never overwrite content they don't own,
so the target directory can safely hold other, unrelated agents or skills alongside these.

- **Claude Code, from any project on this machine** — run
  [`scripts/setup_claude_code.py`](scripts/setup_claude_code.py) once. It symlinks each role and
  skill into `~/.claude/agents/` and `~/.claude/skills/`, and imports [AGENTS.md](AGENTS.md) into
  `~/.claude/CLAUDE.md`, so the whole roster is available from every working directory. Pass a
  different config directory as an optional argument (defaults to `~/.claude`); safe to re-run after
  every `git pull`.
- **GitHub Copilot, in a given project** — run
  [`scripts/setup_github_copilot.py`](scripts/setup_github_copilot.py) `<project-root>` (use `.` for
  this repo itself). Copilot has no machine-wide config directory, so this links `.github/agents/`,
  `.github/skills/`, and `.github/AGENTS.md` at the project level, and is re-run per project that
  should see this roster.

> **Windows note:** creating symlinks needs `core.symlinks=true` and either Developer Mode or an
> elevated shell. Without symlink support the setup scripts fail rather than silently linking; on
> Windows, enable symlinks — or replace each link with a real copy of the role or skill.

### Kickoff template

```text
Roster: lightweight
Vision: <what to build and why>
Stack: <e.g. Python 3.13 + uv, C++17 + CMake, or Rust 2024 + cargo>
Constraints: <deadlines, non-goals, quality bars>
```

Hand this to the roster; the Product Owner and Software Architect pick it up first, and routing
takes it from there.
