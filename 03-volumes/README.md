# Challenge 03 — Volumes

## Goal
Understand the three kinds of mounts (anonymous, named, bind) and when each one is the right tool. Make Postgres data survive `docker rm`.

## Concepts introduced
- Anonymous volume vs **named volume** vs **bind mount**.
- Where data lives on the host for each kind.
- Editing source code on the host and seeing changes in the container (bind mount).
- Permission gotchas (UID/GID inside container vs on host).

## The challenge
The `starter/` Flask app stores notes in Postgres. Work from `03-volumes/starter/`. Using **either** raw `docker` commands **or** a small `compose.yaml`, set things up so that:

1. Postgres runs in its own container and Flask connects to it.
2. Postgres data lives in a **named volume**: destroying and recreating the Postgres container preserves all notes.
3. The Flask source code is **bind-mounted** from the host, so editing `app.py` and restarting Flask picks up the change without rebuilding the image.

You may use the official `postgres:16-alpine` image and write a tiny `Dockerfile` for Flask (or reuse the pattern from Challenge 01).

## Success criteria
- [ ] `POST /notes/hello` adds a note; `GET /notes` returns it.
- [ ] `docker rm -f <postgres-container>` followed by recreating it (against the same named volume) still returns the previous notes.
- [ ] Editing `app.py` on the host changes the response after a Flask restart (no rebuild needed).
- [ ] `docker volume ls` lists the named volume; `docker volume inspect <name>` shows a `Mountpoint` on the host.

## Hints
1. Named volume syntax: `-v pgdata:/var/lib/postgresql/data` (or `volumes:` in compose).
2. Bind mount syntax: `-v "$(pwd)/app.py:/app/app.py"` mounts a single file; `-v "$(pwd):/app"` mounts the whole directory.
3. Postgres connection envs needed by the starter: `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.

## Reference
- https://docs.docker.com/engine/storage/volumes/
- https://docs.docker.com/engine/storage/bind-mounts/
