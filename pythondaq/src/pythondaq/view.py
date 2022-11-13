print('test import staement')
from src.pythondaq.controller.arduino_device import list_devices, ArduinoVISADevice
from src.pythondaq.model.DiodeExperiment import DiodeExperiment
import matplotlib.pyplot as plt
import numpy as np

# Check if ArduinoVisaDevice class works
port = list_devices()
device = ArduinoVISADevice(port = port[2])
device.set_output_volt(value = 1)
device.set_output_value(value =0)

#Check if DiodeExperiment class works
measurement= DiodeExperiment(port=port[2])
measurement.standby()
measurement.get_identification()
measure = measurement.measure_volt(2.3,1,3.2)
measurement.close()

port = list_devices()
print(port)
device = ArduinoVISADevice(port = port[2])
device.set_output_volt(value = 1)
device.set_output_value(value =0)

# #Check if DiodeExperiment class works
measurement= DiodeExperiment(port=port[2])
measurement.standby()
measurement.get_identification()
measure = measurement.measure_volt(2.3,1,3)
measurement.close()

port = list_devices()
print(port)
measurement= DiodeExperiment(port=port[2])

# measure = measurement.measure_volt(2,1000,3.3)
# fig, axes = plt.subplots()
# n, bins, patches = axes.hist(np.asarray(measure), 50, density=True,histtype='step')
# axes.set_yscale('log')
# plt.show()

# Vled,Iled,Iled_err = measurement.scan_value(start = 2,stop = 1000,step=60, N= 10)

# fig,axes=plt.subplots(1,1,figsize=(5,5))
# axes.errorbar(Vled,Iled,yerr=Iled_err,ms =5,color= 'black',
#               mfc='white',mec='black',fmt='.',elinewidth=2,capsize=2)
# axes.set_ylabel(r'$I_{led} (A)$',fontsize=14)
# axes.set_xlabel(r'$V_{led} (V)$',fontsize=14)
# plt.show()

