from db import db
from flask import session
from sqlalchemy.sql import text
import users

def get_rating_by_user(recipe_id):
    user_id = users.get_user_id()
    command = "SELECT rating FROM ratings WHERE user_id=:user_id AND recipe_id=:recipe_id"
    try:
        result = db.session.execute(text(command), {"user_id":user_id, "recipe_id":recipe_id})
        rating = result.fetchone()
        return rating[0]
    except:
        return "-"

def rate_recipe(rating):
    user_id = users.get_user_id()
    recipe_id = session["recipe_id"]
    command = "INSERT INTO ratings (rating,user_id,recipe_id) VALUES (:rating,:user_id,:recipe_id)"
    #try:
    db.session.execute(text(command), {"rating":rating,"user_id":user_id,"recipe_id":recipe_id})
    db.session.commit()
    return True
    #except:
    #    return False


#TODO add_rating(recipe_id, user_id, rating)check that user hasn't rated the item already
#modify_rating(recipe_id, user_id, rating)
#get_recipe_average_rating(recipe_id)
#get_user_rating_for_recipe(recipe_id, user_id)
#rank_recipes_by_average()
#rank_recipes_by_user_rating()