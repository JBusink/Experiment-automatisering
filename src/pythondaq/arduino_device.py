import pyvisa

def list_devices():
    '''Function that returns the ports of the usb.
    '''
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return (ports)

def stand_by(device):
    """stand-by function of device.

    Args:
        device (_type_): arduino device.
    """
    device.query("OUT:CH0 0")

    return 

class ArduinoVISADevice:
    """Controller for Arduino Iot33 nano
    """
    def __init__(self,port):
        """Initialise device.

        Args:
            port (_str_): _Initialize the port and configures device_
        """
        rm = pyvisa.ResourceManager("@py")
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n",timeout=1000)
    
    def get_identification(self):
        """Returns the device identification string."""
        return self.device.query("*IDN?")
    
    def set_output_value(self, channel=0,value=0):
        """Set output value [0-1023] of the arduino on a given channel number.
        Channel is 0 by default, since we only acces channel 0.

        Args:
            channel (int, optional): _description_. Defaults to 0.
            value (int, optional): _description_. Defaults to 0.
        """
        if channel == 0:
            OUTPUT = int(self.device.query(f"OUT:CH{channel} "+ f"{value}"))
            return(OUTPUT)
        else:
            print("Invalid channel to set output voltage!")
    
    def set_output_volt(self, channel=0,value=0):
        """Set output voltage [0,3.3] of the arduino on a given channel number.
        Channel is 0 by default, since we only acces channel 0.

        Args:
            channel (int, optional): _description_. Defaults to 0.
            value (int, optional): _description_. Defaults to 0.
        """
        if channel == 0:
            OUTPUT = float(self.device.query(f"OUT:CH{channel}"+ f":VOLT {value}"))
            return(OUTPUT)
        else:
            print("Invalid channel to set output voltage!")
        
    def get_output_value(self, channel):
        """get output value

        Args:
            channel (_type_): _description_

        Returns:
            _type_: Output value in adc.
        """
        return int(self.device.query(f"OUT:CH{channel}?"))
    
    def get_output_volt(self, channel=1):
        """Gets output voltage of a channel number.

        Args:
            channel (_type_): _description_. Defaults to 1.

        Returns:
            _type_: output voltage of channel.
        """
        return float(self.device.query(f"OUT:CH{channel}:VOLT?"))
    
    def get_input_value(self, channel=1):
        """Gets input value of a channel number.

        Args:
            channel (_type_): _description_. Defaults to 1.

        Returns:
            _type_: output value of channel.
        """
        return int(self.device.query(f"MEAS:CH{channel}?"))

    def get_input_volt(self, channel):
        """Gets input voltage channel number.

        Args:
            channel (_type_): _description_. Default to 1.

        Returns:
            _type_: output voltage of channel.
        """
        return float(self.device.query(f"MEAS:CH{channel}:VOLT?"))


# list ports
rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()

if __name__ == "__main__":
    print(ports)