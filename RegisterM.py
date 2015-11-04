import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.users
users = db.users

def Register(username, password):
    if checkAvail(username):
        uname = username
        pword = password
        nextID = getNextID()
        user = {"username":uname,
                "password":pword,
                "ID":nextID}
        users.insert(user)
        print user
        return True
    else:
        return False

def getNextID():
    ids = []
    for user in users.find():
        ids.insert(0,user["ID"])
    if(len(ids)==0):
        return 1
    nextID = max(ids)+1;
    return nextID

def checkAvail(username):
    unames=[]
    for user in users.find({"username":username})
        unames.insert(0,user["username"]);
    if (len(unames)!=0): 
        return False #so the username is already in the system
    else:
        return True

def checkAvail(username):
    l = []
    for user in users.find({"username":usernames}):
        l.insert(0,user["username"])
    if (len(l)!=0):
        return False #so the username is already in the system
    else:
        return True

def retrieveUsers():
    result = users.find()
    print result
