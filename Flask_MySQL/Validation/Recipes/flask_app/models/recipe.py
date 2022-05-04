from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re

DATABASE = 'recipes'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cook_time = data['cook_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.made_on = data['made_on']


    @classmethod
    def save(cls, data:dict ) -> int:
        query = "INSERT INTO recipes (name, description, instructions, cook_time, user_id, made_on) VALUES ( %(name)s, %(description)s, %(instructions)s, %(cook_time)s, %(user_id)s, %(made_on)s);"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s, cook_time=%(cook_time)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipes.append( cls(row) )
        return recipes

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM recipes WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe:dict) -> bool:
        is_valid = True # ! we assume this is true
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if(recipe['cook_time'] == ""):
            flash("Must check if under thirty minutes")
            is_valid = False
        if(recipe['made_on'] == ""):
            flash("Must select date")
            is_valid = False
        return is_valid
