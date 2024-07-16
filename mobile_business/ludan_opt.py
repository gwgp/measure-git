import os
import re
import shutil
import json
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
from mobile_business.xiaoshou_ludan import Ludan_Form

class Ludanopt_Form(QWidget,Ludan_Form):
    def __init__(self):
        super(Ludanopt_Form,self).__init__()
        self.setupUi(self)
        self.time.setReadOnly(True)  # 设置为只读，防止手动输入
        self.calendarWidget.setHidden(True)
        self.time.mousePressEvent = self.show_calendar  # 点击时显示日历
        self.calendarWidget.clicked.connect(self.set_date_time)  # 选择日期时设置时间
        self.calendarWidget.activated.connect(self.set_date_time)  # 双击日期时设置时间
        self.image_binaries=[]
        self.insert_img.clicked.connect(self.insert_image)
        self.add_fitting.clicked.connect(self.add_fittings)
        self.fitting_name_row = 2  # 初始行号
        self.fitting_quantity_row = 2  # 初始行号
        self.pushButton.clicked.connect(self.write_database)
        self.setTabOrder(self.name,self.phone_number)
        self.setTabOrder(self.phone_number, self.usr_info)
        self.setTabOrder(self.usr_info, self.time)
        self.setTabOrder(self.time,self.serial_number)
        self.setTabOrder(self.serial_number,self.channel)
        self.setTabOrder(self.channel,self.sales_money)
        self.fittings_dict = {}
        self.fittings_name_edits = []  # 用于存储所有的 fittings_name_edit
        self.fittings_quantity_edits = []  # 用于存储所有的 fittings_quantity_edit
    def show_calendar(self, event):
        self.calendarWidget.setHidden(False)

    def set_date_time(self):
        selected_date = self.calendarWidget.selectedDate()
        current_time = QDateTime.currentDateTime().time()
        date_time = QDateTime(selected_date, current_time)
        self.time.setText(date_time.toString("yyyy-MM-dd HH:mm"))
        self.calendarWidget.setHidden(True)  # 选择日期后隐藏日历

    def insert_image(self):
        # 打开文件对话框选择图像
        file_names, _ = QFileDialog.getOpenFileNames(self, "选择图像", "",
                                                     "图像文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*)")
        if file_names:
            # 确保 self.image_url 有一个布局
            if not self.widget.layout():
                self.widget.setLayout(QVBoxLayout())
            # 创建一个水平布局来放置图像
            row_layout = QHBoxLayout()
            self.widget.layout().addLayout(row_layout)
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
    def add_fittings(self):
        # 在 label_10 下方添加 QLineEdit
        fittings_name_edit = QLineEdit(self)
        self.gridLayout_2.addWidget(fittings_name_edit, self.fitting_name_row, 0, 1, 1)
        self.fitting_name_row += 1
        self.fittings_name_edits.append(fittings_name_edit)  # 将 QLineEdit 添加到列表中

        # 在 label_11 下方添加 QLineEdit
        fittings_quantity_edit = QLineEdit(self)
        self.gridLayout_2.addWidget(fittings_quantity_edit, self.fitting_quantity_row, 1, 1, 1)
        self.fitting_quantity_row += 1
        self.fittings_quantity_edits.append(fittings_quantity_edit)  # 将 QLineEdit 添加到列表中

    def write_database(self):
        name=self.name.text() or None
        phone_number=self.phone_number.text() or None
        usr_info=self.usr_info.text() or None
        time=self.time.text() or None
        serial_number=self.serial_number.text() or None
        channel=self.channel.text() or None
        sale_money=self.sales_money.text() or None
        image_binaries_str=b''.join(self.image_binaries) or None
        for name_edit, quantity_edit in zip(self.fittings_name_edits, self.fittings_quantity_edits):
            fitting_name = name_edit.text()
            fitting_quantity = quantity_edit.text()
            self.fittings_dict[fitting_name] = fitting_quantity
        # 连接到数据库并插入数据
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        cursor.execute("""
                INSERT INTO 销售录单 (name, phone_number, usr_info, time, serial_number, channel, sale_money, 
                img_url, fittings_name_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
        name, phone_number, usr_info, time, serial_number, channel, sale_money, image_binaries_str,json.dumps(self.fittings_dict)))

        # 更新手机入库表中的is_sold字段
        cursor.execute("""
                UPDATE 手机入库
                SET is_sold = 1
                WHERE serial_number = %s
                """, (serial_number,))
        db.commit()

        cursor.close()
        db.close()
        # 弹出入库成功消息框
        QMessageBox.information(self, "成功", "提交成功！")

        # 关闭当前窗口
        self.close()

