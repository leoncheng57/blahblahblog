from bson.objectid import ObjectId
import pymongo, datetime, time, re

posts = pymongo.MongoClient().blogdb.posts

def make_post(title, author, content):
    posts.insert({
        'title':    title,
        'author':   author,
        'content':  content,
        'date':     time.strftime('%x %X'),
    })

def get_posts(query=None):
    if query:
        expression = re.compile(r'%s' % query, re.IGNORECASE)
        return posts.find(
            {'$or': [
                {'title':            expression},
                {'content':          expression},
                {'comments.content': expression},
                ]
            }
        )
    return posts.find()

def make_comment(postid, author, content):
    posts.find_one_and_update(
        {'_id': ObjectId(postid)},
        {'$push': {
            'comments': {
                'author': author,
                'content': content,
                'date': time.strftime('%x %X'),
            }
        }},
    )

def delete_post(postid):
    posts.delete_one({'_id': ObjectId(postid)})



