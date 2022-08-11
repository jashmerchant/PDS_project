import sqlite3
import re
dataBasePath = "database.db"

# regex expressions for validations
email_reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
password_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

def login(username, password):

    login_query = f"""
        login query
        {username} {password}
    """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    cursor.execute(login_query)

def register(username, password):
    if not re.fullmatch(email_reg, username):
        return False
    pat = re.compile(password_reg)
    # searching regex
    mat = re.search(pat, password)
    if not mat:
        return False
    register_query = f"""INSERT INTO “users” VALUES ({username},{password}); """
    connection = sqlite3.connect(dataBasePath)
    cursor = connection.cursor()
    cursor.execute(register_query)
    return True



class Users:
    def __init__(self):
        self.cust_id = 6
        self.emp_id = 100
    def register(self, username, password, cust_type):
        if not re.fullmatch(email_reg, username):
            return False
        pat = re.compile(password_reg)
        # searching regex
        mat = re.search(pat, password)
        if not mat:
            return False
        if cust_type == 'C':
            user_id = self.cust_id
            self.cust_id += 1
        else:
            user_id = self.emp_id
            self.emp_id += 100
        register_query = f"""INSERT INTO “users” VALUES ({user_id},{username},{password}, {cust_type}); """
        connection = sqlite3.connect(dataBasePath)
        cursor = connection.cursor()
        cursor.execute(register_query)
        return True


username, password = "abc@gmail.com", "Bhargav@56223"



users = Users()

print(users.register(username, password, 'C'))
