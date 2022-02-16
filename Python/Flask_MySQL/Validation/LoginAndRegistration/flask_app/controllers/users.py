from operator import methodcaller
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }
    user_id = User.create_user(data)
    session["user_id"] = user_id
    return redirect("/success")

@app.route("/login", methods=["POST"])
def login_user():
    data = {"email" : request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password", 'error')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password", 'error')
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect("/success")

@app.route("/success")
def show_user():
    if "user_id" not in session:
        return redirect("/")
    data = {"id" : session["user_id"]}
    return render_template("success.html", user = User.get_by_id(data))

@app.route("/clear", methods=["POST"])
def clear_session():
    session.clear()
    return redirect("/")