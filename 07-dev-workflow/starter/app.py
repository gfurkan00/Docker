from flask import Flask
import os, sys

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello from {os.environ.get('STAGE', 'prod')}</h1>"

if __name__ == "__main__":
    # Production server stub (no reload).
    app.run(host="0.0.0.0", port=8080, debug=False)
