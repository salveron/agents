---
name: ops-jenkins
description: Authoring Jenkins declarative pipelines — Jenkinsfile stages, agents, credentials, post actions, parallelism, shared libraries. Load when writing or maintaining Jenkins pipelines.
---

# Jenkins

## When to use this skill
A Jenkinsfile pipeline is being created, extended, or debugged.

## Scope
- **Covers:** Declarative Jenkinsfile: structure, agents, credentials, post handling, reuse.
- **Does not cover:** GitLab CI — see `ops-gitlab-ci`; what the gates verify (the testers' domain).

## Core guidance
- **Stay declarative:** `pipeline { agent … stages { stage { steps } } post { } }`. Drop to a
  `script {}` block only for genuinely dynamic logic — and keep it small; if Groovy grows, move
  it to a shared library or a versioned shell script.
- **Agents:** pin where work runs — `agent { label '…' }` or `agent { docker { image '…' } }` for
  reproducible toolchains; per-stage agents when stages need different environments.
- **Structure stages after the quality gates:** build → unit → integration → system/functional →
  package/deploy; `parallel {}` for independent gates so failures localize.
- **Credentials:** only via `credentials()` bindings or `withCredentials {}` — values are masked;
  never interpolate secrets into `sh "…"` double-quoted strings (Groovy interpolation leaks them —
  use single-quoted shell with env vars).
- **Post actions:** `post { always { junit '…' } failure { … } }` — publish test evidence and
  clean the workspace (`cleanWs()`) regardless of outcome.
- **Options worth defaulting:** `timeout`, `timestamps`, `disableConcurrentBuilds`,
  `buildDiscarder` — pipelines that hang or hoard history are operational debt.

## Steps / patterns
1. Sketch stages from the roster's gates; one stage per gate, named after it.
2. Choose the agent strategy (label vs. docker) before writing steps.
3. Wire `post { always }` with JUnit publishing and workspace cleanup first — evidence and
   hygiene survive failures.
4. Extract repetition into a shared library `vars/` step once it appears a second time.

## Pitfalls & anti-patterns
- Groovy-heavy scripted pipelines where declarative would do — unreadable and unrestartable.
- Secrets in double-quoted `sh` strings — masked in bindings, leaked by interpolation.
- No timeouts: a wedged stage blocks the executor pool.
- Workspace state leaking between builds; assume nothing survived, clean and re-checkout.

## References
- [Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax/) · [Using credentials](https://www.jenkins.io/doc/book/using/using-credentials/) · [Shared libraries](https://www.jenkins.io/doc/book/pipeline/shared-libraries/)
