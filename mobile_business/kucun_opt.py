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

    def open_choose(self):
        if self.widget.isHidden():
            self.widget.setHidden(False)
        else:
            self.widget.setHidden(True)

    def show_kuncunlist(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        cursor.execute("SELECT model, color, memory, serial_number, store, warehouse, channel, appearance_condition, battery_efficiency,"
                       "repair_status, recycle_price, wholesale_price, retail_price, notes, status, image_url, is_sold, Inbound_time FROM 手机入库 WHERE is_sold = 0")

        results = cursor.fetchall()
        layout = QVBoxLayout()
        for row in results:
            name, color, memory, entry_time = row[:4]
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
            label = QLabel(f"字段{index + 1}: {value}")
            layout.addWidget(label)

        details_dialog.setLayout(layout)
        details_dialog.exec()

