import pymongo 
from pymongo import MongoClient
import CommentsM
import PostsM
import RegisterM

print
print
print
print "********PRINTING IS BEGINNING********"
print

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
PostsM.makePost("title1", "body1", "uname1");
PostsM.makePost("title2", "body2", "uname2");
print

print "--GETTING NEXT POST ID:"
print PostsM.getNextPostID()
print

print "--RETRIEVING POSTS:"
posts = PostsM.retrievePost()
for p in posts:
    print p
print


###############################
# TESTING USERS aka REGISTERM #
###############################
client = MongoClient()
db = client.users
users = db.users

print "--USERS: " + str(users)
for user in users.find():
    users.remove()
print

print "--CHECKAVAIL:"
print RegisterM.checkAvail("username1");
print

print "--CHECKAVAIL:"
print RegisterM.checkAvail("username1");
print

print "--GETNEXTID:"
print RegisterM.getNextID();
print

print "--REGISTER:"
print RegisterM.Register("username2", "password2")
print
