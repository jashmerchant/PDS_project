from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import app as original_app
from flask_bcrypt import Bcrypt
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


users = [
        ['rossBennett','RossBennett@gmail.com','12345'],
        ['joCastillo','JoCastillo@gmail.com','12345'],
        ['wendyKelly','WendyKelly@gmail.com','12345'],
        ['sheilaRobinson','SheilaRobinson@gmail.com','12345'],
        ['ronnie', 'ronnie@gmail.com', '12345'],
        ['admin', 'merchantjash@gmail.com', 'admin']
        ]

customers = [
        [1,'Ross','Bennett','872 Learn st','Williamsport',17701,'M','S'],
        [2,'Jo','Castillo','7933 Mcclellan Rd','Champaign',61821,'F','W'],
        [3,'Wendy','Kelly','2675 Harrison Ct','Baltimore',21206,'F','S'],
        [4,'Sheila','Robinson','3524 Frances Ct','Montclair',17042,'F','S'],
        [5,'Ronnie','Caldwell','2230 Oak Lawn Ave','Hyde Park',12136,'M','M'],
        # [6,'Sofia','Wade','18 Learn st','Roanoke',24012,'F','S'],
        # [7,'Ashley','Rodriguez','1141 W Belt Line Rd','Palos Verdes Peninsula',90274,'F','S'],
        # [8,'Isobel','Williams','262 Poplar Dr','Lebanon',17042,'F','S'],
        # [9,'Harold','Powell','2694 Valwood Pkwy','Westlake',44145,'M','M'],
        # [10,'Jane','Knight','5755 Hickory Creek Dr','Pelham',35124,'F','M'],
        # [11,'Scott','Johnson','53 Pockrus Page Rd','Graham',27253,'M','M'],
        # [12,'Daniel','Cook','1124 Valwood Pkwy','Cumming',30040,'M','S'],
        # [13,'Terrence','Watts','7013 Fairview St','Lacey',98503,'M','S'],
        # [14,'Mike','Fletcher','8120 Avondale Ave','Addison',60101,'M','S'],
        # [15,'Emily','Russell','8807 E Center St','Tacoma',98444,'F','S'],
        # [16,'Dan','Ferguson','4960 Edwards Rd','Lakeland',33801,'M','M'],
        # [17,'Clara','Sims','5689 Daisy Dr','Nazareth',18064,'M','S'],
        # [18,'Denise','Burke','9124 Hunters Creek Dr','Beckley',25801,'F','S'],
        # [19,'Violet','Robertson','1183 Ash Dr','Leesburg',20175,'F','M'],
        # [20,'Jim','Robinson','2684 Daisy Dr','Homestead',33030,'M','S'],
        # [21,'Ronnie','Jordan','8477 Hogan St','Sun City',85351,'M','S'],
        # [22,'Lily','Vasquez','Learn st','Stuart',34997,'F','S'],
        # [23,'Esther','Webb','9143 Stevens Creek Blvd','Woburn',11801,'F','S'],
        # [24,'Enrique','Lawson','7010 Groveland Terrace','Tuckerton',28087,'M','S'],
        # [25,'Ana','Williamson','3291 Locust Rd','Franklin',22038,'F','M']
        ]

customer_insurance =[
        [101,1],
        [102,2],
        [103,3],
        [104,4],
        [105,5],
        # [106,6],
        # [107,7],
        # [108,8],
        # [109,9],
        # [110,10],
        # [111,11],
        # [112,12],
        # [113,13],
        # [114,14],
        # [115,15],
        # [116,16],
        # [117,17],
        # [118,18],
        # [119,19],
        # [120,20],
        # [121,21],
        # [122,22],
        # [123,23],
        # [124,24],
        # [125,25],
        # [126,6],
        # [127,7],
        # [128,14],
        # [129,14],
        # [130,18]
        ]

insurance = [
        [101,'H'],
        [102,'A'],
        [103,'H'],
        [104,'A'],
        [105,'H'],
        # [106,'A'],
        # [107,'H'],
        # [108,'H'],
        # [109,'A'],
        # [110,'H'],
        # [111,'A'],
        # [112,'H'],
        # [113,'A'],
        # [114,'H'],
        # [115,'A'],
        # [116,'A'],
        # [117,'H'],
        # [118,'A'],
        # [119,'H'],
        # [120,'A'],
        # [121,'H'],
        # [122,'A'],
        # [123,'H'],
        # [124,'H'],
        # [125,'A'],
        # [126,'H'],
        # [127,'A'],
        # [128,'H'],
        # [129,'A'],
        # [130,'H']
        ]

auto_insurance = [
        [102, 'JH4KA4551KC003961', datetime.datetime.now(), datetime.datetime.now(), 223.64, 'C'],
        [104, 'WP0AA2991YS620631', datetime.datetime.now(), datetime.datetime.now(), 500.02, 'P'],
        # [106, '1HGCP263X8A035447', datetime.datetime.now(), datetime.datetime.now(), 1601.11, 'C'],
        # [109, 'JH4KA8260MC000458', datetime.datetime.now(), datetime.datetime.now(), 133.43, 'P'],
        # [111, '1G8DC18H4CF114023', datetime.datetime.now(), datetime.datetime.now(), 609.74, 'C'],
        # [113, '1P3XP48K6LN273071', datetime.datetime.now(), datetime.datetime.now(), 212.12, 'C'],
        # [115, '1FAFP52UXXA197384', datetime.datetime.now(), datetime.datetime.now(), 873.43, 'C'],
        # [116, '4S3BJ6329M1918965', datetime.datetime.now(), datetime.datetime.now(), 687.78, 'C'],
        # [118, 'JTDBE30K620061417', datetime.datetime.now(), datetime.datetime.now(), 189.33, 'C'],
        # [120, 'JN8AS1MU0CM120061', datetime.datetime.now(), datetime.datetime.now(), 2543.32, 'C'],
        # [122, '4F2CU08102KM50866', datetime.datetime.now(), datetime.datetime.now(), 982.15, 'C'],
        # [125, 'LM4AC113061105688', datetime.datetime.now(), datetime.datetime.now(), 982.15, 'C'],
        # [127, '1FVAF3CV84DM31815', datetime.datetime.now(), datetime.datetime.now(), 189.33, 'P'],
        # [129, 'JH4KA4650JC000403', datetime.datetime.now(), datetime.datetime.now(), 2105.50, 'C'],
        # [129, 'JH4DA1842JS003823', datetime.datetime.now(), datetime.datetime.now(), 686.66, 'C'],
        # [129, 'YV1MS672892447094', datetime.datetime.now(), datetime.datetime.now(), 521.75, 'P'],
        [102, 'JH4DA3450JS001899', datetime.datetime.now(), datetime.datetime.now(), 445.89, 'C'],
        # [118, '1B4GP45R6WB718087', datetime.datetime.now(), datetime.datetime.now(), 2888.10, 'C'],
        # [118, '1GTEK19RXVE536195', datetime.datetime.now(), datetime.datetime.now(), 145.50, 'C'],
        # [111, '3B7HF13Y81G193584', datetime.datetime.now(), datetime.datetime.now(), 1623.15, 'C'],
        [104, 'WVWAF93D258002461', datetime.datetime.now(), datetime.datetime.now(), 455.55, 'C'],
        [104, '1FV3GFBC0YHA74039', datetime.datetime.now(), datetime.datetime.now(), 198.75, 'C'],
        [102, '3VWSB81H8WM210368', datetime.datetime.now(), datetime.datetime.now(), 75.30, 'C'],
        # [111, '1FVACYDC37HW59012', datetime.datetime.now(), datetime.datetime.now(), 896.52, 'C'],
        # [111, '1FTJW36F2TEA03179', datetime.datetime.now(), datetime.datetime.now(), 750.0, 'P'],
        # [125, '1FUJA6CV74DM34063', datetime.datetime.now(), datetime.datetime.now(), 609.09, 'C'],
        # [127, 'JTLKE50E191068256', datetime.datetime.now(), datetime.datetime.now(), 795.85, 'C'],
        # [127, 'ZAMBC38A450014565', datetime.datetime.now(), datetime.datetime.now(), 1513.50, 'C'],
        # [118, '5GZEV337X7J141405', datetime.datetime.now(), datetime.datetime.now(), 333.25, 'C']
        ]

home_insurance =[
        [101, 8274870194, datetime.datetime.now(), datetime.datetime.now(), 223.64, 'C'],
        [101, 6040047612, datetime.datetime.now(), datetime.datetime.now(), 500.02, 'P'],
        [103, 6110382967, datetime.datetime.now(), datetime.datetime.now(), 1601.11, 'C'],
        [105, 5155334165, datetime.datetime.now(), datetime.datetime.now(), 133.43, 'P'],
        [105, 1510876130, datetime.datetime.now(), datetime.datetime.now(), 609.74, 'C'],
        # [107, 1653192697, datetime.datetime.now(), datetime.datetime.now(), 212.12, 'C'],
        # [108, 8190022816, datetime.datetime.now(), datetime.datetime.now(), 873.43, 'C'],
        # [108, 1177406054, datetime.datetime.now(), datetime.datetime.now(), 687.78, 'C'],
        # [110, 8794014691, datetime.datetime.now(), datetime.datetime.now(), 189.33, 'C'],
        # [112, 9491123506, datetime.datetime.now(), datetime.datetime.now(), 2543.32, 'C'],
        # [114, 4803249101, datetime.datetime.now(), datetime.datetime.now(), 982.15, 'C'],
        # [117, 7386832621, datetime.datetime.now(), datetime.datetime.now(), 982.15, 'C'],
        # [119, 8968421088, datetime.datetime.now(), datetime.datetime.now(), 189.33, 'P'],
        # [121, 5584316830, datetime.datetime.now(), datetime.datetime.now(), 2105.50, 'C'],
        # [123, 1889246262, datetime.datetime.now(), datetime.datetime.now(), 686.66, 'C'],
        # [124, 4894121408, datetime.datetime.now(), datetime.datetime.now(), 521.75, 'P'],
        # [126, 9645655435, datetime.datetime.now(), datetime.datetime.now(), 445.89, 'C'],
        # [128, 5695603761, datetime.datetime.now(), datetime.datetime.now(), 2888.10, 'C'],
        # [130, 3335510137, datetime.datetime.now(), datetime.datetime.now(), 145.50, 'C'],
        # [130, 8718951280, datetime.datetime.now(), datetime.datetime.now(), 1623.15, 'C'],
        # [130, 8690937663, datetime.datetime.now(), datetime.datetime.now(), 455.55, 'C'],
        [101, 2933651928, datetime.datetime.now(), datetime.datetime.now(), 198.75, 'C'],
        # [114, 7355546679, datetime.datetime.now(), datetime.datetime.now(), 75.30, 'C'],
        # [119, 6246892852, datetime.datetime.now(), datetime.datetime.now(), 896.52, 'C'],
        # [114, 2078102300, datetime.datetime.now(), datetime.datetime.now(), 750.0, 'P'],
        # [128, 4518817008, datetime.datetime.now(), datetime.datetime.now(), 609.09, 'C'],
        # [130, 9845445669, datetime.datetime.now(), datetime.datetime.now(), 795.85, 'C'],
        # [114, 7137708216, datetime.datetime.now(), datetime.datetime.now(), 1513.50, 'C'],
        # [130, 5990598804, datetime.datetime.now(), datetime.datetime.now(), 762.40, 'C'],
        # [126, 3120205778, datetime.datetime.now(), datetime.datetime.now(), 333.25, 'C']
        ]

def add_user(u):
    hashed_password = bcrypt.generate_password_hash(u[2])
    new_user = original_app.User(username=u[0], email=u[1], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

def add_customer(c):
    new_customer = original_app.Customer(cid=c[0], first_name=c[1], last_name=c[2],\
                                         street=c[3], city=c[4], zipcode=c[5], gender=c[6], marital_status=c[7])
    db.session.add(new_customer)
    db.session.commit()

def add_customer_insurance(ci):
    new_customer_insurance = original_app.CustomerInsurance(policy_id=ci[0], cid=ci[1])
    db.session.add(new_customer_insurance)
    db.session.commit()

def add_insurance(i):
    new_insurance = original_app.Insurance(policy_id=i[0], policy_type=i[1])
    db.session.add(new_insurance)
    db.session.commit()

def add_home_insurance(i):
    new_home_insurance = original_app.HomeInsurance(policy_id=i[0], hid=i[1], \
                                                    start_date=i[2], end_date=i[3], premium=i[4], status=i[5])
    db.session.add(new_home_insurance)
    db.session.commit()

def add_auto_insurance(i):
    new_auto_insurance = original_app.AutoInsurance(policy_id=i[0], vin=i[1],\
                                        start_date=i[2], end_date=i[3], premium=i[4], status=i[5])
    db.session.add(new_auto_insurance)
    db.session.commit()


for u in users:
    try:
        add_user(u)
    except:
        pass

for c in customers:
    try:
        add_customer(c)
    except:
        pass

for ci in customer_insurance:
    try:
        add_customer_insurance(ci)
    except:
        pass

for i in insurance:
    try:
        add_insurance(i)
    except:
        pass

for i in home_insurance:
    try:
        add_home_insurance(i)
    except:
        pass

for i in auto_insurance:
    try:
        add_auto_insurance(i)
    except:
        pass