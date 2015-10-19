import sqlite3
import time

def makeComment(ID, body, uname):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    I = ID
    B = body
    P = 0
    D = time.strftime("%x %X")
    U = uname
    params = (I, B, P, D, U)
    c.execute("INSERT INTO comments VALUES(?,?,?,?,?)", params)
    conn.commit()

def retrieveComments(ID):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    TEMPLATE = "SELECT * FROM comments WHERE postID=%s;"
    I = ID
    q = TEMPLATE%I
    c.execute(q)
    comments = c.fetchall()
    print(comments)
