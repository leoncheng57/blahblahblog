import pymongo 
from pymongo import MongoClient
import CommentsM
import PostsM

####################
# TESTING COMMENTS #
####################

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

#################
# TESTING POSTS #
#################
client = MongoClient()
db = client.posts
posts = db.posts

print "--POSTS: " + str(posts)
for post in posts.find():
    posts.remove()
print


print "--MAKING POST..."
PostsM.makePost("sample title", "sample body", "sample uname");
PostsM.makePost("sample title", "sample body", "sample uname");
PostsM.makePost("sample title", "sample body", "sample uname");
print "--GETTING NEXT POST ID..."
print PostsM.getNextPostID();
