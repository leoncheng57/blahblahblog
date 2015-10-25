import sqlite3


def Register(username, password):
    if checkAvail(username):
        conn = sqlite3.connect("backend")
        c = conn.cursor()
        uname = username
        pword = password
        blah = getNextID()
        params = (uname, pword, blah)
        c.execute("INSERT INTO users VALUES(?,?,?)", params)
        conn.commit()
        return True
    else:
        return False

#TODO: remove getNextID
def getNextID():
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    c.execute("SELECT * FROM users ORDER BY ID ASC")
    ALL = c.fetchall()
    last = ALL[-1][-1] + 1
    return last

def checkAvail(username):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    uname = (username,)
    c.execute("SELECT * FROM users WHERE username = ?;", uname)
    ret = c.fetchall()
    if ret:
        return False
    else:
        return True
    
