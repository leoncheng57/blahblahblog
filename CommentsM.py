import pymongo
from pymongo import MongoClient
import datetime
import time

client = MongoClient()
db = client.test_database
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

#TODO: Fix this command so that it retrieves all comments that have postID==ID, not just one
def retrieveComments(ID):
    result = posts.find({"postID":ID})
    return result
    #TODO: What does this return? A dictionary i think. What is it supposed to return?

def deleteComments(ID):
    posts.remove({"postID":ID})
    
