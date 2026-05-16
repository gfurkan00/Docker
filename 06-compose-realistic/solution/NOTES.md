# Notes — solution

- **`depends_on` without `condition`** only orders startup, not readiness. With `condition: service_healthy` Compose waits until the dependency's healthcheck returns success.
- **`/docker-entrypoint-initdb.d/`** is run by the Postgres image only on first initialisation of the data directory. Once `pgdata` has files in it, the scripts are skipped — so editing them after the first up won't re-seed.
- **`$$POSTGRES_USER`** in the healthcheck command: a single `$` would make Compose interpolate the value before passing it to the container. `$$` escapes that so the variable is resolved by the shell inside the container, where it's actually set.
- **Restart policy** matters here because the app intentionally crashes if it can't reach Postgres on startup. `unless-stopped` brings it back automatically once the dependency recovers.
