# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '维修数据统计.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(605, 539)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.daiweixiu = QLabel(Form)
        self.daiweixiu.setObjectName(u"daiweixiu")

        self.gridLayout.addWidget(self.daiweixiu, 1, 0, 1, 1)

        self.wiexiushouru = QLabel(Form)
        self.wiexiushouru.setObjectName(u"wiexiushouru")

        self.gridLayout.addWidget(self.wiexiushouru, 5, 0, 1, 1)

        self.yiwancheng = QLabel(Form)
        self.yiwancheng.setObjectName(u"yiwancheng")

        self.gridLayout.addWidget(self.yiwancheng, 4, 0, 1, 1)

        self.daiquzou = QLabel(Form)
        self.daiquzou.setObjectName(u"daiquzou")

        self.gridLayout.addWidget(self.daiquzou, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.daiweixiu.setText(QCoreApplication.translate("Form", u"\u5f85\u7ef4\u4fee", None))
        self.wiexiushouru.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u6536\u5165", None))
        self.yiwancheng.setText(QCoreApplication.translate("Form", u"\u5df2\u5b8c\u6210", None))
        self.daiquzou.setText(QCoreApplication.translate("Form", u"\u5f85\u53d6\u8d70", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

