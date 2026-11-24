import os
import sqlite3
import subprocess

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(service="b", ok=True)


@app.route("/lookup")
def lookup():
    user_id = request.args.get("id", "")
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    rows = cursor.fetchall()
    connection.close()
    return jsonify(rows)


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    output = subprocess.check_output("ping -c 1 " + host, shell=True)
    return jsonify(output=output.decode("utf-8", "replace"))


@app.route("/render")
def render():
    template = request.args.get("template", "")
    return app.jinja_env.from_string(template).render()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
