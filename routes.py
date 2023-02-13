from app import app
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_recipe")
def add_recipe():
    return render_template("error.html", message="Adding recipe hasn't been coded yet")
    #TODO
    #creates ID for recipe, notes user ID and directs to edit recipe

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
    return render_template("error.html", message="Logout hasn't been coded yet")
    #TODO

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
        else:
            return render_template("error.html", message="Register failed")
