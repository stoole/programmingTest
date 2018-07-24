""" Shannon Toole
    Rinberg Lab Programming Test
    July 2018                   
"""

##############
import h5py
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


## a) Load HDF5 Data File
FileName = 'data.h5'
DataFile = h5py.File(FileName,'r')

## b) Obtain Trial0004 Sniff Data
TrialNum = 'Trial0004'              # Selected Trial
GroupName = 'sniff'                 # Selected Group

TrialData = DataFile[TrialNum]
GroupFile = TrialData[GroupName]

## Combine Packets into Single Array
SniffArray = GroupFile[0]                                   # First array
for num in range(len(GroupFile)):
    NextArray = GroupFile[num]                              # Next array
    SniffArray = np.concatenate((SniffArray,NextArray))     # Concatenate

NumVals = len(SniffArray)                                   # Number of Data Points
time = list(range(1,NumVals+1))                             # Time array

## c) Segment Into Individual Sniff Cycles
i = 0                                   # Initialize counter variable
timVal = []; sigVal = []                # Initialize arrays
pastVal = SniffArray[0]                 # Start with first value in array
for val in SniffArray:
    if val <= -50 and pastVal > -50:    # If signal passes threshold
        sigVal.append(float(val))       # Value at start of inhalation
        timVal.append(float(i))         # Time of start of inhalation
    pastVal = val
    i = i+1

numCycles = len(timVal)-1                              # Number of Complete Sniff Cycles
avgDur = (timVal[numCycles] - timVal[0]) / numCycles   # Average Duration (of Complete Cycle)

## Plot Data
def plotData():
    def _destroyWindow():
        root.quit()         # Exit main loop
        root.destroy()      # Destroy widget

    fig = plt.figure()
    plt.plot(time,SniffArray,label='Sniff trace')
    plt.plot(timVal,sigVal,'bo',label='Start of inhalation')
    plt.axis([min(time),max(time),min(SniffArray),max(SniffArray)])
    plt.xlabel('Time (milliseconds)')
    plt.title('Sniff Trace')
    plt.legend(fontsize='small')
    
    root = tk.Tk()                                      # Root
    root.title("Toole - Programming Test [Jul18]")
    root.geometry('900x400')                            # Window size
    root.withdraw()                                     # Remove default window
    root.protocol('WM_DELETE_WINDOW', _destroyWindow)   # If window is closed, quit loop
    
    canvas = FigureCanvasTkAgg(fig, master=root)                    # Create drawing area
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)      # Fit to window

    root.update()           # Update display
    root.deiconify()        # Redraw widget
    root.mainloop()         # Main loop

plotData()
print(numCycles,'sniff cycles')
print(round(avgDur,2),'ms per cycle\n')