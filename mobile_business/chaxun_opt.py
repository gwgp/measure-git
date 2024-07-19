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
from mobile_business.shuju_chaxun import Ui_Dialog
class Chaxunopt_Dialog(QWidget,Ui_Dialog):
    def __init__(self):
        super(Chaxunopt_Dialog, self).__init__()
        self.setupUi(self)
        self.show_details()

    def show_details(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()

        # 查询手机入库中 is_sold = 0 的 id 个数
        cursor.execute("SELECT COUNT(id) FROM 手机入库 WHERE is_sold = 0")
        label_count = cursor.fetchone()[0]

        # 查询手机入库中的所有 id 个数
        cursor.execute("SELECT COUNT(id) FROM 手机入库")
        label_2_count = cursor.fetchone()[0]

        # 查询销售录单中的所有记录个数
        cursor.execute("SELECT COUNT(id) FROM 销售录单")
        label_3_count = cursor.fetchone()[0]

        # 查询手机入库中的所有 recycle_price 之和
        cursor.execute("SELECT SUM(recycle_price) FROM 手机入库")
        label_4_sum = cursor.fetchone()[0]

        # 查询销售录单中的所有 sale_money 之和
        cursor.execute("SELECT SUM(sale_money) FROM 销售录单")
        label_5_sum = cursor.fetchone()[0]

        # 查询手机入库和销售录单中有相同 serial_number 的所有 sale_money 之和减去 recycle_price 之和
        cursor.execute("""
            SELECT SUM(销售录单.sale_money) - SUM(手机入库.recycle_price)
            FROM 销售录单
            JOIN 手机入库 ON 销售录单.serial_number = 手机入库.serial_number
        """)
        label_6_diff = cursor.fetchone()[0]
        self.label.setText(f"{label_count}")
        self.label_2.setText(f"{label_2_count}")
        self.label_3.setText(f"{label_3_count}")
        self.label_4.setText(f"{label_4_sum}")
        self.label_5.setText(f"{label_5_sum}")
        self.label_6.setText(f"{label_6_diff}")

        cursor.close()
        db.close()


