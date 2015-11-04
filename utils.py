import Posts

def search(query, posts, comments):
    posts_with_query = []
    for post in posts:
        if query in post['title'] or query in post['body']:
            # If the request form query is in post[0] or post[1]... (title and contents?)
            posts_with_query.append(post)
    for comment in comments:
        if query in comment['body']:
            is_unique_post = True
            #checks if the post the comment belongs to has already independently been added to posts.
            for post in posts_with_query:
                if post['id'] == comment['commentID']:
                    is_unique_post = False
            if(is_unique_post):
                for post in posts:
                    if post['id'] == comment['commentID']:
                        posts_with_query.append(post)
    return posts_with_query
