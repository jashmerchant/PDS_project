import sqlite3

dataBasePath = "database.db"

def login(username, password):
    access = False
    login_query = f"""
        login query
        {username} 
    """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    expected password = cursor.execute(login_query)
    if expected_password == password:
        access = True
    return access

def register(username, password):
    register_query = f"""INSERT INTO users VALUES ({username},{password}); """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    cursor.execute(register_query)