from controller.arduino_device import ArduinoVISADevice
import numpy as np

class DiodeExperiment:
    _ch_set_diode_voltage =0
    _resistor_value = 220.
    _max_voltage = 3.3
    
    def __init__(self,port):
        
        self.device=ArduinoVISADevice(port=port)

        pass
    
    def get_identification(self):
        print(self.device.get_identification())
        pass

    def standby(self):
        '''Set zero voltage'''
        self.device.set_output_volt(self._ch_set_diode_voltage, 0)
        pass
    
    def adc_to_volt(self, value):
        voltage = value / 1023 * 3.3
        return voltage
    
    def volt_to_adc(self, value):
        adc = int(value *1023/3.3)
        return adc
    
    def scan_value(self, start,stop,step=10,N=int(1)):
        if start>=stop:
            print('not possible')
            return None
        
        elif N<1:
            print('Number of measurements need to be larger than 0.')
            
        else:
            print(N)
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
                ILED = self.adc_to_volt(np.asarray(V2list))/self._resistor_value
                ILED_mean.append(ILED)
                VLED_mean.append(VLED)
            self.standby()
            return (np.mean(VLED_mean,axis=0),np.mean(ILED_mean,axis=0),np.std(ILED_mean)/np.sqrt(N))
        
    def scan_volt(self, start,stop,step=11,N=int(1)):
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
            return (np.mean(VLED_mean,axis=0),np.mean(ILED_mean,axis=0),np.std(ILED_mean)/np.sqrt(N))
    
    def measure_volt(self,channel,N,volt):
        if volt > self._max_voltage:
            print('No such thing as V>3.3 volt')
            pass
            
        if int(channel)>2 or int(channel)<0:
            print('Good Job, this cannot happen')
            pass
        
        self.device.set_output_volt(0,value = volt)
        Vlist = []
        for i in range(N):
            Vlist.append(self.adc_to_volt(self.device.get_input_value(channel = int(channel))))           

        self.standby()
        return (Vlist)
    
    def measure_value(self,channel,N,value):
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
        self.standby()
        del self.device
    

# from pythondaq.arduino_device import ArduinoVISADevice


# class DiodeExperiment:
#     def __init__(self):
#         # open communication with arduino
#         self.device = ArduinoVISADevice(port="ASRL3::INSTR")
#         # print information about arduino
#         # print(self.device.get_identification())
#         pass
    
#     def get_device_info(self):
#     """Get device information.

#     Returns:
#         The device identification string.

#     """
#     return self.device.get_identification()

#     def scan(self, start, stop):
#         # List for measured values
#         LED_measured_voltage = []
#         LED_measured_current = []

#         # measure voltage and current of LED when output voltage is set from 0 to 3.3 V
#         for value in np.arange(start, stop, 5):
#             # set output voltage
#             self.device.set_output_value(value=value)
#             # measure ADC value on resistance and CH1
#             resistance_value = self.device.get_input_value(channel=2)
#             channel_1_value = self.device.get_input_value(channel=1)
#             # calculate ADC value on LED, convert to voltage
#             LED_value = channel_1_value - resistance_value
#             LED_voltage = self.ADC_to_voltage(LED_value)
#             resistance_voltage = self.ADC_to_voltage(resistance_value)

#             # calculate current trough LED, is same as current trough resistance
#             LED_current = resistance_voltage / 220

#             # save measurements in lists.
#             LED_measured_voltage.append(LED_voltage)
#             LED_measured_current.append(LED_current)

#         # set LED off
#         self.device.set_output_value(0)

#         return LED_measured_voltage, LED_measured_current

#     # convert digital values of arduino to voltage
#     def ADC_to_voltage(self, value):
#         voltage = value / 1023 * 3.3
#         return voltage

# from math import sqrt
# from statistics import mean, stdev

# import numpy as np

# from pythondaq.controllers import arduino_device
# from pythondaq.controllers.arduino_device import DeviceNotFoundError


# class DiodeExperiment:
#     """An experiment to measure the current-voltage characteristic of a diode."""

#     _max_voltage = 3.3

#     _ch_set_diode_voltage = 0
#     _ch_diode_voltage = 1
#     _ch_resistor_voltage = 2
#     _resistor_value = 220

#     def __init__(self, device_name):
#         """Instantiate the class.

#         Args:
#             device_name (str): the (partial) name of the device to connec to.

#         """
#         full_name = search_device(device_name)
#         self.device = arduino_device.ArduinoVISADevice(full_name)

#     def get_device_info(self):
#         """Get device information.

#         Returns:
#             The device identification string.

#         """
#         return self.device.get_identification()

#     def set_voltage(self, voltage):
#         """Apply voltage to the high-side of the diode.

#         Args:
#             voltage (float): the voltage to apply to the high side of the diode.

#         """
#         if voltage > self._max_voltage:
#             voltage = self._max_voltage
#         self.device.set_output_voltage(self._ch_set_diode_voltage, voltage)

#     def measure(self, N=1):
#         """Measure the current through the diode.

#         The voltage must be set previously using the :meth:`set_voltage` method
#         and is applied to the high side of the diode. Because of the resistor in
#         the circuit this is not equal to the resulting voltage difference across
#         the diode.

#         An optional number of measurements can be specified to more accurately
#         measure the voltage and current through the diode and estimate the
#         measurement uncertainty.

#         Args:
#             N (int): the number of measurements to perform.

#         Returns:
#             A tuple consisting of the voltage across the diode, the current
#             through the diode, the uncertainty of the voltage and the
#             uncertainty of the current, in that order.

#         """
#         U, I = [], []
#         for _ in range(N):
#             highside_voltage = float(
#                 self.device.get_input_voltage(self._ch_diode_voltage)
#             )
#             R_voltage = float(self.device.get_input_voltage(self._ch_resistor_voltage))
#             diode_voltage = highside_voltage - R_voltage
#             current = R_voltage / self._resistor_value
#             U.append(diode_voltage)
#             I.append(current)

#         if N > 1:
#             err_U = stdev(U) / sqrt(N)
#             err_I = stdev(I) / sqrt(N)
#         else:
#             err_U = float("nan")
#             err_I = float("nan")

#         return mean(U), mean(I), err_U, err_I

#     def scan(self, start, stop, num_steps, N=1):
#         """Perform measurements across a range of voltages.

#         Scan data is stored in the :attr:`scan_data` attribute, but also
#         returned by the function call.

#         Args:
#             start (float): start of the voltage range.
#             stop (float): end of the voltage range.
#             num_steps (int): number of steps in voltage range.
#             N (int): the number of measurements to perform.

#         Returns:
#             A list of measurements. Each measurement consists of a tuple of the
#             applied voltage, the voltage across the diode, the current through
#             the diode, the uncertainty of the voltage and the uncertainty of the
#             current, in that order.

#         """
#         scan_data = []
#         for voltage in np.linspace(start, stop, num_steps):
#             self.set_voltage(voltage)
#             measurement = self.measure(N)
#             scan_data.append((voltage,) + measurement)
#         self.standby()
#         return scan_data







# def search_device(partial_name):
#     """Search for a device using a partial name.

#     Args:
#         partial_name (str): the (partial) name to search for.

#     Returns:
#         A string containing the full device name, or None if no match was found.

#     """
#     devices = list_devices()
#     for device in devices:
#         if partial_name in device:
#             return device
#     raise DeviceNotFoundError(f"No device found matching string '{partial_name}'")



    