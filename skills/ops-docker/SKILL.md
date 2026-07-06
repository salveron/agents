---
name: ops-docker
description: Containers in CI/CD — pipeline jobs running in containers, building images in pipelines, registries, build caching, tag strategy. Load when pipelines build images or run inside containers.
---

# Docker (CI/CD)

## When to use this skill
Pipeline jobs run inside containers or build container images: GitLab CI `image:`/executors,
Jenkins docker agents, image builds and pushes as pipeline stages.

## Scope
- **Covers:** Container-based pipeline jobs, in-pipeline image building, registries, caching,
  tagging.
- **Does not cover:** Writing the application's Dockerfile and local dev stacks — see
  `dev-docker`; pipeline structure — `ops-gitlab-ci` / `ops-jenkins`.

## Core guidance
- **Jobs run in pinned toolchain images:** GitLab `image:` per job, Jenkins `agent { docker { … } }`
  — the same images developers use (`dev-docker`), pinned by tag or digest, never `latest`.
- **Building images in CI — pick the mechanism deliberately:**
  - *Docker-in-Docker (DinD):* isolated but needs `privileged` — a real security cost.
  - *Host socket mount:* fast but jobs can control the host daemon — trusted pipelines only.
  - *Daemonless builders (kaniko, buildah):* no privilege, registry-native caching — prefer for
    shared runners.
- **Registry discipline:** authenticate with masked CI credentials; push immutable tags
  (commit SHA) plus a moving convenience tag; deploys reference the immutable tag.
- **Cache across builds:** registry-backed layer cache (`--cache-from`, kaniko `--cache=true`) —
  an uncached CI build pays the full price every run.
- **Scan before push** when a scanner is available; a failing scan is a pipeline gate like any test.

## Steps / patterns
1. Pin every job image; prove a pipeline run is reproducible a week later.
2. Choose the build mechanism per runner trust level; document why.
3. Wire layer caching and verify: a no-change rebuild must be measurably faster.
4. Tag with the commit SHA; make the deploy job consume exactly that tag.

## Pitfalls & anti-patterns
- `privileged: true` copied from a tutorial without understanding what it grants.
- Deploying moving tags (`latest`, `main`) — rollbacks become guesswork.
- Rebuilding without cache on every pipeline — slow and expensive for nothing.
- Credentials in image layers or echoed into job logs.

## References
- [GitLab: Docker in CI](https://docs.gitlab.com/ee/ci/docker/) · [kaniko](https://github.com/GoogleContainerTools/kaniko) · [Jenkins docker agents](https://www.jenkins.io/doc/book/pipeline/docker/)
