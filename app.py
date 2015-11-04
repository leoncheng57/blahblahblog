from flask import Flask, render_template, request, session, redirect, url_for
import Login, Register, Posts, Comments, utils
import sqlite3, csv

app = Flask(__name__)

def check_user():
    if 'user' not in session:
        session['user'] = None

@app.route("/", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
def home():
    check_user()
    comments = []
    posts = Posts.retrievePost()
    query = None
    error = None
    for post in posts: # Comment retrieval.
        if len(Comments.retrieveComments(post[2])) != 0: 
            comments.append(Comments.retrieveComments(post[2]))
    if request.method == "POST": # If a POST request is received...
        if session['user'] == None: # If the user is not signed in...
            if 'search' in request.form: # If the user is performing a search...
                posts = utils.search(request.form['query'], posts, comments)
                query = request.form['query']
            else: # Otherwise, send them back to home... (should give an error as well)
                error = "Sorry! You need to be signed in to do that."
        else:
            if 'submitcomment' in request.form:
                for post in posts:
                    if str(post[2]) in request.form:
                        Comments.makeComment(
                            post[2],
                            request.form[str(post[2])],
                            session['user']) 
                        return redirect('/')
            if 'submitpost' not in request.form: # Well that's one [very backwards] way of doing it...
                for post in Posts.retrievePost():
                    if str(post[2]) in request.form: # OH IS THIS WHY?! Ugh.
                        Posts.deletePost(post[2])
                        Comments.deleteComments(post[2]) # This should probably be built in to deletePost()
            else:
                title = request.form['title']
                cont = request.form['cont']
                Posts.makePost(title, cont, session['user'])
    return render_template(
        "home.html",
        LOGGEDIN = session['user'],
        POSTS = Posts.retrievePost(),
        COMMENTS = comments,
        QUERY = query,
        ERROR = error)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    check_user()
    error = None
    if request.method == 'POST':
        if Login.Login(request.form['user'], request.form['pass']):
            session['user'] = request.form['user']
            return redirect('/')
        else:
            error = "Error: Wrong username or password."
    return render_template("accounts.html", NOTLOGGEDIN = error)

@app.route("/logout/")
def logout():
    session['user'] = None
    return redirect('/')

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    check_user()
    error = None
    if request.method=="POST":
        username = request.form['user']
        password = request.form['pass']
        if len(username) < 4 or len(password) < 8:
            error = "Error: Username must be at least 4 characters and password must be at least 8 characters."
        elif password != request.form['confirmpass']:
            error = "Error: Passwords do not match."
        else:
            if not Register.Register(username, password):
                error = "Error: Username already exists."
            else:
                return redirect(url_for('login'))
    return render_template("accounts.html", NOTLOGGEDIN = error, signup = True)

@app.route("/myaccount/")
def myaccount():
    check_user()
    if session['user'] == None:
        return redirect(url_for('login'))
    return render_template("myaccount.html", LOGGEDIN = session['user'])
		
@app.route("/about/")
def about():
    check_user()
    return(render_template("about.html", LOGGEDIN = session['user']))


if __name__== "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
