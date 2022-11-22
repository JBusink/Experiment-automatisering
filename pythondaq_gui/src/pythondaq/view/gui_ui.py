# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_app_scan.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDoubleSpinBox, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpinBox,
    QSplitter, QStatusBar, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(20, 10, 761, 421))

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(150, 440, 194, 24))

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 440, 121, 96))
        self.splitter.setOrientation(Qt.Vertical)

        self.scan_button = QSpinBox(self.splitter)
        self.scan_button.setObjectName(u"spinBox")
        self.scan_button.setMinimum(2)
        self.scan_button.setMaximum(999)
        self.splitter.addWidget(self.scan_button)

        self.steps_button = QSpinBox(self.splitter)
        self.steps_button.setObjectName(u"steps_button")
        self.steps_button.setMinimum(21)
        self.splitter.addWidget(self.steps_button)

        self.stop_voltage_button = QDoubleSpinBox(self.splitter)
        self.stop_voltage_button.setObjectName(u"doubleSpinBox")
        self.stop_voltage_button.setDecimals(1)
        self.stop_voltage_button.setMaximum(3.300000000000000)
        self.stop_voltage_button.setSingleStep(0.100000000000000)
        self.stop_voltage_button.setValue(3.300000000000000)
        self.splitter.addWidget(self.stop_voltage_button)

        self.start_voltage_button = QDoubleSpinBox(self.splitter)
        self.start_voltage_button.setObjectName(u"start")
        self.start_voltage_button.setDecimals(1)
        self.start_voltage_button.setMaximum(3.300000000000000)
        self.start_voltage_button.setSingleStep(0.100000000000000)
        self.splitter.addWidget(self.start_voltage_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))

        self.menufiles = QMenu(self.menubar)
        self.menufiles.setObjectName(u"menufiles")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufiles.menuAction())
        self.menufiles.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.scan_button.setSuffix("")
        self.scan_button.setPrefix(QCoreApplication.translate("MainWindow", u"Scans = ", None))
        self.steps_button.setSuffix("")
        self.steps_button.setPrefix(QCoreApplication.translate("MainWindow", u"steps =  ", None))
        self.stop_voltage_button.setPrefix(QCoreApplication.translate("MainWindow", u"Vfin = ", None))
        self.stop_voltage_button.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.start_voltage_button.setPrefix(QCoreApplication.translate("MainWindow", u"Vin = ", None))
        self.start_voltage_button.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.menufiles.setTitle(QCoreApplication.translate("MainWindow", u"files", None))
    # retranslateUi

