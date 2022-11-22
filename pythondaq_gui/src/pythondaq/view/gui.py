from ui_scan_design_V22Nov import Ui_MainWindow
from scipy.optimize import curve_fit
import sys
from PySide6 import QtWidgets
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import Slot

from pythondaq.model.DiodeExperiment import DiodeExperiment
from pythondaq.controller.arduino_device import list_devices
# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")




class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.U,self.I,self.dU,self.dI = 0,0,0,0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.clear_button.clicked.connect(self.clear_plot)
        self.ui.plot_button.clicked.connect(self.update_plot)
        self.ui.scan_button.clicked.connect(self.scan_function_update)
        self.ui.fit_button.clicked.connect(self.fit)

        
        # self.ui.Start.valueChanged.connect(self.scan_function_update)
        # self.ui.end.valueChanged.connect(self.scan_function_update)
        # self.ui.steps.valueChanged.connect(self.scan_function_update)
        # self.ui.scans.valueChanged.connect()
        
        # self.scan_function(self.ui.Start.value(),self.ui.end.value(),self.ui.steps.value(),self.ui.scans.value())
        # self.plot(self.U,self.I,self.dU,self.dI)

        self.show()




    @Slot()
    def update_plot(self):
        self.ui.plot_widget.clear()
        self.plot(self.U,self.I,self.dU,self.dI)
        

    @Slot()
    def clear_plot(self):
        self.ui.plot_widget.clear()
        

    # @Slot()
    # def test_button_func(self):
    #     self.ui.plot_widget.plot(x=np.arange(0,10,0.1),y=np.sin(np.arange(0,10,0.1)))


    @Slot()
    def plot(self,U,I,dU,dI):
        print(I[-1],dI[-1])
        # error = pg.ErrorBarItem(x=U, y=I, height=dI,width = dU, beam=.00001)
        # self.ui.plot_widget.addItem(error)
        self.ui.plot_widget.plot(U, I, symbol='o', name = "I-U LED",symbolSize = 5, pen={'color': 'black', 'width': 4})

        self.ui.plot_widget.addLegend([0,2])
        self.ui.plot_widget.showGrid(x=True, y=True)
        self.ui.plot_widget.setLabel("left","I (mA)")
        self.ui.plot_widget.setLabel("bottom","U (Volt)")


    @Slot()
    def scan_function(self, start, stop,step,scans):
        measurement = DiodeExperiment(port=2)
        self.U,self.I,self.dU,self.dI = measurement.scan_volt(start,stop,step,scans)


    @Slot()
    def scan_function_update(self):
        self.scan_function(self.ui.Start.value(),self.ui.end.value(),self.ui.steps.value(),self.ui.scans.value())


    @Slot()
    def fit(self):
        def model(x,a,b,c,d):
            return a*(np.exp(b*x)-c)+d

        popt,pcov = curve_fit(model,self.U,self.I,p0=[0,1,2,0.1])
        self.ui.plot_widget.plot(self.U,model(self.U,*popt),symbolSize = 2, pen={'color': 'darkred', 'width': 4})
        self.ui.fit_text.append('xgf')





        


def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()