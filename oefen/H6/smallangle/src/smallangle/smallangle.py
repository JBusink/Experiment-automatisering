import click
import numpy as np
import pandas as pd


@click.group()
def cmd_group():
    pass


@cmd_group.command("sin")
@click.option("-n", "--number", default=5, help="Number of samples in linear spacing")
def sin(number):
    """Compares the value of sin(x) with x ([-n --number]). Both values are returned in a datafram.

    Args:
        number (int): makes a list from 0 to 2*pi with n number of steps.
    """
    x = np.linspace(0, 2 * np.pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command("tan")
@click.option("-n","--number",default = 5,help = "Number of samples in linear spacing")
def tan(number):
    """Compares the value of tan(x) with x ([-n --number]). Both values are returned in a datafram.
    [-n --number]\f

    Args:
        number (int): makes a list from 0 to 2*pi with n number of steps.
    """
    x = np.linspace(0, 2 * np.pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@cmd_group.command("approx")
@click.option("-e","--epsilon",default = .01,help = "Define epsilon in which abs(x-sin(x))<= epsilon.")
def approx(epsilon):
    """Returns the angle in degrees in which the small angle approximation 
    sin(x) $\approx$ x still holds ([-e --epsilon]).
    The approximation abs(x-sin(x))<= epsilon, for epsilon default at 0.01.\f  
    

    Args:
        epsilon (float): float that defines the quality of the approximation.
    """
    x = np.arange(0,2*pi,0.0001)
    y = np.sin(x)
    for i in range(len(x)):
        if abs(x[i]-y[i])<=epsilon:
            angle = i
        else: 
            pass
    print("Angle is approximately:", round(x[angle]*180/pi,6),"degrees")

if __name__ == "__main__":
    cmd_group()