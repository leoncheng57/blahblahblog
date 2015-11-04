import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.users
users = db.users

def getNextID():
    ids = []
    for user in users.find():
        ids.insert(0,user["id"])
    if(len(ids)==0):
        return 1
    nextID = max(ids)+1;
    return nextID

def checkAvail(username):
    unames=[]
    for user in users.find():
        unames.insert(0,user["username"]);
    if (len(unames)==0):
        return False
    else:
        return True
