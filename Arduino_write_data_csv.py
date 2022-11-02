import os
import csv
import datetime, time
import pyvisa
import numpy as np

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
device = rm.open_resource("ASRL/dev/cu.usbmodem11101::INSTR", read_termination="\r\n", write_termination="\n")

def volt_adc(number):
    v = np.asarray(number)*3.3/1024
    return v
def adc_volt(number):
    adc= int(np.asarray(number)*1024/3.3)
    return adc


measurement = "blauwe_led_11"
if os.path.isfile(f"LED_curve_m{measurement}.csv") == True:
    print('File excists',os.path.isfile(f"LED_curve_m{measurement}.csv"))
else:
    with open(f"LED_curve_m{measurement}.csv",'w') as file:
        wr=csv.writer(file)
        Tbegin = time.time()
        
        Vinput,tlist = [],[]
        V0list,V1list,V2list = [],[],[]
        volt=0
        
        seconds = time.time()
        local_time = time.ctime(seconds)

        wr.writerow([str(local_time),"Experiment LED arduino 33IoT"])
        wr.writerow(["time(s)", "Vinput(V)", "V0","V1","V2"])

        while volt<3.3:
            V_input, V2,V1,V0 = device.query(f"OUT:CH0 {adc_volt(volt)}"),float(device.query("MEAS:CH2:VOLT?")),float(device.query("MEAS:CH1:VOLT?")),float(device.query("MEAS:CH0:VOLT?"))
            # print(V_input,V0,V1,V2)
            tlist.append(time.time()-Tbegin)
            Vinput.append(V_input)
            V0list.append(V0)
            V1list.append(V1)
            V2list.append(V2)
            wr.writerow([time.time()-Tbegin,V_input, V0,V1,V2])
            volt+=0.003
        
device.query("OUT:CH0 1000")
time.sleep(.5)
device.query("OUT:CH0 0")

