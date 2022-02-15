from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_email():
    if not Email.validate_email(request.form):
        return redirect("/")
    data = {
        "email" : request.form["email"]
    }
    Email.create_email(data)
    return redirect("/emails")

@app.route("/emails")
def display_emails():
    emails = Email.get_all_emails()
    return render_template("success.html", all_emails = emails)