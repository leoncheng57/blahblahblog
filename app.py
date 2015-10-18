from flask import Flask, render_template,request, session,redirect, url_for
import sqlite3
import csv
import utils

app = Flask(__name__)


conn = sqlite3.connect("backend")
c = conn.cursor()

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])

def home():
    return render_template("home.html")
    if request.method == "POST":
    	return(render_template("home.html"))
    else:

    	post = request.form['post']
    	utils.add_post("r", post, 4, 4, "a")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__== "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
