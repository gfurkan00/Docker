# Notes — solution

- **Compose auto-merges** `compose.yaml` + `compose.override.yaml` when you run `docker compose up`. To opt out, pass `-f compose.yaml` explicitly.
- **Why bind-mount the whole directory** instead of just `app.py`: any new files you create on the host (e.g. a `models.py`) are picked up too.
- **debugpy + `--no-reload`:** The Werkzeug reloader spawns a child process that also tries to bind debugpy on port 5678, causing "Address already in use". The solution uses `--no-reload` instead; pick up source changes with `docker compose restart web` (fast, since the bind-mount means no rebuild is needed).
- **Hot reload without debugpy:** If you don't need the debugger, replace the `command:` with `flask --app app run --host 0.0.0.0 --port 8080 --reload` and drop the `5678` port mapping.
- **Attaching VS Code:** add a `.vscode/launch.json` with `"type": "debugpy", "request": "attach", "connect": {"host": "localhost", "port": 5678}` — but that's outside Docker's scope.
- **Two-file pattern scales:** a `compose.test.yaml` selected with `-f compose.yaml -f compose.test.yaml` can swap in test databases, etc.
