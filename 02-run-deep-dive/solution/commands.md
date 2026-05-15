# Solution — challenge 02 commands

````bash
# 1. Build
docker build -t ch02 .

# 2. Foreground, auto-removed
docker run --rm --name ch02-fg -p 8080:8080 ch02
# (Ctrl-C to stop; the container is removed automatically.)

# 3. Background, restart policy
docker run -d --name ch02-bg -p 8081:8081 -e PORT=8081 \
  --restart unless-stopped ch02

# 4. Follow logs
docker logs -f ch02-bg

# 5. Interactive shell inside
docker exec -it ch02-bg sh
# inside: cat /app/app.py ; exit

# 6. Graceful stop + remove
docker stop ch02-bg
docker rm ch02-bg
````

## stop vs kill (one-liners)

- `docker stop`: sends SIGTERM, gives the process 10s to clean up, then SIGKILL. Flask logs a shutdown line.
- `docker kill`: sends SIGKILL immediately. No shutdown line, no graceful cleanup.
