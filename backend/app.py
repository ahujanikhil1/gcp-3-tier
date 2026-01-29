from flask import Flask, jsonify
from db import get_users

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/users")
def users():
    data = get_users()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
