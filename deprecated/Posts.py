import sqlite3
import time

def makePost(title, body, uname):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    T = title
    B = body
    I = getNextPostID()
    P = 0
    D = time.strftime("%x %X")
    U = uname
    params = (T, B, I, P, D, U)
    c.execute("INSERT INTO posts VALUES(?,?,?,?,?,?)", params)
    conn.commit()

def retrievePost():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute('SELECT * FROM posts')
    posts = c.fetchall()[::-1]
    return posts

def getNextPostID():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY ID ASC")
    ALL = c.fetchall()
    last = ALL[-1][2] + 1 #go to last entry, second element of list, then add 1
    return last
	
def deletePost(ID):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    #query = "DELETE FROM posts WHERE ID='" + ID + "';"
    c.execute("DELETE FROM posts WHERE ID=?", (ID,))
    conn.commit()
    conn.close()
