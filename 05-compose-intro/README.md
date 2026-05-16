# Challenge 05 — Compose intro

## Goal
Replace a manual chain of `docker network create` + `docker run` + `docker run` with a single `compose.yaml`. One file, one `up`, one `down`.

## Concepts introduced
- `compose.yaml` v2 structure: `services`, `build`, `image`, `ports`, `volumes`, `depends_on`.
- Default network: Compose creates one automatically and puts every service on it.
- Service names as DNS hostnames.
- `docker compose up`, `down`, `ps`, `logs`, `build`.

## The challenge
Work from `05-compose-intro/starter/`. Take the working Flask+Redis setup from Challenge 04 and convert it into a single `compose.yaml`. Requirements:

1. Two services: `web` (built from the local `Dockerfile`) and `cache` (`redis:7-alpine`).
2. `web` reaches Redis at host `cache` (use the service name).
3. Host port 8080 is mapped to container port 8080 on `web`.
4. `docker compose up` brings everything online; `docker compose down` cleans up.

## Success criteria
- [ ] `docker compose up -d` (from inside `solution/`) succeeds.
- [ ] `curl localhost:8080` works and the counter increments.
- [ ] `docker compose ps` shows both services as running.
- [ ] `docker compose down` removes both containers and the auto-created network.

## Hints
1. The service name becomes the DNS hostname inside the auto-created network. So if you name the Redis service `cache`, set `REDIS_HOST=cache`.
2. `build: .` tells Compose to build the image from the Dockerfile in the current directory.
3. Compose v2 doesn't need a `version:` key at the top.

## Reference
- https://docs.docker.com/compose/intro/compose-application-model/
- https://docs.docker.com/reference/compose-file/services/
