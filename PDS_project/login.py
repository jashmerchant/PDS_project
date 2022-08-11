import sqlite3

dataBasePath = "database.db"

def login(username, password):
    access = "denied"
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    login_query = "SELECT password FROM users WHERE email="+"\'"+username+"\';"
    expected_password = cursor.execute(login_query).fetchone()
    if (expected_password == None):
        return "not found"
    if expected_password[0] == password:
        access = "granted"
    connection.close()
    return access

def register(username, password):
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    existing_email = cursor.execute("SELECT email FROM users WHERE email="+"\'"+username+"\';").fetchone()
    if (existing_email):
        return False
    _id = max(cursor.execute("""SELECT uid from users;""").fetchall())[0]+1
    register_query = "INSERT INTO users VALUES ("+str(_id)+",\'"+username+"\',\'"+password+"\', +'C'); "
    cursor.execute(register_query)
    connection.commit()
    cursor.close()
    connection.close()
    return True