from handle_db import HandleDataBase
from werkzeug.security import check_password_hash


def check_user(username: str, password: str):
    user_db = HandleDataBase()
    user = user_db.get_user(username)

    if user:
        correct_password = check_password_hash(user[5], password)
        if correct_password:
            return user

    return None
