# blahblahblog
For Softdev Bloginator assignment.
A very bland blog. (a.k.a. Spreddit)


## Original Team
|      **Member**      |            **Role**            |
|:--------------------:|:------------------------------:|
|Krzysztof Hochlewicz  | Leader, Middleware             |
|Peter Strbik          | Backend                        |
|Andrew Kratsios       | Middleware                     |
|Serena Chan           | UX                             |

## Refactoring Team
|      **Member**      |            **Role**            |
|:--------------------:|:------------------------------:|
|Angela Chan           | Leader                         |
|Leon Cheng            | Backend                        |
|Amanda Chiu           | UX                             |
|Eric Stringham        | Middleware                     |


## Checklist

 - [ ] encrypt the password
 - [ ] change all instances of getNextID() to either row or primary key (so it is automatic) 

 
## How to use:
 Mostly self-explanatory.
 You can create a new account by clicking "Sign up"
 Once you successfully create a new account, you will be redirected to the Login page.
 Upon logging in, you will be redirected back to the home page, now with the ability to make posts and comments.
 You can comment on any post anyone made, and you can delete your own posts (along with all of their comments).
 There is a search box on the homepage that lets you retrieve all posts and comments that contain a certain phrase.
 The search feature searches all posts and all comments, returning any posts that contain the phrase in their title, body, or any of their comments. 
 It ensures that there are no duplicate results even if the query appears multiple times in a post or in both a post and its comment(s).
 
 The user interface was designed with the use of Bootstrap; all backend and middleware code is original and manually typed.
 
## Possible future plans:
   - [ ] Implement a point system for upvoting/downvoting posts and comments that tracks whether a user has already voted on a particular post or comment.
   - [ ] For the search feature, make the query show up in bold in all instances of it in the posts/comments that contain it.