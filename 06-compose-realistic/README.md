# Challenge 06 — Compose realistic

## Goal
Stand up a realistic three-service stack — web + Postgres + Redis — where the web service waits for the database to be **actually ready** (not just started) before running.

## Concepts introduced
- `healthcheck` per service.
- `depends_on: condition: service_healthy`.
- Init scripts mounted into `/docker-entrypoint-initdb.d/` for Postgres bootstrap.
- `restart` policies in a compose context.

## The challenge
Work from `06-compose-realistic/starter/`. You have a Flask app that reads `items` from Postgres, caches them in Redis for 30s, and exposes `GET /items`. There's also a SQL bootstrap file in `starter/initdb.d/`.

Write a `compose.yaml` so that:

1. Three services: `web` (built from the local Dockerfile), `db` (`postgres:16-alpine`), `cache` (`redis:7-alpine`).
2. `db` has a healthcheck using `pg_isready`.
3. `web` uses `depends_on` with `condition: service_healthy` for `db` — it should **not** start before Postgres accepts connections.
4. `db` mounts the SQL files in `starter/initdb.d/` so the `items` table is created and seeded on first startup.
5. Postgres data persists across `docker compose down && up` via a named volume.
6. `restart: unless-stopped` on `web` so it survives intermittent failures.

## Success criteria
- [ ] `docker compose up -d` brings the stack online; `web` only becomes healthy after `db` is.
- [ ] `curl localhost:8080/items` returns `[{"id":1,"name":"alpha"},...]`.
- [ ] First call returns header `X-Cache: MISS`; subsequent calls within 30s return `X-Cache: HIT`.
- [ ] `docker compose down && docker compose up -d` preserves the items (volume survives).
- [ ] Stopping the DB while running the app produces a clean error in `web`'s logs without crashing it (restart policy keeps it alive).

## Hints
1. `healthcheck` for Postgres:
   ```yaml
   healthcheck:
     test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
     interval: 2s
     timeout: 2s
     retries: 20
   ```
   The `$$` is required so Compose doesn't try to interpolate the variable itself.
2. To mount the init scripts: `./initdb.d:/docker-entrypoint-initdb.d:ro`.
3. The `wait_for_db()` in the app gives a second safety net — `condition: service_healthy` is the primary one.

## Reference
- https://docs.docker.com/reference/compose-file/services/#healthcheck
- https://docs.docker.com/reference/compose-file/services/#depends_on
- https://hub.docker.com/_/postgres (search for "initialization scripts")
