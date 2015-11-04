import pymongo
from pymongo import MongoClient
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
    print post
    
def retreivePost():
    result = posts.find();
    return result;

#TODO: Finish writing this function
#TODO: Cut out all the extraneous debuggnig code when done
def getNextPostID():
    #print "inside getNextPostID"
    ids = []
    for post in posts.find():
        # print post
        ids.insert(0,post["id"])
    if (len(ids)==0):
        return 1
    nextID = max(ids)+1;
    #print "ids: "+str(ids)
    return nextID;
