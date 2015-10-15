from flask import Flask, render_template, session, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")


if __name__== "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
