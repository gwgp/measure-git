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
from mobile_business import ruku_opt,ludan_opt,kucun_opt
class Main_form(QWidget,Ui_Form):
    def __init__(self):
        super(Main_form,self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.page)
        self.shoujiyewu.clicked.connect(self.switch_to_page)
        self.weixiuyewu.clicked.connect(self.switch_to_page_2)
        self.peijianyewu.clicked.connect(self.switch_to_page_3)
        self.zhangdanguanli.clicked.connect(self.switch_to_page_4)
        self.shoujiruku.clicked.connect(self.open_shoujiruku_form)
        self.xiaoshouludan.clicked.connect(self.open_xiaoshou_ludan_form)
        self.kucunshangpin.clicked.connect(self.open_kucun_shangpin_form)
    def switch_to_page(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def switch_to_page_2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
    def switch_to_page_3(self):
        self.stackedWidget.setCurrentWidget(self.page_3)
    def switch_to_page_4(self):
        self.stackedWidget.setCurrentWidget(self.page_4)
    def open_shoujiruku_form(self):
        self.rukuopt_form=ruku_opt.Rukuopt_Form()
        self.rukuopt_form.show()
    def open_xiaoshou_ludan_form(self):
        self.ludanopt_form = ludan_opt.Ludanopt_Form()
        self.ludanopt_form.show()
    def open_kucun_shangpin_form(self):
        self.kucunopt_form=kucun_opt.Kucunopt_Form()
        self.kucunopt_form.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Main_form()
    # 展示窗口
    w.show()
    sys.exit(app.exec())