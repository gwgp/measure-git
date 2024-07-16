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
cursor.execute("""
ALTER TABLE 手机入库
ADD COLUMN is_sold BOOLEAN DEFAULT FALSE
""")

cursor.execute("""
ALTER TABLE 手机入库
ADD COLUMN Inbound_time DATETIME
""")


# 关闭连接
cursor.close()
db.close()
