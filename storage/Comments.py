import sqlite3

def makeComment(ID, body, points, date, uname):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    I = ID
    B = body
    P = points
    D = date
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
