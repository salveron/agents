# Agents

Routing rules and roster line-ups for the agent collection — see [README](README.md) for the
overview. One roster is active at a time; only its agents take tasks; technology-specific know-how
lives in [skills](skills/README.md), loaded on demand.

## Routing

Each agent takes what matches its scope and delegates the rest to the obvious owner; each agent
file's **Delegation & escalation** section defines what to hand off, to whom, and when to escalate
to the human. If a referenced role is not in the active roster, route to the nearest roster
member, else to the human. Each agent file's `roster` frontmatter lists the rosters it belongs to.

A new engagement starts from the human's project vision, constraints, and technology stack: the
Product Owner turns the vision into requirements, and the Software Architect fits the design to
the stack.

## Working agreements

Always-on rules for every agent, in every roster.

- **Concise everything.** All inputs and outputs are as concise and simple to read as possible
  without sacrificing readability or needed detail. Lead with the result (verdict, answer,
  done/blocked); details after, so the reader can stop early.
- **One home per fact.** Information is never duplicated across places. Find the best home for
  it first — requirement, design record, user doc, code doc — write it there once, and reference
  it from everywhere else.
- **Self-documenting code.** Code explains itself through naming and structure; comments carry
  only what code cannot. Hard cap, enforced in every code review: comment lines — including
  docstrings and doc-comments — are at most 20% of a file's lines; files over the cap go back to
  the Software Developer for compacting. In header/source languages (C/C++), headers are the
  primary documentation home; source files carry only inline comments, at most 10%.
- **Reference, don't paste.** Hand-offs carry file paths, line references, and links — never
  copied content a pointer could replace.
- **Decide, record, drop.** Once a decision is made, record it in its proper home (ADR, task,
  doc) and stop carrying the debate in context; later references point to the record.
- **Document over memorize.** Knowledge worth keeping is written down, not held in context.
  Reusable, non-project-specific knowledge belongs in a [skill](skills/README.md) — propose the
  best target skill (or a new one) to the human before writing it.
- **Load only what the task needs.** Skills, files, searches: targeted, not whole-repo sweeps.

## Rosters

One roster is active at a time; only its agents take tasks; technology-specific know-how lives
in [skills](skills/README.md), loaded on demand.

- [Lightweight](rosters/lightweight.md) — default; small projects, no PM/Tech Lead/DevOps
- [Classic](rosters/classic.md) — full methodology-agnostic line-up
- [Scrum](rosters/scrum.md) — Scrum framework, no Project Manager
