import pyvisa
import numpy as np
def list_devices():
    '''Function that returns the ports of the usb.
    '''
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return (ports)

class DeviceNotFoundError(Exception):
    """Device not found error.

    Raised when a device is requested, but not found.
    """

    pass

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
    
# port = "ASRL/dev/cu.usbmodem11101::INSTR"
# device = ArduinoVISADevice(port = port)

# device.set_output_volt(channel =1,value =2.9)
# device.set_output_value(channel = 0, value=1023)

# print(device.get_output_value(channel = 0))
# print(device.get_output_volt(channel = 0))

# print(device.get_input_value(channel = 0))
# print(device.get_input_volt(channel = 0))
