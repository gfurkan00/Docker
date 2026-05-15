# Notes — solution

- **Why a user-defined network:** on the default `bridge`, containers can reach each other only by IP, and IPs change. Docker only provides automatic DNS for **user-defined** bridge networks. Always create your own.
- **`--network` + `--name` = address book:** once a container is on a user-defined network, every other container on that network can reach it as `<container-name>`.
- **One process per container:** Redis is a separate container instead of being installed inside the Flask image. This is the Docker way: each service is independent, scalable, and replaceable.
- **Networks are first-class objects:** they outlive containers. Useful for keeping a dev stack wired together while you recreate one service.
