import os, time, json, psycopg, redis

DSN = (
    f"host={os.environ['DB_HOST']} dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} password={os.environ['DB_PASSWORD']}"
)
r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379, decode_responses=True)

def process(payload: dict) -> str:
    # Toy processing: uppercase a 'message' if present.
    return (payload.get("message") or "").upper()

def main():
    print("[worker] listening on jobs queue", flush=True)
    while True:
        item = r.brpop("jobs", timeout=5)
        if not item:
            continue
        _, job_id = item
        with psycopg.connect(DSN) as conn:
            row = conn.execute("SELECT payload FROM jobs WHERE id = %s", (job_id,)).fetchone()
            if not row:
                continue
            raw = row[0]
            payload = raw if isinstance(raw, dict) else json.loads(raw)
            result = process(payload)
            conn.execute(
                "UPDATE jobs SET status='done', result=%s WHERE id=%s",
                (result, job_id),
            )
            conn.commit()
        print(f"[worker] processed {job_id} → {result}", flush=True)

if __name__ == "__main__":
    main()
