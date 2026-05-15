# Docker — Useful Commands

Quick reference for the most common Docker CLI commands.

---

## Build

| Command | Description |
|---------|-------------|
| `docker build .` | Build an image from the Dockerfile in the current directory. |
| `docker build -t name:tag .` | Build and tag the image as `name:tag`. |
| `docker build -f path/Dockerfile .` | Build using a Dockerfile at a custom path. |
| `docker build --no-cache .` | Build without using any cached layers (fresh build). |
| `docker build --build-arg KEY=val .` | Pass a build-time variable to the Dockerfile `ARG` instruction. |
| `docker build --target stage .` | Stop the build at the named multi-stage target. |
| `docker build --platform linux/amd64 .` | Build for a specific OS/architecture (useful for cross-compilation). |

---

## Run

| Command | Description |
|---------|-------------|
| `docker run name` | Create and start a container from image `name` (foreground). |
| `docker run -d name` | Run the container in detached (background) mode. |
| `docker run -p 8080:80 name` | Map host port 8080 to container port 80. |
| `docker run -e KEY=val name` | Set an environment variable inside the container. |
| `docker run --env-file .env name` | Load environment variables from a `.env` file. |
| `docker run -v /host:/container name` | Bind-mount a host directory into the container. |
| `docker run -v vol_name:/container name` | Mount a named Docker volume into the container. |
| `docker run --name my_container name` | Assign a human-readable name to the container. |
| `docker run --rm name` | Automatically remove the container when it exits. |
| `docker run -it name bash` | Start an interactive terminal session inside the container. |
| `docker run --network net name` | Connect the container to a specific Docker network. |
| `docker run --restart always name` | Always restart the container if it stops (including on daemon start). |
| `docker run --restart unless-stopped name` | Restart unless the container was explicitly stopped. |
| `docker run -m 512m name` | Limit the container's memory usage to 512 MB. |
| `docker run --cpus 1.5 name` | Limit the container to 1.5 CPU cores. |
| `docker run --read-only name` | Mount the container's root filesystem as read-only. |

---

## Container — Management

| Command | Description |
|---------|-------------|
| `docker ps` | List all running containers. |
| `docker ps -a` | List all containers, including stopped ones. |
| `docker ps -q` | List only container IDs of running containers. |
| `docker stop <id>` | Gracefully stop a running container (sends SIGTERM). |
| `docker kill <id>` | Immediately terminate a container (sends SIGKILL). |
| `docker start <id>` | Start a previously stopped container. |
| `docker restart <id>` | Stop then start a container. |
| `docker rm <id>` | Remove a stopped container. |
| `docker rm -f <id>` | Forcefully remove a container, even if it is running. |
| `docker rm $(docker ps -aq)` | Remove all stopped containers at once. |
| `docker rename <old> <new>` | Rename an existing container. |
| `docker pause <id>` | Suspend all processes in a container (freezes it). |
| `docker unpause <id>` | Resume a paused container. |

---

## Container — Inspection & Logs

| Command | Description |
|---------|-------------|
| `docker logs <id>` | Print the logs (stdout/stderr) of a container. |
| `docker logs -f <id>` | Follow (stream) the container logs in real time. |
| `docker logs --tail 100 <id>` | Show only the last 100 lines of logs. |
| `docker logs --since 1h <id>` | Show logs from the past hour. |
| `docker inspect <id>` | Return detailed low-level JSON info about a container or image. |
| `docker stats` | Live resource usage (CPU, memory, network, I/O) for all running containers. |
| `docker stats <id>` | Live resource usage for a single container. |
| `docker top <id>` | Display running processes inside a container (like `ps`). |
| `docker diff <id>` | Show filesystem changes made inside the container since it started. |
| `docker port <id>` | List all port mappings for a container. |

---

## Container — Interaction

| Command | Description |
|---------|-------------|
| `docker exec -it <id> sh` | Open an interactive shell (`sh`) in a running container. |
| `docker exec -it <id> bash` | Open an interactive Bash shell in a running container. |
| `docker exec <id> <cmd>` | Run a one-off command in a running container without a TTY. |
| `docker cp /host/file <id>:/container/path` | Copy a file from the host into a container. |
| `docker cp <id>:/container/path /host/dest` | Copy a file out of a container to the host. |
| `docker attach <id>` | Attach your terminal to a running container's stdin/stdout/stderr. |
| `docker wait <id>` | Block until a container stops, then print its exit code. |

---

## Images

| Command | Description |
|---------|-------------|
| `docker images` | List all locally available images. |
| `docker pull name:tag` | Download an image from a registry (defaults to Docker Hub). |
| `docker push name:tag` | Upload a tagged image to a registry. |
| `docker rmi <id>` | Remove a local image (must not be in use by any container). |
| `docker tag src dst` | Create an alias (`dst`) for an existing image (`src`). |
| `docker save -o file.tar name` | Export an image to a tar archive. |
| `docker load -i file.tar` | Import an image from a tar archive. |
| `docker history name` | Show the layer history and sizes of an image. |
| `docker image prune` | Remove all dangling (untagged) images. |
| `docker image prune -a` | Remove all unused images (not referenced by any container). |

---

## Volumes

| Command | Description |
|---------|-------------|
| `docker volume ls` | List all Docker-managed volumes. |
| `docker volume create name` | Create a named volume. |
| `docker volume inspect name` | Show detailed information about a volume. |
| `docker volume rm name` | Delete a volume (must not be in use). |
| `docker volume prune` | Remove all volumes not referenced by any container. |

---

## Networks

| Command | Description |
|---------|-------------|
| `docker network ls` | List all Docker networks. |
| `docker network create name` | Create a new user-defined bridge network. |
| `docker network inspect name` | Show detailed information about a network. |
| `docker network connect net container` | Connect a running container to a network. |
| `docker network disconnect net container` | Disconnect a container from a network. |
| `docker network rm name` | Delete a network (must have no connected containers). |
| `docker network prune` | Remove all networks not used by any container. |

---

## Compose

| Command | Description |
|---------|-------------|
| `docker compose up` | Build (if needed) and start all services defined in `compose.yaml`. |
| `docker compose up -d` | Start all services in detached mode. |
| `docker compose up --build` | Force a rebuild of images before starting services. |
| `docker compose down` | Stop and remove containers and the default network. |
| `docker compose down -v` | Stop and remove containers, networks, **and** named volumes. |
| `docker compose ps` | List containers managed by the current Compose project. |
| `docker compose logs -f` | Stream logs from all services. |
| `docker compose logs -f <service>` | Stream logs from a single service. |
| `docker compose exec <service> sh` | Open a shell in a running Compose service container. |
| `docker compose build` | Build (or rebuild) service images without starting them. |
| `docker compose pull` | Pull the latest images for all services. |
| `docker compose restart <service>` | Restart a single service without recreating it. |
| `docker compose config` | Validate and print the resolved Compose configuration. |

---

## System Cleanup

| Command | Description |
|---------|-------------|
| `docker system df` | Show disk usage by images, containers, volumes, and build cache. |
| `docker system prune` | Remove stopped containers, dangling images, unused networks, and build cache. |
| `docker system prune -a` | Same as above, but also removes all unused images (not just dangling). |
| `docker system prune -af --volumes` | ⚠ Remove **everything** unused: containers, images, networks, volumes, and build cache. |
