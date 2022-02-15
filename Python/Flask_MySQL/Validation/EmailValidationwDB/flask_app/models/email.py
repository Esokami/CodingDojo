from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL("email_schema").query_db(query)
        emails = []
        for row in results:
            emails.append(cls(row))
        return emails
    
    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL("email_schema").query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email["email"]):
            flash("Invalid email address.")
            is_valid = False
        if EMAIL_REGEX.match(email["email"]):
            flash("Success!")
            is_valid = True
        return is_valid