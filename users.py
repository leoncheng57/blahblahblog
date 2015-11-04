from werkzeug.security import generate_password_hash, check_password_hash
import pymongo, datetime, time

users = pymongo.MongoClient().blogdb.users

def login(username, password):
    user = users.find_one({'username': username})
    return check_password_hash(user['password'], password)

def register(username, password):
    if users.find_one({'username': username}):
        return False
    password = generate_password_hash(password)
    print "PASSWORD =", password
    users.insert({
        'username': username,
        'password': password,
    })
    return True
    