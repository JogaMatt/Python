from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re
from pprint import pprint

DATABASE = 'belt_exam'

class Magazine:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.first_name = data['first_name']

    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO magazines (title, description, user_id) VALUES ( %(title)s, %(description)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_all_magazines(cls):
        query = "SELECT magazines.*, users.first_name FROM magazines LEFT JOIN users ON users.id = magazines.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        magazines = []
        for row in results:
            magazines.append( cls(row) )
        return magazines

    

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM magazines WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM magazines WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_magazine(recipe:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(recipe['title']) < 2:
            flash("Title must be at least 2 characters.")
            is_valid = False
        if len(recipe['description']) < 10:
            flash("Description must be at least 10 characters.")
            is_valid = False
        return is_valid
