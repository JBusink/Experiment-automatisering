import matplotlib.pyplot as plt

#Voltage measured at Ch.1 and Ch.2 
V1list = [0.01, 0.15, 0.31, 0.47, 0.64, 0.79, 0.95, 1.13, 1.28, 1.44,
          1.59, 1.76, 1.92, 2.09, 2.25, 2.4, 2.57, 2.72, 2.88, 3.03, 3.09]
V2list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 0.0, 0.0, 0.02, 0.12, 0.23, 0.36, 0.49, 0.55]

VLED = V1list - V2list #Voltage drop across the LED
Resistance = 220. #Resistance
Iled = V2list*1000/Resistance #Convert voltage to current in mA in LED

fig,axes=plt.subplots(1,figsize=(6,6))

axes.scatter(VLED,Iled,c='black',s=25,fc = 'none',ec='black')

axes.set_xlim(0,None)
axes.set_ylim(-0.1,None)
axes.set_xlabel(r"$V_{Led}$ (Volt)", fontsize=12)
axes.set_ylabel(r"$I_{Led}$ (A)", fontsize=12)

plt.show()