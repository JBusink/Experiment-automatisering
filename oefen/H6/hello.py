import click
from time import sleep

@click.command()
@click.argument("name")
@click.option("-c","--count",default=1,help="Number of times to print greeting.",
show_default=True, # show default in help
)
@click.option("-t","--time",default=float(0),help="Pauze between greeting.",
show_default=True, # show default in help
)
@click.option("-f","--flag",default='H',help="Press H for hello and G for Goodbye.",
show_default=True, # show default in help
)
def hello(name,count,time,flag):
    
    for _ in range(count):
        if flag == 'G':
            print(f"Goodbye {name}!")
            sleep(time)
        if flag =='H':
            print(f'Hello {name}!')
            sleep(time)
        
        
if __name__ == "__main__":
    hello()