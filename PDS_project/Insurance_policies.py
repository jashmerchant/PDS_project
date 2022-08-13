import sqlite3
dataBasePath="database.db"

class Insurance_policies:
     def __init__(self):
          connection = sqlite3.connect(dataBasePath)
          cursor = connection.cursor()
          self.max_policy_id = cursor.execute("""SELECT MAX(policy_id) FROM INSURANCE;""").fetchone()[0] +1
          connection.close()

     def get_client_insurances(self, cid, insurance_type):
          """
          :param cid: customer id
          :param insurance_type: auto or home
          :return:
          """
          query = """SELECT c.policy_id, c.premium, c.end_date
                     FROM CUST_INSURANCE a JOIN INSURANCE b on a.policy_id = b.policy_id JOIN """+insurance_type+"""_INSURANCE c ON b.policy_id=c.policy_id
                     WHERE cid="""+str(cid)+";"
          connection = sqlite3.connect(dataBasePath)
          cursor = connection.cursor()
          res = cursor.execute(query).fetchall()
          return res

     def add_auto_insurance_to_db(self, vin, start_date, end_date, premium, status):
          try:
               policy_id = self.max_policy_id
               connection = sqlite3.connect(dataBasePath)
               cursor = connection.cursor()
               query = f"""INSERT into AUTO_INSURANCE values (
                         {policy_id},{vin},{start_date},{end_date},{premium},{status} );"""
               cursor.execute(query)
               self.max_policy_id+=1
               return True
          except:
               return False

     def add_home_insurance_to_db(self, HID, start_date, end_date, premium, status):
          try:
               policy_id = self.max_policy_id
               connection = sqlite3.connect(dataBasePath)
               cursor = connection.cursor()
               query = f"""INSERT into AUTO_INSURANCE values (
                         {policy_id},{HID},{start_date},{end_date},{premium},{status} );"""
               cursor.execute(query)
               self.max_policy_id+=1
               return True
          except:
               return False

ins = Insurance_policies()
print(ins.get_client_insurances(1, "home"))