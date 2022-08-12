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
        register_query = f"""INSERT INTO users VALUES ({user_id},\"{username}\",\"{password}\", \"{cust_type}\"); """
        print(register_query)
        connection = sqlite3.connect(dataBasePath)

        cursor = connection.cursor()
        cursor.execute(register_query)
        connection.commit()
        return True


username, password = "abc@gmail.com", "Bhargav@56223"



users = Users()

print(users.register(username, password, 'C'))