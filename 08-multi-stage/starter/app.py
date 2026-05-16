from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)
KEY = Fernet.generate_key()
F = Fernet(KEY)

@app.route("/")
def index():
    token = F.encrypt(b"secret payload")
    return {"token": token.decode(), "key": KEY.decode()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
