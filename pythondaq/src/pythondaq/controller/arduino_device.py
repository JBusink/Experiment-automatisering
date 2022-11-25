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

