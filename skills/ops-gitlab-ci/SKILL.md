---
name: ops-gitlab-ci
description: Authoring GitLab CI pipelines — .gitlab-ci.yml stages, jobs, rules, cache vs. artifacts, needs-based DAGs, environments, CI/CD variables. Load when writing or maintaining GitLab CI configuration.
---

# GitLab CI

## When to use this skill
A .gitlab-ci.yml pipeline is being created, extended, or debugged.

## Scope
- **Covers:** GitLab CI YAML: pipeline structure, execution control, caching, artifacts, environments.
- **Does not cover:** Jenkins — see `ops-jenkins`; what the gates verify (the testers' domain).

## Core guidance
- **Structure:** `stages:` defines phase order; jobs bind to a stage; `needs:` builds a DAG so
  independent jobs skip the stage barrier. Map test levels to stages (unit → integration →
  system/functional) so each tester's gate is a visible pipeline step.
- **Execution control with `rules:`** (never legacy `only/except`): match on branch, MR, tags,
  changed paths; add a top-level `workflow: rules:` to prevent duplicate branch+MR pipelines.
- **Cache vs. artifacts:** cache = dependency reuse between runs (keyed on the lockfile, e.g.
  `key: files: [uv.lock]`); artifacts = job outputs passed forward (builds, `reports:` for JUnit
  test evidence). Don't ship dependencies as artifacts.
- **Reuse:** `default:` for shared image/before_script; hidden `.job-template` keys with
  `extends:`; `include:` for cross-repo templates. Keep each job's `script` short — real logic
  lives in versioned scripts, not YAML.
- **Variables & secrets:** CI/CD variables (masked, protected) for anything sensitive — never in
  the YAML; `environment:` blocks for deploy jobs to get tracked deployments and rollbacks.
- Mark long jobs `interruptible: true` so superseded pipelines cancel; add `timeout:` per job.

## Steps / patterns
1. Sketch stages from the roster's quality gates; one job per gate, named after it.
2. Write `workflow: rules:` first; verify with a draft MR that exactly one pipeline runs.
3. Wire caching on the dependency lockfile; confirm a warm run is measurably faster.
4. Emit `reports: junit:` from every test job — the evidence feeds review and acceptance.

## Pitfalls & anti-patterns
- No `workflow: rules:` → double pipelines per MR push, doubled minutes.
- Monolithic do-everything jobs — no parallelism, no failure locality.
- Caching artifacts or shipping caches — slow pipelines that "work".
- Inline secrets or `echo $TOKEN` in scripts; unmasked variables in logs.

## References
- [.gitlab-ci.yml reference](https://docs.gitlab.com/ee/ci/yaml/) · [rules](https://docs.gitlab.com/ee/ci/jobs/job_rules.html) · [caching](https://docs.gitlab.com/ee/ci/caching/)
