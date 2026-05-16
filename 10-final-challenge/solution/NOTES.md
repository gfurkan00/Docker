# Notes — solution

- **Service responsibilities are crisp:** `api` accepts HTTP and enqueues. `worker` only reads the queue and writes results. They share `db` and `cache` but never call each other directly.
- **Nginx is dumb on purpose.** Its only job is to forward port 80 → `api:8080`. Adds TLS termination, rate limiting, or load balancing later if you want — but starting simple makes failures obvious.
- **`depends_on: service_healthy` on Postgres** stops the api/worker from racing against an uninitialised DB. Without it you'd see flaky startup failures on cold boots.
- **Why multi-stage for both:** `psycopg[binary]` ships wheels, but `libpq` headers (`libpq-dev`) are still needed for some platforms — keeping them out of the runtime image saves space and surface.
- **Dev workflow:** the override mounts source for both services so you can iterate without rebuilds. The worker doesn't auto-reload — just `docker compose restart worker` after edits.
- **Production deltas (out of scope):** real secret manager instead of `.env`; image tags pinned by digest; resource limits; centralised logs; TLS at the proxy; replicated workers.
