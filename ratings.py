from db import db
from flask import session
from sqlalchemy.sql import text
import users

def get_rating_by_user():
    command = "SELECT rating FROM ratings WHERE user_id=:user_id AND recipe_id=:recipe_id"
    try:
        result = db.session.execute(text(command), {"user_id":users.get_user_id(), "recipe_id":session["recipe_id"]})
        rating = result.fetchone()
        return rating[0]
    except:
        return "-"

def rate_recipe(rating):
    prev_rating = get_rating_by_user()
    if prev_rating == rating:
        return True
    if prev_rating != "-":
        return edit_rating_on_recipe(rating)
    command = "INSERT INTO ratings (rating,user_id,recipe_id) VALUES (:rating,:user_id,:recipe_id)"
    try:
        db.session.execute(text(command), {"rating":rating,"user_id":users.get_user_id(),"recipe_id":session["recipe_id"]})
        db.session.commit()
        return True
    except:
        return False

def edit_rating_on_recipe(new_rating):
    command = "UPDATE ratings SET rating=:new_rating WHERE user_id=:user_id"
    try:
        db.session.execute(text(command), {"new_rating":new_rating, "user_id":session["user_id"]})
        db.session.commit()
        return True
    except:
        return False


#TODO
#get_recipe_average_rating(recipe_id)
#rank_recipes_by_average()
#rank_recipes_by_user_rating()