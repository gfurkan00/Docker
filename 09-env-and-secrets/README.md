# Challenge 09 — Env and secrets (dev-grade)

## Goal
Stop hard-coding configuration in `compose.yaml`. Use a `.env` file for values that change per environment, document them in a checked-in `.env.example`, and keep real secrets out of git.

## Concepts introduced
- `ENV` (in Dockerfile) vs `environment:` (in compose) vs `env_file:` (in compose).
- The implicit `.env` file picked up by `docker compose` for variable interpolation.
- `.env.example` as documentation that ships with the repo.
- Why baking secrets into images is a one-way trip (anyone with the image has the secret).

## The challenge
Work from `09-env-and-secrets/starter/`. The `starter/compose.yaml` has a hard-coded password and tightly-coupled values. Refactor so that:

1. All tunable values (`APP_PORT`, `APP_DEBUG`, `DB_USER`, `DB_PASSWORD`) live in a `.env` file at the project root.
2. `compose.yaml` references them with `${VAR}` interpolation OR uses `env_file:` to pass them into the container.
3. A `.env.example` documents every variable with safe sample values and inline comments.
4. A `.gitignore` ensures the real `.env` is never committed.
5. The image itself (built without the runtime env) contains no secret — `docker inspect <image>` reveals no password.

## Success criteria
- [ ] Running `cp .env.example .env` and `docker compose up -d` works end-to-end.
- [ ] `curl localhost:${APP_PORT}` returns the JSON with the configured user (no password).
- [ ] `docker image inspect $(docker compose images -q web)` shows no secret in `Env` or `Labels`.
- [ ] `git check-ignore .env` prints `.env` (i.e. it would be skipped by git).
- [ ] Changing `APP_PORT` in `.env` and restarting maps the new port without touching `compose.yaml`.

## Hints
1. Compose auto-loads a `.env` file next to `compose.yaml` for `${VAR}` interpolation. Different from `env_file:`, which forwards a file into the container.
2. Use both:
   - `${APP_PORT}` interpolation for things Compose itself needs (ports).
   - `env_file: .env` for things the container needs at runtime (DB creds).
3. `.env.example` should be committed; `.env` should NOT.

## Reference
- https://docs.docker.com/compose/how-tos/environment-variables/set-environment-variables/
- https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/
