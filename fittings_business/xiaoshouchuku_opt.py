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
                               QWidget, QFileDialog, QDialog, QComboBox)
import sys
import os
import mysql.connector
from fittings_business.xiaoshouchuku import Ui_Form
class Xiaoshouchukuopt_form(QWidget,Ui_Form):
    def __init__(self):
        super(Xiaoshouchukuopt_form, self).__init__()
        self.setupUi(self)

        self.setTabOrder(self.lineEdit, self.comboBox)
        self.setTabOrder(self.comboBox, self.lineEdit_3)
        self.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        self.pushButton.clicked.connect(self.add_line)
        self.pushButton_2.clicked.connect(self.write_database)
        self.row_count = 3  # 初始行数

        # 存储新生成的控件
        self.new_line_edits = [(self.lineEdit, self.lineEdit_3, self.lineEdit_4)]
        self.new_combo_boxes = [self.comboBox]
        self.lineEdit.setPlaceholderText("请输入配件名")
        self.set_completer(self.lineEdit)
    def set_completer(self, line_edit):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()
        cursor.execute("SELECT name FROM 配件入库")
        results = cursor.fetchall()
        names = [row[0] for row in results]

        # 创建 QCompleter 和 QStringListModel
        name_model = QStringListModel(names, self)
        completer = QCompleter(name_model, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)  # 设置为包含匹配模式
        line_edit.setCompleter(completer)

        cursor.close()
        db.close()

    def add_line(self):
        # 创建新的 QLineEdit 和 QComboBox
        new_line_edit_1 = QLineEdit(self)
        new_line_edit_2 = QLineEdit(self)
        new_line_edit_3 = QLineEdit(self)
        new_combo_box = QComboBox(self)

        # 复制现有 comboBox 的选项
        for index in range(self.comboBox.count()):
            new_combo_box.addItem(self.comboBox.itemText(index))

        # 设置大小策略
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        new_line_edit_1.setSizePolicy(sizePolicy1)
        new_line_edit_2.setSizePolicy(sizePolicy1)
        new_line_edit_3.setSizePolicy(sizePolicy1)
        new_combo_box.setSizePolicy(sizePolicy1)

        # 设置占位符文本和 completer
        new_line_edit_1.setPlaceholderText("请输入配件名")
        self.set_completer(new_line_edit_1)

        # 将新控件添加到布局中
        self.gridLayout.addWidget(new_line_edit_1, self.row_count, 0, 1, 1)
        self.gridLayout.addWidget(new_combo_box, self.row_count, 1, 1, 1)
        self.gridLayout.addWidget(new_line_edit_2, self.row_count, 2, 1, 1)
        self.gridLayout.addWidget(new_line_edit_3, self.row_count, 3, 1, 1)

        # 将新控件存储到列表中
        self.new_line_edits.append((new_line_edit_1, new_line_edit_2, new_line_edit_3))
        self.new_combo_boxes.append(new_combo_box)

        # 更新行数
        self.row_count += 1

        # 将 pushButton_2 移动到最后一行
        self.gridLayout.addWidget(self.pushButton_2, self.row_count, 0, 1, 1)

        # 调整布局，使新添加的控件紧凑排列
        for i in range(self.row_count):
            self.gridLayout.setRowStretch(i, 0)
        self.gridLayout.setRowStretch(self.row_count, 1)

    def write_database(self):
        # 连接到数据库
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aa..123456",
            database="second_hand_repair_system"
        )
        cursor = db.cursor()

        current_time = datetime.now()

        for line_edits, combo_box in zip(self.new_line_edits, self.new_combo_boxes):
            name = line_edits[0].text()

            channel = combo_box.currentText()
            off_number = line_edits[1].text()
            all_out_price = line_edits[2].text()
            if not name or not channel or not off_number or not all_out_price:
                QMessageBox.warning(self, "警告", "所有字段必须填写完整！")
                return
            try:
                off_number = int(off_number)
                all_out_price = float(all_out_price)
            except ValueError:
                QMessageBox.warning(self, "警告", "数量和总价必须是数字！")
                return
            cursor.execute(
                "SELECT name, type, number, all_cost,present_cost FROM 配件入库 WHERE name = %s",
                (name,))
            result = cursor.fetchone()
            if result is None:
                QMessageBox.warning(self, "警告", f"未找到名为{name}的记录！")
                return
            new_number = int(result[2])-off_number
            if new_number < 0:
                QMessageBox.information(self, "失败", f"{name }库存不足！")
            else:
                cursor.execute("""
                                UPDATE 配件入库
                                SET number = %s WHERE name = %s
                            """, (new_number, name))
                cost_money = float(result[4])*int(off_number)
                sale_money = float(all_out_price)
                earn_money = sale_money-cost_money
                cursor.execute("""
                                    INSERT INTO 销售记录
                                    (name, number, cost_money, sale_money, earn_money, out_time)
                                    VALUES (%s, %s, %s, %s, %s, %s)
                                """, (name, off_number, cost_money, sale_money, earn_money, current_time))

        db.commit()
        cursor.close()
        db.close()

        # 弹出入库成功消息框
        QMessageBox.information(self, "成功", "出库成功！")

        # 关闭当前窗口
        self.close()