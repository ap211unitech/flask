from flask import Flask, render_template
app = Flask(__name__)


@app.route("/<name>")
def fun(name):
    return render_template("./html/index.html", val=name)


if __name__ == "__main__":
    app.run("127.0.0.1", 80, debug=True)
