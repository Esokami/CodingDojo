# dojos.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"],
    }
    Dojo.save(data)
    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def dojo_page(dojo_id):
    data = {
        "id" : dojo_id
    }
    return render_template("read(one).html", dojo = Dojo.get_dojo_with_ninjas(data))


@app.route("/delete/<int:dojo_id>")
def delete_dojo(dojo_id):
    data = {
        "id" : dojo_id
    }
    Dojo.destroy(data)
    return redirect("/dojos")