import pyvisa
import numpy as np
import matplotlib.pyplot as plt 
 
rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
device = rm.open_resource("ASRL/dev/cu.usbmodem1101::INSTR", read_termination="\r\n", write_termination="\n")
# print(ports,device.query("*IDN?"))

V0list,V1list,V2list =[],[],[]
for i in range(1024):
    device.query(f"OUT:CH0 {i}")
    V2list.append(float(device.query("MEAS:CH2:VOLT?")))
    V1list.append(float(device.query("MEAS:CH1:VOLT?")))

fig,axes=plt.subplots(1,1,figsize=(6,6))
axes.scatter(np.asarray(V1list)-np.asarray(V2list),np.asarray(V2list)*1000/220.,c='black',marker='p',
             s=15,fc='none',ec='black')
axes.set_xlim(0,None)
axes.set_ylim(0,None)
axes.set_xlabel(r"$V_{LED} V$", fontsize=12)
axes.set_ylabel(r"$I_{LED}$ mA", fontsize=12)
plt.tight_layout()
plt.show()
