# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_designv22Nov.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDoubleSpinBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QSplitter, QStatusBar, QTextBrowser, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setGeometry(QRect(20, 10, 761, 401))
        self.Date = QDateTimeEdit(self.centralwidget)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(580, 20, 194, 24))
        self.fit_text = QTextBrowser(self.centralwidget)
        self.fit_text.setObjectName(u"fit_text")
        self.fit_text.setGeometry(QRect(270, 440, 431, 91))
        self.fit_button = QRadioButton(self.centralwidget)
        self.fit_button.setObjectName(u"fit_button")
        self.fit_button.setGeometry(QRect(720, 440, 100, 20))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 440, 121, 96))
        self.splitter.setOrientation(Qt.Vertical)
        self.scans = QSpinBox(self.splitter)
        self.scans.setObjectName(u"scans")
        self.scans.setMinimum(1)
        self.scans.setMaximum(999)
        self.scans.setValue(2)
        self.splitter.addWidget(self.scans)
        self.steps = QSpinBox(self.splitter)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimum(1)
        self.steps.setValue(50)
        self.splitter.addWidget(self.steps)
        self.Start = QDoubleSpinBox(self.splitter)
        self.Start.setObjectName(u"Start")
        self.Start.setDecimals(1)
        self.Start.setMaximum(3.300000000000000)
        self.Start.setSingleStep(0.100000000000000)
        self.Start.setValue(0.0)
        self.splitter.addWidget(self.Start)

        self.end = QDoubleSpinBox(self.splitter)
        self.end.setObjectName(u"end")
        self.end.setDecimals(1)
        self.end.setMaximum(3.300000000000000)
        self.end.setSingleStep(0.100000000000000)
        self.end.setValue(3.3)

        self.splitter.addWidget(self.end)
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(150, 440, 113, 96))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.scan_button = QPushButton(self.splitter_2)
        self.scan_button.setObjectName(u"scan_button")
        self.splitter_2.addWidget(self.scan_button)
        self.plot_button = QPushButton(self.splitter_2)
        self.plot_button.setObjectName(u"plot_button")
        self.splitter_2.addWidget(self.plot_button)
        self.clear_button = QPushButton(self.splitter_2)
        self.clear_button.setObjectName(u"clear_button")
        self.splitter_2.addWidget(self.clear_button)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(20, 420, 501, 16))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter_3)
        self.label_2.setObjectName(u"label_2")
        self.splitter_3.addWidget(self.label_2)
        self.label = QLabel(self.splitter_3)
        self.label.setObjectName(u"label")
        self.splitter_3.addWidget(self.label)
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
        self.fit_button.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.scans.setSuffix("")
        self.scans.setPrefix(QCoreApplication.translate("MainWindow", u"Scans = ", None))
        self.steps.setSuffix("")
        self.steps.setPrefix(QCoreApplication.translate("MainWindow", u"Steps = ", None))
        self.Start.setPrefix(QCoreApplication.translate("MainWindow", u"End = ", None))
        self.Start.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.end.setPrefix(QCoreApplication.translate("MainWindow", u"Start = ", None))
        self.end.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input values:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fit results:", None))
        self.menufiles.setTitle(QCoreApplication.translate("MainWindow", u"files", None))
    # retranslateUi

