from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password):
    hashword = generate_password_hash(password)
    try:
        command = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(command, {"username":username, "password":hashword})
        db.session.commit()
    except:
        return False
    return True