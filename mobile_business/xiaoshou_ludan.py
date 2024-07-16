# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '销售录单.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ludan_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(824, 757)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)

        self.calendarWidget = QCalendarWidget(Form)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 3, 5, 1, 1)

        self.time = QLineEdit(Form)
        self.time.setObjectName(u"time")

        self.gridLayout.addWidget(self.time, 2, 5, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 1)

        self.phone_number = QLineEdit(Form)
        self.phone_number.setObjectName(u"phone_number")

        self.gridLayout.addWidget(self.phone_number, 2, 1, 1, 1)

        self.channel = QLineEdit(Form)
        self.channel.setObjectName(u"channel")

        self.gridLayout.addWidget(self.channel, 5, 0, 1, 1)

        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 2, 0, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 8, 0, 1, 1)

        self.serial_number = QLineEdit(Form)
        self.serial_number.setObjectName(u"serial_number")

        self.gridLayout.addWidget(self.serial_number, 2, 6, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.usr_info = QLineEdit(Form)
        self.usr_info.setObjectName(u"usr_info")

        self.gridLayout.addWidget(self.usr_info, 2, 4, 1, 1)

        self.sales_money = QLineEdit(Form)
        self.sales_money.setObjectName(u"sales_money")

        self.gridLayout.addWidget(self.sales_money, 5, 1, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 11, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.insert_img = QPushButton(self.widget)
        self.insert_img.setObjectName(u"insert_img")
        self.insert_img.setGeometry(QRect(710, 10, 75, 24))

        self.gridLayout.addWidget(self.widget, 7, 0, 1, 7)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.add_fitting = QPushButton(self.widget_3)
        self.add_fitting.setObjectName(u"add_fitting")

        self.gridLayout_2.addWidget(self.add_fitting, 0, 2, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 9, 0, 1, 7)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 11, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 10)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(9, 20)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4e32\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u642d\u914d\u914d\u4ef6", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6e20\u9053", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u4ed8\u6b3e\u622a\u56fe", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u91d1\u989d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u6807\u7b7e", None))
        self.label_8.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u53f7", None))
        self.insert_img.setText(QCoreApplication.translate("Form", u"\u63d2\u5165\u56fe\u50cf", None))
        self.add_fitting.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6570\u91cf", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4", None))
    # retranslateUi

