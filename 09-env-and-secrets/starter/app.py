from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    debug = os.environ.get("APP_DEBUG", "false")
    db_user = os.environ.get("DB_USER", "?")
    # Intentionally do NOT print DB_PASSWORD — secret hygiene.
    return {"debug": debug, "db_user": db_user}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("APP_PORT", "8080")))
