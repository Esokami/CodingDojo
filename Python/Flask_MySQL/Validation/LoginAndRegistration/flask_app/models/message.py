from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Message:
    def __init__(self, data):
        self.id = data["id"]
        self.message = data["message"]
        self.recipient = data["recipient"]
        self.recipient_id = data["recipient_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = data["creator"]
        self.user_id = data["user_id"]
    
    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (message, recipient_id, user_id, created_at, updated_at) VALUES (%(message)s, %(recipient_id)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL("register_schema").query_db(query, data)

    @classmethod
    def get_all_messages_with_creator(cls, data):
        query = "SELECT users.first_name AS creator, users2.first_name AS recipient, messages.* FROM users LEFT JOIN messages ON users.id = messages.user_id LEFT JOIN users as users2 ON users2.id = messages.recipient_id WHERE users2.id = %(id)s;"
        results = connectToMySQL("register_schema").query_db(query, data)
        all_messages = []
        for row in results: 
            all_messages.append(cls(row))
        return all_messages

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL("register_schema").query_db(query, data)

