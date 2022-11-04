import numpy as np
class ElectronicLoadMeasurements:
    '''Docstring example'''
    #Algemene uitleg over de class ElectronicLoadMeasurements.
    #Geen overbodige code.
    #Geen onnodige ingewikkelde structuren.
    #Geen onnodige lijsten definieren in methods.
    
    def __init__(self): 
        #Init moet logische namen hebben. Zolang het werk, is het prima.
        #lijst of array is prima. Wel de package numpy toevoegen aan het script.
        self.Rlijst = np.array([])
        self.Ulijst = np.array([])
        self.Ilijst = np.array([])
        self.Plijst = np.array([])

    def add_measurement(self,R,U):
        #Uitleg method
        self.R=R
        self.U=U
        self.Rlijst = np.append(self.Rlijst,R)
        self.Ulijst = np.append(self.Ulijst,U)
        
    def get_loads(self):
        return (self.Rlijst)
    
    def get_voltages(self):
        return (self.Ulijst)
        
    def get_currents(self):
        #berekening in de method is iets netter.
        self.I = self.Ulijst/self.Rlijst
        return (self.I)

    def get_powers(self):
        #berekening power in de method is iets netter.
        self.P = self.Ulijst**2/self.Rlijst
        return (self.P)
        
    def clear(self):
        self.Rlijst = np.array([])
        self.Ulijst = np.array([])
        
        
measurements = ElectronicLoadMeasurements()
measurements.add_measurement(R=10, U=.5)
measurements.add_measurement(R=20, U=1)

R = measurements.get_loads()
U = measurements.get_voltages()
I = measurements.get_currents()
P = measurements.get_powers()

measurements.clear()
