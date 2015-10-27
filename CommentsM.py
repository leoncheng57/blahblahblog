import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.posts
posts = db.posts

def makeComment(ID, body, uname):
    I = ID
    B = body
    P = 0
    D = time.strftime("%x %X")
    U = uname
    post = {"postID":I,
            "body":B,
            "points": P,
            "date":D,
            "user":U}
    posts.insert(post)


def retrieveComments(ID):
    result = posts.find({"postID":ID})
    return result


def deleteComments(ID):
    posts.remove({"postID":ID})
    
