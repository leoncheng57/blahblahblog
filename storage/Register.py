import sqlite3




def Register(username, password, ID):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    uname = username
    pword = password
    blah = ID
    params = (uname, pword, blah)
    c.execute("INSERT INTO users VALUES(?,?,?)", params)
    conn.commit()
