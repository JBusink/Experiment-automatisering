from pythondaq.controller.arduino_device import ArduinoVISADevice,list_devices
import numpy as np

class DiodeExperiment:
    """Diode experiment class. This is a model based on a Arduino 33IOT. The input/output voltage is a
    digital number {0,...,1023}, this is converted along a linear scale to 3.3 Volt. 
    The input voltage is applied to Ch0,
    a 220 ohm resistors makes a small current that powers the LED. The voltage on the LED is measured using the
    voltage measured at port 1 minus the voltage measured at port 2. Th

    Returns:
        _type_: _description_
    """
    _ch_set_diode_voltage =0
    _resistor_value = 220.
    _max_voltage = 3.3
    
    def __init__(self,port):
        """Initializes the diode class.

        Args:
            port (int): needs device string, using list_devices we ask for the avaialble ports
            the user is asked to provide the number of the device. 
        """
        self.device = ArduinoVISADevice(port = str(list_devices()[int(port)]))
        pass
    
    def get_identification(self):
        """Provides the firmware version in the arduino device.
        """
        print(self.device.get_identification())

    def standby(self):
        """Standby mode, applies 0 voltage.
        """
        self.device.set_output_volt(self._ch_set_diode_voltage, 0)
        pass
    
    def adc_to_volt(self, value):
        """Converts adc to volt.

        Args:
            value (int): converts adc to max 3.3 volt.

        Returns:
            float: return voltage, max 3.3 volt.
        """
        voltage = value / 1023 * 3.3
        return voltage
    
    def volt_to_adc(self, value):
        """Converts volt tot adc.

        Args:
            value (float): voltage value, max 3.3 Volt.

        Returns:
            int: adc value, value from 0 to 1023.
        """
        adc = int(value *1023/3.3)
        return adc
    
    def scan_value(self, start,stop,step=10,N=int(1)):
        """Performs a voltage scan from start to stop value, with steps of step.
        The total number of scans N can be chosen, default = 1.

        Args:
            start (float): start value of scan in adc.
            stop (float): stop value of scan in adc.
            step (int, optional): Scan steps. Defaults to 10.
            N (int, optional): Number of scans. Defaults to int(1).

        Returns:
            Array: 4x1 array: the mean of the voltage applied,
            the mean of the current measured and the uncertainty of the current and voltage.
        """
        if start>=stop:
            print('not possible')
            return None
        
        elif N<1:
            print('Number of measurements need to be larger than 0.')
            
        else:
            VLED_mean = []
            ILED_mean = []
            for n in range(int(N)):
                V1list = []
                V2list = []
                for value in np.linspace(start,stop,step):
                    
                    self.device.set_output_value(channel=0,value = int(value))
                    V1list.append(self.device.get_input_value(channel = 1))
                    V2list.append(self.device.get_input_value(channel = 2))
                    
                VLED = self.adc_to_volt(np.asarray(V1list)-np.asarray(V2list))
                ILED = self.adc_to_volt(np.asarray(V2list))*1000/self._resistor_value
                ILED_mean.append(ILED)
                VLED_mean.append(VLED)
            self.standby()
            return (np.mean(VLED_mean,axis=0),np.mean(ILED_mean,axis=0),
                    np.std(VLED_mean,axis=0)/np.sqrt(N),np.std(ILED_mean,axis=0)/np.sqrt(N))
        
    def scan_volt(self, start=0,stop=3.3,step=11,N=int(1)):
        """Performs a voltage scan from start to stop value, with steps of step.
        The total number of scans N can be chosen, default = 1.

        Args:
            start (float): start value of scan in volt.
            stop (float): stop value of scan in volt.
            step (int, optional): Scan steps. Defaults to 10.
            N (int, optional): Number of scans. Defaults to int(1).

        Returns:
            Array: 4x1 array: the mean of the voltage applied,
            the mean of the current measured and the uncertainty of the current and voltage.
        """
        if (start or stop) > self._max_voltage:
            print('not possible1')
            pass
        
        elif start>=stop:
            print('not possible2')
            return None
        
        elif N<1:
            print('Number of measurements need to be larger than 0.')
            
        else:
            VLED_mean = []
            ILED_mean = []
            for n in range(int(N)):
                V1list = []
                V2list = []
                for value in np.linspace(start,stop,step):
                    self.device.set_output_value(channel=0,value = self.volt_to_adc(value))
                    V1list.append(self.adc_to_volt( self.device.get_input_value(channel = 1)))
                    V2list.append(self.adc_to_volt(self.device.get_input_value(channel = 2)))
                    
                VLED = np.asarray(V1list)-np.asarray(V2list)
                ILED = np.asarray(V2list)/self._resistor_value
                ILED_mean.append(ILED)
                VLED_mean.append(VLED)
            self.standby()
            return (np.mean(VLED_mean,axis=0),np.mean(ILED_mean,axis=0),
                    np.std(ILED_mean,axis=0)/np.sqrt(N),np.std(VLED_mean,axis=0)/np.sqrt(N))
    
    def measure_volt(self,channel,N,volt):
        """Measures voltage of specific channel N times, with input voltage Volt.
    

        Args:
            channel (int): choose channel number 1 or 2.
            N (int): the number of measurements.
            volt (float): the applied voltage to ch0.

        Returns:
            array: the measured values in volt.
        """
        if volt > self._max_voltage:
            print('No such thing as V>3.3 volt')
            return
            
        if int(channel)>2 or int(channel)<0:
            print('Good Job, this cannot happen')
            return 
        
        self.device.set_output_volt(0,value = volt)
        Vlist = []
        for i in range(N):
            Vlist.append(self.adc_to_volt(self.device.get_input_value(channel = int(channel))))           

        self.standby()
        return np.asarray(Vlist)
    
    def measure_value(self,channel,N,value):
        """Measures voltage (adc) of specific channel N times, with input voltage Volt.
    

        Args:
            channel (int): choose channel number 1 or 2.
            N (int): the number of measurements.
            volt (float): the applied voltage to ch0.

        Returns:
            array: the measured values in volt.
        """
        if int(channel)>2 or int(channel)<0:
            print('Good Job, this cannot happen')
            pass
        
        self.device.set_output_value(0,value = value)
        Vlist = []
        for i in range(N):
            Vlist.append(self.adc_to_volt(self.device.get_input_value(channel = int(channel))))
            
        self.standby()
        return (Vlist)
    
    def close(self):
        """deletes devices.
        """
        self.standby()
        del self.device
