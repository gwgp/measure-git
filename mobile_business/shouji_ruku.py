# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '手机入库.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QWidget)

class Shoujiruku_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(906, 840)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.color = QLineEdit(Form)
        self.color.setObjectName(u"color")

        self.gridLayout.addWidget(self.color, 1, 1, 1, 1)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)

        self.channel = QLineEdit(Form)
        self.channel.setObjectName(u"channel")

        self.gridLayout.addWidget(self.channel, 3, 1, 1, 1)

        self.appearance_condition = QLineEdit(Form)
        self.appearance_condition.setObjectName(u"appearance_condition")

        self.gridLayout.addWidget(self.appearance_condition, 3, 2, 1, 1)

        self.battery_efficiency = QLineEdit(Form)
        self.battery_efficiency.setObjectName(u"battery_efficiency")

        self.gridLayout.addWidget(self.battery_efficiency, 3, 3, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.wholesale_price = QLineEdit(Form)
        self.wholesale_price.setObjectName(u"wholesale_price")

        self.gridLayout.addWidget(self.wholesale_price, 5, 1, 1, 1)

        self.retail_price = QLineEdit(Form)
        self.retail_price.setObjectName(u"retail_price")

        self.gridLayout.addWidget(self.retail_price, 5, 2, 1, 1)

        self.notes = QLineEdit(Form)
        self.notes.setObjectName(u"notes")

        self.gridLayout.addWidget(self.notes, 5, 3, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.recycle_price = QLineEdit(Form)
        self.recycle_price.setObjectName(u"recycle_price")

        self.gridLayout.addWidget(self.recycle_price, 5, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 4, 1, 1)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 4, 3, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.memory = QLineEdit(Form)
        self.memory.setObjectName(u"memory")

        self.gridLayout.addWidget(self.memory, 1, 2, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 4, 4, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.serial_number = QLineEdit(Form)
        self.serial_number.setObjectName(u"serial_number")

        self.gridLayout.addWidget(self.serial_number, 1, 3, 1, 1)

        self.status = QComboBox(Form)
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")

        self.gridLayout.addWidget(self.status, 5, 4, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.warehouse = QComboBox(Form)
        self.warehouse.addItem("")
        self.warehouse.addItem("")
        self.warehouse.setObjectName(u"warehouse")
        self.warehouse.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.warehouse, 3, 0, 1, 1)

        self.repair_status = QLineEdit(Form)
        self.repair_status.setObjectName(u"repair_status")

        self.gridLayout.addWidget(self.repair_status, 3, 4, 1, 1)

        self.model = QLineEdit(Form)
        self.model.setObjectName(u"model")

        self.gridLayout.addWidget(self.model, 1, 0, 1, 1)

        self.store = QComboBox(Form)
        self.store.addItem("")
        self.store.addItem("")
        self.store.setObjectName(u"store")

        self.gridLayout.addWidget(self.store, 1, 4, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)

        self.image_url = QScrollArea(Form)
        self.image_url.setObjectName(u"image_url")
        self.image_url.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 707, 643))
        self.insert_img = QPushButton(self.scrollAreaWidgetContents)
        self.insert_img.setObjectName(u"insert_img")
        self.insert_img.setGeometry(QRect(20, 20, 75, 24))
        self.image_url.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.image_url, 6, 1, 1, 4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u578b\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6e20\u9053", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u5185\u5b58", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u56de\u6536\u4ef7", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4ed3\u5e93", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6240\u5c5e\u5e97\u94fa", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e32\u53f7", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6563\u5ba2\u4ef7", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u60c5\u51b5", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5916\u89c2\u6210\u8272", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u989c\u8272", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u8d27\u7269\u72b6\u6001", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6279\u53d1\u4ef7", None))
        self.status.setItemText(0, QCoreApplication.translate("Form", u"\u5df2\u4ed8\u6b3e\uff0c\u5df2\u5230\u8d27", None))
        self.status.setItemText(1, QCoreApplication.translate("Form", u"\u5df2\u4ed8\u6b3e\uff0c\u672a\u5230\u8d27", None))

        self.label_9.setText(QCoreApplication.translate("Form", u"\u7535\u6c60\u6548\u7387", None))
        self.warehouse.setItemText(0, QCoreApplication.translate("Form", u"\u4e8c\u624b\u673a", None))
        self.warehouse.setItemText(1, QCoreApplication.translate("Form", u"\u65b0\u673a", None))

        self.store.setItemText(0, QCoreApplication.translate("Form", u"\u5e97\u94fa\u540d1", None))
        self.store.setItemText(1, QCoreApplication.translate("Form", u"\u5e97\u94fa\u540d2", None))

        self.label_11.setText(QCoreApplication.translate("Form", u"\u56fe\u7247", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u5165\u5e93", None))
        self.insert_img.setText(QCoreApplication.translate("Form", u"\u63d2\u5165\u56fe\u50cf", None))
    # retranslateUi

