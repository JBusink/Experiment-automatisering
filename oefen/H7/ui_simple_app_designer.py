from ui_simple_app import Ui_MainWindow

import sys
from PySide6 import QtWidgets
import numpy as np
# class UserInterface(QtWidgets.QMainWindow):
#     pass
# import matplotlib.pyplot as plt
import pyqtgraph as pg
from PySide6.QtCore import Slot

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clear_button.clicked.connect(self.ui.textedit.clear)
        self.ui.add_button.clicked.connect(self.add_button_clicked)
        self.show()
        
        
    @Slot()
    def add_button_clicked(self):
        self.ui.textedit.append("You clicked me.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()