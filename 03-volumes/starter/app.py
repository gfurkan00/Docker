from flask import Flask, jsonify
import os, psycopg
from psycopg.rows import dict_row

app = Flask(__name__)

DSN = (
    f"host={os.environ['DB_HOST']} "
    f"port={os.environ.get('DB_PORT', '5432')} "
    f"dbname={os.environ['DB_NAME']} "
    f"user={os.environ['DB_USER']} "
    f"password={os.environ['DB_PASSWORD']}"
)

def init_db():
    with psycopg.connect(DSN) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT)")
        conn.commit()

@app.route("/notes", methods=["GET"])
def list_notes():
    with psycopg.connect(DSN, row_factory=dict_row) as conn:
        rows = conn.execute("SELECT id, text FROM notes ORDER BY id").fetchall()
        return jsonify(rows)

@app.route("/notes/<text>", methods=["POST"])
def add_note(text):
    with psycopg.connect(DSN) as conn:
        conn.execute("INSERT INTO notes (text) VALUES (%s)", (text,))
        conn.commit()
    return {"ok": True}, 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)
