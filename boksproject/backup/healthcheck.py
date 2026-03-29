#!/usr/bin/env python 


from flask import Flask, render_template, request
import subprocess
import socket

app = Flask(__name__)

def run_local_commands():
    commands = {
        "uptime": "uptime",
        "memory": "free -h",
        "disk": "df -h"
    }

    output = {}

    for key, cmd in commands.items():
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output[key] = result.stdout.strip()

    return output


@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        input_host = request.form["hostname"]

        # Get current machine hostname
        current_host = socket.gethostname()

        if input_host == current_host:
            data = run_local_commands()
        else:
            error = f"Invalid hostname! This app only runs on: {current_host}"

    return render_template("index.html", data=data, error=error)
app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    app.run(debug=True)
