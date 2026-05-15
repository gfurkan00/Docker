from flask import Flask
import os, redis

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("hits")
    return f"<h1>Hit #{count}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
