# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6 import QtWidgets

# class UserInterface(QtWidgets.QMainWindow):
#     pass


from PySide6.QtCore import Slot


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add")
        self.add_button.setGeometry(QRect(180, 480, 113, 32))

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear")
        self.clear_button.setGeometry(QRect(310, 480, 113, 32))

        self.textedit = QTextBrowser(self.centralwidget)
        self.textedit.setObjectName(u"textBrowser")
        self.textedit.setGeometry(QRect(180, 50, 256, 411))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"click", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"del", None))
    # retranslateUi

