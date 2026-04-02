from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("name", "World")
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
