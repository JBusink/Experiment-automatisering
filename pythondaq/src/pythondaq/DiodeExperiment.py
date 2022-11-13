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
    


    