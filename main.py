from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def fun():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug=True)
