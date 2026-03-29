#!/usr/bin/env python

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        host_input = request.form.get("hostname")

        if host_input:
            hosts = [h.strip() for h in host_input.split(",")]
            results = []

            for host in hosts:
                try:
                    # uptime (no params)
                    uptime_result = subprocess.check_output(
                        ["uptime"], stderr=subprocess.STDOUT
                    )

                    # netstat with option (like -an)
                    netstat_result = subprocess.check_output(
                        ["netstat"] + host.split(),
                        stderr=subprocess.STDOUT
                    )

                    results.append(
                        f"===== OPTION: {host} =====\n"
                        f"UPTIME:\n{uptime_result.decode()}\n\n"
                        f"NETSTAT:\n{netstat_result.decode()}"
                    )

                except subprocess.CalledProcessError as e:
                    results.append(
                        f"===== OPTION: {host} =====\nERROR:\n{e.output.decode()}"
                    )

            output = "\n\n".join(results)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
