from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
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

# Hashing/Validation

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect("/")
        # ... do other things
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username" : request.form["username"],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session["user_id"] = user_id
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def loging():
    # see if the username provided exists in the database
    data = {"email" : request.form["email"]}
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect("/")
    # if the passwords matched, we set the user_id into session
    session["user_id"] = user_in_db.id
    # never render on a post
    return redirect("/dashboard")