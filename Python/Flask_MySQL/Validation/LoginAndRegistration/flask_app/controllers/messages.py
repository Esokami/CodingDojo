#messages.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app.models.user import User

# @app.route("/wall")
# def show_wall():
#     return render_template("success.html")

# @app.route("/create_message", methods=["POST"])
# def create_message():
#     # validations
#     data = {
#         "message" : request.form["message"],
#         "user_id" : session["user_id"]
#     }
#     Message.create_message(data)
#     return redirect("/wall")

# @app.route("/delete/<int:message_id>")
# def delete_message(message_id):
#     data = {
#         "id" : message_id
#     }
#     Message.destroy(data)
#     return redirect("/wall")