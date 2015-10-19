from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import csv
import utils
import Login
import Register
import Posts
import Comments

app = Flask(__name__)


conn = sqlite3.connect("backend")
c = conn.cursor()

@app.route("/", methods=["GET","POST"])

@app.route("/home", methods=["GET","POST"])
def home():
    coms = []
    for i in Posts.retrievePost():
        if len(Comments.retrieveComments(i[2])) != 0:
            coms.append(Comments.retrieveComments(i[2]))
    if request.method == "POST":
        #if doing a search
        if 'search' in request.form:
            postswithquery = []
            for i in Posts.retrievePost():
                if request.form['query'] in i[0] or request.form['query'] in i[1]:
                    postswithquery.append(i)
            for z in coms:
                for x in z:
                    if request.form['query'] in x[1]:
                        tempbool = True
                        #checks if the post the comment belongs to has already independently been added to posts.
                        for a in postswithquery:
                            if a[2] == x[0]:
                                tempbool = False
                        if(tempbool):
                            for i in Posts.retrievePost():
                                if i[2] == x[0]:
                                    postswithquery.append(i)
            return render_template("searchresults.html", LOGGEDIN = session['user'], POSTS = postswithquery, COMMENTS = coms, QUERY = request.form['query'])
        #all other POST requests require a login.
        elif "loggedin" not in session or session["loggedin"] == False:
            return redirect(url_for("home"))
        else:
            if 'submitcomment' in request.form:
                for i in Posts.retrievePost():
                    if str(i[2]) in request.form:
                        Comments.makeComment(i[2], request.form[str(i[2])], session['user']) 
                        return redirect(url_for("home"))
                    #return render_template("home.html", LOGGEDIN = value, POSTS = Posts.retrievePost())
                return render_template("home.html", LOGGEDIN = session['user'], POSTS = Posts.retrievePost(), COMMENTS = coms)
            elif 'submitpost' not in request.form:
                for i in Posts.retrievePost():
                    if str(i[2]) in request.form:
                        Posts.deletePost(i[2])
                        Comments.deleteComments(i[2])
                        return render_template("home.html", LOGGEDIN = session['user'], POSTS = Posts.retrievePost(), COMMENTS = coms)
                    #return render_template("home.html", LOGGEDIN = value, POSTS = Posts.retrievePost())
                return render_template("home.html", LOGGEDIN = session['user'], POSTS = Posts.retrievePost(), COMMENTS = coms)
            else:
                title = request.form['title']
                cont = request.form['cont']
                button = request.form['submitpost']
    	        Posts.makePost(title, cont, session['user'])
                return render_template("home.html", LOGGEDIN = session['user'], POSTS = Posts.retrievePost(), COMMENTS = coms)
    else:
        if "loggedin" not in session:
            session["loggedin"] = False
        if 'loggedin' in session and 'user' in session and session["loggedin"]:
		    return render_template("home.html", LOGGEDIN = session['user'], POSTS = Posts.retrievePost(), COMMENTS = coms)
        else:
		    return render_template("home.html", POSTS = Posts.retrievePost(), COMMENTS = coms)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if "loggedin" not in session:
        session["loggedin"] = False
    if request.method=="GET":
        return render_template("login.html")
    else:
        uname = request.form['user']
        passw = request.form['pass']
        button = request.form['button']
        if Login.Login(uname, passw):
            session["loggedin"] = True
            session['user'] = uname
            return redirect(url_for("home"))
        else:
            return render_template("login.html", NOTLOGGEDIN = "Error: Wrong username or password.")  

@app.route("/logout")
def logout():
    session["loggedin"] = False
    return redirect(url_for("home"))
			
@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    else:
        if request.form['pass'] != request.form['confirmpass']:
            return render_template("signup.html", NOTLOGGEDIN = "Error: 'Password' and 'Confirm Password' do not match.")
        elif len(request.form['user']) < 4 or len(request.form['pass']) < 8:
            return render_template("signup.html", NOTLOGGEDIN = "Error: 'Username' must be at least 4 characters and 'Password' must be at least 8 characters.")
        else: 
            uname = request.form['user']
            passw = request.form['pass']
            button = request.form['button']			
            if Register.Register(uname, passw):
                return redirect(url_for("login"))
            else:
                return render_template("signup.html", NOTLOGGEDIN = "Error: Username already exists")

@app.route("/myaccount")
def myaccount():
    if 'loggedin' in session and 'user' in session and session["loggedin"]:
		return render_template("myaccount.html", LOGGEDIN = session['user'])
    else:
		return(render_template("myaccount.html"))
		
@app.route("/about")
def about():
    if 'loggedin' in session and 'user' in session and session["loggedin"]:
		return render_template("about.html", LOGGEDIN = session['user'])
    else:
		return(render_template("about.html"))


if __name__== "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0',port=8000)
