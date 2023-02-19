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
        db.session.execute(command, {"text":text})
        db.session.commit()
        return True
    except:
        return False

#TODO
#def get_recipe_by_id(id):
#add_directions(recipe_id, text)
#create_new_ingredient(ingredient)
#add_ingredient_to_recipe(recipe_id, ingredient_id, quantity)
#delete_ingredient_from_recipe
#edit_ingredient_quantity_in_recipe
#edit_alcohol_status(recipe_id, status)
#get_racipes_by_ingredient(ingredient)
#get_recipes_by_name(title)
