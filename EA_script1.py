import pyvisa
rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)
device = rm.open_resource("ASRL/dev/cu.usbmodem11101::INSTR", read_termination="\r\n", write_termination="\n")
print(device.query("*IDN?"))

for volt in range(0,1024,1):
    volt = int(volt)
    print(device.query(f"OUT:CH0 {volt}"))
print(device.query("OUT:CH0 0"))