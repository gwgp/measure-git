import os
import re
import shutil
from datetime import datetime

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, Signal,
                            QSize, QStringListModel, QTime, QUrl, Qt, QBuffer, QIODevice)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCompleter, QGridLayout, QHBoxLayout, QInputDialog, QLabel,
                               QLineEdit, QListView, QMainWindow, QMenu, QMessageBox,
                               QPushButton, QScrollArea, QSizePolicy, QSpacerItem, QStatusBar, QTabBar, QTabWidget,
                               QVBoxLayout,
                               QWidget, QFileDialog)
import sys
import os
import mysql.connector
from mobile_business.shouji_ruku import Shoujiruku_Form

class Rukuopt_Form(QWidget,Shoujiruku_Form):
    def __init__(self):
        super(Rukuopt_Form,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.write_database)
        self.insert_img.clicked.connect(self.insert_image)
        self.image_binaries = []
        self.setTabOrder(self.model, self.color)
        self.setTabOrder(self.color, self.memory)
        self.setTabOrder(self.memory, self.serial_number)
        self.setTabOrder(self.serial_number, self.channel)
        self.setTabOrder(self.channel, self.appearance_condition)
        self.setTabOrder(self.appearance_condition, self.battery_efficiency)
        self.setTabOrder(self.battery_efficiency, self.repair_status)
        self.setTabOrder(self.repair_status, self.recycle_price)
        self.setTabOrder(self.recycle_price, self.wholesale_price)
        self.setTabOrder(self.wholesale_price, self.retail_price)
        self.setTabOrder(self.retail_price, self.notes)



    def insert_image(self):
        # 打开文件对话框选择图像
        file_names, _ = QFileDialog.getOpenFileNames(self, "选择图像", "",
                                                     "图像文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*)")
        if file_names:
            # 确保 self.image_url 有一个布局
            if not self.image_url.layout():
                self.image_url.setLayout(QVBoxLayout())

            # 创建一个水平布局来放置图像
            row_layout = QHBoxLayout()
            self.image_url.layout().addLayout(row_layout)

            for file_name in file_names:
                # 创建 QLabel 并设置图像
                label = QLabel(self)
                pixmap = QPixmap(file_name)
                buffer = QBuffer()
                buffer.open(QIODevice.WriteOnly)
                pixmap.save(buffer, "jpg")
                self.image_binaries.append(buffer.data())
                scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                label.setPixmap(scaled_pixmap)
                label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                # 将 QLabel 添加到水平布局中
                row_layout.addWidget(label)

    def write_database(self):
        model = self.model.text() or None
        color = self.color.text() or None
        memory = self.memory.text() or None
        serial_number = self.serial_number.text() or None
        store = self.store.currentText() or None
        warehouse = self.warehouse.currentText() or None
        channel = self.channel.text() or None
        appearance_condition = self.appearance_condition.text() or None
        battery_efficiency = self.battery_efficiency.text() or None
        repair_status = self.repair_status.text() or None
        recycle_price = self.recycle_price.text() or None
        wholesale_price = self.wholesale_price.text() or None
        retail_price = self.retail_price.text() or None
        notes = self.notes.text() or None
        status = self.status.currentText() or None
        image_binaries_str=b''.join(self.image_binaries) or None

        # 连接到数据库并插入数据
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()

        current_time = datetime.now()

        cursor.execute("""
            INSERT INTO 手机入库 (model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency, repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_url, is_sold, Inbound_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
        model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency,
        repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_binaries_str, 0,
        current_time))

        db.commit()
        cursor.close()
        db.close()

        # 弹出入库成功消息框
        QMessageBox.information(self, "成功", "入库成功！")

        # 关闭当前窗口
        self.close()




