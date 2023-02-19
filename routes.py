from app import app
from flask import render_template, request, redirect
import users
import recipes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "GET":
        return render_template("add_recipe.html")
    if request.method == "POST":
        title = request.form["title"]
        alcohol = request.form["alcohol"]
        value = recipes.add_new_recipe(title, alcohol)
        if value:
            if value == 0:
                return render_template("error.html", message="Please log in before adding recipe.")
            else:
                return redirect("/edit_recipe")
        return render_template("error.html", message="Could not add new recipe.")


@app.route("/edit_recipe")
def edit_recipe():
    return render_template("error.html", message="Recipe editing hasn't been coded yet")
    #TODO

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
            return render_template("error.html", "Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        print("render template")
        return render_template("register.html")
    if request.method == "POST":
        print("post")
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords don't match")
        elif users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Register failed")
