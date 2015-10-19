from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import csv
import utils
import Login
import Register

app = Flask(__name__)


conn = sqlite3.connect("backend")
c = conn.cursor()

@app.route("/", methods=["GET","POST"])

@app.route("/home", methods=["GET","POST"])
def home():
    if "loggedin" not in session:
        session["loggedin"] = False
    if 'loggedin' in session and 'user' in session and session["loggedin"]:
		return render_template("home.html", LOGGEDIN = session['user'])
    else:
		return(render_template("home.html"))
    if request.method == "POST":
    	return(render_template("home.html"))
    else:

    	post = request.form['post']
    	utils.add_post("r", post, 4, 4, "a")

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
