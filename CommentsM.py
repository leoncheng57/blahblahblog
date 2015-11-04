import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.blogdb
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
    result = []
    for comment in comments.find({"commentID":ID}):
        result.append(comment)
    return result


def deleteComments(ID):
    comments.remove({"commentID":ID})
    
