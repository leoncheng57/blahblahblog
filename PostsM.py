import pymongo
import pymongo from MongoClient
import datetime
import time

client = MongoClient()
db = client.posts
posts = db.posts

#TODO: This function has not been tested yet, has just been written
def makePost(title, body, uname):
    T = title
    B = body
    I = getNextPostID()
    P = 0
    D = time.strftime("%x %X")
    U = uname
    post = {"title":T,
            "body":B,
            "id":I,
            "points":P,
            "date":D,
            "user":U}
    posts.insert(post)
