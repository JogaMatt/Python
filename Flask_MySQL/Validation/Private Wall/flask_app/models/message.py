from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash

DATABASE = 'private_wall'

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages (message, sender_id, receiver_id) VALUES ( %(message)s, %(sender_id)s, %(receiver_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all_messages(cls):
        query = "SELECT * FROM messages;"
        results = connectToMySQL(DATABASE).query_db(query)
        messages = []
        for row in results:
            messages.append( cls(row) )
        return messages

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_message(message:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(message['message']) < 5:
            flash("Message must be at least 5 characters.")
            is_valid = False
        return is_valid