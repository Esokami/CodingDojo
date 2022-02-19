#/controllers/recipes.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/view/<int:recipe_id>")
def view_recipe(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : recipe_id,
        }
    user_data = {
        "id" : session["user_id"]
    }
    return render_template("recipe(view).html", user = User.get_by_id(user_data), recipe = Recipe.get_one_recipe(data))

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    if not Recipe.validate_recipe(request.form):
        return redirect("/new_recipe")
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "thirty_minutes" : int(request.form["thirty_minutes"]),
        "created_at" : request.form["created_at"],
        "user_id" : session["user_id"]
    }
    Recipe.create_recipe(data)
    return redirect("/success")

@app.route("/new_recipe")
def new_recipe():
    if "user_id" not in session:
        return redirect("/")
    data = {"id" : session["user_id"]}
    return render_template("recipe(add).html")

@app.route("/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id" : recipe_id,
        "user_id" : session["user_id"]
    }
    return render_template("recipe(edit).html", recipe = Recipe.get_one_recipe(data))

@app.route("/recipes/<int:recipe_id>/update", methods=["POST"])
def update_recipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/{request.form['recipe_id']}")
    data = {
        "id" : recipe_id,
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "thirty_minutes" : int(request.form["thirty_minutes"]),
        "created_at" : request.form["created_at"],
        "user_id" : session["user_id"]
    }
    Recipe.update_recipe(data)
    return redirect("/success")

@app.route("/delete/<int:recipe_id>")
def delete_recipe(recipe_id):
    data = {'id' : recipe_id}
    Recipe.delete_recipe(data)
    return redirect("/success")