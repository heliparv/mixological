from app import app
from flask import render_template, request, redirect, session
import users
import recipes

@app.route("/")
def index():
    return render_template("index.html", id=users.get_user_id())

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "GET":
        return render_template("add_recipe.html")
    if request.method == "POST":
        title = request.form["title"]
        value = recipes.add_new_recipe(title, request.form["alcohol"])
        if value:
            if value == -1:
                return render_template("error.html", message="Please log in before adding recipe.")
            elif value == -2:
                return render_template("error.html", message="Recipe title taken.")
            else:
                session['title'] = title
                return redirect("/edit_recipe")
        return render_template("error.html", message="Could not add new recipe.")

@app.route("/edit_recipe")
def edit_recipe():
    recipe = recipes.get_recipe_by_full_title(session['title'])
    return render_template("edit_recipe.html")

@app.route("/view_recipe")
def view_recipe():
    #TODO
    #here's where we would get recipe info
    #but now just testing layout with some values
    title = "Shirley Temple"
    alcohol = "moctail"
    ingredients = [["grenadine", "0.75 cl"],
                   ["lemon juice", "1 cl"],
                   ["ginger beer", "10 cl"],
                   ["ice", ""],
                   ["cherry", "1"]]
    directions = "Fill glass with ice, pour grenadine and ginger beer, mix and garnish with cherry"
    return render_template("view_recipe.html", title=title, alcohol=alcohol, ingredients=ingredients, directions=directions)

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
