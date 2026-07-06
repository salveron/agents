---
name: dev-docker
description: Containerized development environments — Dockerfiles, compose stacks for local development, reproducible toolchains. Load when the development environment is containerized.
---

# Docker (development environments)

## When to use this skill
The development environment is containerized: writing Dockerfiles, running the local stack in
compose, or keeping toolchains reproducible across machines.

## Scope
- **Covers:** Dockerfiles, docker-compose for local development, image hygiene, dev containers.
- **Does not cover:** Containers in CI/CD pipelines — see `ops-docker`.

## Core guidance
- **Image hygiene:** slim, pinned base images (`python:3.13-slim`, not `latest`); a `.dockerignore`
  that keeps the build context small; a non-root user in the final image.
- **Layer order is cache design:** copy dependency manifests and install first, copy source last —
  code changes must not re-install dependencies.
- **Multi-stage builds:** a build stage with toolchains, a lean runtime stage with only what runs;
  the runtime stage is what ships.
- **Compose for the local stack:** one service per component; bind-mount source for live editing,
  named volumes for dependency caches and data; `depends_on` with healthchecks for start order.
- **Reproducibility is the point:** the container defines the toolchain (compiler, Python, uv)
  so "works on my machine" means "works in the image"; document `docker compose up` as the one
  entry point.

## Steps / patterns
1. Write the runtime Dockerfile first (what does the product need to run?), then the dev overlay
   (what does a developer need on top?).
2. Prove the cache: change a source file → rebuild must skip dependency layers.
3. Wire the compose stack with healthchecks; `docker compose up` from a clean clone must succeed.
4. Keep image builds in sync with the pipeline images (`ops-docker`) — one definition, two uses.

## Pitfalls & anti-patterns
- `latest` tags — builds that change under your feet.
- Secrets baked into layers (build args, copied config) — they persist in history.
- Root containers writing bind-mounted files — permission wreckage on the host.
- Giant contexts (no `.dockerignore`) and dependency re-installs on every code change.

## References
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) · [Compose](https://docs.docker.com/compose/)
