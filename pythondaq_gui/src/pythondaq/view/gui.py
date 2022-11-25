"""A CLI to measure the current-voltage characteristic of a LED.
In this experiment, a specific circuit schematic is assumed. 
The circuit contains a diode (e.g. a LED) and a resistor in series. 
A voltage is applied to the high side of the diode and the low side of the resistor is grounded. 
The voltage across the diode and the resistor are measured and the 
latter is used to calculate the current flowing through the diode.
"""

from ui_scan_design_V22Nov import Ui_MainWindow
from scipy.optimize import curve_fit
import sys
from PySide6 import QtWidgets
import numpy as np
import pyqtgraph as pg
from pythondaq.model.DiodeExperiment import DiodeExperiment

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

        # self.functions_dict = {"":"","sin(x)": np.sin, "cos(x)": np.cos, "x": lambda x: x}
        # self.ui.Qcombo_button.addItems(self.functions_dict.keys())
        # self.ui.Qcombo_button.activated.connect(self.activated)


        self.ui.clear_button.clicked.connect(self.clear_plot)
        self.ui.plot_button.clicked.connect(self.update_plot)
        self.ui.scan_button.clicked.connect(self.scan_function)
        self.ui.fit_button.clicked.connect(self.fit)

        # self.ui.Start.valueChanged.connect(self.activated)
        # self.ui.end.valueChanged.connect(self.activated)
        # self.ui.steps.valueChanged.connect(self.activated)

        self.show()

    # @Slot()
    # def activated(self):
    #     """Test button that plots predefined function (in a dictionary). Will be removed in the near future.
    #     """

    #     self.ui.plot_widget.clear()
    #     function = self.functions_dict[self.ui.Qcombo_button.currentText()]
    #     x = np.linspace(self.ui.Start.value(), self.ui.end.value(), self.ui.steps.value())
    #     self.ui.plot_widget.plot(x, function(x), symbol='o', symbolSize = 5, pen={'color': 'black', 'width': 4})
    #     self.ui.plot_widget.setLabel('left', '<math>x<sup>2</sup></math>', **{'font-size':'16pt'})
    #     self.ui.plot_widget.setLabel("bottom","x", **{'font-size':'16pt'})

    def update_plot(self):
        """Clears the plot and updates it if a new scan is initialized.
        """

        self.ui.plot_widget.clear()
        self.plot(self.U,self.I,self.dU,self.dI)

    def clear_plot(self):
        """Clears plot button.
        """
        self.ui.plot_widget.clear()
        
    def plot(self,U,I,dU,dI):
        """Plots the captured data from the diode-experiment.
        The scan method provides the voltage-drop, current in plus the corresponding standard deviations of the mean 
        of a blue LED. Here we plot these quantities.

        Args:
            U (float): Voltage drop across LED.
            I (float): current throug LED.
            dU (float): error on U.
            dI (float): error on I.
        """

        error = pg.ErrorBarItem(x=U, y=I, height=2*dI,width = 2*dU)
        self.ui.plot_widget.addItem(error)
        self.ui.plot_widget.plot(U, I, symbol='o', name = "I-U LED",symbolSize = 5, pen={'color': 'black', 'width': 4})

        self.ui.plot_widget.addLegend([0,2])
        self.ui.plot_widget.showGrid(x=True, y=True)
        self.ui.plot_widget.setLabel("left","I (mA)")
        self.ui.plot_widget.setLabel("bottom","U (Volt)")

    def scan_function(self):
        """Scan function that initializes the devices and performs a voltage-scan on the 
        LED. The start, stop, steps and number of scans can be adjusted. 

        Args:
            start (float): start-value of scan in volt.
            stop (float): stop-value of scan in volt.
            step (int): number of steps in a linear space between the start and stop value.
            scans (int): number of scans.
        """
        measurement = DiodeExperiment(port=2)
        self.U,self.I,self.dU,self.dI = measurement.scan_volt(self.ui.Start.value(),self.ui.end.value(),self.ui.steps.value(),self.ui.scans.value())

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
        self.ui.fit_text.clear()
        def model(x,a,b,c):
            return a*(np.exp(b*x)-c)

        p0=[1e-10,10,1e6]
        popt,pcov = curve_fit(model,self.U,self.I,p0=p0,maxfev = 10000)
        print(popt,pcov)
        if len(popt) == 0:
            self.ui.fit_text.append("Fit not converged!")
        else:
            self.ui.plot_widget.plot(self.U,model(self.U,*popt),symbolSize = 2, pen={'color': 'darkred', 'width': 4})
            for i in range(len(popt)):
                self.ui.fit_text.append("P{}= {:.2e} +- {:.2e}".format(i,popt[i],pcov[i][i]**0.5))

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()