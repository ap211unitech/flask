from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3307/codingthunder'
db = SQLAlchemy(app)


class Contacts(db.Model):
    serial_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_no = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def fun():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        msg = request.form.get("msg")
        entry = Contacts(name=name,  phone_no=phone, msg=msg,
                         date=datetime.now(), email=email)
        db.session.add(entry)
        db.session.commit()
        print(name, email, phone, msg)

    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug=True)
