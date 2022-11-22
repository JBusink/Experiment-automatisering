import sys
from PySide6 import QtWidgets

# class UserInterface(QtWidgets.QMainWindow):
#     pass


from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):

    # roep de __init__() aan van de parent class
     
        super().__init__()

        # elk QMainWindow moet een central widget hebben
        # hierbinnen maak je een layout en hang je andere widgets
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        vbox = QtWidgets.QVBoxLayout(central_widget)
        hbox = QtWidgets.QHBoxLayout()
        vbox.addLayout(hbox,stretch=1)
        self.textedit = QtWidgets.QTextEdit()
        vbox.addWidget(self.textedit)

        clear_button = QtWidgets.QPushButton("Clear")
        hbox.addWidget(clear_button)

        add_button = QtWidgets.QPushButton("Add text")
        hbox.addWidget(add_button)
        add2_button = QtWidgets.QPushButton("Hello World")
        hbox.addWidget(add2_button)
        quit_button = QtWidgets.QPushButton('Quit')
        hbox.addWidget(quit_button)


        # # Slots and signals
        clear_button.clicked.connect(self.textedit.clear)
        add_button.clicked.connect(self.add_hello_world)
        add2_button.clicked.connect(self.add_button_clicked)
        quit_button.clicked.connect(self.quit)

    @Slot()
    def add_button_clicked(self):
        self.textedit.append("You clicked me.")

    @Slot()
    def add_hello_world(self):
        self.textedit.append("Hello World!")
    
    @Slot()
    def quit(self):
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()