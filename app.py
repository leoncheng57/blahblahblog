from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("home.html")
