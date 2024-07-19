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
from mobile_business.kucun_shangpin import Kucun_Form

class Kucunopt_Form(QWidget,Kucun_Form):
    def __init__(self):
        super(Kucunopt_Form, self).__init__()
        self.setupUi(self)
        self.widget.setHidden(True)
        self.pushButton.clicked.connect(self.open_choose)
        self.show_kuncunlist()
        self.list1=["手机型号","颜色","内存","串号","店铺名","仓库","渠道","外观成色","电池效率","维修情况","回收价","批发价","散客价","备注"
                    ,"货物状态","手机图像","是否售出","入库时间"]
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
        cursor.execute("SELECT model FROM 手机入库 WHERE is_sold = 0")
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
                    "FROM 手机入库 WHERE is_sold = 0 AND model LIKE %s"
            cursor.execute(query, ('%' + search_text + '%',))
        else:
            query = "SELECT model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency," \
                    "repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_url, is_sold, Inbound_time " \
                    "FROM 手机入库 WHERE is_sold = 0"
            cursor.execute(query)

        results = cursor.fetchall()
        layout = QVBoxLayout()
        for row in results:
            name, color, memory, entry_time,image_data  = row[0],row[1],row[2], row[17], row[15]
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
        layout = QVBoxLayout(details_dialog)

        for index, value in enumerate(row):
            if index <= 10 or index == 13 or index==17:
                label = QLabel(f"{self.list1[index]}: {value}")
                layout.addWidget(label)
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

        # 将图像容器添加到主布局中
        layout.addWidget(image_container)

        details_dialog.setLayout(layout)
        details_dialog.exec()

