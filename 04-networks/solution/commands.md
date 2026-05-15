# Solution — challenge 04 commands

````bash
# Build the Flask image
docker build -t ch04-web .

# Create a user-defined bridge network
docker network create lab-net

# Run Redis on the network (no port published — only Flask needs it)
docker run -d --name redis --network lab-net redis:7-alpine

# Run Flask on the same network; REDIS_HOST defaults to "redis" in the app
docker run -d --name web --network lab-net -p 8080:8080 ch04-web

# Test
curl localhost:8080   # Hit #1
curl localhost:8080   # Hit #2

# Prove DNS works
docker exec web ping -c1 redis

# Break the dependency
docker network disconnect lab-net redis
curl -i localhost:8080   # 500 (Redis unreachable)

# Cleanup
docker rm -f web redis
docker network rm lab-net
````
