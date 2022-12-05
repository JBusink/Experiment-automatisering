from pythondaq.controller.arduino_device import ArduinoVISADevice,list_devices,info_devices
import numpy as np
import threading

class PV:
    """Solar cell experiment class. This is a model based on a Arduino 33IOT. The input/output voltage is a
    digital number {0,...,1023}, this is converted along a linear scale to 3.3 Volt. 
    

    Returns:
        _type_: _description_
    """
    _max_voltage = 3.3
    _max_value = 1023.

    _ch_set_gate_voltage = 0
    _ch_pv_voltage = 1
    _ch_resistor_voltage = 2

    _resistor_value = 4.7
    
    def __init__(self,port):
        """Initializes the diode class.

        Args:
            port (int): needs device string, using list_devices we ask for the avaialble ports
            the user is asked to provide the number of the device. 
        """
        self.device_model = ArduinoVISADevice(port = port)
        pass
    
    def get_identification(self):
        """Provides the firmware version in the arduino device.
        """
        print(self.device_model.get_identification())

    def standby(self):
        """Standby mode, applies 0 voltage.
        """
        self.device_model.set_output_volt(self._ch_set_gate_voltage, 1023)
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
        
    
    def measure_volt(self,volt,N=2):
        """_summary_

        Args:
            volt (_type_): _description_
            N (int, optional): _description_. Defaults to 2.

        Returns:
            _type_: _description_
        """
        if volt > self._max_voltage:
            print('No such thing as V>3.3 volt')
            return
            
        
        self.device_model.set_output_volt(self._ch_set_gate_voltage ,value = volt)
        Vlist = []
        Ilist = []
        Plist = []
        Rlist = []
        for _ in range(N):
            pv_voltage = float(self.device_model.get_input_value(self._ch_pv_voltage)*self._max_voltage*3/self._max_value)
            voltage_resistor = (float(self.device.get_input_value(self._ch_resistor_voltage)* self._max_voltage/ self._max_value))
            current = voltage_resistor/self._resistor_value
            power = current*pv_voltage

            Vlist.append(pv_voltage)
            Ilist.append(current)
            Plist.append(power)
            Rlist.append(pv_voltage/current)

        errU  = np.std(Vlist)/np.sqrt(N)
        errI  = np.std(Ilist)/np.sqrt(N)
        errP  = np.std(Plist)/np.sqrt(N)
        errR  = np.std(Rlist)/np.sqrt(N)

        self.standby()
        return np.mean(pv_voltage),np.mean(current),np.mean(power),np.mean(Rlist),errU,errI,errP,errR

    
    def close(self):
        """deletes devices.
        """
        self.standby()
        del self.device_model

    def start_scan(self, start, stop, steps, N=2):
        self._scan_thread = threading.Thread(
            target=self.scan_individual, args=(start, stop, steps, N)
        )
        self._scan_thread.start()

    def scan_individual(self,start,stop,step,N):
        self.data_measure = []
        for i in np.linspace(start,stop,step):
            data = self.measure_volt(i,N)
            self.data_measure.append(data)

        return self.data_measure



def devices_list():
    return list_devices()

def devices_info():
    return info_devices()