from flask import Flask, request
import os, psycopg, redis, json, uuid

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/jobs", methods=["POST"])
def submit():
    payload = request.get_json() or {}
    job_id = str(uuid.uuid4())
    with psycopg.connect(DSN) as conn:
        conn.execute(
            "INSERT INTO jobs (id, payload, status) VALUES (%s, %s, 'pending')",
            (job_id, json.dumps(payload)),
        )
        conn.commit()
    r.lpush("jobs", job_id)
    return {"id": job_id}, 201

@app.route("/jobs/<job_id>")
def status(job_id):
    with psycopg.connect(DSN) as conn:
        row = conn.execute(
            "SELECT id, status, result FROM jobs WHERE id = %s", (job_id,)
        ).fetchone()
    if not row:
        return {"error": "not found"}, 404
    return {"id": row[0], "status": row[1], "result": row[2]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8080")))
