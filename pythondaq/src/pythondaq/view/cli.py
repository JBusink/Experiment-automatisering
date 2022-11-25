import click
from pythondaq.model.DiodeExperiment import DiodeExperiment, devices_list,devices_info
import pandas as pd
import os
import matplotlib.pyplot as plt
from rich.console import Console

# Console object with which the interface can be decorated
console =Console()

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
    "-v", "--voltage",default = 0, type = click.FloatRange(0,3.3), show_default = True, required = True,
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

    devices_info()
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
    "-v", "--voltage",default = 0, type=click.FloatRange(0,3.3), show_default = True, required=True, help="Voltage to apply to the diode.")
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
    devices_info()
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
@click.option("-i", "--interval", default=10,type=int, help="Number of datapoints.")
@click.option("-n", "--number", default=2,type=int, help="Number of scans.")
@click.option("-g", "--graph/--no-graph",default=False,
help="Plot a graph of the current versus the applied voltage.",)
@click.option("-d", "--data/--no-data",default=False,show_default = True,
help="Save a csv of the current versus the applied voltage.",)
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

    devices_info()
    device_index = input("Please choose the index of the device to use: ")
    measurement= DiodeExperiment(port=device_index)
    Vled,Iled,Vled_err,Iled_err = measurement.scan_volt(start,end,interval, number)
    df  = [Vled,Iled,Iled_err,Vled_err]

    print_data(Vled,Iled,Iled_err,Vled_err)
    if data:
        data_to_csv(df)
    if graph:
        plot_graph(Vled,Iled,Iled_err,Vled_err)


@cmd_group.command('list')
def list():
    """Shows the available devices and the current version of the
    firmware of the device.
    """
    print(devices_list()) 

@cmd_group.command('info')
def info():
    """Shows the available devices and the current version of the
    firmware of the device.
    """
    devices_info() 


##Extra functions
def print_data(U,I,err_U,err_I):
    """Prints U,I, dU, dI in rich console.

    Args:
        U (float): Voltage in volt.
        I (float): current in ampere.
        err_U (float): error on Voltage in volt.
        err_I (float): error on Current in ampere.
    """
    console.print("U [V] \t\t I \[mA] \t err_U [V] \t err_I \[mA]",  style='bold underline white on black')
    for i,j,k,l in zip(U,I,err_U,err_I):
        console.print(f"{i}\t\t{j}\t\t{k}\t\t{l}",style = 'white bold on black')



def data_to_csv(data):
    Vled,Iled,Iled_err,Vled_err = data
    """Saves data to csv file. Creates csv file at new folder data/measurement_index.csv.
    Index is checked and counts up if pre-excisting.

    Args:
        data list : list of data.
    """
    path = 'data'
    if path_check(path):
        i = 0
        for filename in os.listdir(path):
            if filename.endswith(f'measurement_{i}.csv'):
                i += 1
    df = pd.DataFrame({'Vled(V)':Vled, 'Iled(A)':Iled,'Vled_err':Vled_err,'Iled_err(A)':Iled_err})
    df.to_csv(f'{path}/scan_{i}.csv', sep = ',',index=True,index_label='Index') 


def path_check(path):
    """Check if path excist, if not create folder.

    Args:
        path (str): location of the path.

    Returns:
        Boolean: True of False.
    """
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("Not allowed to write in this path, please change the permissions or run the program through a different path")
            return False
    return True

def plot_graph(Vled,Iled,Iled_err,Vled_err):
    """Plot a graph of the measurements.

    Plots a graph of the current versus the applied voltage.

    Args:
        4 (list): list of measurements. 
    """
    
    fig,axes=plt.subplots(1,1,figsize=(8,4))
    axes.errorbar(Vled,Iled,xerr=Vled_err,yerr=Iled_err,ms =5,color= 'black',
                mfc='white',mec='black',fmt='.',elinewidth=2,capsize=2)
    axes.set_ylabel(r'$I_{led} (A)$',fontsize=14)
    axes.set_xlabel(r'$V_{led} (V)$',fontsize=14)
    axes.set_xlim(0,None)
    axes.set_ylim(-0.001,None)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    cmd_group()