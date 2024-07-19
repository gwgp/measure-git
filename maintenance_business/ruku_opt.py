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
from maintenance_business.weixiu_ruku import Ui_Form

class Rukuopt_Form(QWidget,Ui_Form):
    def __init__(self):
        super(Rukuopt_Form,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.write_database)
        self.pushButton_2.clicked.connect(self.insert_image)
        self.image_binaries = []
        self.setTabOrder(self.lineEdit, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        self.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        self.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        self.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        self.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        self.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        self.setTabOrder(self.lineEdit_9, self.lineEdit_10)


    def insert_image(self):
        # 打开文件对话框选择图像
        file_names, _ = QFileDialog.getOpenFileNames(self, "选择图像", "",
                                                     "图像文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*)")
        if file_names:
            # 确保 self.image_url 有一个布局
            if not self.scrollArea.layout():
                self.scrollArea.setLayout(QVBoxLayout())

            # 创建一个水平布局来放置图像
            row_layout = QHBoxLayout()
            self.scrollArea.layout().addLayout(row_layout)

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
        name = self.lineEdit.text() or None
        phone_number = self.lineEdit_2.text() or None
        usr_info = self.lineEdit_3.text() or None
        model = self.lineEdit_4.text() or None
        serial_number = self.lineEdit_5.text() or None
        password = self.lineEdit_6.text() or None
        channel = self.lineEdit_7.text() or None
        store = self.comboBox_2.currentText() or None
        description = self.lineEdit_8.text() or None
        estimated_cost = self.lineEdit_9.text() or None
        engineer = self.lineEdit_10.text() or None
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
            INSERT INTO 维修入库 (name, phone_number, usr_info, model, serial_number, password, channel, store, description, estimated_cost, engineer, img_url, time, is_repaired,is_done)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
            """, (
        name, phone_number, usr_info, model, serial_number, password, channel, store, description, estimated_cost, engineer, image_binaries_str, current_time, 0, 0))

        db.commit()
        cursor.close()
        db.close()

        # 弹出入库成功消息框
        QMessageBox.information(self, "成功", "入库成功！")

        # 关闭当前窗口
        self.close()