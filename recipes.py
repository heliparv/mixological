from db import db
from flask import session
import users

def add_new_recipe(title, alcohol):
    user_id = users.get_user_id()
    if user_id == 0:
        return -1
    command = "INSERT INTO recipes (title,alcohol,directions,user_id) VALUES (:content,:alcohol,:directions,:user_id)"
    try:
        directions = ""
        db.session.execute(command, {"title":title, "alcohol":alcohol, "directions":directions, "user_id":user_id})
        db.session.commit()
        return True
    except:
        return False

def add_directions(recipe_id, text):
    command = "UPDATE recipes SET directions = text WHERE id = recipe_id"
    try:
        db.session.execute(command, {"text":text, "recipe_id":recipe_id})
        db.session.commit()
        return True
    except:
        return False

def get_recipe_by_id(recipe_id):
    command = "SELECT title, alcohol, directions FROM recipes WHERE id=:recipe_id"
    result = db.session.execute(command, {"recipe_id":recipe_id})
    recipe = result.fetchall()
    return recipe

def get_contents_by_recipe_id(recipe_id):
    command = "SELECT ingredient_id, quantity FROM recipes WHERE recipe_id=:recipe_id"
    try:
        result = db.session.execute(command, {"recipe_id":recipe_id})
        contents = result.fetchall()
        ingredients = []
    #for i in contents:
    #choose ingredient name based on ingredient id in result, haven't figured it out
    #not sure if ditching ingredients table would be better
        return contents, ingredients
    except:
        return False

def create_new_ingredient(ingredient):
    command = "INSERT INTO ingredients (ingredient) VALUES (:ingredient)"
    try:
        db.session.execute(command, {"ingredient":ingredient})
        db.session.commit()
        return True
    except:
        return False


#TODO
#create_new_ingredient(ingredient)
#add_ingredient_to_recipe(recipe_id, ingredient_id, quantity)
#delete_ingredient_from_recipe
#edit_ingredient_quantity_in_recipe
#edit_alcohol_status(recipe_id, status)
#get_racipes_by_ingredient(ingredient)
#get_recipes_by_name(title)
