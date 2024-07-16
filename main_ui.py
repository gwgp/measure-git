# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jiemian.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(873, 779)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shoujiyewu = QPushButton(self.widget)
        self.shoujiyewu.setObjectName(u"shoujiyewu")

        self.horizontalLayout.addWidget(self.shoujiyewu)

        self.weixiuyewu = QPushButton(self.widget)
        self.weixiuyewu.setObjectName(u"weixiuyewu")

        self.horizontalLayout.addWidget(self.weixiuyewu)

        self.peijianyewu = QPushButton(self.widget)
        self.peijianyewu.setObjectName(u"peijianyewu")

        self.horizontalLayout.addWidget(self.peijianyewu)

        self.zhangdanguanli = QPushButton(self.widget)
        self.zhangdanguanli.setObjectName(u"zhangdanguanli")

        self.horizontalLayout.addWidget(self.zhangdanguanli)

        self.shujuchaxun = QPushButton(self.widget)
        self.shujuchaxun.setObjectName(u"shujuchaxun")

        self.horizontalLayout.addWidget(self.shujuchaxun)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.shoujiruku = QPushButton(self.page)
        self.shoujiruku.setObjectName(u"shoujiruku")

        self.horizontalLayout_2.addWidget(self.shoujiruku)

        self.xiaoshouludan = QPushButton(self.page)
        self.xiaoshouludan.setObjectName(u"xiaoshouludan")

        self.horizontalLayout_2.addWidget(self.xiaoshouludan)

        self.kucunshangpin = QPushButton(self.page)
        self.kucunshangpin.setObjectName(u"kucunshangpin")

        self.horizontalLayout_2.addWidget(self.kucunshangpin)

        self.yingshouzhangkuan = QPushButton(self.page)
        self.yingshouzhangkuan.setObjectName(u"yingshouzhangkuan")

        self.horizontalLayout_2.addWidget(self.yingshouzhangkuan)

        self.xiaoshouliebiao = QPushButton(self.page)
        self.xiaoshouliebiao.setObjectName(u"xiaoshouliebiao")

        self.horizontalLayout_2.addWidget(self.xiaoshouliebiao)

        self.shujuchaxun_2 = QPushButton(self.page)
        self.shujuchaxun_2.setObjectName(u"shujuchaxun_2")

        self.horizontalLayout_2.addWidget(self.shujuchaxun_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.weixiuruku = QPushButton(self.page_2)
        self.weixiuruku.setObjectName(u"weixiuruku")

        self.horizontalLayout_3.addWidget(self.weixiuruku)

        self.daiweixiu = QPushButton(self.page_2)
        self.daiweixiu.setObjectName(u"daiweixiu")

        self.horizontalLayout_3.addWidget(self.daiweixiu)

        self.daiquzou = QPushButton(self.page_2)
        self.daiquzou.setObjectName(u"daiquzou")

        self.horizontalLayout_3.addWidget(self.daiquzou)

        self.yiwancheng = QPushButton(self.page_2)
        self.yiwancheng.setObjectName(u"yiwancheng")

        self.horizontalLayout_3.addWidget(self.yiwancheng)

        self.yingshouzhangkuan_2 = QPushButton(self.page_2)
        self.yingshouzhangkuan_2.setObjectName(u"yingshouzhangkuan_2")

        self.horizontalLayout_3.addWidget(self.yingshouzhangkuan_2)

        self.shujutongji = QPushButton(self.page_2)
        self.shujutongji.setObjectName(u"shujutongji")

        self.horizontalLayout_3.addWidget(self.shujutongji)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_4 = QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.peijianruku = QPushButton(self.page_3)
        self.peijianruku.setObjectName(u"peijianruku")

        self.horizontalLayout_4.addWidget(self.peijianruku)

        self.xiaoshouchuku = QPushButton(self.page_3)
        self.xiaoshouchuku.setObjectName(u"xiaoshouchuku")

        self.horizontalLayout_4.addWidget(self.xiaoshouchuku)

        self.zengjiapeijian = QPushButton(self.page_3)
        self.zengjiapeijian.setObjectName(u"zengjiapeijian")

        self.horizontalLayout_4.addWidget(self.zengjiapeijian)

        self.kucunbianhuarizhi = QPushButton(self.page_3)
        self.kucunbianhuarizhi.setObjectName(u"kucunbianhuarizhi")

        self.horizontalLayout_4.addWidget(self.kucunbianhuarizhi)

        self.peijiankucun = QPushButton(self.page_3)
        self.peijiankucun.setObjectName(u"peijiankucun")

        self.horizontalLayout_4.addWidget(self.peijiankucun)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.zhangdanguanli_2 = QPushButton(self.page_4)
        self.zhangdanguanli_2.setObjectName(u"zhangdanguanli_2")

        self.horizontalLayout_5.addWidget(self.zhangdanguanli_2)

        self.chakanzhangdan = QPushButton(self.page_4)
        self.chakanzhangdan.setObjectName(u"chakanzhangdan")

        self.horizontalLayout_5.addWidget(self.chakanzhangdan)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 54, 16))
        self.widget1 = QWidget(self.widget_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 48, 811, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.jinriyingyee = QPushButton(self.widget1)
        self.jinriyingyee.setObjectName(u"jinriyingyee")

        self.horizontalLayout_6.addWidget(self.jinriyingyee)

        self.xianjinzhichu = QPushButton(self.widget1)
        self.xianjinzhichu.setObjectName(u"xianjinzhichu")

        self.horizontalLayout_6.addWidget(self.xianjinzhichu)

        self.lirunmingxi = QPushButton(self.widget1)
        self.lirunmingxi.setObjectName(u"lirunmingxi")

        self.horizontalLayout_6.addWidget(self.lirunmingxi)

        self.yingshouzhangkuan_3 = QPushButton(self.widget1)
        self.yingshouzhangkuan_3.setObjectName(u"yingshouzhangkuan_3")

        self.horizontalLayout_6.addWidget(self.yingshouzhangkuan_3)

        self.zaikujine = QPushButton(self.widget1)
        self.zaikujine.setObjectName(u"zaikujine")

        self.horizontalLayout_6.addWidget(self.zaikujine)


        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.shoujiyewu_2 = QPushButton(self.widget_3)
        self.shoujiyewu_2.setObjectName(u"shoujiyewu_2")

        self.horizontalLayout_7.addWidget(self.shoujiyewu_2)

        self.weixiuyewu_2 = QPushButton(self.widget_3)
        self.weixiuyewu_2.setObjectName(u"weixiuyewu_2")

        self.horizontalLayout_7.addWidget(self.weixiuyewu_2)

        self.peijianyewu_2 = QPushButton(self.widget_3)
        self.peijianyewu_2.setObjectName(u"peijianyewu_2")

        self.horizontalLayout_7.addWidget(self.peijianyewu_2)


        self.gridLayout.addWidget(self.widget_3, 3, 0, 1, 1)

        self.stackedWidget_4 = QStackedWidget(Form)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4Page1 = QWidget()
        self.stackedWidget_4Page1.setObjectName(u"stackedWidget_4Page1")
        self.horizontalLayout_8 = QHBoxLayout(self.stackedWidget_4Page1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.jinriruku = QPushButton(self.stackedWidget_4Page1)
        self.jinriruku.setObjectName(u"jinriruku")

        self.horizontalLayout_8.addWidget(self.jinriruku)

        self.pushButton_2 = QPushButton(self.stackedWidget_4Page1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.stackedWidget_4Page1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.stackedWidget_4Page1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.stackedWidget_4Page1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.stackedWidget_4Page1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_8.addWidget(self.pushButton_5)

        self.stackedWidget_4.addWidget(self.stackedWidget_4Page1)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_9 = QHBoxLayout(self.page_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.page_5)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.pushButton_7 = QPushButton(self.page_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_9.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.page_5)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_9.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.page_5)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_9.addWidget(self.pushButton_8)

        self.pushButton_10 = QPushButton(self.page_5)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_9.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.page_5)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_9.addWidget(self.pushButton_11)

        self.stackedWidget_4.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_10 = QHBoxLayout(self.page_6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_12 = QPushButton(self.page_6)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_10.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.page_6)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_10.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.page_6)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_10.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.page_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_10.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.page_6)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_10.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.page_6)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_10.addWidget(self.pushButton_17)

        self.stackedWidget_4.addWidget(self.page_6)

        self.gridLayout.addWidget(self.stackedWidget_4, 4, 0, 1, 1)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 54, 16))
        self.comboBox = QComboBox(self.widget_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(760, 10, 68, 22))

        self.gridLayout.addWidget(self.widget_4, 5, 0, 3, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.shoujiyewu.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u4e1a\u52a1", None))
        self.weixiuyewu.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u4e1a\u52a1", None))
        self.peijianyewu.setText(QCoreApplication.translate("Form", u"\u914d\u4ef6\u4e1a\u52a1", None))
        self.zhangdanguanli.setText(QCoreApplication.translate("Form", u"\u8d26\u5355\u7ba1\u7406", None))
        self.shujuchaxun.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u67e5\u8be2", None))
        self.shoujiruku.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u5165\u5e93", None))
        self.xiaoshouludan.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5f55\u5355", None))
        self.kucunshangpin.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u5546\u54c1", None))
        self.yingshouzhangkuan.setText(QCoreApplication.translate("Form", u"\u5e94\u6536\u8d26\u6b3e", None))
        self.xiaoshouliebiao.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u5217\u8868", None))
        self.shujuchaxun_2.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u67e5\u8be2", None))
        self.weixiuruku.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u5165\u5e93", None))
        self.daiweixiu.setText(QCoreApplication.translate("Form", u"\u5f85\u7ef4\u4fee", None))
        self.daiquzou.setText(QCoreApplication.translate("Form", u"\u5f85\u53d6\u8d70", None))
        self.yiwancheng.setText(QCoreApplication.translate("Form", u"\u5df2\u5b8c\u6210", None))
        self.yingshouzhangkuan_2.setText(QCoreApplication.translate("Form", u"\u5e94\u6536\u8d26\u6b3e", None))
        self.shujutongji.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u7edf\u8ba1", None))
        self.peijianruku.setText(QCoreApplication.translate("Form", u"\u914d\u4ef6\u5165\u5e93", None))
        self.xiaoshouchuku.setText(QCoreApplication.translate("Form", u"\u9500\u552e\u51fa\u5e93", None))
        self.zengjiapeijian.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u914d\u4ef6", None))
        self.kucunbianhuarizhi.setText(QCoreApplication.translate("Form", u"\u5e93\u5b58\u53d8\u5316\u65e5\u5fd7", None))
        self.peijiankucun.setText(QCoreApplication.translate("Form", u"\u914d\u4ef6\u5e93\u5b58", None))
        self.zhangdanguanli_2.setText(QCoreApplication.translate("Form", u"\u8d26\u5355\u7ba1\u7406", None))
        self.chakanzhangdan.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u8d26\u5355", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e1a\u52a1\u6c47\u603b", None))
        self.jinriyingyee.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u8425\u4e1a\u989d", None))
        self.xianjinzhichu.setText(QCoreApplication.translate("Form", u"\u73b0\u91d1\u652f\u51fa", None))
        self.lirunmingxi.setText(QCoreApplication.translate("Form", u"\u5229\u6da6\u660e\u7ec6", None))
        self.yingshouzhangkuan_3.setText(QCoreApplication.translate("Form", u"\u5e94\u6536\u8d26\u6b3e", None))
        self.zaikujine.setText(QCoreApplication.translate("Form", u"\u5728\u5e93\u91d1\u989d", None))
        self.shoujiyewu_2.setText(QCoreApplication.translate("Form", u"\u624b\u673a\u4e1a\u52a1", None))
        self.weixiuyewu_2.setText(QCoreApplication.translate("Form", u"\u7ef4\u4fee\u4e1a\u52a1", None))
        self.peijianyewu_2.setText(QCoreApplication.translate("Form", u"\u914d\u4ef6\u4e1a\u52a1", None))
        self.jinriruku.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5165\u5e93", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u51fa\u5e93", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5229\u6da6", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5f85\u6536\u8d26", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u5728\u5e93\u91d1\u989d", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5df2\u4ed8\u6b3e\u672a\u5230\u8d27", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5165\u5e93", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5f85\u53d6\u8d70", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5df2\u5b8c\u6210", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u4ee3\u6536\u6b3e", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u5728\u4fee\u8ba2\u5355\u4e2a\u6570", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5229\u6da6", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u5165\u5e93", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"\u4eca\u65e5\u51fa\u5e93", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"\u914d\u5408\u624b\u673a\u9500\u552e", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"\u914d\u5408\u7ef4\u4fee\u4f7f\u7528", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u5728\u5e93\u91d1\u989d", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"\u76f4\u63a5\u9500\u552e\u5229\u6da6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6536\u5165\u6c47\u603b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u672c\u5468", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u4e0a\u5468", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u672c\u6708", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u4e0a\u6708", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u672c\u5e74", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u53bb\u5e74", None))

    # retranslateUi

