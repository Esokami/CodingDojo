from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo: 
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        dojos_from_db = connectToMySQL("dojo_survey_schema").query_db(query)
        dojos = []
        for row in dojos_from_db:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL("dojo_survey_schema").query_db(query,data)

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(dojo["location"]) < 5:
            flash("Location must be selected")
            is_valid = False
        if len(dojo["language"]) < 1:
            flash("Language must be selected")
            is_valid = False
        if len(dojo["comment"]) < 3:
            flash("Comment must be at least 3 characters")
        return is_valid