import pymongo 
from pymongo import MongoClient
import CommentsM




client = MongoClient()
db = client.test_database
posts = db.posts

print "  POSTS: " + str(posts)
for post in posts.find():
    posts.remove()
print

#NOTE: Insert commands to test in here
CommentsM.makeComment(42,"this is the body","this is the username")
CommentsM.makeComment(42,"this is the body2","this is the username2")
result = CommentsM.retrieveComments(42)
for r in result:
    print "  RETRIEVING COMMENTS: " + str(r)
#NOTE: This only retrieves one comment for some reason, not all in the db that have postID==42, just one document/entry
# CommentsM.deleteComments(42)
#NOTE: This removes every single comment that has postID==42, in CONTRAST to the single retrieving of retrieveComments
print

print "  PRINTING OUT EVERYTHING IN POSTS: "
for post in posts.find():
    print post

