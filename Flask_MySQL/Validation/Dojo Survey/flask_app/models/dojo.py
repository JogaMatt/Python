from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

DATABASE = 'dojo_survey'

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_last_survey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        return Survey(results[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, location, language, comment) VALUES ( %(name)s , %(location)s , %(language)s , %(comment)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid