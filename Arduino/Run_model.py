from arduino_device import ArduinoVISADevice, list_devices
import matplotlib.pyplot as plt
import numpy as np
port = list_devices()
device = ArduinoVISADevice(port = port[2])
device.set_output_volt(channel=0,value = 3)


    
fig,axes=plt.subplots(1,1,figsize=(5,5))
axes.scatter(np.asarray(V1list)-np.asarray(V2list),np.asarray(V2list)/R)
plt.show()

class DiodeExperiment:
    _ch_set_diode_voltage = 0
    def __init__():
        self.device = ArduinoVISADevice(port = port)
        return
    
    def scan(self,start, stop,step):
        R=220
        V1list,V2list = [],[]
        for i in range(start,stop,step):
            device.set_output_volt(channel=0,value=i)
            V2 = device.get_input_volt(channel=2)
            V1 = device.get_input_volt(channel=1)
            V1list.append(V1)
            V2list.append(V2)
        return V1list,V2list
    
    def standby(self):
        """Put the device in standby mode.
        Applies a zero voltage to the diode.
        """
        self.device.set_output_voltage(self._ch_set_diode_voltage, 0)