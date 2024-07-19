# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '维修入库.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(756, 670)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 588, 427))
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(480, 20, 75, 24))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 11, 1, 1, 5)

        self.lineEdit_10 = QLineEdit(Form)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 10, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 12, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(Form)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 5, 0, 1, 6)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 4, 1, 1)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 6)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(Form)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 10, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 9, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 0, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 3, 1, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 3, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u63d2\u5165\u56fe\u50cf", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u59d3\u540d", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u5165\u5e93", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u524d\u56fe\u7247", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6545\u969c\u63cf\u8ff0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9884\u4f30\u8d39\u7528", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4e32\u53f7", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u6807\u7b7e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u578b\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5de5\u7a0b\u5e08", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u9501\u5c4f\u5bc6\u7801", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6e20\u9053", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6240\u5c5e\u5e97\u94fa", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u5e97\u94fa\u540d1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u5e97\u94fa\u540d2", None))

    # retranslateUi

