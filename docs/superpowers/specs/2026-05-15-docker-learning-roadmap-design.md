# Docker Learning Roadmap — Design

## Goal

Build a hands-on, folder-based roadmap that takes the learner from current level (basic `Dockerfile` + `build` + `run`, as shown in `example1/`) to **confident daily-dev usage** of Docker: containerizing apps, multi-container setups with `docker-compose`, volumes, networks, dev workflow with live reload, and clean multi-stage builds.

The roadmap is delivered as a sequence of **challenges**: each folder states a problem and ships starter files; the learner writes the `Dockerfile` / `compose.yaml`; a `solution/` folder contains a commented reference solution.

All content (READMEs, comments, file names) is written in **English**.

## Out of Scope

To keep the roadmap focused on "daily dev usage", the following are explicitly excluded:

- Private registries, pushing to Docker Hub / GHCR
- Advanced security hardening (rootless, seccomp, AppArmor, image scanning)
- Orchestration (Swarm, Kubernetes)
- CI/CD pipelines
- Production observability stacks (Prometheus, Grafana, ELK)
- Windows containers

These can be added as a follow-up roadmap once the learner is comfortable with the basics.

## Audience & Prerequisites

- Learner already knows: how to write a basic `Dockerfile`, run `docker build` and `docker run`, expose a port (see `example1/`).
- Learner has: Docker Engine and Docker Compose v2 installed locally, basic Python knowledge, terminal fluency.
- Style preference: **challenge-driven**. Each step is a problem to solve, not a tutorial to copy.

## Structure

```
Docker/
├── example1/                          # Existing — kept as-is
├── 01-dockerfile-basics/
├── 02-run-deep-dive/
├── 03-volumes/
├── 04-networks/
├── 05-compose-intro/
├── 06-compose-realistic/
├── 07-dev-workflow/
├── 08-multi-stage/
├── 09-env-and-secrets/
├── 10-final-challenge/
├── RESOURCES.md
└── README.md                          # Roadmap index + how to use
```

### Per-challenge layout

Every numbered folder follows the same shape:

```
0X-name/
├── README.md       # Problem statement, key concepts, success criteria, hints
├── starter/        # Files the learner starts from (app code, requirements, etc.)
└── solution/       # Reference solution with commented Dockerfile / compose / notes
```

### README template (each challenge)

Each challenge README contains these sections:

1. **Goal** — one paragraph: what the learner will be able to do after this.
2. **Concepts introduced** — bullet list of the new Docker concepts (e.g. "named volumes", "bridge networks", "HEALTHCHECK").
3. **The challenge** — concrete task, including starter file layout.
4. **Success criteria** — verifiable checks the learner must satisfy (commands to run, expected output, e.g. `curl localhost:8080 returns "Hello"` or `data persists after docker compose down && up`).
5. **Hints** — 2–4 progressive hints (collapsed-style, hardest concept last).
6. **Reference** — link to the official Docker docs page(s) for the concepts covered.

## Tech Stack of Example Apps

- **Primary language:** Python 3.13 + Flask (continuity with existing `example1/`).
- **Databases:** PostgreSQL (relational), Redis (cache/queue).
- **Reverse proxy (final challenge only):** Nginx.
- No Node/Go to avoid splitting focus across runtimes.

## Challenge Breakdown

### 01 — Dockerfile basics
**Concepts:** layer caching, `.dockerignore`, `COPY` vs `ADD`, ordering instructions for cache efficiency, `WORKDIR`, `RUN` vs `CMD` vs `ENTRYPOINT`.
**Challenge:** given a Flask app with a `requirements.txt`, write a `Dockerfile` that:
- Rebuilds quickly when only `app.py` changes (i.e. dependencies aren't reinstalled).
- Excludes `__pycache__/`, `.git/`, local virtualenvs from the image.
- Uses `ENTRYPOINT` + `CMD` correctly so the container can accept extra args.
**Success criteria:** second build after editing `app.py` finishes in < 5s; image size under 150 MB; `docker run image --help` prints app's help.

### 02 — Run deep-dive
**Concepts:** `-p` vs `-P`, `--rm`, `-d`, `-it`, `docker exec`, `docker logs -f`, `--name`, `--restart`.
**Challenge:** start the image from challenge 01 in three different modes (foreground for debugging, detached for "production-like", interactive shell to poke inside). Inspect logs and exec into a running container to read a file.
**Success criteria:** learner can produce the 3 commands without looking; can answer "what's the difference between `stop` and `kill`?".

### 03 — Volumes
**Concepts:** anonymous vs named vs bind mounts, where data lives, ownership/permission gotchas.
**Challenge:** run Postgres with a named volume so data survives `docker rm`; mount the Flask app source as a bind mount to edit code from the host.
**Success criteria:** create a row in Postgres, destroy and recreate the container, row still there; edit `app.py` on the host and see the change reflected (with `--reload` server) without rebuilding.

### 04 — Networks
**Concepts:** default bridge vs user-defined bridge, DNS resolution between containers, why the default bridge is a trap.
**Challenge:** run two containers (Flask + Redis) on a user-defined network; Flask must reach Redis by name (e.g. `redis:6379`), not by IP.
**Success criteria:** `docker exec flask ping redis` works; removing the network connection breaks the app.

### 05 — Compose intro
**Concepts:** `docker-compose.yaml` v2 syntax, `services`, `build` vs `image`, `ports`, `volumes`, `depends_on`, project name.
**Challenge:** convert challenge 04 (Flask + Redis) into a single `compose.yaml`. One `up`, one `down`.
**Success criteria:** `docker compose up` brings everything online; `docker compose down -v` cleans up including volumes.

### 06 — Compose realistic
**Concepts:** `healthcheck`, `depends_on: condition: service_healthy`, multiple services, init scripts (`./initdb.d`), restart policies.
**Challenge:** Flask + Postgres + Redis. Flask must wait for Postgres to be **actually ready** (not just started) before running migrations.
**Success criteria:** stop Postgres, restart the stack — Flask retries instead of crashing; Postgres comes up with a pre-seeded schema.

### 07 — Dev workflow
**Concepts:** `compose.override.yaml`, bind-mounting source code in dev, attaching a debugger (`debugpy`), reading logs across services, hot reload.
**Challenge:** produce two compose files — `compose.yaml` (prod-like, no source mount) and `compose.override.yaml` (dev: bind mount, reload, debugger port exposed). Default `docker compose up` should give the dev experience.
**Success criteria:** editing source on host triggers Flask reload inside the container; can attach VS Code / `debugpy` to a breakpoint.

### 08 — Multi-stage builds
**Concepts:** `FROM ... AS builder`, `COPY --from`, why a build stage is separate from a runtime stage, picking slim/distroless base images.
**Challenge:** take a Flask app whose `requirements.txt` includes a package needing build tools (e.g. `psycopg2` from source or `cryptography`). Final image must NOT contain gcc/build tools.
**Success criteria:** final image < 100 MB; `docker run image which gcc` returns nothing.

### 09 — Env and secrets (dev-grade)
**Concepts:** `ENV` in Dockerfile vs `environment:` in compose vs `env_file:`, `.env` files, why secrets in images are a mistake, dev-grade approach with `.env` ignored by git.
**Challenge:** parameterise the stack from challenge 06 with a `.env` file (DB password, app port, debug flag). Provide a `.env.example` template, ensure real `.env` is gitignored.
**Success criteria:** stack works with a fresh `.env` copied from `.env.example` and edited; no secret appears in `docker inspect` output of the image itself.

### 10 — Final challenge
**Concepts:** everything above, integrated.
**Challenge:** build a small "microservice" stack:
- `api` — Flask REST API
- `worker` — background Python worker consuming a Redis queue
- `db` — Postgres
- `cache` — Redis (shared between api and worker)
- `proxy` — Nginx reverse proxy in front of `api`

Requirements:
- Multi-stage Dockerfiles for api and worker.
- Named volume for Postgres data.
- User-defined network.
- Healthchecks for db and cache; `api` and `worker` wait for them.
- `.env` for configuration.
- `compose.override.yaml` for the dev workflow.

**Success criteria:** `curl localhost/health` returns OK; posting a job via the API gets processed by the worker; `docker compose down && up` preserves the database state.

## Top-level files

### `README.md` (project root, replaces current 1-line README)
- One-paragraph intro to the roadmap.
- Table listing all 10 challenges with one-line descriptions.
- "How to use" section: clone, `cd 01-...`, read README, attempt in place (or in a side branch), check `solution/` only after attempting.
- Prerequisites + how to verify Docker install.
- Pointer to `RESOURCES.md` for external material.
- Pointer to existing `usefull commands.md` as the cheat sheet.

### `RESOURCES.md`
Curated external resources, grouped:
- **Official:** Docker docs landing pages for build, run, compose, networking, volumes.
- **Free interactive:** Play with Docker, Docker's own tutorials.
- **Books:** 1–2 recommendations max (e.g. "Docker Deep Dive" by Nigel Poulton).
- **Videos:** 1–2 quality channels (e.g. TechWorld with Nana for visual overview).
- **Cheat sheets:** link to the existing `usefull commands.md`.

Quality over quantity — five great resources beat fifty mediocre ones.

## Implementation Notes

- All starter apps reuse a similar small Flask scaffold to keep cognitive load on Docker, not on app code.
- Each `solution/Dockerfile` and `solution/compose.yaml` carry inline comments explaining the **why**, not the what.
- Solutions are runnable as-is (`docker compose up` from inside `solution/`).
- Existing `example1/` is left untouched.
- Existing `usefull commands.md` is left untouched and linked from the new README.

## Done Definition

The roadmap is "done" when:
1. All 10 folders exist with `README.md`, `starter/`, `solution/`.
2. Every `solution/` can be built and run end-to-end (manual smoke test).
3. Root `README.md` and `RESOURCES.md` are in place.
4. The whole tree is committed.
