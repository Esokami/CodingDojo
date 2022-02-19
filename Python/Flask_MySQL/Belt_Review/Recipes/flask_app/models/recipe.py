from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe():
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.thirty_minutes = data["thirty_minutes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.users = []

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, thirty_minutes, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instruction)s, %(thirty_minutes)s, %(user_id)s, %(created_at)s, NOW());"
        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes_schema").query_db(query)
        recipes = []
        for row in recipes:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def get_all_recipes_with_user(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        all_recipes = []
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, thirty_minutes=%(thirty_minutes)s, user_id=%(user_id)s, created_at=%(created_at)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("recipes_schema").query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) < 3:
            flash("Name must be at least 3 characters.", 'recipe')
            is_valid = False
        if len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters.", 'recipe')
            is_valid = False
        if len(recipe["instruction"]) < 3: 
            flash("Instructions must be at least 3 characters.", 'recipe')
            is_valid = False
        if recipe["created_at"] == "":
            flash("Please enter a date.", 'recipe')
            is_valid = False
        return is_valid


