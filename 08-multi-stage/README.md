# Challenge 08 — Multi-stage builds

## Goal
Build a final image that contains your app and its runtime deps, but **none** of the C compilers or build tools used during installation.

## Concepts introduced
- `FROM ... AS builder` — naming a build stage.
- `COPY --from=builder` — pulling artefacts from a previous stage.
- Wheels (`pip wheel`) as the transfer format between stages.
- Why "slim" or "distroless" runtime bases shrink images and attack surface.

## The challenge
Work from `08-multi-stage/starter/`. The app uses `cryptography`, which may compile native code if no prebuilt wheel matches the platform. A naïve single-stage Dockerfile with `python:3.13-slim` either fails to build (no `gcc`) or works after you `apt-get install build-essential` — leaving ~250 MB of build tools in the final image.

Write a multi-stage Dockerfile that:

1. Uses a build stage with the toolchain to compile / install dependencies.
2. Uses a clean runtime stage (`python:3.13-slim`) that does NOT install any build tools.
3. Copies installed packages from the build stage into the runtime stage.
4. Produces a final image whose `which gcc` returns nothing and whose size is under 100 MB.

## Success criteria
- [ ] `docker build -t ch08 .` succeeds without `apt-get install build-essential` in the final stage.
- [ ] `docker run --rm -p 8080:8080 ch08` serves a token at `/`.
- [ ] `docker run --rm ch08 sh -c "which gcc; which cc; which make"` prints nothing.
- [ ] `docker image inspect ch08 --format '{{.Size}}'` returns a value under 100 MB (100_000_000 bytes).

## Hints
1. Build stage: install `build-essential` and `libffi-dev`, then `pip install --prefix=/install -r requirements.txt`.
2. Runtime stage: `COPY --from=builder /install /usr/local` to drop the packages into the standard Python path.
3. No need to copy `/usr/bin/gcc` etc. — they stay in the builder, which is discarded.

## Reference
- https://docs.docker.com/build/building/multi-stage/
- https://pythonspeed.com/articles/multi-stage-docker-python/
