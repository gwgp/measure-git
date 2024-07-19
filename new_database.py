import mysql.connector

# 连接到 MySQL 服务器
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aa..123456"
)

cursor = db.cursor()

# 创建数据库
cursor.execute("CREATE DATABASE IF NOT EXISTS second_hand_repair_system")

# 关闭连接
cursor.close()
db.close()

# 连接到新创建的数据库
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aa..123456",
    database="second_hand_repair_system"
)

cursor = db.cursor()

# 创建 phone_inventory 表
cursor.execute("""
CREATE TABLE IF NOT EXISTS 手机入库 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(255),
    color VARCHAR(50),
    memory VARCHAR(50),
    serial_number VARCHAR(255),
    store VARCHAR(255),
    warehouse VARCHAR(255),
    channel VARCHAR(255),
    appearance_condition VARCHAR(255),
    battery_efficiency VARCHAR(50),
    repair_status TEXT,
    recycle_price DECIMAL(10, 2),
    wholesale_price DECIMAL(10, 2),
    retail_price DECIMAL(10, 2),
    notes TEXT,
    status VARCHAR(50),
    image_url LONGBLOB
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS 销售录单 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(20),
    usr_info VARCHAR(255),
    time DATETIME,
    serial_number VARCHAR(255),
    channel VARCHAR(255),
    sale_money DECIMAL(10, 2),
    img_url LONGBLOB,
    fittings_name_number JSON
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 维修入库 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(20),
    usr_info VARCHAR(255),
    model VARCHAR(255),
    serial_number VARCHAR(255),
    password VARCHAR(255),
    channel VARCHAR(255),
    store VARCHAR(255),
    description VARCHAR(255),
    estimated_cost DECIMAL(10, 2),
    engineer VARCHAR(255),
    img_url LONGBLOB,
    time DATETIME
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS 配件入库 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(20),
    number VARCHAR(255),
    all_cost DECIMAL(10, 2),
    channel VARCHAR(255),
    kucun_number VARCHAR(255),
    off_number VARCHAR(255),
    present_cost DECIMAL(10, 2),
    present_earn DECIMAL(10, 2),
    in_time DATETIME,
    out_time DATETIME
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS 销售记录 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    number VARCHAR(255),
    cost_money DECIMAL(10, 2),
    sale_money DECIMAL(10, 2),
    earn_money DECIMAL(10, 2),
    out_time DATETIME
)
""")

# cursor.execute("""
# ALTER TABLE 手机入库
# ADD COLUMN is_sold BOOLEAN DEFAULT FALSE
# """)
#
# cursor.execute("""
# ALTER TABLE 手机入库
# ADD COLUMN Inbound_time DATETIME
# """)
# cursor.execute("""
# ALTER TABLE 维修入库 MODIFY model VARCHAR(255);
# """)
# cursor.execute("""
# ALTER TABLE 维修入库
# ADD COLUMN is_done tinyint;
# """)
# cursor.execute("""
# ALTER TABLE 维修入库
# ADD COLUMN off_time DATETIME;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN daily_earn ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN channel ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN kucun_number ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN off_number ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN present_earn ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN in_time ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN out_time ;
# """)
# cursor.execute("""
# ALTER TABLE 配件入库
# DROP COLUMN all_out_price ;
# """)


# 关闭连接
cursor.close()
db.close()
