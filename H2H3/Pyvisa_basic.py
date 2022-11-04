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



V0list,V1list,V2list =[],[],[]
for i in range(1024):
    
    '''Note that the order of measurement is important here.
    Im not sure why, but if I measure channel 0 the LED shuts down.
    I guess this has to do with the channel output, it is not a volt meter,
    but is a an analog device that reports the output. So the output is affected
    by making a 'measurement'.
    
    Voltage drop across led is V1-V2
    The current is V2/weerstand'''
    
    device.query(f"OUT:CH0 {i}")
    V2list.append(float(device.query("MEAS:CH2:VOLT?")))
    V1list.append(float(device.query("MEAS:CH1:VOLT?")))
    
weerstand = 220
Vled = np.asarray(V1list)-np.asarray(V2list)
Stroomsterkte = np.asarray(V2list)/weerstand

fig,axes=plt.subplots(1,figsize=(6,4))
axes.scatter(Vled,Stroomsterkte,c='black',s=15)
axes.set_xlim(0,None)
axes.set_ylim(0,None)
axes.set_xlabel(r"$V_{input}$", fontsize=12)
axes.set_ylabel(r"$V_{output}$ ", fontsize=12)
plt.tight_layout()
plt.show()