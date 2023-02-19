from db import db
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

def register(username, password):
    hashword = generate_password_hash(password)
    print("hashword generated")
    try:
        command = "INSERT INTO users (username,password) VALUES (:username,:password)"
        print(username, hashword)
        db.session.execute(command, {"username":username, "password":hashword})
        db.session.commit()
    except:
        return False
    return login(username, password)

def login(username, password):
    command = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(command, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def get_user_id():
    return session.get("user_id",0)