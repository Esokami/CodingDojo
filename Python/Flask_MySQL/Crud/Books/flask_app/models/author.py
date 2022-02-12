from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, db):
        self.id = db["id"]
        self.first_name = db["first_name"]
        self.last_name = db["last_name"]
        self.created_at = db["created_at"]
        self.updated_at = db["updated_at"]
        self.books = []

    # Method to get all authors from the database
    @classmethod
    def get_all_authors(cls):
        # Need to use a query 
        query = "SELECT * FROM authors;"
        # run the above created query, in the following 
        results = connectToMySQL("books_schema").query_db(query)
        # create an empty dictionary
        authors = []
        # use a loop to get all the authors and input them into the dictionary
        for row_in_db in results:
            authors.append(cls(row_in_db))
        return authors

    # Method to create authors
    @classmethod
    def create_author(cls, data):
        # Need to use appropriate commands to insert data into database
        query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        # return the updated database
        return connectToMySQL("books_schema").query_db(query, data)

    # Method to get author with favorite books
    @classmethod
    def get_author_with_favorite(cls, data):
        # Need to use LEFT JOIN to connect author and books tables that have favorites
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        #return updated database
        results = connectToMySQL("books_schema").query_db(query, data)
        # results will be alist of authors with favorites attached to each row
        author = cls(results[0])
        #use a loop the books associated with the author
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.books.append(book.Book(book_data))
        return author

    @classmethod
    def add_favorite_book(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)

    @classmethod
    def get_unfavorited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        results = connectToMySQL("books_schema").query_db(query, data)
        authors = []
        for row_in_db in results:
            authors.append(cls(row_in_db))
        return authors