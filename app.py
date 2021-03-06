from flask import Flask, render_template, request, session, redirect, url_for
import posts, users
import sqlite3, csv

app = Flask(__name__)

def check_user():
    if 'user' not in session:
        session['user'] = None
    return session['user']

@app.route("/", methods=["GET","POST"])
@app.route("/home/", methods=["GET","POST"])
@app.route("/index/", methods=["GET", "POST"])
def index():
    if check_user():
        if 'submitpost' in request.form:
            posts.make_post(
                request.form['title'],
                session['user'],
                request.form['content'])
        if 'submitcomment' in request.form:
            posts.make_comment(
                request.form['postid'],
                session['user'],
                request.form['content'])
        if 'deletepost' in request.form:
            posts.delete_post(request.form['postid'])
    return render_template(
        "home.html",
        posts = posts.get_posts(request.args.get('query')),
        user = session['user'],
        query = request.args.get('query'))

@app.route("/login/", methods=['GET', 'POST'])
def login():
    check_user()
    error = None
    if request.method == 'POST':
        if users.login(request.form['user'], request.form['pass']):
            session['user'] = request.form['user']
            return redirect('/index')
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
            if not users.register(username, password):
                error = "Error: Username already exists."
            else:
                return redirect(url_for('login'))
    return render_template("accounts.html", NOTLOGGEDIN = error, signup = True)

@app.route("/myaccount/")
def myaccount():
    user = check_user()
    if user:
        return redirect(url_for('login'))
    return render_template("myaccount.html", LOGGEDIN = user)
		
@app.route("/about/")
def about():
    return(render_template("about.html", LOGGEDIN = check_user()))


if __name__== "__main__":
    app.debug = True
    app.secret_key = "Password"
    app.run(host='0.0.0.0', port=8000)
