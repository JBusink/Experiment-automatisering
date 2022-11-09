import pyvisa
import numpy as np
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
device = rm.open_resource(ports[2], read_termination="\r\n", write_termination="\n")
print(device.query("*IDN?"))

def adc_volt(adc):
    '''(input is voltage V= {0,3.3}
    returns adc = {1,1024})^-1'''
    return np.asarray(adc)*3.3/1024

def volt_adc(volt):
    '''input is voltage V= {0,3.3}
    returns adc = {1,1024}'''
    return np.asarray(volt)*1024/3.3

#2.8 breathing_light.py
#2.9
print(adc_volt(700))
print("minimal value of voltage: ", adc_volt(1))
print("2.0 V :", volt_adc(2.0))
print("2.28 V :", volt_adc(2.28))

#2.10



VLEDlist,V2list =[],[]
for i in range(1024,10): #Measure every tenth value.
    device.query(f"OUT:CH0 {i}") #set output voltage in Ch. 0

    '''We are interested in the voltage drop across the LED:
    so VLED = V1-V2. The voltage that we measure is a 'binary' number
    it is converted to volt by *3.3/1023. 
    The current over the LED can be determined by the voltage drop 
    (V2) across the resistor (divided by the resistance). 
    
    Both voltages are appended to a list: VLEDlist and V2list. '''
    
    VLEDlist.append((float(device.query("MEAS:CH1?"))-float(device.query("MEAS:CH2?")))*3.3/1023)
    V2list.append(float(device.query("MEAS:CH2?"))*3.3/1023)
    
weerstand = 220
Stroomsterkte = V2list/weerstand #Convert voltage to current

fig,axes=plt.subplots(1,figsize=(6,4))
axes.scatter(VLEDlist,Stroomsterkte,c='black',s=15)
axes.set_xlim(0,None)
axes.set_ylim(0,None)
axes.set_xlabel(r"$V_{Led}$", fontsize=12)
axes.set_ylabel(r"$I_{Led}$ ", fontsize=12)
plt.show()