import pymongo 
from pymongo import MongoClient
import CommentsM

client = MongoClient()
db = client.comments
comments = db.comments

print "--COMMENTS: " + str(comments)
for comment in comments.find():
    comments.remove()
print

#NOTE: Insert commands to test in starting here...

print "--MAKING COMMENTS..."
CommentsM.makeComment(42,"this is the body","this is the username")
CommentsM.makeComment(42,"hello there body","unamestuff")
print

result = CommentsM.retrieveComments(42)
for r in result:
    print "--RETRIEVING COMMENTS: "
    print str(r)
print

print "--REMOVING COMMENTS..."
CommentsM.deleteComments(42)
print

print "--PRINTING OUT EVERYTHING IN COMMENTS: "
for comment in comments.find():
    print comment
print
