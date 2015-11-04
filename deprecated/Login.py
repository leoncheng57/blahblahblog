import sqlite3

def Login(username, password):
    conn = sqlite3.connect("backend")
    c = conn.cursor()
    uname = username
    pword = password
    params = (uname, pword)
    c.execute('SELECT * FROM users WHERE username=? and password=?', params)
    check = c.fetchall()
    return correct_login(check)


def correct_login(blah):
    if blah:
        return True
    else:
        return False
