import os
import re
import shutil
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, Signal,
                            QSize, QStringListModel, QTime, QUrl, Qt, QBuffer, QIODevice, QByteArray)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCompleter, QGridLayout, QHBoxLayout, QInputDialog, QLabel,
                               QLineEdit, QListView, QMainWindow, QMenu, QMessageBox,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem, QStatusBar, QTabBar, QTabWidget,
                               QVBoxLayout,
                               QWidget, QFileDialog, QDialog)
import sys
import os
import mysql.connector
from mobile_business.shouji_chuku import Ui_Form

class Chukuopt_Form(QWidget,Ui_Form):
    def __init__(self):
        super(Chukuopt_Form, self).__init__()
        self.setupUi(self)
        self.widget.setHidden(True)
        self.pushButton.clicked.connect(self.open_choose)
        self.show_kuncunlist()
        self.list1=["手机型号","颜色","内存","串号","店铺名","仓库","渠道","外观成色","电池效率","维修情况","回收价","批发价","散客价","备注"
                    ,"货物状态","手机图像","是否售出","入库时间"]
        self.list2=["客户姓名","电话","信息","出售时间","串号","渠道","销售价格","图像","配件"]
        self.lineEdit.setPlaceholderText("请输入手机型号")
        self.set_completer()
        self.lineEdit.textChanged.connect(self.show_kuncunlist)

    def set_completer(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        cursor.execute("SELECT model FROM 手机入库 WHERE is_sold = 1")
        results = cursor.fetchall()
        models = [row[0] for row in results]

        # 创建 QCompleter 和 QStringListModel
        model = QStringListModel(models, self)
        completer = QCompleter(model, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer)

        cursor.close()
        db.close()
    def open_choose(self):
        if self.widget.isHidden():
            self.widget.setHidden(False)
        else:
            self.widget.setHidden(True)

    def show_kuncunlist(self):
        search_text = self.lineEdit.text()
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        if search_text:
            query = "SELECT model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency," \
                    "repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_url, is_sold, Inbound_time " \
                    "FROM 手机入库 WHERE is_sold = 1 AND model LIKE %s"
            cursor.execute(query, ('%' + search_text + '%',))
        else:
            query = "SELECT model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency," \
                    "repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_url, is_sold, Inbound_time " \
                    "FROM 手机入库 WHERE is_sold = 1"
            cursor.execute(query)

        results = cursor.fetchall()
        layout = QVBoxLayout()
        for row in results:
            name, color, memory, entry_time,image_data  = row[0],row[1],row[2], row[17], row[15]
            first_image_data = image_data.split(b',')[0]
            label = QLabel(f"手机型号: {name}, 手机颜色: {color}, 手机内存:{memory  },入库时间: {entry_time  }")
            label.mouseDoubleClickEvent = lambda event, row=row: self.show_details(row)
            layout.addWidget(label)
        container = QWidget()
        container.setLayout(layout)
        self.scrollArea.setWidget(container)
        cursor.close()
        db.close()

    def show_details(self, row):
        details_dialog = QDialog(self)
        details_dialog.setWindowTitle("详细信息")

        # 创建水平布局来容纳两列
        main_layout = QHBoxLayout(details_dialog)

        # 创建两个垂直布局分别显示两列标签
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # 显示基本信息
        for index, value in enumerate(row):
            if index <= 10 or index == 13 or index == 17:
                label = QLabel(f"{self.list1[index]}: {value}")
                left_layout.addWidget(label)

        # 创建一个新的QWidget来容纳图像
        image_container = QWidget()
        image_layout = QVBoxLayout(image_container)

        image_data = row[15]
        if image_data:
            # 使用正则表达式匹配JPEG图像数据
            image_data_list = re.findall(b'\xff\xd8.*?\xff\xd9', image_data, re.DOTALL)
            for image_data in image_data_list:
                pixmap = QPixmap()
                if not pixmap.loadFromData(QByteArray(image_data)):
                    print("Failed to load image data")
                    continue

                # 创建QLabel并设置图像
                image_label = QLabel()
                image_label.setFixedSize(200, 200)  # 设置固定大小
                pixmap = pixmap.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(pixmap)
                image_layout.addWidget(image_label)

        # 将图像容器添加到左侧布局中
        left_layout.addWidget(image_container)

        # 从数据库中查找相同 serial_number 的记录
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        serial_number = row[3]
        cursor = db.cursor()
        query = "SELECT name, phone_number, usr_info, time, serial_number, channel, sale_money, img_url,fittings_name_number FROM 销售录单 WHERE serial_number = %s"
        cursor.execute(query, (serial_number,))
        result = cursor.fetchone()

        # 检查是否找到结果
        if result:
            # 显示查找到的记录
            for index, value in enumerate(result):
                if index <= 6 or index == 8:
                    label = QLabel(f"{self.list2[index]}: {value}")
                    right_layout.addWidget(label)

            # 创建一个新的QWidget来容纳图像
            image_container1 = QWidget()
            image_layout1 = QVBoxLayout(image_container1)

            image_data1 = result[7]  # 假设结果集中第7列是图像数据
            if image_data1:
                # 使用正则表达式匹配JPEG图像数据
                image_data_list1 = re.findall(b'\xff\xd8.*?\xff\xd9', image_data1, re.DOTALL)
                for image_data1 in image_data_list1:
                    pixmap = QPixmap()
                    if not pixmap.loadFromData(QByteArray(image_data1)):
                        print("Failed to load image data")
                        continue

                    # 创建QLabel并设置图像
                    image_label1 = QLabel()
                    image_label1.setFixedSize(200, 200)  # 设置固定大小
                    pixmap = pixmap.scaled(image_label1.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    image_label1.setPixmap(pixmap)
                    image_layout1.addWidget(image_label1)

            # 将图像容器添加到右侧布局中
            right_layout.addWidget(image_container1)

        else:
            # 如果没有找到结果，显示一条消息
            label = QLabel("没有找到相应的记录")
            right_layout.addWidget(label)

        # 将两个垂直布局添加到主水平布局中
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        details_dialog.setLayout(main_layout)
        details_dialog.exec()

