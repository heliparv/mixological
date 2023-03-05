from app import app
from flask import render_template, request, redirect, session
import users
import recipes
import ratings

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        recipe_list = recipes.get_alphabetized_list_of_recipes()
        return render_template("index.html", id=users.get_user_id(), recipes=recipe_list)
    if request.method == "POST":
        session['recipe_id'] = request.form["recipe_id"]
        return redirect("/view_recipe")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "GET":
        return render_template("add_recipe.html")
    if request.method == "POST":
        check_token()
        title = request.form["title"]
        value = recipes.add_new_recipe(title, request.form["alcohol"])
        if value:
            if value == -1:
                return render_template("error.html", message="Please log in before adding recipe.")
            elif value == -2:
                return render_template("error.html", message="Recipe title taken.")
            else:
                session['recipe_id'] = recipes.get_recipe_id_by_full_title(title)
                return redirect("/edit_recipe")
        return render_template("error.html", message="Could not add new recipe.")

@app.route("/edit_recipe", methods=["GET", "POST"])
def edit_recipe():
    recipe = recipes.get_recipe_by_id(session['recipe_id'])
    ingredients = recipes.get_contents_by_recipe_id(session['recipe_id'])
    if request.method == "GET":
        return render_template("edit_recipe.html",
                               name=recipe['title'],
                               alcohol=recipe['alcohol'],
                               directions=recipe['directions'],
                               ingredients=ingredients)
    if request.method == "POST":
        check_token()
        new_title = request.form["title"]
        if new_title != recipe["title"]:
            recipes.edit_recipe_title(session["recipe_id"], new_title)
        new_alcohol_status = request.form["alcohol"]
        if new_alcohol_status != recipe["alcohol"]:
            recipes.edit_alcohol_status(session["recipe_id"], new_alcohol_status)
        new_directions = request.form["directions"]
        if new_directions != recipe["directions"]:
            recipes.edit_recipe_directions(session["recipe_id"], new_directions)
        delete = request.form.getlist("delete")
        if delete != []:
            for ingredient_id in delete:
                recipes.delete_ingredient_from_recipe(session["recipe_id"], ingredient_id)
        return redirect("/view_recipe")

@app.route("/view_recipe")
def view_recipe():
    recipe = recipes.get_recipe_by_id(session['recipe_id'])
    ingredients = recipes.get_contents_by_recipe_id(session['recipe_id'])
    user_rating = ratings.get_rating_by_user()
    if recipe and ingredients:
        return render_template("view_recipe.html", title=recipe['title'], alcohol=recipe['alcohol'], ingredients=ingredients, directions=recipe['directions'], user_rating=user_rating)
    else:
        return render_template("error.html", message="Could not retrieve recipe data from database.")

@app.route("/add_ingredient", methods=["GET", "POST"])
def add_ingredient():
    if request.method == "GET":
        ingredient_list = recipes.get_alphabetized_list_of_ingredients()
        return render_template("add_ingredient.html", ingredients=ingredient_list)
    if request.method == "POST":
        check_token()
        if request.form["action"] == "new":
            ingredient = request.form["ingredient"]
            ingredient_id = recipes.create_new_ingredient(ingredient)
            if not ingredient_id:
                return redirect("/error", message="Could not create new ingredient")
        else:
            choice = request.form["ingredient"]
            choice = choice.split(",")
            ingredient_id = choice[0]
            ingredient = choice[1]
        added = recipes.add_ingredient_to_recipe(session['recipe_id'], ingredient_id, ingredient, request.form["quantity"])
        if not added:
            return redirect("/error", message="Could not add ingredient to recipe")
        return redirect("/edit_recipe")

@app.route("/rate_recipe", methods=["GET", "POST"])
def rate_recipe():
    if request.method == "GET":
        return render_template("rate_recipe.html")
    if request.method == "POST":
        check_token()
        rating = request.form["rating"]
        rated = ratings.rate_recipe(rating)
        if rated:
            return redirect("/view_recipe")
        return render_template("error.html", message="Could not add rating")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        elif users.register(username, password1):
            return redirect("/")
        return render_template("error.html", message="Register failed. Username might be taken or database connection lost.")

def check_token():
    if session["csrf_token"] != request.form["csrf_token"]:
        users.logout()
        session["csrf_token"] = 0
        return redirect("error.html", message="You don't have the correct credentials to do this. Try logging in again.")
    