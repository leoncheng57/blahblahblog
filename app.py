from flask import Flask, render_template, request, session, redirect, url_for
import Login, Register, Posts, Comments, utils
import sqlite3, csv

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
def home():
    # Preliminary sets that I don't like and think should probably be removed.
    if 'user' not in session:
        session['user'] = None
    if "loggedin" not in session:
        session["loggedin"] = False
    # End sets.
    comments = [] # I also don't yet understand the need for distinct POSTS and COMMENTS lists.
    for post in Posts.retrievePost(): # Comment retrieval.
        if len(Comments.retrieveComments(post[2])) != 0: 
            comments.append(Comments.retrieveComments(post[2]))
    if request.method == "POST":
        # Maybe add an author search too...
        # Actually, how are mongodb's builtin search capabilities?
        if 'search' in request.form: # This statement could be optimized...
            return render_template(
                "searchresults.html",
                LOGGEDIN = session['user'],
                POSTS = utils.search(request.form['query'], comments),
                COMMENTS = comments,
                QUERY = request.form['query'])
        #all other POST requests require a login.
        if session['user'] == None or session["loggedin"] == False:
            return redirect('/')
        # Short-circuit evaluation for the win!
        if 'submitcomment' in request.form: # Really, the use of the 'in' keyword here bugs me...
            for post in Posts.retrievePost():
                if str(post[2]) in request.form:
                    Comments.makeComment(
                        post[2],
                        request.form[str(post[2])],
                        session['user']) 
                    return redirect(url_for("home"))
            return render_template(
                "home.html",
                LOGGEDIN = session['user'],
                POSTS = Posts.retrievePost(),
                COMMENTS = comments)
        if 'submitpost' not in request.form: # Well that's one [very backwards] way of doing it...
            for post in Posts.retrievePost():
                if str(post[2]) in request.form:
                    Posts.deletePost(post[2])
                    Comments.deleteComments(post[2]) # This should probably be built in to deletePost()
                    return render_template(
                        "home.html",
                        LOGGEDIN = session['user'],
                        POSTS = Posts.retrievePost(),
                        COMMENTS = comments)
            return render_template(
                "home.html",
                LOGGEDIN = session['user'],
                POSTS = Posts.retrievePost(),
                COMMENTS = comments) # Just noticed, this is not DRY in the *least*.
        title = request.form['title']
        cont = request.form['cont']
        Posts.makePost(title, cont, session['user'])
        return render_template(
            "home.html",
            LOGGEDIN = session['user'],
            POSTS = Posts.retrievePost(),
            COMMENTS = comments)
    if session['user'] != None and session["loggedin"]:
	    return render_template(
	        "home.html",
	        LOGGEDIN = session['user'],
	        POSTS = Posts.retrievePost(),
	        COMMENTS = comments)
    # The fact that it's necessary to make this return distinction is a bit weird.
    # Why don't we let Jinja handle it? Wait... doesn't it already...? Technically?
    # Ugh -_-
    return render_template(
        "home.html",
        POSTS = Posts.retrievePost(),
        COMMENTS = comments)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if 'user' not in session:
        session['user'] = None
    if 'loggedin' not in session:
        session['loggedin'] = False
    if request.method=='GET':
        return render_template("login.html")
    uname = request.form['user']
    passw = request.form['pass']
    button = request.form['button']
    if Login.Login(uname, passw):
        session["loggedin"] = True
        session['user'] = uname
        return redirect(url_for("home"))
    return render_template("login.html", NOTLOGGEDIN = "Error: Wrong username or password.")  

@app.route("/logout/")
def logout():
    session['loggedin'] = False
    session['user'] = None
    return redirect('/')
			
@app.route("/terms/")
def terms():
    return render_template("terms.html")

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    if request.form['pass'] != request.form['confirmpass']:
        return render_template("signup.html", NOTLOGGEDIN = "Error: 'Password' and 'Confirm Password' do not match.")
    if len(request.form['user']) < 4 or len(request.form['pass']) < 8:
        return render_template("signup.html", NOTLOGGEDIN = "Error: 'Username' must be at least 4 characters and 'Password' must be at least 8 characters.")
    username = request.form['user']
    password = request.form['pass']
    button = request.form['button']			
    if Register.Register(username, password):
        return redirect(url_for("login"))
    return render_template("signup.html", NOTLOGGEDIN = "Error: Username already exists")

@app.route("/myaccount/")
def myaccount():
    if 'loggedin' in session and 'user' in session and session["loggedin"]:
        return render_template("myaccount.html", LOGGEDIN = session['user'])
    return(render_template("myaccount.html"))
		
@app.route("/about/")
def about():
    if 'loggedin' in session and 'user' in session and session['loggedin']:
        # No, see, this check shouldn't ve necessary. It should be coded the same regardless.
        return render_template("about.html", LOGGEDIN = session['user'])
    return(render_template("about.html"))


if __name__== "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
