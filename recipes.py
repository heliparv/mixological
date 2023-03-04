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
    command = "INSERT INTO recipes (title,alcohol,directions,user_id) VALUES (:title,:alcohol,:directions,:user_id)"
    try:
        directions = "No directions added yet"
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

def get_alphabetized_list_of_recipes():
    command = "SELECT id, title FROM recipes ORDER BY title"
    result = db.session.execute((text(command)))
    recipe_list = result.fetchall()
    return recipe_list

def get_alphabetized_list_of_ingredients():
    command = "SELECT * FROM ingredients ORDER BY ingredient"
    result = db.session.execute((text(command)))
    ingredients = result.fetchall()
    return ingredients

def add_ingredient_to_recipe(recipe_id, ingredient_id, ingredient_name, quantity):
    command = "INSERT INTO contents (ingredient_id, ingredient_name, quantity, recipe_id) VALUES (:ingredient_id, :ingredient_name, :quantity, :recipe_id)"
    try:
        db.session.execute(text(command), {"ingredient_id":ingredient_id, "ingredient_name":ingredient_name, "quantity":quantity, "recipe_id":recipe_id})
        db.session.commit()
        return True
    except:
        return False

def get_recipe_by_id(recipe_id):
    try:
        command = "SELECT * FROM recipes WHERE id=:recipe_id"
        result = db.session.execute(text(command), {"recipe_id":recipe_id})
        recipe = result.fetchone()
        return recipe_to_dictionary(recipe)
    except:
        return False

def get_contents_by_recipe_id(recipe_id):
    command = "SELECT * FROM contents WHERE recipe_id=:recipe_id"
    try:
        result = db.session.execute(text(command), {"recipe_id":recipe_id})
        contents = result.fetchall()
        if contents == []:
            return [(0, 0, "No ingredients added yet", "", 0)]
        return contents
    except:
        return False

def create_new_ingredient(ingredient):
    command = "INSERT INTO ingredients (ingredient) VALUES (:ingredient)"
    try:
        db.session.execute(text(command), {"ingredient":ingredient})
        db.session.commit()
        return get_ingredient_id_by_name(ingredient)
    except:
        return False

def get_ingredient_id_by_name(ingredient):
    command = "SELECT id FROM ingredients WHERE ingredient=:ingredient"
    try:
        result = db.session.execute(text(command), {"ingredient":ingredient})
        id = result.fetchone()
        return id[0]
    except:
        return False

def edit_recipe_title(recipe_id, new_title):
    command = "UPDATE recipes SET title=:new_title WHERE id=:recipe_id"
    db.session.execute(text(command), {"new_title":new_title, "recipe_id":recipe_id})
    db.session.commit()

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
        recipe = result.fetchone()
        recipe_dict = recipe_to_dictionary(recipe)
        return recipe_dict
    except:
        return False

def get_recipe_id_by_full_title(title):
    command = "SELECT id FROM recipes WHERE title=:title"
    try:
        result = db.session.execute(text(command), {"title":title})
        id = result.fetchone()
        return id[0]
    except:
        return False

def recipe_to_dictionary(recipe):
    return {"id":recipe[0], "title":recipe[1], "alcohol":recipe[2], "directions":recipe[3], "user_id":recipe[4]}

def get_ingredient_id_by_name(name):
    command = "SELECT id FROM ingredients WHERE ingredient=:name"
    try:
        result = db.session.execute(text(command), {"name":name})
        id = result.fetchone()
        return id[0]
    except:
        return False

#TODO
#get_recipes_by_ingredient(ingredient_id):
