import os
import csv
import datetime, time
import pyvisa
import numpy as np

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
device = rm.open_resource("ASRL/dev/cu.usbmodem1101::INSTR", read_termination="\r\n", write_termination="\n")

def adc_volt(number):
    v = np.asarray(number)*3.3/1023
    return v
def volt_adc(number):
    adc= int(np.asarray(number)*1023/3.3)
    return adc
              
def save_Led(name,start,stop,step,device):
    if os.path.isfile(f"LED_{name}.csv") == True:
        print('File excists',os.path.isfile(f"LED_{name}.csv"))
    else:
        with open(f"LED_{name}.csv",'w') as file:
            wr=csv.writer(file)
            Tbegin = time.time()
            
            tlist = []
            V0list,V1list,V2list = [],[],[]
                    
            seconds = time.time()
            local_time = time.ctime(seconds)

            wr.writerow([str(local_time),"Experiment LED arduino 33IoT"])
            wr.writerow(["time(s)", "V0","V1","V2"])

            for number in range(start,stop,step):
                print(number)
                volt =adc_volt(number)
                device.query(f"OUT:CH0 {volt_adc(volt)}")
                V2,V1,V0 = float(device.query("MEAS:CH2:VOLT?")),float(device.query("MEAS:CH1:VOLT?")),float(device.query("MEAS:CH0:VOLT?"))
                tlist.append(round(time.time()-Tbegin,6))
                V0list.append(V0)
                V1list.append(V1)
                V2list.append(V2)
                wr.writerow([round(time.time()-Tbegin,6), V0,V1,V2])
                time.sleep(0.1)
            print(V2list,V1list)


    device.query("OUT:CH0 1000")
    time.sleep(.5)
    device.query("OUT:CH0 0")
    return print("Files saved")

for i in range(0,1,1):
    save_Led(f'test_data_{3}',0,1024,50,device)
    
print()
    