from flask import Flask
import os, sys

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "World")
    return f"<h1>Hello, {name}!</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

def print_help():
    print("Usage: docker run <image> [--help]")
    print("Env vars: NAME (default: World), PORT (default: 8080)")

if __name__ == "__main__":
    if "--help" in sys.argv:
        print_help()
        sys.exit(0)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
