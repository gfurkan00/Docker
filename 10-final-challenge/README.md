# Challenge 10 — Final challenge: API + worker + DB + cache + proxy

## Goal
Wire everything you've learned into one realistic stack: a REST API enqueues jobs into Redis, a worker processes them and writes results to Postgres, Nginx fronts the API, and the whole thing has a clean dev workflow on top of a prod-like baseline.

## Concepts revisited
- Multi-stage Dockerfiles for the Python services.
- User-defined network (auto, via Compose).
- Named volume for Postgres data.
- Healthchecks and `depends_on: condition: service_healthy`.
- `.env` configuration + `.gitignore`.
- `compose.override.yaml` for the dev experience.

## The challenge
Work from `10-final-challenge/starter/`. It ships application code only — no Dockerfiles, no compose, no init scripts. Build:

1. `api/Dockerfile` — multi-stage, slim final image.
2. `worker/Dockerfile` — multi-stage, slim final image.
3. `db/initdb.d/01_schema.sql` — creates a `jobs(id, payload, status, result)` table.
4. `compose.yaml` — five services: `api`, `worker`, `db`, `cache`, `proxy`. Postgres has a healthcheck; `api` and `worker` wait for it. Named volume for `pgdata`. Nginx forwards from host port 80 to `api:8080`.
5. `compose.override.yaml` — bind-mount source for `api` and `worker`; enable Flask reload on `api`.
6. `.env.example` + `.gitignore` for configuration.

## Success criteria
- [ ] `cp .env.example .env && docker compose up -d` brings the whole stack online.
- [ ] `curl localhost/health` returns `{"status":"ok"}` (via Nginx).
- [ ] `curl -X POST localhost/jobs -H 'Content-Type: application/json' -d '{"message":"hi"}'` returns a job id.
- [ ] Within 5 seconds, `curl localhost/jobs/<id>` returns `{"status":"done","result":"HI",...}`.
- [ ] `docker compose down && docker compose up -d` preserves jobs in the database.
- [ ] No `gcc` in the final api/worker images: `docker run --rm <image> which gcc` is empty.

## Hints
1. Reuse the multi-stage Dockerfile from Challenge 08 for both `api` and `worker`. Worker doesn't need `EXPOSE`.
2. Postgres healthcheck: same `pg_isready` recipe as Challenge 06.
3. Nginx config is already provided in `starter/proxy/nginx.conf`. Just mount it.
4. The override file can override `command:` for `api` to use `flask run --reload` (mirroring Challenge 07).
5. `.env` should hold: `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `APP_PORT`.

## Reference
- All previous challenges' READMEs.
- https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
