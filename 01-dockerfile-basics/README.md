# Challenge 01 — Dockerfile basics

## Goal
Build a small Flask image that rebuilds quickly when only source code changes, ignores junk files from the build context, and accepts a CLI flag.

## Concepts introduced
- Layer caching and how `COPY` ordering affects it.
- `.dockerignore` and why it matters (build speed, image hygiene, secrets).
- `WORKDIR`, `COPY` vs `ADD`.
- `ENTRYPOINT` + `CMD` so the container can accept extra args.

## The challenge
Inside `starter/` you have a Flask app and a `requirements.txt`. Write a `Dockerfile` and a `.dockerignore` **inside `starter/`** (run `docker build` from there) so that:

1. The first `docker build` succeeds and the resulting image runs the app on port 8080.
2. After the first build, editing only `app.py` and rebuilding does **not** reinstall pip dependencies.
3. Running the container with the extra arg `--help` prints usage instead of starting the server.
4. The image does not contain `__pycache__/`, `.git/`, local virtualenvs (`.venv/`, `venv/`), or any `.dockerignore.example` artifact.

## Success criteria
- [ ] `docker build -t ch01 .` succeeds.
- [ ] `docker run --rm -p 8080:8080 ch01` serves `http://localhost:8080` and returns the greeting.
- [ ] `docker run --rm ch01 --help` prints the usage. Verify the exit code with `echo $?` immediately after — it must be `0`.
- [ ] After touching `app.py`, `docker build -t ch01 .` finishes in under 5 seconds (use the cache).
- [ ] `docker run --rm ch01 ls -la /app` shows no `__pycache__` or `.git`.
- [ ] `docker image inspect ch01 --format '{{.Size}}'` returns a size below 150 MB.

## Hints
1. Order matters: which `COPY` should come first, dependencies or source code?
2. Skim the [ENTRYPOINT vs CMD interaction table](https://docs.docker.com/reference/dockerfile/#understand-how-cmd-and-entrypoint-interact) in the Dockerfile reference. Which combination lets every `docker run` argument be forwarded to the entrypoint?
3. `.dockerignore` works exactly like `.gitignore` — list every directory you don't want in the build context.

## Reference
- https://docs.docker.com/build/cache/
- https://docs.docker.com/build/concepts/context/#dockerignore-files
- https://docs.docker.com/reference/dockerfile/#entrypoint
