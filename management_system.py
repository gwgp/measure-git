import os
import re
import shutil
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,Signal,
    QSize, QStringListModel, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCompleter, QGridLayout, QHBoxLayout, QInputDialog, QLabel, QLineEdit, QListView, QMainWindow, QMenu, QMessageBox,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem, QStatusBar, QTabBar, QTabWidget, QVBoxLayout,
    QWidget)
import sys
import os
import re
import traceback
import pandas as pd
from typing import Optional, List
from os.path import dirname, abspath
from git import Repo  # rely on gitpython
import json
script_dir = os.path.dirname(os.path.abspath(__file__))
# 将脚本所在目录添加到sys.path中
sys.path.insert(0, script_dir)
from main_ui import Ui_Form
from mobile_business import ruku_opt,ludan_opt,kucun_opt,chuku_opt,chaxun_opt
from maintenance_business import ruku_opt as weixiuruku_opt
from maintenance_business import daweixiu_opt,daiquzou_opt,yiwancheng_opt,weixiutongji_opt
from fittings_business import peijianruku_opt,xiaoshouchuku_opt,peijiankucun_opt
class Main_form(QWidget, Ui_Form):
    def __init__(self):
        super(Main_form, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page)

        self.page_switcher = PageSwitcher(self)
        self.page_switcher2 = PageSwitcher2(self)
        self.page_switcher3 = PageSwitcher3(self)
        self.page_switcher4 = PageSwitcher4(self)
        self.page_switcher.switch_to_page()

        self.shoujiyewu.clicked.connect(self.page_switcher.switch_to_page)
        self.weixiuyewu.clicked.connect(self.page_switcher2.switch_to_page_2)
        self.peijianyewu.clicked.connect(self.page_switcher3.switch_to_page_3)
        self.zhangdanguanli.clicked.connect(self.page_switcher4.switch_to_page_4)

class PageSwitcher:
    def __init__(self, main_form):
        self.main_form = main_form
    def switch_to_page(self):
        self.main_form.stackedWidget.setCurrentWidget(self.main_form.page)
        self.main_form.shoujiruku.clicked.connect(self.open_shoujiruku_form)
        self.main_form.xiaoshouludan.clicked.connect(self.open_xiaoshou_ludan_form)
        self.main_form.kucunshangpin.clicked.connect(self.open_kucun_shangpin_form)
        self.main_form.xiaoshouliebiao.clicked.connect(self.open_chuku_shangpin_form)
        self.main_form.shujuchaxun_2.clicked.connect(self.open_shuju_chaxun_form)

    def open_shoujiruku_form(self):
        self.main_form.rukuopt_form = ruku_opt.Rukuopt_Form()
        self.main_form.rukuopt_form.show()

    def open_xiaoshou_ludan_form(self):
        self.main_form.ludanopt_form = ludan_opt.Ludanopt_Form()
        self.main_form.ludanopt_form.show()

    def open_kucun_shangpin_form(self):
        self.main_form.kucunopt_form = kucun_opt.Kucunopt_Form()
        self.main_form.kucunopt_form.show()

    def open_chuku_shangpin_form(self):
        self.main_form.chukuopt_form = chuku_opt.Chukuopt_Form()
        self.main_form.chukuopt_form.show()

    def open_shuju_chaxun_form(self):
        self.main_form.chaxunopt_form = chaxun_opt.Chaxunopt_Dialog()
        self.main_form.chaxunopt_form.show()

class PageSwitcher2:
    def __init__(self, main_form):
        self.main_form = main_form

    def switch_to_page_2(self):
        self.main_form.stackedWidget.setCurrentWidget(self.main_form.page_2)
        self.main_form.weixiuruku.clicked.connect(self.open_weixiuruku_form)
        self.main_form.daiweixiu.clicked.connect(self.open_daiweixiu_form)
        self.main_form.daiquzou.clicked.connect(self.open_daiquzou_form)
        self.main_form.yiwancheng.clicked.connect(self.open_yiwancheng_form)
        self.main_form.shujutongji.clicked.connect(self.open_weixiutongji_form)

    def open_weixiuruku_form(self):
        self.main_form.weixiuopt_form=weixiuruku_opt.Rukuopt_Form()
        self.main_form.weixiuopt_form.show()
    def open_daiweixiu_form(self):
        self.main_form.daiweixiuopt_form=daweixiu_opt.Daiweixiuopt_Form()
        self.main_form.daiweixiuopt_form.show()
    def open_daiquzou_form(self):
        self.main_form.daiquzouopt_form=daiquzou_opt.Daiquzouopt_Form()
        self.main_form.daiquzouopt_form.show()

    def open_yiwancheng_form(self):
        self.main_form.yiwanchengopt_form = yiwancheng_opt.Yiwanchengopt_Form()
        self.main_form.yiwanchengopt_form.show()
    def open_weixiutongji_form(self):
        self.main_form.weixiutongjiopt_form=weixiutongji_opt.Weixiutongjiopt_form()
        self.main_form.weixiutongjiopt_form.show()

class PageSwitcher3:
    def __init__(self, main_form):
        self.main_form = main_form

    def switch_to_page_3(self):
        self.main_form.stackedWidget.setCurrentWidget(self.main_form.page_3)
        self.main_form.peijianruku.clicked.connect(self.open_peijianruku_form)
        self.main_form.xiaoshouchuku.clicked.connect(self.open_xiaoshouchuku_form)
        self.main_form.peijiankucun.clicked.connect(self.open_peijiankucun_form)

    def open_peijianruku_form(self):
        self.main_form.peijianrukuopt_form=peijianruku_opt.Peijianrukuopt_form()
        self.main_form.peijianrukuopt_form.show()
    def open_xiaoshouchuku_form(self):
        self.main_form.xiaoshouchukuopt_form=xiaoshouchuku_opt.Xiaoshouchukuopt_form()
        self.main_form.xiaoshouchukuopt_form.show()
    def open_peijiankucun_form(self):
        self.main_form.peijiankucunopt_form=peijiankucun_opt.Peijiankucun_form()
        self.main_form.peijiankucunopt_form.show()

class PageSwitcher4:
    def __init__(self, main_form):
        self.main_form = main_form

    def switch_to_page_4(self):
        self.main_form.stackedWidget.setCurrentWidget(self.main_form.page_4)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Main_form()
    # 展示窗口
    w.show()
    sys.exit(app.exec())