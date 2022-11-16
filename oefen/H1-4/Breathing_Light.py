import pyvisa
import numpy as np
import tables as pt
import matplotlib.pyplot as plt  
import datetime, time

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
device = rm.open_resource("ASRL/dev/cu.usbmodem11101::INSTR", read_termination="\r\n", write_termination="\n")
print(ports,device.query("*IDN?"))


Tbegin = time.time()
Tend = Tbegin+10
T = Tbegin
while T < Tend:
    ''' Set channel 0 to 1022 (Volt/1024*3.3) after that, .1 s pause. Repeat.
    '''
    device.query(f"OUT:CH0 {1022}")
    time.sleep(.1)
    device.query("OUT:CH0 0")
    time.sleep(.1)
    device.query(f"OUT:CH0 {1022}")
    time.sleep(.1)
    device.query("OUT:CH0 0")
    time.sleep(1)
    T=time.time()
device.query("OUT:CH0 0")

T = Tbegin
while T < Tend:
    ''' Set channel 0 from 0 to 1023 (Volt/1024*3.3) in a sine wave (0.005 s pause). Convert to int.
    Repeat.
    '''
    xlist = np.arange(0,2*np.pi,0.01)
    for i in range(len(xlist)):
        device.query(f"OUT:CH0 {int(1023*np.abs(np.sin(xlist[i])))}")
        time.sleep(.005)
    T=time.time()
device.query("OUT:CH0 0")