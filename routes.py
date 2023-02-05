from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("add_recipe")
#def add_recipe():
    #TODO
    #creates ID for recipe, notes user ID and directs to edit recipe

#@app.route("/edit_recipe")
#def edit_recipe():
    #TODO

#@app.route("logout")
#def logout():
    #TODO

#@app.route("/login")
#def login():
    #TODO

#@app.route("/register"):
#def register():
    #TODO

