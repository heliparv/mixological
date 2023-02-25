from db import db
from flask import session
from sqlalchemy.sql import text
import users

def add_new_recipe(title, alcohol):
    user_id = users.get_user_id()
    if user_id == 0:
        return -1
    if get_recipe_by_full_title(title):
        return -2
    command = "INSERT INTO recipes (title,alcohol,directions,user_id) VALUES (:content,:alcohol,:directions,:user_id)"
    try:
        directions = ""
        db.session.execute(text(command), {"title":title, "alcohol":alcohol, "directions":directions, "user_id":user_id})
        db.session.commit()
        return True
    except:
        return False

def add_directions(recipe_id, text):
    command = "UPDATE recipes SET directions=:text WHERE id=:recipe_id"
    try:
        db.session.execute(text(command), {"text":text, "recipe_id":recipe_id})
        db.session.commit()
        return True
    except:
        return False

def add_ingredient_to_recipe(recipe_id, ingredient_id, quantity):
    command = "INSERT INTO contents (ingredient_id, quantity, recipe_id) VALUES (:ingredient_id, :quantity, :recipe_id)"
    try:
        db.session.execute(text(command), {"ingredient_id":ingredient_id, "quantity":quantity, "recipe_id":recipe_id})
        db.session.commit()
        return True
    except:
        return False

def get_recipe_by_id(recipe_id):
    command = "SELECT title, alcohol, directions FROM recipes WHERE id=:recipe_id"
    result = db.session.execute(text(command), {"recipe_id":recipe_id})
    recipe = result.fetchall()
    return recipe

def get_contents_by_recipe_id(recipe_id):
    command = "SELECT ingredient_id, quantity FROM recipes WHERE recipe_id=:recipe_id"
    try:
        result = db.session.execute(text(command), {"recipe_id":recipe_id})
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
        db.session.execute(text(command), {"ingredient":ingredient})
        db.session.commit()
        return True
    except:
        return False

def get_ingredient_id_by_name(ingredient):
    command = "SELECT id FROM ingredients WHERE ingredient=:ingredient"
    try:
        result = db.session.execute(text(command), {"ingredient":ingredient})
        return result.fetchone()
    except:
        return False

def delete_ingredient_from_recipe(recipe_id, ingredient_id):
    command = "DELETE FROM contents WHERE recipe_id=:recipe_id AND ingredient_id=:ingredient_id"
    try:
        db.session.execute(text(command), {"recipe_id":recipe_id, "ingredient_id":ingredient_id})
        db.session.commit()
        return True
    except:
        return False

def edit_ingredient_quantity_in_recipe(content_id, quantity):
    command = "UPDATE contents SET quantity=:quantity WHERE id=:content_id"
    try:
        db.session.execute(text(command), {"quantity":quantity, "content_id":content_id})
        db.session.commit()
        return True
    except:
        return False

def edit_alcohol_status(recipe_id, status):
    command = "UPDATE recipes SET alcohol=:status WHERE id=:recipe_id"
    try:
        db.session.execute(text(command), {"status":status, "recipe_id":recipe_id})
        db.session.commit()
        return True
    except:
        return False

def get_recipe_by_full_title(title):
    command = "SELECT * FROM recipes WHERE title=:title"
    try:
        result = db.session.execute(text(command), {"title":title})
        return result.fetchone()
    except:
        return False

#TODO
#get_recipes_by_ingredient(ingredient_id):
