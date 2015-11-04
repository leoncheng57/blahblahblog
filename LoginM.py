import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.users
users = db.users



#seems like this function just returns True is the param is True?
def correct_login(blah):
    if blah:
        return True
    else:
        return False
