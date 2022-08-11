import sqlite3

dataBasePath = "database.db"

def login(username, password):

    login_query = f"""
        login query
        {username} {password}
    """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    cursor.execute(login_query)

def register(username, password):
    register_query = f"""INSERT INTO “users” VALUES ({username},{password}); """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    cursor.execute(register_query)