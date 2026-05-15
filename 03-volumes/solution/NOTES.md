# Notes — solution

- **Why a named volume for Postgres:** the Postgres image writes data to `/var/lib/postgresql/data`. Without a volume, that directory lives in the container's writable layer and dies with `docker rm`. A named volume is managed by Docker (so you don't pick the host path), and survives container deletion.
- **Why a bind mount for the source:** during learning/dev you want edits on the host to show up instantly in the container. The trade-off: the path is host-specific and the file system perms are shared with the host.
- **Anonymous volumes** (`-v /var/lib/postgresql/data` with no name) work for persistence within a single `up`/`down` cycle but produce volumes with random names that pile up — avoid them.
- **Demo of persistence:**
  ```bash
  docker compose up -d
  curl -X POST localhost:8080/notes/first
  docker compose rm -sf db          # destroy postgres container
  docker compose up -d db           # recreate it
  curl localhost:8080/notes         # 'first' is still there
  ```
