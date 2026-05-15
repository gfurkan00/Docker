# Challenge 07 — Dev workflow

## Goal
Run the same app in two flavours from the same `compose.yaml`: a clean production-like build for verification, and a dev experience with hot reload + a debugger attached — without touching the prod file.

## Concepts introduced
- `compose.override.yaml` (loaded automatically by `docker compose up`).
- Bind-mounting source into the container for live editing.
- Flask `debug=True` for auto-reload (and `debugpy` exposed on a port for VS Code).
- Reading logs of a single service.

## The challenge
Work from `07-dev-workflow/starter/`. You start with a working `compose.yaml` that runs the app in prod-like mode. Add a `compose.override.yaml` (do NOT modify the prod file) so that the default `docker compose up` provides:

1. Bind mount of the host source into `/app` so edits show up live.
2. Hot reload (Flask debug mode, or `--reload`).
3. Debugger port `5678` exposed for VS Code / `debugpy` attach.
4. `STAGE=dev` overrides the prod value.

You must keep the original `compose.yaml` usable as-is for "prod" verification:
- `docker compose -f compose.yaml up` (override skipped) → prod behaviour.
- `docker compose up` (default loads override) → dev behaviour.

## Success criteria
- [ ] `docker compose -f compose.yaml up -d` runs prod mode — editing `app.py` does NOT update the response without a rebuild.
- [ ] `docker compose up -d` runs dev mode — the bind-mounted source is live in `/app`, and `STAGE=dev` is active.
- [ ] `docker compose up -d` exposes port 5678 to the host for debugger attach.
- [ ] `curl localhost:8080` returns "Hello from dev" in dev mode and "Hello from prod" in prod mode.

## Hints
1. `compose.override.yaml` is merged on top of `compose.yaml` automatically. Override keys win; arrays may be concatenated or replaced depending on the key (consult the docs for `command:` vs `volumes:`).
2. Override the `command:` in the override file. Use debugpy to expose a debugger port and flask run:
   `python -m debugpy --listen 0.0.0.0:5678 -m flask --app app run --host 0.0.0.0 --port 8080 --no-reload`.
   Note: `--no-reload` is required when wrapping with `debugpy` — the Werkzeug reloader and debugpy both try to bind port 5678, causing a conflict. Use `docker compose restart web` to pick up source changes.
3. The override file does **not** need its own `image:` or `build:` — it inherits from the base.

## Reference
- https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/
- https://flask.palletsprojects.com/en/stable/cli/#run-the-development-server
