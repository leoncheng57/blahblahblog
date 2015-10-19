import sqlite3

def makePost(title, body, date, uname):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    T = title
    B = body
    I = getNextPostID()
    P = 0
    D = date
    U = uname
    params = (T, B, I, P, D, U)
    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)", params)
    conn.commit()

def retrievePost():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()
    return posts

def getNextPostID():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY ID ASC")
    ALL = c.fetchall()
    last = ALL[-1][2] + 1
    return last
