import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.blogdb
users = db.users

def Login(username, password):
    uname = username
    pword = password
    user = {"username":uname,
            "password":pword}
    print user
    l = []
    for user in users.find(user):
        l.insert(0,user)
    if (len(l)==0):
        return False
    else:
        return True
