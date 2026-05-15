from flask import Flask, jsonify
import os, time, psycopg, redis
from psycopg.rows import dict_row

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "cache"), port=6379, decode_responses=True)

def wait_for_db(max_tries=30):
    for i in range(max_tries):
        try:
            with psycopg.connect(DSN) as conn:
                conn.execute("SELECT 1")
                return
        except Exception as e:
            print(f"[wait_for_db] attempt {i+1}: {e}", flush=True)
            time.sleep(1)
    raise RuntimeError("Database not reachable")

@app.route("/items")
def items():
    cached = r.get("items")
    if cached:
        return cached, 200, {"Content-Type": "application/json", "X-Cache": "HIT"}
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        rows = conn.execute("SELECT id, name FROM items ORDER BY id").fetchall()
    payload = jsonify(rows).get_data(as_text=True)
    r.setex("items", 30, payload)
    return payload, 200, {"Content-Type": "application/json", "X-Cache": "MISS"}

if __name__ == "__main__":
    wait_for_db()
    app.run(host="0.0.0.0", port=8080)
