# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Design_28Nov.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QTextBrowser,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 759)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Plot_widget = PlotWidget(self.centralwidget)
        self.Plot_widget.setObjectName(u"Plot_widget")
        self.Plot_widget.setGeometry(QRect(10, 190, 761, 411))
        font = QFont()
        font.setBold(False)
        self.Plot_widget.setFont(font)
        self.Plot_widget.setMouseTracking(True)
        self.Plot_widget.setFrameShape(QFrame.NoFrame)
        self.Plot_widget.setFrameShadow(QFrame.Sunken)
        self.Plot_widget.setLineWidth(0)
        self.label_Fit_results = QLabel(self.centralwidget)
        self.label_Fit_results.setObjectName(u"label_Fit_results")
        self.label_Fit_results.setGeometry(QRect(310, 610, 91, 16))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.label_Fit_results.setFont(font1)
        self.label_Fit_results.setFrameShape(QFrame.NoFrame)
        self.label_Fit_results.setTextFormat(Qt.AutoText)
        self.label_Input_Values = QLabel(self.centralwidget)
        self.label_Input_Values.setObjectName(u"label_Input_Values")
        self.label_Input_Values.setGeometry(QRect(10, 610, 121, 16))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_Input_Values.setFont(font2)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 10, 551, 16))
        self.progressBar.setValue(24)
        self.Residuals = PlotWidget(self.centralwidget)
        self.Residuals.setObjectName(u"Residuals")
        self.Residuals.setGeometry(QRect(10, 70, 761, 111))
        self.Residuals.setFrameShape(QFrame.NoFrame)
        self.Residuals.setLineWidth(0)
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(620, 40, 151, 21))
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(51, 631, 118, 96))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.scans = QSpinBox(self.splitter_2)
        self.scans.setObjectName(u"scans")
        self.scans.setMinimum(1)
        self.scans.setMaximum(999)
        self.scans.setValue(2)
        self.splitter_2.addWidget(self.scans)
        self.steps = QSpinBox(self.splitter_2)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimum(1)
        self.steps.setMaximum(1024)
        self.steps.setSingleStep(10)
        self.steps.setValue(50)
        self.splitter_2.addWidget(self.steps)
        self.Start = QDoubleSpinBox(self.splitter_2)
        self.Start.setObjectName(u"Start")
        self.Start.setDecimals(1)
        self.Start.setMaximum(3.300000000000000)
        self.Start.setSingleStep(0.100000000000000)
        self.Start.setValue(0.000000000000000)
        self.splitter_2.addWidget(self.Start)
        self.end = QDoubleSpinBox(self.splitter_2)
        self.end.setObjectName(u"end")
        self.end.setDecimals(1)
        self.end.setMaximum(3.300000000000000)
        self.end.setSingleStep(0.100000000000000)
        self.end.setValue(3.300000000000000)
        self.splitter_2.addWidget(self.end)
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(170, 630, 141, 96))
        self.splitter_3.setOrientation(Qt.Vertical)
        self.scan_button = QPushButton(self.splitter_3)
        self.scan_button.setObjectName(u"scan_button")
        self.splitter_3.addWidget(self.scan_button)
        self.plot_button = QPushButton(self.splitter_3)
        self.plot_button.setObjectName(u"plot_button")
        self.splitter_3.addWidget(self.plot_button)
        self.clear_button = QPushButton(self.splitter_3)
        self.clear_button.setObjectName(u"clear_button")
        self.splitter_3.addWidget(self.clear_button)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 630, 37, 101))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_Scans = QLabel(self.splitter)
        self.label_Scans.setObjectName(u"label_Scans")
        self.splitter.addWidget(self.label_Scans)
        self.label_Scans_2 = QLabel(self.splitter)
        self.label_Scans_2.setObjectName(u"label_Scans_2")
        self.splitter.addWidget(self.label_Scans_2)
        self.label_Start = QLabel(self.splitter)
        self.label_Start.setObjectName(u"label_Start")
        self.splitter.addWidget(self.label_Start)
        self.label_Stop = QLabel(self.splitter)
        self.label_Stop.setObjectName(u"label_Stop")
        self.splitter.addWidget(self.label_Stop)
        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(700, 610, 61, 20))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.splitter_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.splitter_4.addWidget(self.label_7)
        self.fit_button = QRadioButton(self.splitter_4)
        self.fit_button.setObjectName(u"fit_button")
        self.splitter_4.addWidget(self.fit_button)
        self.splitter_5 = QSplitter(self.centralwidget)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(310, 630, 461, 91))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.fit_text = QTextBrowser(self.splitter_5)
        self.fit_text.setObjectName(u"fit_text")
        self.fit_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.splitter_5.addWidget(self.fit_text)
        
        self.Device = QComboBox(self.centralwidget)
        self.Device.setObjectName(u"Device")
        self.Device.setGeometry(QRect(143, 40, 201, 26))
        self.label_Fit_results_2 = QLabel(self.centralwidget)
        self.label_Fit_results_2.setObjectName(u"label_Fit_results_2")
        self.label_Fit_results_2.setGeometry(QRect(20, 40, 121, 19))
        self.label_Fit_results_2.setFont(font1)
        self.label_Fit_results_2.setFrameShape(QFrame.NoFrame)
        self.label_Fit_results_2.setTextFormat(Qt.AutoText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Fit_results.setText(QCoreApplication.translate("MainWindow", u"Fit results:", None))
        self.label_Input_Values.setText(QCoreApplication.translate("MainWindow", u"Input values:", None))
        self.scans.setSuffix("")
        self.scans.setPrefix("")
        self.steps.setSuffix("")
        self.steps.setPrefix("")
        self.Start.setPrefix("")
        self.Start.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.end.setPrefix("")
        self.end.setSuffix(QCoreApplication.translate("MainWindow", u" Volt", None))
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_Scans.setText(QCoreApplication.translate("MainWindow", u"Scans", None))
        self.label_Scans_2.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.label_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Fit: ", None))
        self.fit_button.setText("")
        self.label_Fit_results_2.setText(QCoreApplication.translate("MainWindow", u"Choose Device:", None))
    # retranslateUi
