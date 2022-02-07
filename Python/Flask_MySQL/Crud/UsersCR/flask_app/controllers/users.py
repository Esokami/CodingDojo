from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("create.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/users")
def show_users():
    users = User.get_all()
    return render_template("read(all).html", all_users = users)

@app.route("/users/<int:user_id>")
def current_user(user_id):
    data = {
        "id": user_id
    }
    return render_template("read(one).html", user=User.get_one(data))

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    data = {
        "id" : user_id
    }
    return render_template("edit.html", user=User.get_one(data))

@app.route("/users/<int:user_id>/update", methods=["POST"])
def update_user(user_id):
    data = {
        "id": user_id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect(f"/users/{user_id}")

@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    data = {
    "id" : user_id
    }
    User.destroy(data)
    return redirect("/users")
