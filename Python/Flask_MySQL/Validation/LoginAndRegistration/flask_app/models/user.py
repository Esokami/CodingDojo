from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, db):
        self.id = db["id"]
        self.first_name = db["first_name"]
        self.last_name = db["last_name"]
        self.email = db["email"]
        self.password = db["password"]
        self.created_at = db["created_at"]
        self.updated_at = db["updated_at"]

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("register_schema").query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL("register_schema").query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("register_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL("register_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("register_schema").query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.", 'register')
            is_valid = False
        if len(user["first_name"]) < 3:
            flash("First Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user["last_name"]) < 3:
            flash("Last Name must be at least 3 characters.", 'register')
            is_valid = False
        if len(user["password"]) < 8: 
            flash("Password must be at least 8 characters.", 'register')
            is_valid = False
        if user["password"] != user["confirm_password"]:
            flash("Passwords must match.", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user["email"]):
            flash("Invalid email", 'register')
            is_valid = False
        return is_valid