from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/process", methods=["POST"])
# def process():
#     session["username"] = request.form["user_name"]
#     session["userlocation"] = request.form["dojo_location"]
#     session["userlanguage"] = request.form["fav_language"]
#     session["usercomment"] = request.form["comment"]
#     return redirect("/result")

@app.route("/create", methods=["POST"])
def create_user():
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    Dojo.create(data)
    return redirect("/result")

@app.route("/result")
def show_result():
    return render_template("results.html", all_dojos = Dojo.get_all_dojos())