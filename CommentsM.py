import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.comments
comments = db.comments

def makeComment(ID, body, uname):
    I = ID
    B = body
    P = 0
    D = time.strftime("%x %X")
    U = uname
    comment = {"commentID":I,
            "body":B,
            "points": P,
            "date":D,
            "user":U}
    comments.insert(comment)
   

def retrieveComments(ID):
    result = comments.find({"commentID":ID})
    return result


def deleteComments(ID):
    comments.remove({"commentID":ID})
    
