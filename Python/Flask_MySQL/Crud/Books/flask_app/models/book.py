from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, db):
        self.id = db["id"]
        self.title = db["title"]
        self.num_of_pages = db["num_of_pages"]
        self.created_at = db["created_at"]
        self.updated_at = db["created_at"]
        self.authors = []

    # Method to get all books in database
    @classmethod
    def get_all_books(cls):
        # Use query to get all books from databse
        query = "SELECT * FROM books;"
        # insert "query" into querydb 
        results = connectToMySQL("books_schema").query_db(query)
        # create an empty dictionary 
        books = []
        # use a loop to go through each book
        for row_in_db in results:
            books.append(cls(row_in_db))
        return books

    # Method to create a book
    @classmethod
    def create_book(cls, data):
        # Use appropriate commands to insert data in database
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        # return the updated databse with the new entry
        return connectToMySQL("books_schema").query_db(query, data)

    #Method to get authors that favorited the book
    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)
        book = cls(results[0])
        for row_from_db in results: 
            author_data ={
                "id" : row_from_db["authors.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book

    @classmethod
    def get_unfavorited_books(cls, data):
        query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);"
        results = connectToMySQL("books_schema").query_db(query, data)
        books = []
        for row_in_db in results:
            books.append(cls(row_in_db))
        return books