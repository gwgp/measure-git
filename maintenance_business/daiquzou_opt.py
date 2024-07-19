import os
import re
import shutil
import json
from datetime import datetime

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
from maintenance_business.daiquzou import Ui_Form

class Daiquzouopt_Form(QWidget,Ui_Form):
    def __init__(self):
        super(Daiquzouopt_Form, self).__init__()
        self.setupUi(self)
        self.widget.setHidden(True)
        self.pushButton.clicked.connect(self.open_choose)
        self.list1=["姓名","电话号码","信息","型号","串号","密码","渠道","店铺名","备注","预估价格","工程师","手机图像","入库时间","是否修理完成"
                    ,"是否完成订单","修理完成时间","订单完成时间"]
        self.show_kuncunlist()
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
        cursor.execute("SELECT model FROM 维修入库 WHERE is_repaired = 1")
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
            query = "SELECT name, phone_number, usr_info, model, serial_number, password, channel, store, description, estimated_cost,"\
                     "engineer, img_url, time, is_repaired, is_done,off_time,finish_time "\
                    "FROM 维修入库 WHERE is_done = 0 AND is_repaired=1 AND model LIKE %s"
            cursor.execute(query, ('%' + search_text + '%',))
        else:
            query = "SELECT name, phone_number, usr_info, model, serial_number, password, channel, store, description, estimated_cost,"\
                     "engineer, img_url, time, is_repaired, is_done,off_time,finish_time "\
                    "FROM 维修入库 WHERE is_done = 0 AND is_repaired=1"
            cursor.execute(query)

        results = cursor.fetchall()
        layout = QVBoxLayout()

        for row in results:
            img_data = row[11]
            label = CustomLabel(row, self.list1, img_data,self)
            layout.addWidget(label)
        container = QWidget()
        container.setLayout(layout)
        self.scrollArea.setWidget(container)
        cursor.close()
        db.close()



class CustomLabel(QLabel):
    def __init__(self, row, list1,img_data, main_form, parent=None,):
        super().__init__(parent)
        self.row = row
        self.setText(f"手机型号: {row[3]}, 损坏信息: {row[8]}, 预计价格: {row[9]}, 维修完成时间: {row[15]}")
        self.list1=list1
        self.image_data=img_data
        self.main_form=main_form

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.show_details(self.row)

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        open_details_action = QAction("打开详细信息", self)
        open_details_action.triggered.connect(lambda: self.show_details(self.row))
        menu.addAction(open_details_action)

        mark_repaired_action = QAction("标记已完成", self)
        mark_repaired_action.triggered.connect(lambda: self.mark_as_finsihed(self.row))
        menu.addAction(mark_repaired_action)

        menu.exec_(event.globalPos())

    def show_details(self, row):
        details_dialog = QDialog(self)
        details_dialog.setWindowTitle("详细信息")
        layout = QVBoxLayout(details_dialog)
        for index, value in enumerate(row):
            if index <= 12 and index!=11 :
                label = QLabel(f"{self.list1[index]}: {value}")
                layout.addWidget(label)
        # 创建一个新的QWidget来容纳图像
        image_container = QWidget()
        image_layout = QVBoxLayout(image_container)
        if self.image_data:
            # 使用正则表达式匹配JPEG图像数据
            image_data_list = re.findall(b'\xff\xd8.*?\xff\xd9', self.image_data, re.DOTALL)
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

    def mark_as_finsihed(self, row):
        # 更新数据库中的 is_repaired 字段
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        current_time = datetime.now()
        query = "UPDATE 维修入库 SET is_done = 1,finish_time = %s WHERE serial_number=%s"
        cursor.execute(query, (current_time, row[4]))
        db.commit()
        cursor.close()
        db.close()
        self.main_form.show_kuncunlist()
