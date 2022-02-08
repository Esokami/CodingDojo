# ninjas.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo, ninja

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    print(ninja)
    return redirect("/")

@app.route("/ninjas")
def ninjas():
    return render_template("edit.html", all_dojos = dojo.Dojo.get_all())
