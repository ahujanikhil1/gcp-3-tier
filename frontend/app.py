from flask import Flask
import requests
import os

app = Flask(__name__)
BACKEND_URL = os.environ["BACKEND_URL"]

@app.route("/")
def home():
    users = requests.get(f"{BACKEND_URL}/users").json()
    html = "<h1>Users</h1><ul>"
    for u in users:
        html += f"<li>{u['name']}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
