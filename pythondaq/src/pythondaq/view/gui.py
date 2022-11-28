"""A CLI to measure the current-voltage characteristic of a LED.
In this experiment, a specific circuit schematic is assumed. 
The circuit contains a diode (e.g. a LED) and a resistor in series. 
A voltage is applied to the high side of the diode and the low side of the resistor is grounded. 
The voltage across the diode and the resistor are measured and the 
latter is used to calculate the current flowing through the diode.
"""

from Design_28Nov import Ui_MainWindow
from scipy.optimize import curve_fit
import sys
from PySide6 import QtWidgets, QtCore
import numpy as np
import pyqtgraph as pg
import pandas as pd
from pythondaq.model.DiodeExperiment import DiodeExperiment,devices_list
# from PyQt6 import QtCore, QtWidgets


pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


class UserInterface(QtWidgets.QMainWindow):
    """GUI for arduino device using a specific design on a breadboard.
    """


    def __init__(self):
        """Initiate GUI, design made using Designer QT. Buttons are directed to specific functions.
        
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Choose devicce
        self.ports = devices_list()
        self.ports_dict = generate_dict(self.ports)
        self.ui.Device.addItems(self.ports_dict.values())
        self.ui.Device.activated.connect(self.activated)


        #Connect buttons
        self.ui.clear_button.clicked.connect(self.clear_plot)
        self.ui.plot_button.clicked.connect(self.update_plot)
        self.ui.scan_button.clicked.connect(self.scan_function)
        # self.ui.fit_button.clicked.connect(self.fit)
        self.ui.fit_button.toggled.connect(self.fit)


        #Save data
        fileMenu = self.menuBar().addMenu('File')
        saveAction = fileMenu.addAction('Save data')
        saveAction.setShortcut("Ctrl+S")
        saveAction.triggered.connect(self.save)


        #Time
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.show()

    def activated(self):
        """Function that initializes the port devices
        """

        port = self.ui.Device.currentText()
        self.device = DiodeExperiment(port=port) #need to change this to take the port again.
        
    def save(self):
        """Saves the data to .csv file"""

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(filter="CSV files (*.csv)")
        save_csv(self.data,filename)

    def update_plot(self):
        """Clears the plot and updates it if a new scan is initialized.
        """

        self.ui.Plot_widget.clear()
        # self.ui.Histogram.clear()
        self.ui.Residuals.clear()

        self.plot_main(self.U,self.I,self.dU,self.dI)
        # self.plot_histogram(self.I)

        if len(self.popt) != 0:
            self.plot_residuals(self.U,self.I,self.dU,self.dI,self.popt)
        else: 
            pass

    def clear_plot(self):
        """Clears plot button.
        """

        self.ui.Plot_widget.clear()
        # self.ui.Histogram.clear()
        self.ui.Residuals.clear()

    # def plot_histogram(self,I):
    #     """Plots histogram of y-data using 20 bins, flipped.

    #     Args:
    #         I (np.array): array of y data (current).
    #     """

    #     a,b = np.histogram(I,bins=50)
    #     self.ui.Histogram.plot(a,0.5*(b[1:]+b[:-1]), pen={'color': 'black', 'width': 4})
    #     self.ui.Histogram.setLabel("left","I (mA)")
    #     self.ui.Histogram.setLabel("top","P(I)")

    def plot_residuals(self,U,I,dU,dI,popt):
        """Plots the residuals based on a predescribed model.

        Args:
            U (array): Voltage drop across LED.
            I (array): current throug LED.
            dU (array): error on U.
            dI (array): error on I.
        """

        def model(x,a,b,c):
            return a*(np.exp(b*x)-c)

        error = pg.ErrorBarItem(x=np.asarray(U), y=(np.asarray(I)-model(U,*popt)), height=2*dI,width = 2*dU)
        self.ui.Residuals.addItem(error)
        self.ui.Residuals.plot(U, (I-model(U,*popt)), symbol='o', name = "I-U LED",symbolSize = 5, pen={'color': 'black', 'width': 4})

        self.ui.Residuals.setXRange(0,2.6)
        self.ui.Residuals.setYRange(-0.5,0.5)
        self.ui.Residuals.addLegend([0,2])
        self.ui.Residuals.showGrid(x=True, y=True)
        self.ui.Residuals.setLabel("left","r (mA)")

        
    def plot_main(self,U,I,dU,dI):
        """Plots the captured data from the diode-experiment.
        The scan method provides the voltage-drop, current in plus the corresponding standard deviations of the mean 
        of a blue LED. Here we plot these quantities.

        Args:
            U (array): Voltage drop across LED.
            I (array): current throug LED.
            dU (array): error on U.
            dI (array): error on I.
        """

        error = pg.ErrorBarItem(x=U, y=I, height=2*dI,width = 2*dU)
        self.ui.Plot_widget.addItem(error)
        self.ui.Plot_widget.plot(U, I, symbol='o', name = "I-U LED",symbolSize = 5, pen={'color': 'black', 'width': 4})

        self.ui.Plot_widget.addLegend([0,2])
        self.ui.Plot_widget.setXRange(0,2.6)
        self.ui.Plot_widget.setYRange(0,3)
        self.ui.Plot_widget.showGrid(x=True, y=True)
        self.ui.Plot_widget.setLabel("left","I (mA)")
        self.ui.Plot_widget.setLabel("bottom","U (Volt)")


    def scan_function(self):
        """Scan function that initializes the devices and performs a voltage-scan on the 
        LED. The start, stop, steps and number of scans can be adjusted. 

        Args:
            start (float): start-value of scan in volt.
            stop (float): stop-value of scan in volt.
            step (int): number of steps in a linear space between the start and stop value.
            scans (int): number of scans.
        """

        self.data = self.device.scan_volt(self.ui.Start.value(),self.ui.end.value(),self.ui.steps.value(),self.ui.scans.value())
        self.U,self.I,self.dU,self.dI = self.data


    def fit(self):
        """Apply a fit function to the data. The data consists of two lists of voltages and currents of the Led. 
        The model that I use is based on the Shockley equation, with parameters:

        a = leakage current,
        b = inverse of Vt (thermal current), i.e. Vt = 1/b,
        c = constant set to 1 in ordinary LEDs.


        Returns:
            popt (float): optimized parameters of a,b,c;
            pcov (float): covariance matrix of a,b,c.
        """
        if self.ui.fit_button.isChecked() == True:
            self.ui.fit_text.clear()
            def model(x,a,b,c):
                return a*(np.exp(b*x)-c)

            p0=[1e-10,10,1e6]
            self.popt,pcov = curve_fit(model,self.U,self.I,p0=p0,maxfev = 10000)
            if len(self.popt) == 0:
                self.ui.fit_text.append("Fit not converged!")
            else:
                self.ui.Plot_widget.plot(self.U,model(self.U,*self.popt),symbolSize = 2, pen={'color': 'darkred', 'width': 4})
                self.plot_residuals(self.U,self.I,self.dU,self.dI,self.popt)
                
                for i in range(len(self.popt)):
                    self.ui.fit_text.append("P{}= {:.2e} +- {:.2e}".format(i,self.popt[i],pcov[i][i]**0.5))

        else:
            self.ui.fit_text.clear()
            self.ui.Residuals.clear()
            self.ui.Plot_widget.clear()
            self.plot_main(self.U,self.I,self.dU,self.dI)

				

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())

def save_csv(data,filename):
    """Saves data to csv file at location "filename".

    Args:
        data (array): Voltage and current (+ corresponding errors) of the data.
        filename (string): string of the location of the data
    """
    Vled,Iled,Iled_err,Vled_err = data

    df = pd.DataFrame({'Vled(V)':Vled, 'Iled(A)':Iled,'Vled_err':Vled_err,'Iled_err(A)':Iled_err})
    df.to_csv(filename, sep = ',',index=True,index_label='Index') 

def generate_dict(devices_list):
    """Generates a dictionary for the devices.

    Args:
        devices_list (tuple): tuple of str.

    Returns:
        dictionairy: dictionairy that has an empty element --Choose device-- and the rest of the ports.
    """
    dict =  {"":"-- Choose device --"}
    for i in range(len(devices_list)):
        dict[f'Port {i}:']= str(devices_list[i])

    return dict

if __name__ == "__main__":
    main()