from pythondaq.controller.arduino_device import list_devices, ArduinoVISADevice,info_devices
from pythondaq.model.DiodeExperiment import DiodeExperiment
import matplotlib.pyplot as plt
import numpy as np


#Check if DiodeExperiment class works
measurement= DiodeExperiment(port=2)
measurement.standby()
measure = measurement.measure_volt(2.3,1,3.2)
measurement.close()


# #Check if DiodeExperiment class works
measurement= DiodeExperiment(port=2)
measurement.standby()
measurement.get_identification()
measure = measurement.measure_volt(2.3,1,3)
measurement.close()


    #A simple scan 
def main():
    
    """Input is 
    """
    info_devices()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)
    Vled,Iled,Iled_err = measurement.scan_value(start = 2,stop = 1000,step=60, N= 10)

    fig,axes=plt.subplots(1,1,figsize=(5,5))
    axes.errorbar(Vled,Iled,yerr=Iled_err,ms =5,color= 'black',
                mfc='white',mec='black',fmt='.',elinewidth=2,capsize=2)
    axes.set_ylabel(r'$I_{led} (A)$',fontsize=14)
    axes.set_xlabel(r'$V_{led} (V)$',fontsize=14)
    plt.show()
    
    
    #print ID of device and found devices.
def identification():
    ArduinoVISADevice(port = list_devices()[2]).get_identification()     
    
    
    #histogram at a specific voltage value, to observe distribution of noise.
def histogram():
    info_devices()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)
    measure = measurement.measure_volt(2,1000,3.3)
    fig, axes = plt.subplots()
    n, bins, patches = axes.hist(np.asarray(measure), 50, density=True,histtype='step')
    axes.set_ylabel(r'$\mathcal{P}(I)$',fontsize=16)
    axes.set_xlabel(r'$I (A)$',fontsize=16)
    axes.set_yscale('log')
    plt.show()
