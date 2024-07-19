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
from maintenance_business.weixiutongji import Ui_Form
class Weixiutongjiopt_form(QWidget,Ui_Form):
    def __init__(self):
        super(Weixiutongjiopt_form, self).__init__()
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
        cursor.execute("SELECT COUNT(id) FROM 维修入库 WHERE is_repaired = 0")
        label_count = cursor.fetchone()[0]

        # 查询销售录单中的所有记录个数
        cursor.execute("SELECT COUNT(id) FROM 维修入库 WHERE is_repaired = 1 AND is_done=0")
        label_2_count = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(id) FROM 维修入库 WHERE is_done=1")
        label_3_count = cursor.fetchone()[0]

        # 查询手机入库中的所有 recycle_price 之和
        cursor.execute("SELECT SUM(estimated_cost) FROM 维修入库 WHERE is_done=1")
        label_4_sum = cursor.fetchone()[0]

        self.label.setText(f"{label_count}")
        self.label_2.setText(f"{label_2_count}")
        self.label_3.setText(f"{label_3_count}")
        self.label_4.setText(f"{label_4_sum}")

        cursor.close()
        db.close()


