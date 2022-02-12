#books.py
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route("/books")
def books():
    books = Book.get_all_books()
    return render_template("books.html", all_books = books)

@app.route("/create_book", methods=["POST"])
def create_book():
    data = {
        "title" :request.form["title"],
        "num_of_pages" : request.form["num_of_pages"]
    }
    Book.create_book(data)
    return redirect("/books")

@app.route("/books/<int:book_id>")
def show_book(book_id):
    data = {
        "id" : book_id
    }
    return render_template("show_book.html", book = Book.get_book_with_authors(data), unfavorited_authors = Author.get_unfavorited_authors(data))

@app.route("/book/favorite_author", methods=["POST"])
def add_favorite_author():
    data = {
        "author_id" : request.form["author_id"],
        "book_id" : request.form["book_id"]
    }
    Author.add_favorite_book(data)
    return redirect(f"/books/{request.form['book_id']}")