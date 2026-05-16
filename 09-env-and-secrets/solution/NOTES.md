# Notes — solution

- **Three layers of env variables in compose:**
  1. The `.env` file next to `compose.yaml` — Compose reads it ONLY for `${VAR}` interpolation in the YAML itself.
  2. `environment:` block — sets vars in the container; values can come from the host or `${VAR}`.
  3. `env_file:` — Compose reads each line and forwards it to the container at runtime, no interpolation in the YAML.
- **Never put secrets in `ENV` inside a Dockerfile.** They become part of the image's history; anyone who pulls the image gets them.
- **`.env` is dev-grade.** For prod, use a secret manager (Vault, AWS Secrets Manager, K8s Secrets) and inject at runtime. Out of scope for this roadmap but worth knowing.
- **Pattern for new repos:** commit `.env.example`, gitignore `.env`, document the variables in the README's "Getting started" section.
