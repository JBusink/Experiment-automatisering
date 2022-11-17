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


@cmd_group.command('scan')
@click.option("-s", "--start", default=0.,type=float, help="Start position of scan in Volt.")
@click.option("-e", "--end", default=3.3,type=float, help="End position of scan in Volt (3.3 Volt max.).")
@click.option("-i", "--interval", default=10,type=int, help="Number of datapoints.")
@click.option("-n", "--number", default=2,type=int, help="Number of scans.")
@click.option("-g", "--graph/--no-graph",default=False,help="Plot a graph of the current versus the applied voltage.",
)
@click.option("-c", "--data/--no-data",default=False,help="Save a csv of the current versus the applied voltage.",
)
def scan(start,end,interval,number,graph,data):
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
    Vled,Iled,Iled_err,Vled_err = measurement.scan_volt(start,end,interval, number)
    df  = [Vled,Iled,Iled_err,Vled_err]
    if data:
        data_to_csv(df)
    if graph:
        plot_graph(Vled,Iled,Iled_err,Vled_err)
    else:
        return df


@cmd_group.command('list')
@click.argument("tekst",type=str)
def list(tekst):
    print(f'hello {tekst}')



@cmd_group.command('ID')
def identification():
    """Shows the available devices and the current version of the
    firmware of the device.
    """
    info_devices()
    ArduinoVISADevice(port = list_devices()[2]).get_identification()     
    
    
if __name__ == "__main__":
    cmd_group()