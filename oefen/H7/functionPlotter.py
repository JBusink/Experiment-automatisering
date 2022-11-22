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

        # elk QMainWindow moet een central widget hebben
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        vbox = QtWidgets.QVBoxLayout(central_widget)

        hbox = QtWidgets.QHBoxLayout()

        vbox.addLayout(hbox)

        self.plot_widget = pg.PlotWidget(title="Sine plot")

        vbox.addWidget(self.plot_widget)

        #make plot

        #start
        self.start = QtWidgets.QDoubleSpinBox()
        self.start.setPrefix("Start = ")
        self.start.setSuffix("")
        self.start.setRange(-100,100)
        self.start.setValue(0)
        self.start.setSingleStep(0.01*np.pi)
        hbox.addWidget(self.start)
        

        #ylim
        self.ylimup = QtWidgets.QSpinBox()
        self.ylimup.setPrefix("ymax = ")
        self.ylimup.setValue(100)
        hbox.addWidget(self.ylimup)

        #ylim
        self.ylimdown = QtWidgets.QSpinBox()
        self.ylimdown.setPrefix("ymin = -")
        self.ylimdown.setValue(100)
        hbox.addWidget(self.ylimdown)

        #stop
        self.stop = QtWidgets.QDoubleSpinBox()
        self.stop.setPrefix("Stop = ")
        self.stop.setRange(0,100)
        self.stop.setValue(2*np.pi)
        self.stop.setSingleStep(0.1*np.pi)
        hbox.addWidget(self.stop)

        #interval
        self.numpoints = QtWidgets.QDoubleSpinBox()
        self.numpoints.setPrefix("Number of points = ")
        self.numpoints.setDecimals(0)
        self.numpoints.setSingleStep(20)
        self.numpoints.setRange(0,1000)
        self.numpoints.setValue(50)
        hbox.addWidget(self.numpoints)  

        show = QtWidgets.QPushButton("Show")
        hbox.addWidget(show)
        quit_button = QtWidgets.QPushButton('Quit')
        hbox.addWidget(quit_button)
        log = QtWidgets.QPushButton("log")
        hbox.addWidget(log)
        linear = QtWidgets.QPushButton("linear")
        hbox.addWidget(linear)

        quit_button.clicked.connect(self.clear_plot)
        show.clicked.connect(self.update_plot)
        log.clicked.connect(self.log)
        linear.clicked.connect(self.linear)
        
        #plot
        self.plot_sin(self.start.value(),self.stop.value(),int(self.numpoints.value()))
       
        #update
        self.start.valueChanged.connect(self.update_plot)
        self.stop.valueChanged.connect(self.update_plot)
        self.numpoints.valueChanged.connect(self.update_plot)
        self.ylimup.valueChanged.connect(self.update_plot)
        self.ylimdown.valueChanged.connect(self.update_plot)

    @Slot()
    def update_plot(self):
        self.plot_widget.clear()
        self.plot_sin(self.start.value(),self.stop.value(),int(self.numpoints.value()))

    @Slot()
    def log(self):
        self.plot_widget.clear()

        self.plot_widget.setLogMode(False, False)
        self.plot_sin(self.start.value(),self.stop.value(),int(self.numpoints.value()))        
        self.plot_widget.setLogMode(False, True)

    @Slot()
    def linear(self):
        self.plot_widget.setLogMode(False, False)    

        self.plot_widget.clear()
        self.plot_sin(self.start.value(),self.stop.value(),int(self.numpoints.value()))
        self.plot_widget.setLogMode(False, False)    

    @Slot()
    def plot_sin(self,start, stop, numpoints):
        self.plot_widget.clear()
        self.plot_widget.setLogMode(False, False)


        x = np.linspace(start,stop,numpoints)

        # error = pg.ErrorBarItem(x=x, y=np.sin(x)+2, height=0.2*np.random.random_sample((numpoints,)),width = 0.01, beam=.2)
        # self.plot_widget.addItem(error)

        # self.plot_widget.plot(x, np.sin(x)+2, symbol='s', name = "Sinewave",symbolSize = 5, pen={'color': 'black', 'width': 4})
        self.plot_widget.plot(x, 100*np.abs(np.sin(5*x))*np.exp(-0.1*x)+0.01, symbol='o', name = "Damped Sine",symbolSize = 5, pen={'color': 'darkred', 'width': 4})

        self.plot_widget.addLegend([0,2])
        self.plot_widget.showGrid(x=True, y=True)

        self.plot_widget.setLabel("left","f(x)")
        self.plot_widget.setLabel("bottom","x (radians)")

        self.plot_widget.setYRange(-self.ylimdown.value(), self.ylimup.value(), padding=0)


    @Slot()
    def clear_plot(self):
        print('hello world')
        """Clear the scan plot and set the axis labels."""

        self.plot_widget.clear()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()