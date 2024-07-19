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
                               QWidget, QFileDialog, QDialog)
import sys
import os
import mysql.connector
from fittings_business.peijiankucun import Ui_Form
class Peijiankucun_form(QWidget,Ui_Form):
    def __init__(self):
        super(Peijiankucun_form, self).__init__()
        self.setupUi(self)
