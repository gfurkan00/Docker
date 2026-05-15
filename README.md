# Docker — Hands-on Learning Roadmap

A challenge-driven path from Dockerfile basics to a realistic multi-container dev stack. Every folder is a problem to solve, not a tutorial to copy.

## How to use

1. Pick the lowest-numbered challenge you haven't finished.
2. Read its `README.md`.
3. Work inside `starter/` — write the Dockerfile / `compose.yaml` yourself.
4. Verify against the **Success criteria** in the README.
5. Only when you're done (or truly stuck after the hints), peek at `solution/`.

## Challenges

| # | Folder | Focus |
|---|---|---|
| 01 | [`01-dockerfile-basics/`](./01-dockerfile-basics/) | Layer caching, `.dockerignore`, `ENTRYPOINT` vs `CMD` |
| 02 | [`02-run-deep-dive/`](./02-run-deep-dive/) | `docker run` flags, `exec`, `logs`, lifecycle |
| 03 | [`03-volumes/`](./03-volumes/) | Bind mounts vs named volumes, data persistence |
| 04 | [`04-networks/`](./04-networks/) | User-defined bridges, DNS between containers |
| 05 | [`05-compose-intro/`](./05-compose-intro/) | First `compose.yaml`: web + Redis |
| 06 | [`06-compose-realistic/`](./06-compose-realistic/) | Healthchecks, `depends_on` conditions, init scripts |
| 07 | [`07-dev-workflow/`](./07-dev-workflow/) | `compose.override.yaml`, hot reload, debugger |
| 08 | [`08-multi-stage/`](./08-multi-stage/) | Builder stage, slim runtime images |
| 09 | [`09-env-and-secrets/`](./09-env-and-secrets/) | `.env`, `env_file`, dev-grade secret handling |
| 10 | [`10-final-challenge/`](./10-final-challenge/) | API + worker + DB + cache + Nginx |

## Prerequisites

- Docker Engine 24+ and Docker Compose v2 (`docker compose version`).
- Python 3 basic knowledge (the example apps are small Flask services).
- A terminal you're comfortable in.

## See also

- [`RESOURCES.md`](./RESOURCES.md) — curated external resources.
- [`usefull commands.md`](./usefull%20commands.md) — cheat sheet of common Docker commands.
- [`example1/`](./example1/) — the original throwaway sample (kept for reference).
