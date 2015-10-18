import csv
import sqlite3
import datetime
import time

def Register(username, password, ID):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    uname = username
    pword = password
    blah = ID
    params = (uname, pword, blah)
    c.execute("INSERT INTO users VALUES(?,?,?)", params)
    conn.commit()



def add_post(title, body, id, points, user):
	conn = sqlite3.connect("blog.db")
	c = conn.cursor()
	Title = title
	Body = body
	ID = id
	p = points
	d = str(datetime.date.today())
	user = user
	params = (Title, Body, ID, p, d, user)
	q = ("INSERT INTO posts VALUES(?,?,?,?,?,?,?)", params)
	c.execute(q)
	conn.commit()