# authors.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route("/")
def index():
    return  redirect("/authors")

@app.route("/authors")
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", all_authors = authors)

@app.route("/create_author", methods=["POST"])
def create_author():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"]
    }
    Author.create_author(data)
    return redirect("/authors")

@app.route("/authors/<int:author_id>")
def show_author(author_id):
    data = {
        "id" : author_id
    }
    return render_template("show_author.html", author = Author.get_author_with_favorite(data), unfavorited_books = Book.get_unfavorited_books(data))

@app.route("/author/favorite_book", methods=["POST"])
def add_favorite_book():
    data = {
        "author_id" : request.form["author_id"],
        "book_id" : request.form["book_id"]
    }
    Author.add_favorite_book(data)
    return redirect(f"/authors/{request.form['author_id']}")