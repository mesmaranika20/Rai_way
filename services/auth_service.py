from database.users import db_get_user, db_create_user, hash_password

def register(username, password):
    db_create_user(username, password)
    return {"registered": True}

def login(username, password):
    user = db_get_user(username)
    if not user:
        return None
    if user["password"] != hash_password(password):
        return None
    return {"id": user["id"], "username": user["username"]}
