class DiodeExperiment:
    _ch_set_diode_voltage =0
    _resistor_value = 220.
    _max_voltage = 3.3
    def __init__(self):
        return

    def standby(self):
        '''Set zero voltage'''
        self.device.set_output_voltage(self._ch_set_diode_voltage, 0)
    
    def scan(self, start,stop,device):
        self.start = start
        self.stop = stop
        for i in range(start,stop,1):
            self.device.query(f"OUT:CH{channel} "+ f"{i}")
            return (self.device.query(f"OUT:CH{channel} "+ f"{i}"))
    
    
"""An experiment to measure the current-voltage characteristic of a diode.

For this experiment, a specific circuit schematic is assumed. The circuit
contains a diode (e.g. a LED) and a resistor in series. A voltage is applied to
the high side of the diode and the low side of the resistor is grounded. The
voltage across the diode and the resistor are measured and the latter is used to
calculate the current flowing through the diode.
"""

from math import sqrt
from statistics import mean, stdev

import numpy as np

from pythondaq.controllers import arduino_device
from pythondaq.controllers.arduino_device import DeviceNotFoundError


class DiodeExperiment:
    """An experiment to measure the current-voltage characteristic of a diode."""

    _max_voltage = 3.3

    _ch_set_diode_voltage = 0
    _ch_diode_voltage = 1
    _ch_resistor_voltage = 2
    _resistor_value = 220

    def __init__(self, device_name):
        """Instantiate the class.

        Args:
            device_name (str): the (partial) name of the device to connec to.

        """
        full_name = search_device(device_name)
        self.device = arduino_device.ArduinoVISADevice(full_name)

    def get_device_info(self):
        """Get device information.

        Returns:
            The device identification string.

        """
        return self.device.get_identification()

    def set_voltage(self, voltage):
        """Apply voltage to the high-side of the diode.

        Args:
            voltage (float): the voltage to apply to the high side of the diode.

        """
        if voltage > self._max_voltage:
            voltage = self._max_voltage
        self.device.set_output_voltage(self._ch_set_diode_voltage, voltage)

    def measure(self, N=1):
        """Measure the current through the diode.

        The voltage must be set previously using the :meth:`set_voltage` method
        and is applied to the high side of the diode. Because of the resistor in
        the circuit this is not equal to the resulting voltage difference across
        the diode.

        An optional number of measurements can be specified to more accurately
        measure the voltage and current through the diode and estimate the
        measurement uncertainty.

        Args:
            N (int): the number of measurements to perform.

        Returns:
            A tuple consisting of the voltage across the diode, the current
            through the diode, the uncertainty of the voltage and the
            uncertainty of the current, in that order.

        """
        U, I = [], []
        for _ in range(N):
            highside_voltage = float(
                self.device.get_input_voltage(self._ch_diode_voltage)
            )
            R_voltage = float(self.device.get_input_voltage(self._ch_resistor_voltage))
            diode_voltage = highside_voltage - R_voltage
            current = R_voltage / self._resistor_value
            U.append(diode_voltage)
            I.append(current)

        if N > 1:
            err_U = stdev(U) / sqrt(N)
            err_I = stdev(I) / sqrt(N)
        else:
            err_U = float("nan")
            err_I = float("nan")

        return mean(U), mean(I), err_U, err_I

    def scan(self, start, stop, num_steps, N=1):
        """Perform measurements across a range of voltages.

        Scan data is stored in the :attr:`scan_data` attribute, but also
        returned by the function call.

        Args:
            start (float): start of the voltage range.
            stop (float): end of the voltage range.
            num_steps (int): number of steps in voltage range.
            N (int): the number of measurements to perform.

        Returns:
            A list of measurements. Each measurement consists of a tuple of the
            applied voltage, the voltage across the diode, the current through
            the diode, the uncertainty of the voltage and the uncertainty of the
            current, in that order.

        """
        scan_data = []
        for voltage in np.linspace(start, stop, num_steps):
            self.set_voltage(voltage)
            measurement = self.measure(N)
            scan_data.append((voltage,) + measurement)
        self.standby()
        return scan_data

    def standby(self):
        """Put the device in standby mode.

        Applies a zero voltage to the diode.

        """
        self.device.set_output_voltage(self._ch_set_diode_voltage, 0)

    def close(self):
        """Close the device.

        Applies a zero voltage to the diode before closing the connection to the
        device.

        """
        self.standby()
        del self.device


def list_devices():
    """List devices connected to the system.

    Returns:
         A list of port names.

    """
    return arduino_device.list_devices()


def search_device(partial_name):
    """Search for a device using a partial name.

    Args:
        partial_name (str): the (partial) name to search for.

    Returns:
        A string containing the full device name, or None if no match was found.

    """
    devices = list_devices()
    for device in devices:
        if partial_name in device:
            return device
    raise DeviceNotFoundError(f"No device found matching string '{partial_name}'")
