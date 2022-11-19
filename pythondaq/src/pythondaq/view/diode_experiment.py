import click
from pythondaq.model.DiodeExperiment import DiodeExperiment
from pythondaq.controller.arduino_device import *

"""A CLI to measure the current-voltage characteristic of a LED.
In this experiment, a specific circuit schematic is assumed. 
The circuit contains a diode (e.g. a LED) and a resistor in series. 
A voltage is applied to the high side of the diode and the low side of the resistor is grounded. 
The voltage across the diode and the resistor are measured and the 
latter is used to calculate the current flowing through the diode.
"""


@click.group()
def cmd_group():
    """A CLI to measure the current-voltage characteristic of a LED.
    """
    pass


@cmd_group.command("measure_voltage")
@click.option(
    "-n", "--number", default = 1, type = int, show_default = True, required = True,
     help="Number of measurements.")
@click.option(
    "-v", "--voltage",default = 0, type = float, show_default = True, required = True,
     help="Voltage to apply to the diode.")
@click.option("-c", "--channel", default = 1, type = int, show_default = True, required = True,
 help = "Channel number: 1 or 2." )
@click.option("-d", "--data/--no-data",default=False,show_default = True,
help="Save a csv of the current versus the applied voltage.")
def measure_voltage(voltage, number,channel,data):
    """Measure the voltage of a given channel number, N times.

    Args:
        voltage (float): the applied voltage to Ch. 0.
        number (int): the number of measurement.
        channel (int): the channel number of the device (1 or 2).
    """

    info_devices()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)

    Vled = measurement.measure_volt(channel=channel, N=number, volt = voltage) 
    measurement.close()
    df = pd.DataFrame({'Vled(V)':Vled})
    if data:
        path = 'data'
        if path_check(path):
            i = 0
            for filename in os.listdir(path):
                if filename.endswith(f'measurement_{i}.csv'):
                    i += 1
        df.to_csv(f'{path}/Vch{channel}_Vinp{voltage}_{i}.csv', sep = ',',index=True,index_label='Index')
    


@cmd_group.command("measure_current")
@click.option(
    "-n", "--number", default = 1, type = int, show_default = True, required = True, help="Number of measurements.")
@click.option(
    "-v", "--voltage",default = 0, type=float, show_default = True, required=True, help="Voltage to apply to the diode.")
@click.option("-d", "--data/--no-data",default=False,show_default = True,
help="Save a csv of the current versus the applied voltage.")
def measure_current(voltage, number,data):
    """Measure the current of the LED using a predescribed breadboard.
    The current is derived from the voltage difference of channel 2 divided by the
    resistance of 220 ohm.

    Args:
        voltage (float): the applied voltage to Ch. 0.
        number (int): the number of measurements.
    """
    info_devices()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)

    Iled = measurement.measure_volt(channel=2, N=number, volt = voltage)/220. 
    measurement.close()
    df = pd.DataFrame({'Iled(A)':Iled})
    if data:
        path = 'data'
        if path_check(path):
            i = 0
            for filename in os.listdir(path):
                if filename.endswith(f'measurement_{i}.csv'):
                    i += 1
        df.to_csv(f'{path}/Iled_Vinp{voltage}_{i}.csv', sep = ',',index=True,index_label='Index') 

        

    


@cmd_group.command('scan')
@click.option("-s", "--start", default=0.,type=click.FloatRange(0, 3.3), help="Start position of scan in Volt.")
@click.option("-e", "--end", default=3.3,type=click.FloatRange(0, 3.3), help="End position of scan in Volt (3.3 Volt max.).")
@click.option("-s", "--step", default=10,type=int, help="Number of datapoints.")
@click.option("-n", "--number", default=2,type=int, help="Number of scans.")
@click.option("-g", "--graph/--no-graph",default=False,
help="Plot a graph of the current versus the applied voltage.",)
@click.option("-d", "--data/--no-data",default=False,show_default = True,
help="Save a csv of the current versus the applied voltage.",)
@click.option("-i", "--info/--no-info",default=False,
help="Print device information.",)
def scan(start,end,step,number,graph,data,info):
    """A scan method (in voltage) that varies the applied voltage and measures the current and Voltage
    of the LED. If the number of scan is larger than 1, it returns the err on the mean of the current 
    and Voltage.

    Args:
        Start (float): Start voltage of the scan, default = 0 Volt.
        Finish (float): End voltage of the scan, default (and maximum) =  3.3 Volt.
        Number (int): The total number of scans, default = 1.
        Interval (int): The total number of datapoint, default = 20.`
    """

    info_devices()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)
    Vled,Iled,Iled_err,Vled_err = measurement.scan_volt(start,end,step, number)
    df  = [Vled,Iled,Iled_err,Vled_err]
    if data:
        data_to_csv(df)
    if graph:
        plot_graph(Vled,Iled,Iled_err,Vled_err)
    if info:
        print(measurement.get_identification())
    else:
        return df



@cmd_group.command('list')
def list():
    """Shows the available devices and the current version of the
    firmware of the device.
    """
    info_devices()
    


if __name__ == "__main__":
    cmd_group()