# Challenge 02 — docker run deep-dive

## Goal
Become fluent with the most common `docker run` flags and container lifecycle commands. No more copy-paste from Stack Overflow.

## Concepts introduced
- `-p` (publish) vs `-P` (publish-all-random).
- `-d` (detached) vs foreground vs `-it` (interactive + TTY).
- `--rm`, `--name`, `--restart`.
- `docker exec`, `docker logs -f`, `docker stop` vs `docker kill`.

## The challenge
You have a working image (`starter/` reuses Challenge 01's solution). Work from `02-run-deep-dive/starter/` (that's the build context). Produce a `commands.md` (in your own scratch directory) with the exact `docker` commands to:

1. Build the image as `ch02`.
2. Run it in the **foreground** with port 8080 mapped, name `ch02-fg`, and auto-removed on exit.
3. Run it in the **background** with port 8081 mapped, name `ch02-bg`, restart policy `unless-stopped`.
4. Stream the logs of `ch02-bg` live.
5. Open an interactive `sh` inside the running `ch02-bg` and `cat /app/app.py` from inside.
6. Stop `ch02-bg` gracefully, then remove it.
7. Show the difference in observable behaviour between `docker stop` and `docker kill` for this image (one sentence each).

## Success criteria
- [ ] `commands.md` is filled in with runnable commands; copy-pasting each in order works end to end.
- [ ] `curl localhost:8080` works during step 2.
- [ ] `curl localhost:8081` works during step 3.
- [ ] `docker logs -f ch02-bg` shows new lines when you `curl` it.
- [ ] You can explain in your own words when you'd use `-d` vs foreground.

## Hints
1. `--rm` removes the container on exit but is incompatible with `--restart`.
2. `docker exec -it <name> sh` opens an interactive shell inside a running container.
3. `docker stop` sends SIGTERM (graceful, 10s grace period). `docker kill` sends SIGKILL (immediate, no cleanup).

## Reference
- https://docs.docker.com/reference/cli/docker/container/run/
- https://docs.docker.com/reference/cli/docker/container/exec/
- https://docs.docker.com/engine/containers/start-containers-automatically/
