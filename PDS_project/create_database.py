import sqlite3

dataBasePath = "database.db"

def run_array_of_instructions(s):
    g = s.replace("\n","").split(";")
    for l in g:
        #print(l)
        cursor.execute(l+";")

connection = sqlite3.connect(dataBasePath)
cursor = connection.cursor()

create_user_table_query = '''CREATE TABLE users (
    uid INTEGER NOT NULL,
	email VARCHAR2(17) NOT NULL,
	password VARCHAR2(17) NOT NULL,
    user_type CHAR(1) NOT NULL);'''

create_auto_insurance_table_query='''CREATE TABLE auto_insurance (
    policy_id  NUMBER(12) NOT NULL,
    vin        VARCHAR2(17) NOT NULL,
    start_date DATE NOT NULL,
    end_date   DATE NOT NULL,
    premium    NUMBER(6, 2) NOT NULL,
    status     CHAR(1)
);'''

create_customer_table_query="""CREATE TABLE cust (
    cid            NUMBER(8) NOT NULL,
    first_name     VARCHAR2(30) NOT NULL,
    last_name      VARCHAR2(30) NOT NULL,
    street         VARCHAR2(40) NOT NULL,
    city           VARCHAR2(40) NOT NULL,
    zipcode        NUMBER(5) NOT NULL,
    gender         CHAR(1),
    marital_status CHAR(1) NOT NULL,
    cust_type      CHAR(1) 
);"""

create_customer_insurance_query="""CREATE TABLE cust_insurance (
    policy_id NUMBER(12) NOT NULL,
    cid       NUMBER(8) NOT NULL
);"""

create_table_driver_query="""CREATE TABLE driver (
    dln        NUMBER(8) NOT NULL,
    state      VARCHAR2(2) NOT NULL,
    first_name VARCHAR2(30) NOT NULL,
    last_name  VARCHAR2(30) NOT NULL,
    dob        DATE NOT NULL
);"""

create_table_home_query="""CREATE TABLE home (
    hid            NUMBER(10) NOT NULL,
    purchase_date  DATE NOT NULL,
    purchase_value NUMBER(9) NOT NULL,
    area           NUMBER(6) NOT NULL,
    home_type      CHAR(1) NOT NULL,
    aff            NUMBER(1) NOT NULL,
    hss            NUMBER(1) NOT NULL,
    sp             CHAR(1),
    basement       NUMBER(1) NOT NULL,
    street         VARCHAR2(30) NOT NULL,
    zipcode        NUMBER(5) NOT NULL,
    city           VARCHAR2(30) NOT NULL
);"""

create_table_home_insurance_query="""CREATE TABLE home_insurance (
    policy_id  NUMBER(12) NOT NULL,
    hid        NUMBER(10) NOT NULL,
    start_date DATE NOT NULL,
    end_date   DATE NOT NULL,
    premium    NUMBER(9, 2) NOT NULL,
    status     CHAR(1) NOT NULL
);"""

create_table_insurance_query="""CREATE TABLE insurance (
    policy_id   NUMBER(12) NOT NULL,
    policy_type CHAR(1) NOT NULL
);"""

create_table_invoice_query="""CREATE TABLE invoice (
    inv_num    NUMBER(10) NOT NULL,
    amount     NUMBER(9, 2) NOT NULL,
    due_date   DATE NOT NULL,
    ipolicy_id NUMBER(12)
);"""

create_table_payment_query="""CREATE TABLE payment (
    transaction_id NUMBER(10) NOT NULL,
    inv_num        NUMBER(10),
    paym_date      DATE NOT NULL,
    method         VARCHAR2(6) NOT NULL,
    amount         NUMBER(9, 2) NOT NULL
);"""


create_table_vehicle_query="""CREATE TABLE vehicle (
    vin    VARCHAR2(17) NOT NULL,
    make   VARCHAR2(12) NOT NULL,
    model  VARCHAR2(30) NOT NULL,
    year   NUMBER(4) NOT NULL,
    status CHAR(1)
);"""

create_table_vehcile_driver_query="""CREATE TABLE vehicle_driver (
    vin   VARCHAR2(17) NOT NULL,
    dln   NUMBER(8) NOT NULL,
    state VARCHAR2(2) NOT NULL
);"""



all_queries = [create_user_table_query, create_auto_insurance_table_query, create_customer_table_query, create_customer_insurance_query, \
               create_table_driver_query, create_table_home_query, create_table_home_insurance_query, create_table_insurance_query, \
               create_table_invoice_query, create_table_payment_query,create_table_vehicle_query, create_table_vehcile_driver_query, \
               ]


users = """INSERT INTO users VALUES (1,'RossBennett@gmail.com','12345','C');
INSERT INTO users VALUES (2,'JoCastillo@gmail.com','12345','C');
INSERT INTO users VALUES (3,'WendyKelly@gmail.com','12345','C');
INSERT INTO users VALUES (4,'SheilaRobinson@gmail.com','12345','C');
INSERT INTO users VALUES (5,'RonnieCaldwell@gmail.com','12345','C');
INSERT INTO users VALUES (100,'NikoAdmin@gmail.com','12345','E');
INSERT INTO users VALUES (200,'JashAdmin@gmail.com','12345','E');
INSERT INTO users VALUES (300, 'BarghavAdmin@gmail.com','12345','E');"""

cust ="""INSERT INTO CUST VALUES (1,'Ross','Bennett','872 Learn st','Williamsport',17701,'M','S','A');
INSERT INTO CUST VALUES (2,'Jo','Castillo','7933 Mcclellan Rd','Champaign',61821,'F','W','A');
INSERT INTO CUST VALUES (3,'Wendy','Kelly','2675 Harrison Ct','Baltimore',21206,'F','S','A');
INSERT INTO CUST VALUES (4,'Sheila','Robinson','3524 Frances Ct','Montclair',07042,'F','S','A');
INSERT INTO CUST VALUES (5,'Ronnie','Caldwell','2230 Oak Lawn Ave','Hyde Park',02136,'M','M','A');
INSERT INTO CUST VALUES (6,'Sofia','Wade','18 Learn st','Roanoke',24012,'F','S','A');
INSERT INTO CUST VALUES (7,'Ashley','Rodriguez','1141 W Belt Line Rd','Palos Verdes Peninsula',90274,NULL,'S','A');
INSERT INTO CUST VALUES (8,'Isobel','Williams','262 Poplar Dr','Lebanon',17042,'F','S','A');
INSERT INTO CUST VALUES (9,'Harold','Powell','2694 Valwood Pkwy','Westlake',44145,'M','M','A');
INSERT INTO CUST VALUES (10,'Jane','Knight','5755 Hickory Creek Dr','Pelham',35124,'F','M','A');
INSERT INTO CUST VALUES (11,'Scott','Johnson','53 Pockrus Page Rd','Graham',27253,'M','M','A');
INSERT INTO CUST VALUES (12,'Daniel','Cook','1124 Valwood Pkwy','Cumming',30040,'M','S','A');
INSERT INTO CUST VALUES (13,'Terrence','Watts','7013 Fairview St','Lacey',98503,NULL,'S','A');
INSERT INTO CUST VALUES (14,'Mike','Fletcher','8120 Avondale Ave','Addison',60101,'M','S','A');
INSERT INTO CUST VALUES (15,'Emily','Russell','8807 E Center St','Tacoma',98444,'F','S','A');
INSERT INTO CUST VALUES (16,'Dan','Ferguson','4960 Edwards Rd','Lakeland',33801,'M','M','A');
INSERT INTO CUST VALUES (17,'Clara','Sims','5689 Daisy Dr','Nazareth',18064,'M','S','A');
INSERT INTO CUST VALUES (18,'Denise','Burke','9124 Hunters Creek Dr','Beckley',25801,NULL,'S','A');
INSERT INTO CUST VALUES (19,'Violet','Robertson','1183 Ash Dr','Leesburg',20175,'F','M','H');
INSERT INTO CUST VALUES (20,'Jim','Robinson','2684 Daisy Dr','Homestead',33030,'M','S','A');
INSERT INTO CUST VALUES (21,'Ronnie','Jordan','8477 Hogan St','Sun City',85351,'M','S','A');
INSERT INTO CUST VALUES (22,'Lily','Vasquez','Learn st','Stuart',34997,'F','S','A');
INSERT INTO CUST VALUES (23,'Esther','Webb','9143 Stevens Creek Blvd','Woburn',01801,'F','S','H');
INSERT INTO CUST VALUES (24,'Enrique','Lawson','7010 Groveland Terrace','Tuckerton',08087,'M','S','A');
INSERT INTO CUST VALUES (25,'Ana','Williamson','3291 Locust Rd','Franklin',02038,'F','M','H');
"""

insurance="""INSERT into INSURANCE VALUES ('101','H');
INSERT into INSURANCE VALUES ('102','A');
INSERT into INSURANCE VALUES ('103','H');
INSERT into INSURANCE VALUES ('104','A');
INSERT into INSURANCE VALUES ('105','H');
INSERT into INSURANCE VALUES ('106','A');
INSERT into INSURANCE VALUES ('107','H');
INSERT into INSURANCE VALUES ('108','H');
INSERT into INSURANCE VALUES ('109','A');
INSERT into INSURANCE VALUES ('110','H');
INSERT into INSURANCE VALUES ('111','A');
INSERT into INSURANCE VALUES ('112','H');
INSERT into INSURANCE VALUES ('113','A');
INSERT into INSURANCE VALUES ('114','H');
INSERT into INSURANCE VALUES ('115','A');
INSERT into INSURANCE VALUES ('116','A');
INSERT into INSURANCE VALUES ('117','H');
INSERT into INSURANCE VALUES ('118','A');
INSERT into INSURANCE VALUES ('119','H');
INSERT into INSURANCE VALUES ('120','A');
INSERT into INSURANCE VALUES ('121','H');
INSERT into INSURANCE VALUES ('122','A');
INSERT into INSURANCE VALUES ('123','H');
INSERT into INSURANCE VALUES ('124','H');
INSERT into INSURANCE VALUES ('125','A');
INSERT into INSURANCE VALUES ('126','H');
INSERT into INSURANCE VALUES ('127','A');
INSERT into INSURANCE VALUES ('128','H');
INSERT into INSURANCE VALUES ('129','A');
INSERT into INSURANCE VALUES ('130','H');
"""

cust_insurance="""INSERT INTO CUST_INSURANCE VALUES (101,1);
INSERT INTO CUST_INSURANCE VALUES (102,2);
INSERT INTO CUST_INSURANCE VALUES (103,3);
INSERT INTO CUST_INSURANCE VALUES (104,4);
INSERT INTO CUST_INSURANCE VALUES (105,5);
INSERT INTO CUST_INSURANCE VALUES (106,6);
INSERT INTO CUST_INSURANCE VALUES (107,7);
INSERT INTO CUST_INSURANCE VALUES (108,8);
INSERT INTO CUST_INSURANCE VALUES (109,9);
INSERT INTO CUST_INSURANCE VALUES (110,10);
INSERT INTO CUST_INSURANCE VALUES (111,11);
INSERT INTO CUST_INSURANCE VALUES (112,12);
INSERT INTO CUST_INSURANCE VALUES (113,13);
INSERT INTO CUST_INSURANCE VALUES (114,14);
INSERT INTO CUST_INSURANCE VALUES (115,15);
INSERT INTO CUST_INSURANCE VALUES (116,16);
INSERT INTO CUST_INSURANCE VALUES (117,17);
INSERT INTO CUST_INSURANCE VALUES (118,18);
INSERT INTO CUST_INSURANCE VALUES (119,19);
INSERT INTO CUST_INSURANCE VALUES (120,20);
INSERT INTO CUST_INSURANCE VALUES (121,21);
INSERT INTO CUST_INSURANCE VALUES (122,22);
INSERT INTO CUST_INSURANCE VALUES (123,23);
INSERT INTO CUST_INSURANCE VALUES (124,24);
INSERT INTO CUST_INSURANCE VALUES (125,25);
INSERT INTO CUST_INSURANCE VALUES (126, 6);
INSERT INTO CUST_INSURANCE VALUES (127, 6);
INSERT INTO CUST_INSURANCE VALUES (128, 14);
INSERT INTO CUST_INSURANCE VALUES (129, 14);
INSERT INTO CUST_INSURANCE VALUES (130, 18);
"""

driver="""INSERT INTO DRIVER VALUES (26638791, 'MN', 'Joe', 'Miller', date(1962-03-10));
INSERT INTO DRIVER VALUES (59246133, 'DE', 'Robert', 'Williams', date(1962-03-10));
INSERT INTO DRIVER VALUES (56068707, 'VT', 'Jim', 'White', date(1962-03-10));
INSERT INTO DRIVER VALUES (27087842, 'WV', 'David', 'Miller', date(1962-03-10));
INSERT INTO DRIVER VALUES (20867586, 'VT', 'Mark', 'Criss', date(1962-03-10));
INSERT INTO DRIVER VALUES (22567409, 'MA', 'Travis', 'Robinson', date(1962-03-10));
INSERT INTO DRIVER VALUES (21195846, 'OH', 'John', 'Harrier', date(1962-03-10));
INSERT INTO DRIVER VALUES (39535180, 'KY', 'James', 'Smith', date(1962-03-10));
INSERT INTO DRIVER VALUES (66983120, 'CA', 'Elizabeth', 'Brown', date(1962-03-10));
INSERT INTO DRIVER VALUES (65176737, 'NV', 'Sturt', 'Jukerberg', date(1962-03-10));
INSERT INTO DRIVER VALUES (42425742, 'NM', 'Jane', 'Williams', date(1962-03-10));
INSERT INTO DRIVER VALUES (98943936, 'FL', 'Maggie', 'Doe', date(1962-03-10));
INSERT INTO DRIVER VALUES (45917819, 'NV', 'Rob', 'Jackson', date(1962-03-10));
INSERT INTO DRIVER VALUES (78433253, 'ME', 'Brian', 'Thomas', date(1962-03-10));
INSERT INTO DRIVER VALUES (71572494, 'WA', 'Charles', 'Kaye', date(1962-03-10));
INSERT INTO DRIVER VALUES (99820321, 'AK', 'Linda', 'Moore', date(1962-03-10));
INSERT INTO DRIVER VALUES (76788146, 'WA', 'Tom', 'Doe', date(1962-03-10));
INSERT INTO DRIVER VALUES (39614859, 'WV', 'Travis', 'Jenkins', date(1962-03-10));
INSERT INTO DRIVER VALUES (14518548, 'IA', 'Mark', 'Robinson', date(1962-03-10));
INSERT INTO DRIVER VALUES (81122292, 'NM', 'Corey', 'Wilks', date(1962-03-10));
INSERT INTO DRIVER VALUES (15681207, 'IA', 'Ravid', 'Harrier', date(1962-03-10));
INSERT INTO DRIVER VALUES (35499072, 'ME', 'Eion', 'Criss', date(1962-03-10));
INSERT INTO DRIVER VALUES (43905694, 'GA', 'Sturt', 'Doe', date(1962-03-10));
INSERT INTO DRIVER VALUES (49573633, 'MA', 'Elon', 'Downy', date(1962-03-10));
INSERT INTO DRIVER VALUES (41204627, 'ID', 'Maggie', 'Arnold', date(1962-03-10));
INSERT INTO DRIVER VALUES (24093997, 'OR', 'Tom', 'Martin', date(1962-03-10));
INSERT INTO DRIVER VALUES (43277652, 'MI', 'Elizabeth', 'Wright', date(1962-03-10));
INSERT INTO DRIVER VALUES (51998138, 'ND', 'Patricia', 'Brewster', date(1962-03-10));
INSERT INTO DRIVER VALUES (85063948, 'MS', 'Mary', 'Wilson', date(1962-03-10));
INSERT INTO DRIVER VALUES (20487220, 'RI', 'Dave', 'Smith', date(1962-03-10));
INSERT INTO DRIVER VALUES (36404734, 'SC', 'Robert', 'Harris', date(1962-03-10));
INSERT INTO DRIVER VALUES (92715774, 'OR', 'Jeremy', 'Patterson', date(1962-03-10));
INSERT INTO DRIVER VALUES (37299758, 'ID', 'Mira', 'Anderson', date(1962-03-10));
INSERT INTO DRIVER VALUES (99901958, 'DC', 'Joe', 'Harris', date(1962-03-10));
INSERT INTO DRIVER VALUES (87621523, 'WI', 'Mark', 'Stuart', date(1962-03-10));
INSERT INTO DRIVER VALUES (27687707, 'NJ', 'Tom', 'Anderson', date(1962-03-10));
INSERT INTO DRIVER VALUES (19886120, 'TX', 'Neil', 'Jackson', date(1962-03-10));
INSERT INTO DRIVER VALUES (26656584, 'OR', 'Michael', 'Parsons', date(1962-03-10));
INSERT INTO DRIVER VALUES (81308918, 'CT', 'David', 'Downy Jr', date(1962-03-10));
INSERT INTO DRIVER VALUES (54019273, 'FL', 'Maggie', 'Moore', date(1962-03-10));
"""

vehicles="""INSERT into VEHICLE values ('JH4KA4551KC003961', 'Bmw', 'G650GS', 2012, 'F');
INSERT into VEHICLE values ('WP0AA2991YS620631', 'Yamaha', 'TTR125L', 2013, 'F');
INSERT into VEHICLE values ('1HGCP263X8A035447', 'Polaris', 'PREDATOR 50', 2013, 'F');
INSERT into VEHICLE values ('JH4KA8260MC000458', 'Bombardier' , 'DS50', 2012, 'O');
INSERT into VEHICLE values ('1G8DC18H4CF114023', 'Tesla', 'ROADSTER', 2008, 'O');
INSERT into VEHICLE values ('1P3XP48K6LN273071', 'Chevrolet', 'CAPRICE', 2014, 'O');
INSERT into VEHICLE values ('1FAFP52UXXA197384', 'Bmw', 'ALPINA B7', 2012, 'L');
INSERT into VEHICLE values ('4S3BJ6329M1918965', 'Ram', 'RAM PICKUP', 2012, 'F');
INSERT into VEHICLE values ('JTDBE30K620061417', 'Bmw', 'Z4', 2014, 'O');
INSERT into VEHICLE values ('JN8AS1MU0CM120061', 'Volkswagen', 'GOLF', 2007, 'L');
INSERT into VEHICLE values ('4F2CU08102KM50866', 'Mercedes', 'CL65 AMG', 2014, 'F');
INSERT into VEHICLE values ('LM4AC113061105688', 'Chrysler', 'TOWN & COUNTRY', 2004, 'F');
INSERT into VEHICLE values ('1FVAF3CV84DM31815', 'Mercedes', 'SLR MCLAREN', 2007, 'F');
INSERT into VEHICLE values ('JH4KA4650JC000403', 'Honda', 'CRF100F', 2012, 'F');
INSERT into VEHICLE values ('JH4DA1842JS003823', 'Bmw', 'K1200RS', 2005, 'O');
INSERT into VEHICLE values ('YV1MS672892447094', 'Nissan', 'ROGUE', 2014, 'O');
INSERT into VEHICLE values ('JH4DA3450JS001899', 'Infiniti', 'FX45', 2005, 'F');
INSERT into VEHICLE values ('1B4GP45R6WB718087', 'Lexus', 'LS460', 2010, 'F');
INSERT into VEHICLE values ('1GTEK19RXVE536195', 'Audi', 'A6', 2008, 'F');
INSERT into VEHICLE values ('3B7HF13Y81G193584', 'Gmc', 'YUKON XL 1500', 2001, 'F');
INSERT into VEHICLE values ('WVWAF93D258002461', 'Honda', 'CRF150R', 2007, 'L');
INSERT into VEHICLE values ('1FV3GFBC0YHA74039', 'Honda', 'TRX700XX', 2008, 'F');
INSERT into VEHICLE values ('3VWSB81H8WM210368', 'Renault', 'MEGANE', 2005, 'O');
INSERT into VEHICLE values ('1FVACYDC37HW59012', 'Dodge', 'CHALLENGER', 2008, 'L');
INSERT into VEHICLE values ('1FTJW36F2TEA03179', 'Dodge', 'SPRINTER 2500', 2009, 'O');
INSERT into VEHICLE values ('1FUJA6CV74DM34063', 'Toyota', '4RUNNER', 2012, 'L');
INSERT into VEHICLE values ('JTLKE50E191068256', 'Chevrolet', 'AVEO', 2009, 'F');
INSERT into VEHICLE values ('ZAMBC38A450014565', 'Bmw' ,'X5', 2014, 'F');
INSERT into VEHICLE values ('5GZEV337X7J141405', 'Mercedes', 'G63 AMG', 2013, 'F');
"""

vehicle_driver="""INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA4551KC003961', 26638791, 'MN');
INSERT INTO VEHICLE_DRIVER VALUES ('1FAFP52UXXA197384', 59246133, 'DE');
INSERT INTO VEHICLE_DRIVER VALUES ('1GTEK19RXVE536195', 56068707, 'VT');
INSERT INTO VEHICLE_DRIVER VALUES ('1GTEK19RXVE536195', 27087842, 'WV');
INSERT INTO VEHICLE_DRIVER VALUES ('1GTEK19RXVE536195', 20867586, 'VT');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA8260MC000458', 22567409, 'MA');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA8260MC000458', 21195846, 'OH');
INSERT INTO VEHICLE_DRIVER VALUES ('WP0AA2991YS620631', 39535180, 'KY');
INSERT INTO VEHICLE_DRIVER VALUES ('WP0AA2991YS620631', 66983120, 'CA');
INSERT INTO VEHICLE_DRIVER VALUES ('1FAFP52UXXA197384', 65176737, 'NV');
INSERT INTO VEHICLE_DRIVER VALUES ('1GTEK19RXVE536195', 42425742, 'NM');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA8260MC000458', 98943936, 'FL');
INSERT INTO VEHICLE_DRIVER VALUES ('ZAMBC38A450014565', 45917819, 'NV');
INSERT INTO VEHICLE_DRIVER VALUES ('JTLKE50E191068256', 78433253, 'ME');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA8260MC000458', 71572494, 'WA');
INSERT INTO VEHICLE_DRIVER VALUES ('1FV3GFBC0YHA74039', 99820321, 'AK');
INSERT INTO VEHICLE_DRIVER VALUES ('LM4AC113061105688', 76788146, 'WA');
INSERT INTO VEHICLE_DRIVER VALUES ('1FUJA6CV74DM34063', 39614859, 'WV');
INSERT INTO VEHICLE_DRIVER VALUES ('1HGCP263X8A035447', 14518548, 'IA');
INSERT INTO VEHICLE_DRIVER VALUES ('4F2CU08102KM50866', 81122292, 'NM');
INSERT INTO VEHICLE_DRIVER VALUES ('LM4AC113061105688', 15681207, 'IA');
INSERT INTO VEHICLE_DRIVER VALUES ('LM4AC113061105688', 35499072, 'ME');
INSERT INTO VEHICLE_DRIVER VALUES ('1G8DC18H4CF114023', 43905694, 'GA');
INSERT INTO VEHICLE_DRIVER VALUES ('1FTJW36F2TEA03179', 49573633, 'MA');
INSERT INTO VEHICLE_DRIVER VALUES ('JTDBE30K620061417', 41204627, 'ID');
INSERT INTO VEHICLE_DRIVER VALUES ('JN8AS1MU0CM120061', 24093997, 'OR');
INSERT INTO VEHICLE_DRIVER VALUES ('LM4AC113061105688', 43277652, 'MI');
INSERT INTO VEHICLE_DRIVER VALUES ('WVWAF93D258002461', 51998138, 'ND');
INSERT INTO VEHICLE_DRIVER VALUES ('YV1MS672892447094', 85063948, 'MS');
INSERT INTO VEHICLE_DRIVER VALUES ('5GZEV337X7J141405', 20487220, 'RI');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4DA3450JS001899', 36404734, 'SC');
INSERT INTO VEHICLE_DRIVER VALUES ('5GZEV337X7J141405', 92715774, 'OR');
INSERT INTO VEHICLE_DRIVER VALUES ('1FVAF3CV84DM31815', 37299758, 'ID');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4KA4650JC000403', 99901958, 'DC');
INSERT INTO VEHICLE_DRIVER VALUES ('JH4DA1842JS003823', 87621523, 'WI');
INSERT INTO VEHICLE_DRIVER VALUES ('3B7HF13Y81G193584', 27687707, 'NJ');
INSERT INTO VEHICLE_DRIVER VALUES ('1B4GP45R6WB718087', 19886120, 'TX');
INSERT INTO VEHICLE_DRIVER VALUES ('1GTEK19RXVE536195', 26656584, 'OR');
INSERT INTO VEHICLE_DRIVER VALUES ('1FVACYDC37HW59012', 81308918, 'CT');
INSERT INTO VEHICLE_DRIVER VALUES ('3VWSB81H8WM210368', 54019273, 'FL');
"""

auto_insurance="""INSERT into AUTO_INSURANCE values (102, 'JH4KA4551KC003961', date(1962-03-10), date(1962-03-10), 223.64, 'C');
INSERT into AUTO_INSURANCE values (104, 'WP0AA2991YS620631', date(1962-03-10), date(1962-03-10), 500.02, 'P');
INSERT into AUTO_INSURANCE values (106, '1HGCP263X8A035447', date(1962-03-10), date(1962-03-10), 1601.11, 'C');
INSERT into AUTO_INSURANCE values (109, 'JH4KA8260MC000458', date(1962-03-10), date(1962-03-10), 133.43, 'P');
INSERT into AUTO_INSURANCE values (111, '1G8DC18H4CF114023', date(1962-03-10), date(1962-03-10), 609.74, 'C');
INSERT into AUTO_INSURANCE values (113, '1P3XP48K6LN273071', date(1962-03-10), date(1962-03-10), 212.12, 'C');
INSERT into AUTO_INSURANCE values (115, '1FAFP52UXXA197384', date(1962-03-10), date(1962-03-10), 873.43, 'C');
INSERT into AUTO_INSURANCE values (116, '4S3BJ6329M1918965', date(1962-03-10), date(1962-03-10), 687.78, 'C');
INSERT into AUTO_INSURANCE values (118, 'JTDBE30K620061417', date(1962-03-10), date(1962-03-10), 189.33, 'C');
INSERT into AUTO_INSURANCE values (120, 'JN8AS1MU0CM120061', date(1962-03-10), date(1962-03-10), 2543.32, 'C');
INSERT into AUTO_INSURANCE values (122, '4F2CU08102KM50866', date(1962-03-10), date(1962-03-10), 982.15, 'C');
INSERT into AUTO_INSURANCE values (125, 'LM4AC113061105688', date(1962-03-10), date(1962-03-10), 982.15, 'C');
INSERT into AUTO_INSURANCE values (127, '1FVAF3CV84DM31815', date(1962-03-10), date(1962-03-10), 189.33, 'P');
INSERT into AUTO_INSURANCE values (129, 'JH4KA4650JC000403', date(1962-03-10), date(1962-03-10), 2105.50, 'C');
INSERT into AUTO_INSURANCE values (129, 'JH4DA1842JS003823', date(1962-03-10), date(1962-03-10), 686.66, 'C');
INSERT into AUTO_INSURANCE values (129, 'YV1MS672892447094', date(1962-03-10), date(1962-03-10), 521.75, 'P');
INSERT into AUTO_INSURANCE values (102, 'JH4DA3450JS001899', date(1962-03-10), date(1962-03-10), 445.89, 'C');
INSERT into AUTO_INSURANCE values (118, '1B4GP45R6WB718087', date(1962-03-10), date(1962-03-10), 2888.10, 'C');
INSERT into AUTO_INSURANCE values (118, '1GTEK19RXVE536195', date(1962-03-10), date(1962-03-10), 145.50, 'C');
INSERT into AUTO_INSURANCE values (111, '3B7HF13Y81G193584', date(1962-03-10), date(1962-03-10), 1623.15, 'C');
INSERT into AUTO_INSURANCE values (104, 'WVWAF93D258002461', date(1962-03-10), date(1962-03-10), 455.55, 'C');
INSERT into AUTO_INSURANCE values (104, '1FV3GFBC0YHA74039', date(1962-03-10), date(1962-03-10), 198.75, 'C');
INSERT into AUTO_INSURANCE values (102, '3VWSB81H8WM210368', date(1962-03-10), date(1962-03-10), 75.30, 'C');
INSERT into AUTO_INSURANCE values (111, '1FVACYDC37HW59012', date(1962-03-10), date(1962-03-10), 896.52, 'C');
INSERT into AUTO_INSURANCE values (111, '1FTJW36F2TEA03179', date(1962-03-10), date(1962-03-10), 750.0, 'P');
INSERT into AUTO_INSURANCE values (125, '1FUJA6CV74DM34063', date(1962-03-10), date(1962-03-10), 609.09, 'C');
INSERT into AUTO_INSURANCE values (127, 'JTLKE50E191068256', date(1962-03-10), date(1962-03-10), 795.85, 'C');
INSERT into AUTO_INSURANCE values (127, 'ZAMBC38A450014565', date(1962-03-10), date(1962-03-10), 1513.50, 'C');
INSERT into AUTO_INSURANCE values (118, '5GZEV337X7J141405', date(1962-03-10), date(1962-03-10), 333.25, 'C');
"""

home_data="""INSERT INTO HOME VALUES (8274870194, date(1962-03-10), 1764000, 4250, 'C', 1, 0, NULL, 0, '872 Learn st', 17701, 'Williamsport');
INSERT INTO HOME VALUES (6040047612, date(1962-03-10), 1141000, 3230, 'S', 1, 1, 'I', 1, '7933 Mcclellan Rd', 61821, 'Champaign');
INSERT INTO HOME VALUES (6110382967, date(1962-03-10), 203000, 500, 'T', 1, 1, 'M', 1, '2675 Harrison Ct', 21206, 'Baltimore');
INSERT INTO HOME VALUES (5155334165, date(1962-03-10), 1124000, 2950, 'S', 1, 0, 'I', 1, '3524 Frances Ct', 21197, 'Smalltown');
INSERT INTO HOME VALUES (1510876130, date(1962-03-10), 1594000, 3530, 'S', 0, 0, 'I', 0, '212 Pearl St.', 40247, 'Balmora');
INSERT INTO HOME VALUES (1653192697, date(1962-03-10), 659000, 1870, 'M', 1, 0, 'U', 1, '212 Pearl St.', 17589, 'Eerie');
INSERT INTO HOME VALUES (8190022816, date(1962-03-10), 868000, 4050, 'C', 0, 0, NULL, 0, '701 Maple St.', 54863, 'Olympus');
INSERT INTO HOME VALUES (1177406054, date(1962-03-10), 236000, 2030, 'M', 1, 1, 'U', 0, '3291 Locust Rd', 94201, 'Springfield');
INSERT INTO HOME VALUES (8794014691, date(1962-03-10), 427000, 1390, 'C', 0, 1, NULL, 1, '212 Pearl St.', 60964, 'Atlanta');
INSERT INTO HOME VALUES (9491123506, date(1962-03-10), 1696000, 3050, 'T', 1, 0, 'O', 0, '7010 Groveland Terrace', 75307, 'Toulouse');
INSERT INTO HOME VALUES (4803249101, date(1962-03-10), 799000, 3870, 'S', 0, 1, 'U', 0, '9143 Stevens Creek Blvd', 37008, 'Metropolis');
INSERT INTO HOME VALUES (7386832621, date(1962-03-10), 181000, 3700, 'T', 0, 0, 'I', 0, '8477 Hogan St', 53614, 'Thundera');
INSERT INTO HOME VALUES (8968421088, date(1962-03-10), 1578000, 2560, 'T', 1, 0, 'U', 0, '2684 Daisy Dr', 51200, 'Mordor');
INSERT INTO HOME VALUES (5584316830, date(1962-03-10), 115000, 950, 'M', 1, 1, NULL, 0, '1183 Ash Dr', 36179, 'Winterfell');
INSERT INTO HOME VALUES (1889246262, date(1962-03-10), 969000, 3760, 'S', 1, 1, 'U', 1, '9124 Hunters Creek Dr', 96779, 'Pythonville');
INSERT INTO HOME VALUES (4894121408, date(1962-03-10), 1142000, 1160, 'C', 1, 0, 'U', 1, '5689 Daisy Dr', 40893, 'Faketown');
INSERT INTO HOME VALUES (9645655435, date(1962-03-10), 1959000, 1140, 'T', 0, 1, 'I', 1, '4960 Edwards Rd', 50695, 'Lakeview');
INSERT INTO HOME VALUES (5695603761, date(1962-03-10), 1173000, 840, 'M', 0, 1, NULL, 1, '8807 E Center St', 71476, 'Braavos');
INSERT INTO HOME VALUES (3335510137, date(1962-03-10), 1229000, 3890, 'M', 0, 0, 'O', 0, '8120 Avondale Ave', 59266, 'Blackwater');
INSERT INTO HOME VALUES (8718951280, date(1962-03-10), 1343000, 1490, 'M', 0, 1, NULL, 1, '8807 E Center St', 64319, 'Gotham');
INSERT INTO HOME VALUES (8690937663, date(1962-03-10), 692000, 4170, 'S', 0, 0, 'M', 0, '8120 Avondale Ave', 64247, 'Dawnstar');
INSERT INTO HOME VALUES (2933651928, date(1962-03-10), 1995000, 3910, 'T', 1, 1, 'U', 0, '7013 Fairview St', 89271, 'Valyria');
INSERT INTO HOME VALUES (7355546679, date(1962-03-10), 1767000, 3190, 'C', 1, 0, 'M', 1, '1124 Valwood Pkwy', 37805, 'Easton');
INSERT INTO HOME VALUES (6246892852, date(1962-03-10), 1016000, 760, 'S', 0, 0, 'O', 0, '53 Pockrus Page Rd', 95711, 'Fairlawn');
INSERT INTO HOME VALUES (2078102300, date(1962-03-10), 198000, 3600, 'M', 0, 1, 'O', 0, '5755 Hickory Creek Dr', 42044, 'Garden City');
INSERT INTO HOME VALUES (4518817008, date(1962-03-10), 1229000, 1390, 'C', 0, 0, 'O', 1, '2694 Valwood Pkwy', 88072, 'Morristown');
INSERT INTO HOME VALUES (9845445669, date(1962-03-10), 988000, 3170, 'T', 0, 0, NULL, 0, '262 Poplar Dr', 49609, 'Mt Olive');
INSERT INTO HOME VALUES (7137708216, date(1962-03-10), 236000, 2190, 'S', 0, 0, 'I', 1, '1141 W Belt Line Rd', 14098, 'Betlehem');
INSERT INTO HOME VALUES (5990598804, date(1962-03-10), 481000, 900, 'T', 0, 0, 'O', 0, '18 Learn st', 58359, 'St Pittersburg');
INSERT INTO HOME VALUES (3120205778, date(1962-03-10), 1068000, 3040, 'T', 1, 1, 'O', 1, '2230 Oak Lawn Ave', 66784, 'Saratoga');
"""

home_insurance="""INSERT INTO HOME_INSURANCE VALUES (101, 8274870194, date(1962-03-10), date(1962-03-10), 223.64, 'C');
INSERT INTO HOME_INSURANCE VALUES (101, 6040047612, date(1962-03-10), date(1962-03-10), 500.02, 'P');
INSERT INTO HOME_INSURANCE VALUES (103, 6110382967, date(1962-03-10), date(1962-03-10), 1601.11, 'C');
INSERT INTO HOME_INSURANCE VALUES (105, 5155334165, date(1962-03-10), date(1962-03-10), 133.43, 'P');
INSERT INTO HOME_INSURANCE VALUES (105, 1510876130, date(1962-03-10), date(1962-03-10), 609.74, 'C');
INSERT INTO HOME_INSURANCE VALUES (107, 1653192697, date(1962-03-10), date(1962-03-10), 212.12, 'C');
INSERT INTO HOME_INSURANCE VALUES (108, 8190022816, date(1962-03-10), date(1962-03-10), 873.43, 'C');
INSERT INTO HOME_INSURANCE VALUES (108, 1177406054, date(1962-03-10), date(1962-03-10), 687.78, 'C');
INSERT INTO HOME_INSURANCE VALUES (110, 8794014691, date(1962-03-10), date(1962-03-10), 189.33, 'C');
INSERT INTO HOME_INSURANCE VALUES (112, 9491123506, date(1962-03-10), date(1962-03-10), 2543.32, 'C');
INSERT INTO HOME_INSURANCE VALUES (114, 4803249101, date(1962-03-10), date(1962-03-10), 982.15, 'C');
INSERT INTO HOME_INSURANCE VALUES (117, 7386832621, date(1962-03-10), date(1962-03-10), 982.15, 'C');
INSERT INTO HOME_INSURANCE VALUES (119, 8968421088, date(1962-03-10), date(1962-03-10), 189.33, 'P');
INSERT INTO HOME_INSURANCE VALUES (121, 5584316830, date(1962-03-10), date(1962-03-10), 2105.50, 'C');
INSERT INTO HOME_INSURANCE VALUES (123, 1889246262, date(1962-03-10), date(1962-03-10), 686.66, 'C');
INSERT INTO HOME_INSURANCE VALUES (124, 4894121408, date(1962-03-10), date(1962-03-10), 521.75, 'P');
INSERT INTO HOME_INSURANCE VALUES (126, 9645655435, date(1962-03-10), date(1962-03-10), 445.89, 'C');
INSERT INTO HOME_INSURANCE VALUES (128, 5695603761, date(1962-03-10), date(1962-03-10), 2888.10, 'C');
INSERT INTO HOME_INSURANCE VALUES (130, 3335510137, date(1962-03-10), date(1962-03-10), 145.50, 'C');
INSERT INTO HOME_INSURANCE VALUES (130, 8718951280, date(1962-03-10), date(1962-03-10), 1623.15, 'C');
INSERT INTO HOME_INSURANCE VALUES (130, 8690937663, date(1962-03-10), date(1962-03-10), 455.55, 'C');
INSERT INTO HOME_INSURANCE VALUES (101, 2933651928, date(1962-03-10), date(1962-03-10), 198.75, 'C');
INSERT INTO HOME_INSURANCE VALUES (114, 7355546679, date(1962-03-10), date(1962-03-10), 75.30, 'C');
INSERT INTO HOME_INSURANCE VALUES (119, 6246892852, date(1962-03-10), date(1962-03-10), 896.52, 'C');
INSERT INTO HOME_INSURANCE VALUES (114, 2078102300, date(1962-03-10), date(1962-03-10), 750.0, 'P');
INSERT INTO HOME_INSURANCE VALUES (128, 4518817008, date(1962-03-10), date(1962-03-10), 609.09, 'C');
INSERT INTO HOME_INSURANCE VALUES (130, 9845445669, date(1962-03-10), date(1962-03-10), 795.85, 'C');
INSERT INTO HOME_INSURANCE VALUES (114, 7137708216, date(1962-03-10), date(1962-03-10), 1513.50, 'C');
INSERT INTO HOME_INSURANCE VALUES (130, 5990598804, date(1962-03-10), date(1962-03-10), 762.40, 'C');
INSERT INTO HOME_INSURANCE VALUES (126, 3120205778, date(1962-03-10), date(1962-03-10), 333.25, 'C');
"""

invoice_data="""INSERT INTO INVOICE VALUES (8007482823, 769.67, date(1962-03-10), 102);
INSERT INTO INVOICE VALUES (9948137411, 633.13, date(1962-03-10), 114);
INSERT INTO INVOICE VALUES (3815191356, 180.18, date(1962-03-10), 104);
INSERT INTO INVOICE VALUES (5413330330, 975.34, date(1962-03-10), 103);
INSERT INTO INVOICE VALUES (3242275858, 10.75, date(1962-03-10), 108);
INSERT INTO INVOICE VALUES (1113990911, 818.01, date(1962-03-10), 102);
INSERT INTO INVOICE VALUES (4962216558, 433.64, date(1962-03-10), 107);
INSERT INTO INVOICE VALUES (3249609658, 526.11, date(1962-03-10), 124);
INSERT INTO INVOICE VALUES (9215164752, 383.51, date(1962-03-10), 127);
INSERT INTO INVOICE VALUES (4088251801, 632.81, date(1962-03-10), 124);
INSERT INTO INVOICE VALUES (2654430917, 678.38, date(1962-03-10), 121);
INSERT INTO INVOICE VALUES (9844216976, 728.34, date(1962-03-10), 127);
INSERT INTO INVOICE VALUES (3931781541, 541.27, date(1962-03-10), 126);
INSERT INTO INVOICE VALUES (2121573015, 520.15, date(1962-03-10), 118);
INSERT INTO INVOICE VALUES (2188331739, 46.32, date(1962-03-10), 127);
INSERT INTO INVOICE VALUES (5820822483, 778.85, date(1962-03-10), 127);
INSERT INTO INVOICE VALUES (3723127014, 896.17, date(1962-03-10), 123);
INSERT INTO INVOICE VALUES (8626743968, 156.07, date(1962-03-10), 123);
INSERT INTO INVOICE VALUES (9341100925, 775.83, date(1962-03-10), 123);
INSERT INTO INVOICE VALUES (8122366158, 106.64, date(1962-03-10), 115);
INSERT INTO INVOICE VALUES (8333189129, 257.56, date(1962-03-10), 107);
INSERT INTO INVOICE VALUES (8617092388, 864.37, date(1962-03-10), 119);
INSERT INTO INVOICE VALUES (9786892223, 643.68, date(1962-03-10), 122);
INSERT INTO INVOICE VALUES (5707643737, 208.79, date(1962-03-10), 118);
INSERT INTO INVOICE VALUES (7086881178, 664.69, date(1962-03-10), 109);
INSERT INTO INVOICE VALUES (5865849753, 106.21, date(1962-03-10), 124);
INSERT INTO INVOICE VALUES (9294124437, 836.6, date(1962-03-10), 114);
INSERT INTO INVOICE VALUES (5161358760, 355.78, date(1962-03-10), 111);
INSERT INTO INVOICE VALUES (8411568177, 28.37, date(1962-03-10), 107);
INSERT INTO INVOICE VALUES (5524157793, 629.26, date(1962-03-10), 112);
INSERT INTO INVOICE VALUES (5109878954, 593.57, date(1962-03-10), 116);
INSERT INTO INVOICE VALUES (7789996210, 24.18, date(1962-03-10), 101);
INSERT INTO INVOICE VALUES (7951661827, 481.61, date(1962-03-10), 118);
INSERT INTO INVOICE VALUES (2833359178, 869.98, date(1962-03-10), 102);
INSERT INTO INVOICE VALUES (8483404329, 711.56, date(1962-03-10), 117);
INSERT INTO INVOICE VALUES (4340221202, 613.88, date(1962-03-10), 129);
INSERT INTO INVOICE VALUES (1363798905, 499.99, date(1962-03-10), 128);
"""

payment="""INSERT INTO PAYMENT VALUES (4571178372, 1363798905, date(1962-03-10), 'Credit', 62.5);
INSERT INTO PAYMENT VALUES (4968869738, 8411568177, date(1962-03-10), 'PayPal', 3.55);
INSERT INTO PAYMENT VALUES (2710965853, 3249609658, date(1962-03-10), 'PayPal', 65.76);
INSERT INTO PAYMENT VALUES (8022892880, 5865849753, date(1962-03-10), 'Debit', 13.28);
INSERT INTO PAYMENT VALUES (9333402429, 8007482823, date(1962-03-10), 'Credit', 96.21);
INSERT INTO PAYMENT VALUES (2360528934, 9948137411, date(1962-03-10), 'PayPal', 79.14);
INSERT INTO PAYMENT VALUES (1497952683, 9215164752, date(1962-03-10), 'Debit', 47.94);
INSERT INTO PAYMENT VALUES (3203479802, 1363798905, date(1962-03-10), 'Debit', 62.5);
INSERT INTO PAYMENT VALUES (7671696619, 3723127014, date(1962-03-10), 'Debit', 112.02);
INSERT INTO PAYMENT VALUES (3668955563, 8333189129, date(1962-03-10), 'Credit', 32.2);
INSERT INTO PAYMENT VALUES (2015166186, 5413330330, date(1962-03-10), 'Debit', 121.92);
INSERT INTO PAYMENT VALUES (8172115305, 5413330330, date(1962-03-10), 'Credit', 121.92);
INSERT INTO PAYMENT VALUES (8537800296, 3723127014, date(1962-03-10), 'PayPal', 57.44);
INSERT INTO PAYMENT VALUES (6154666467, 1363798905, date(1962-03-10), 'Debit', 62.5);
INSERT INTO PAYMENT VALUES (6676073171, 2188331739, date(1962-03-10), 'Credit', 5.79);
INSERT INTO PAYMENT VALUES (8913871479, 8617092388, date(1962-03-10), 'Debit', 108.05);
INSERT INTO PAYMENT VALUES (8214998699, 4088251801, date(1962-03-10), 'Debit', 79.1);
INSERT INTO PAYMENT VALUES (4653510753, 5161358760, date(1962-03-10), 'Credit', 44.47);
INSERT INTO PAYMENT VALUES (2727810481, 5161358760, date(1962-03-10), 'Credit', 57.44);
INSERT INTO PAYMENT VALUES (6356256017, 5161358760, date(1962-03-10), 'Credit', 44.47);
INSERT INTO PAYMENT VALUES (8096265482, 5413330330, date(1962-03-10), 'PayPal', 57.44);
INSERT INTO PAYMENT VALUES (4559698961, 1113990911, date(1962-03-10), 'Credit', 102.25);
INSERT INTO PAYMENT VALUES (4526815293, 5413330330, date(1962-03-10), 'Credit', 121.92);
INSERT INTO PAYMENT VALUES (1095750591, 5865849753, date(1962-03-10), 'Credit', 13.28);
INSERT INTO PAYMENT VALUES (5180348769, 3242275858, date(1962-03-10), 'Credit', 1.34);
INSERT INTO PAYMENT VALUES (4942015243, 9786892223, date(1962-03-10), 'Credit', 80.46);
INSERT INTO PAYMENT VALUES (8838853653, 2188331739, date(1962-03-10), 'Credit', 5.79);
INSERT INTO PAYMENT VALUES (6061483288, 9215164752, date(1962-03-10), 'Debit', 47.94);
INSERT INTO PAYMENT VALUES (1602985651, 8333189129, date(1962-03-10), 'Debit', 32.2);
INSERT INTO PAYMENT VALUES (5623228196, 5413330330, date(1962-03-10), 'Debit', 121.92);
INSERT INTO PAYMENT VALUES (2222194227, 5161358760, date(1962-03-10), 'Credit', 44.47);
INSERT INTO PAYMENT VALUES (3682189246, 9786892223, date(1962-03-10), 'PayPal', 80.46);
INSERT INTO PAYMENT VALUES (9262589586, 9844216976, date(1962-03-10), 'Credit', 91.04);
INSERT INTO PAYMENT VALUES (9738312368, 9786892223, date(1962-03-10), 'PayPal', 80.46);
INSERT INTO PAYMENT VALUES (5254025462, 9294124437, date(1962-03-10), 'PayPal', 104.58);
INSERT INTO PAYMENT VALUES (5611937580, 9341100925, date(1962-03-10), 'Debit', 96.98);
INSERT INTO PAYMENT VALUES (1369695414, 3242275858, date(1962-03-10), 'PayPal', 1.34);
INSERT INTO PAYMENT VALUES (8722535673, 2121573015, date(1962-03-10), 'Debit', 65.02);
INSERT INTO PAYMENT VALUES (5086299469, 8122366158, date(1962-03-10), 'PayPal', 13.33);
INSERT INTO PAYMENT VALUES (8684316520, 3249609658, date(1962-03-10), 'PayPal', 65.76);
INSERT INTO PAYMENT VALUES (8397394818, 3815191356, date(1962-03-10), 'Debit', 22.52);
INSERT INTO PAYMENT VALUES (2879954439, 5524157793, date(1962-03-10), 'Debit', 78.66);
INSERT INTO PAYMENT VALUES (2163126400, 5413330330, date(1962-03-10), 'Credit', 121.92);
INSERT INTO PAYMENT VALUES (5937660743, 4340221202, date(1962-03-10), 'Credit', 76.73);
INSERT INTO PAYMENT VALUES (8285466936, 8617092388, date(1962-03-10), 'Debit', 108.05);
INSERT INTO PAYMENT VALUES (5500763320, 3723127014, date(1962-03-10), 'PayPal', 112.02);
INSERT INTO PAYMENT VALUES (3377700485, 8483404329, date(1962-03-10), 'Debit', 88.94);
INSERT INTO PAYMENT VALUES (5829035635, 9294124437, date(1962-03-10), 'PayPal', 104.58);
INSERT INTO PAYMENT VALUES (4404301614, 4340221202, date(1962-03-10), 'Debit', 76.73);
INSERT INTO PAYMENT VALUES (5390006615, 9786892223, date(1962-03-10), 'Credit', 80.46);
"""

for query in all_queries:
    cursor.execute(query)

run_array_of_instructions(users)
run_array_of_instructions(cust)
run_array_of_instructions(insurance)
run_array_of_instructions(cust_insurance)
run_array_of_instructions(driver)
run_array_of_instructions(auto_insurance)
run_array_of_instructions(home_data)
run_array_of_instructions(home_insurance)
run_array_of_instructions(invoice_data)
run_array_of_instructions(payment)
run_array_of_instructions(vehicles)
run_array_of_instructions(vehicle_driver)