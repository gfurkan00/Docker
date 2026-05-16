# Notes — solution

- **Compose creates a default network** named `<project>_default` and joins every service to it. No need to declare a `networks:` block for simple setups.
- **Service name = DNS name.** Inside the network, `cache` resolves to the Redis container's IP. That's why the app sets `REDIS_HOST=cache`.
- **`depends_on` only orders startup**, not readiness. Redis is fast so it doesn't matter here, but for Postgres we'll need `healthcheck` + `condition: service_healthy` (Challenge 06).
- **`docker compose down` removes containers AND the network.** Add `-v` to also remove named volumes (dangerous: deletes data).
