import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.users
users = db.users

def Login(username, password):
    uname = username
    pword = password
    user = {"username":uname,
            "password":pword}
    print user
    #print users.find(user)
    # for u in users.find(user):
    #     print u
    l = []
    for user in users.find(user):
        l.insert(0,user)
    if (len(l)==0):
        return False
    else:
        return True
        
    
#seems like this function just returns True is the param is True?
def correct_login(blah):
    if blah:
        return True
    else:
        return False
