# Notes — solution

- **`--rm` + `--restart`:** mutually exclusive. `--rm` means "delete on exit"; `--restart` means "bring it back if it exits". Docker rejects both together.
- **`-d` vs foreground:** detached is for "set and forget" runs (services). Foreground is for development and debugging — you see stdout immediately and Ctrl-C kills it.
- **`-it`:** `-i` keeps STDIN open, `-t` allocates a TTY. Both are needed for an interactive shell. Without `-t`, prompts don't render. Without `-i`, you can't type.
- **`docker logs -f`** is your default debugging tool. Add `--tail 100` to start from the recent past.
