import pyvisa
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources() #check if ports[1] is the correct port for you.
device = rm.open_resource(ports[1], read_termination="\r\n", write_termination="\n")

print(device.query("*IDN?")) #Returns adruino VISA firmware version.

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