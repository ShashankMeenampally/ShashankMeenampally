from flask import Flask, render_template, request
from healthcheck import health_check

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = {}

    if request.method == "POST":
        host = request.form["host"]
        data = health_check(host)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)