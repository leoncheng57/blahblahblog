import pymongo 
from pymongo import MongoClient
import CommentsM

client = MongoClient()
db = client.test_database
posts = db.posts

print "--POSTS: " + str(posts)
for post in posts.find():
    posts.remove()
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

print "--PRINTING OUT EVERYTHING IN POSTS: "
for post in posts.find():
    print post
print
