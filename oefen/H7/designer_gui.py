# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QGraphicsView,
    QListView, QPlainTextEdit, QSizePolicy, QSpinBox,
    QSplitter, QVBoxLayout, QWidget)

import sys

from PySide6 import QtWidgets



class UserInterface(QtWidgets.Dialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(730, 330)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(70, 280, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalWidget = QWidget(Dialog)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(30, 20, 261, 211))
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.verticalWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.graphicsView_2 = QGraphicsView(self.verticalWidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout.addWidget(self.graphicsView_2)

        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(300, 60, 191, 171))
        self.dateTimeEdit = QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(300, 20, 194, 24))
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(500, 10, 211, 221))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(190, 240, 104, 31))
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(30, 270, 151, 24))
        self.splitter.setOrientation(Qt.Horizontal)
        self.spinBox_2 = QSpinBox(self.splitter)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.splitter.addWidget(self.spinBox_2)
        self.spinBox = QSpinBox(self.splitter)
        self.spinBox.setObjectName(u"spinBox")
        self.splitter.addWidget(self.spinBox)
        self.splitter_2 = QSplitter(Dialog)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(30, 240, 151, 24))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.doubleSpinBox = QDoubleSpinBox(self.splitter_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.splitter_2.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_3 = QDoubleSpinBox(self.splitter_2)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.splitter_2.addWidget(self.doubleSpinBox_3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()