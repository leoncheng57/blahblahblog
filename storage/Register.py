import sqlite3

conn = sqlite3.connect("backend.db")
c = conn.cursor()

def Register(username, password, ID):
    uname = username
    pword = password
    blah = ID
    TEMPLATE = "INSERT INTO users VALUES (%s,%s,%s)"
    q = TEMPLATE%(uname, pword, blah)
    c.execute(q)


conn.commit()
