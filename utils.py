import Posts

def search(query, comments):
    posts_with_query = []
    for post in Posts.retrievePost():
        if query in post[0] or query in post[1]:
            # If the request form query is in post[0] or post[1]... (title and contents?)
            posts_with_query.append(post)
    for comment_group in comments:
        for comment in comment_group: # At the moment, I can only assume this is what is meant
            if query in comment[1]:
                is_unique_post = True
                #checks if the post the comment belongs to has already independently been added to posts.
                for post in posts_with_query:
                    if post[2] == comment[0]:
                        is_unique_post = False
                if(is_unique_post):
                    for post in Posts.retrievePost():
                        if post[2] == comment[0]:
                            posts_with_query.append(post)
    return posts_with_query
