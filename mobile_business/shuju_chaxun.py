# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '数据查询.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(442, 459)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.xiaoshoushouru = QLabel(Dialog)
        self.xiaoshoushouru.setObjectName(u"xiaoshoushouru")

        self.gridLayout.addWidget(self.xiaoshoushouru, 4, 0, 1, 1)

        self.kucunshuliang = QLabel(Dialog)
        self.kucunshuliang.setObjectName(u"kucunshuliang")

        self.gridLayout.addWidget(self.kucunshuliang, 0, 0, 1, 1)

        self.leijiruku = QLabel(Dialog)
        self.leijiruku.setObjectName(u"leijiruku")

        self.gridLayout.addWidget(self.leijiruku, 1, 0, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.goujichengben = QLabel(Dialog)
        self.goujichengben.setObjectName(u"goujichengben")

        self.gridLayout.addWidget(self.goujichengben, 3, 0, 1, 1)

        self.leijichuku = QLabel(Dialog)
        self.leijichuku.setObjectName(u"leijichuku")

        self.gridLayout.addWidget(self.leijichuku, 2, 0, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.yingyu = QLabel(Dialog)
        self.yingyu.setObjectName(u"yingyu")

        self.gridLayout.addWidget(self.yingyu, 5, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.xiaoshoushouru.setText(QCoreApplication.translate("Dialog", u"\u9500\u552e\u6536\u5165", None))
        self.kucunshuliang.setText(QCoreApplication.translate("Dialog", u"\u5e93\u5b58\u6570\u91cf", None))
        self.leijiruku.setText(QCoreApplication.translate("Dialog", u"\u7d2f\u8ba1\u5165\u5e93", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.goujichengben.setText(QCoreApplication.translate("Dialog", u"\u8d2d\u673a\u6210\u672c", None))
        self.leijichuku.setText(QCoreApplication.translate("Dialog", u"\u7d2f\u8ba1\u51fa\u5e93", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.yingyu.setText(QCoreApplication.translate("Dialog", u"\u76c8\u4f59", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

