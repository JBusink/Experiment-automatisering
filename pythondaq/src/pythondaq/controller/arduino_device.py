import pandas as pd
import os
import matplotlib.pyplot as plt
import pyvisa



def list_devices():
    '''Function that returns the ports of the usb.
    '''
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return (ports)


def stand_by(device):
    """Standby mode device

    Args:
        device (int)): 0 voltage applied to arduino.
    """
    device.query("OUT:CH0 0")

class ArduinoVISADevice:
    """set input value of device, return output device
    """
    def __init__(self,port):
        '''Initialize device'''       
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n",timeout=1000)
    def get_identification(self):
        """Returns the device identification string."""
        return self.device.query("*IDN?")
    
    def set_output_value(self, channel=0,value=0):
        if channel == 0:
            OUTPUT = int(self.device.query(f"OUT:CH{channel} "+ f"{value}"))
            return(OUTPUT)
        else:
            print("Invalid channel to set output voltage!")
    
    def set_output_volt(self, channel=0,value=0):
        if channel == 0:
            OUTPUT = float(self.device.query(f"OUT:CH{channel}"+ f":VOLT {value}"))
            return(OUTPUT)
        else:
            print("Invalid channel to set output voltage!")
        
    def get_output_value(self, channel):
        return int(self.device.query(f"OUT:CH{channel}?"))
    
    def get_output_volt(self, channel):
        return float(self.device.query(f"OUT:CH{channel}:VOLT?"))
    
    def get_input_value(self, channel):
        return int(self.device.query(f"MEAS:CH{channel}?"))

    def get_input_volt(self, channel):
        return float(self.device.query(f"MEAS:CH{channel}:VOLT?"))


# getting the information of the plugged-in devices
def info_devices():
    rm = pyvisa.ResourceManager("@py")
    for i, j in enumerate(rm.list_resources()):
        try:
            print(f'{i}. {j}, information:', rm.open_resource(str(j), read_termination = "\n\r", write_termination = "\n").query("*IDN?"))
        except:
            print(f'{i}. {j}, device unknown') # raises an userwarning

    return rm.list_resources()


def data_to_csv(data):
    Vled,Iled,Iled_err,Vled_err = data
    """Saves data to csv file. Creates csv file at new folder data/measurement_index.csv.
    Index is checked and counts up if pre-excisting.

    Args:
        data list : list of data.
    """
    path = 'data'
    if path_check(path):
        i = 0
        for filename in os.listdir(path):
            if filename.endswith(f'measurement_{i}.csv'):
                i += 1
    df = pd.DataFrame({'Vled(V)':Vled, 'Iled(A)':Iled,'Vled_err':Vled_err,'Iled_err(A)':Iled_err})
    df.to_csv(f'{path}/measurement_{i}.csv', sep = ',',index=True,index_label='Index') 


def path_check(path):
    """Check if path excist, if not create folder.

    Args:
        path (str): location of the path.

    Returns:
        Boolean: True of False.
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("Not allowed to write in this path, please change the permissions or run the program through a different path")
            return False
    return True

def plot_graph(Vled,Iled,Iled_err,Vled_err):
    """Plot a graph of the measurements.

    Plots a graph of the current versus the applied voltage.

    Args:
        4 (list): list of measurements. 
    """
    
    fig,axes=plt.subplots(1,1,figsize=(5,5))
    axes.errorbar(Vled,Iled,xerr=Vled_err,yerr=Iled_err,ms =5,color= 'black',
                mfc='white',mec='black',fmt='.',elinewidth=2,capsize=2)
    axes.set_ylabel(r'$I_{led} (A)$',fontsize=14)
    axes.set_xlabel(r'$V_{led} (V)$',fontsize=14)
    plt.show()