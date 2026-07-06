# Skills

Skills are on-demand knowledge modules that attach a specific technology, pattern, or framework to
an otherwise generic agent. Role files stay technology-agnostic and list their skills in a table;
the "how to use X" lives here and is loaded only when a task needs it.

## Structure

One kebab-case folder per skill, directly under `skills/`, containing a `SKILL.md` (frontmatter:
`name`, `description`) plus optional supporting files (examples, references, checklists). Folder
names carry a prefix for the area they belong to:

| Prefix | Area |
|--------|------|
| `arch-` | Architectural patterns & styles |
| `cr-` | Code-review lenses & checklists |
| `dev-` | Languages, environments, coding practices |
| `functest-` | Functional testing techniques & harnesses |
| `inttest-` | Integration testing techniques & harnesses |
| `ops-` | CI/CD & delivery tooling |
| `sm-` | Process frameworks & facilitation |
| `systest-` | System testing techniques & harnesses |
| `unittest-` | Unit-testing techniques & frameworks |
