# Challenge 04 — Networks

## Goal
Get two containers talking by DNS name on a user-defined bridge network. Learn why the default bridge is a trap.

## Concepts introduced
- Default bridge network vs user-defined bridge.
- DNS resolution between containers (only on user-defined networks).
- Inspecting networks with `docker network inspect`.

## The challenge
Work from `04-networks/starter/`. Run two containers — the Flask app and a Redis instance — so that:

1. Both are on the **same user-defined bridge network**.
2. Flask reaches Redis by the **name** `redis`, not by IP address.
3. Stopping/disconnecting Redis breaks the app (proving the dependency is real).

Use raw `docker network` and `docker run` commands. Save them in `solution/commands.md`.

## Success criteria
- [ ] `docker network ls` shows your custom network.
- [ ] `curl localhost:8080` increments a counter (hit #1, #2, ...).
- [ ] `docker run --rm --network <net> redis:7-alpine ping -c1 web` resolves and replies (uses the Redis image, which ships `ping` — the Flask image doesn't).
- [ ] `docker network disconnect <net> <redis>` causes the next request to error.

## Hints
1. Create the network first: `docker network create lab-net`.
2. Then run each container with `--network lab-net --name <name>`.
3. The official Redis image is just `redis:7-alpine` — no extra config needed.

## Reference
- https://docs.docker.com/engine/network/drivers/bridge/
- https://docs.docker.com/engine/network/#dns-services
