from GreeterBot import GreeterBot

def init_greeter(greeter):

    try:
        while True:
            inp = input("Say hi or type 'info'\npress ctrl+c and enter to quit\n")
            if inp == "info":
                greeter.get_info()
            else:
                print(greeter.get_greeting())

    except KeyboardInterrupt:
        print("Quitting the GreeterBot. See you later!")

if __name__ == "__main__":
    seed = 15
    greeter = GreeterBot()
    greeter.set_seed(seed)
    init_greeter(greeter)