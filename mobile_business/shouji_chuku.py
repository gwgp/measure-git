# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '销售列表.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(796, 575)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_1 = QWidget(self.widget)
        self.widget_1.setObjectName(u"widget_1")
        self.gridLayout_3 = QGridLayout(self.widget_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_1)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.radioButton_8 = QRadioButton(self.widget_1)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout_3.addWidget(self.radioButton_8, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget_1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_3.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.radioButton = QRadioButton(self.widget_1)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_3.addWidget(self.radioButton, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_1, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_5 = QRadioButton(self.widget_2)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout_5.addWidget(self.radioButton_5, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget_2)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout_5.addWidget(self.radioButton_6, 1, 0, 1, 1)

        self.radioButton_7 = QRadioButton(self.widget_2)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout_5.addWidget(self.radioButton_7, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_6 = QGridLayout(self.widget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_15 = QRadioButton(self.widget_4)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_6.addWidget(self.radioButton_15, 1, 1, 1, 1)

        self.radioButton_27 = QRadioButton(self.widget_4)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.gridLayout_6.addWidget(self.radioButton_27, 2, 0, 1, 1)

        self.radioButton_28 = QRadioButton(self.widget_4)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.gridLayout_6.addWidget(self.radioButton_28, 2, 1, 1, 1)

        self.radioButton_16 = QRadioButton(self.widget_4)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_6.addWidget(self.radioButton_16, 1, 0, 1, 1)

        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 2)

        self.radioButton_31 = QRadioButton(self.widget_4)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.gridLayout_6.addWidget(self.radioButton_31, 3, 1, 1, 1)

        self.radioButton_30 = QRadioButton(self.widget_4)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.gridLayout_6.addWidget(self.radioButton_30, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_7 = QGridLayout(self.widget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.radioButton_17 = QRadioButton(self.widget_5)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.gridLayout_7.addWidget(self.radioButton_17, 1, 1, 1, 1)

        self.radioButton_29 = QRadioButton(self.widget_5)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.gridLayout_7.addWidget(self.radioButton_29, 2, 0, 1, 1)

        self.radioButton_32 = QRadioButton(self.widget_5)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.gridLayout_7.addWidget(self.radioButton_32, 2, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.widget_5)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_7.addWidget(self.radioButton_18, 1, 0, 1, 1)

        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 2)

        self.radioButton_33 = QRadioButton(self.widget_5)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.gridLayout_7.addWidget(self.radioButton_33, 3, 1, 1, 1)

        self.radioButton_34 = QRadioButton(self.widget_5)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.gridLayout_7.addWidget(self.radioButton_34, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_5, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 776, 297))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u7b5b\u9009", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4ed3\u5e93", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"\u4e0d\u9650", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u4e8c\u624b\u673a", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u65b0\u673a", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u5df2\u4ed8\u6b3e\uff0c\u5df2\u5230\u8d27", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5546\u54c1\u72b6\u6001", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u4e0d\u9650", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"\u5df2\u4ed8\u6b3e\uff0c\u672a\u5230\u8d27", None))
        self.radioButton_15.setText(QCoreApplication.translate("Form", u"1000-2000", None))
        self.radioButton_27.setText(QCoreApplication.translate("Form", u"2000-3000", None))
        self.radioButton_28.setText(QCoreApplication.translate("Form", u"3000-4000", None))
        self.radioButton_16.setText(QCoreApplication.translate("Form", u"\u4e0d\u9650", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5165\u5e93\u4ef7\u683c\u533a\u95f4", None))
        self.radioButton_31.setText(QCoreApplication.translate("Form", u"5000\u4ee5\u4e0a", None))
        self.radioButton_30.setText(QCoreApplication.translate("Form", u"4000-5000", None))
        self.radioButton_17.setText(QCoreApplication.translate("Form", u"1000-2000", None))
        self.radioButton_29.setText(QCoreApplication.translate("Form", u"2000-3000", None))
        self.radioButton_32.setText(QCoreApplication.translate("Form", u"3000-4000", None))
        self.radioButton_18.setText(QCoreApplication.translate("Form", u"\u4e0d\u9650", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u4ef7\u683c\u533a\u95f4", None))
        self.radioButton_33.setText(QCoreApplication.translate("Form", u"5000\u4ee5\u4e0a", None))
        self.radioButton_34.setText(QCoreApplication.translate("Form", u"4000-5000", None))
    # retranslateUi

