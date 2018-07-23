""" Shannon Toole
    Rinberg Lab Programming Test
    July 2018     """

#######

import h5py
import numpy as np
#import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

## a) Load HDF5 Data File
FileName = 'data.h5'
DataFile = h5py.File(FileName,'r')

## b) Obtain Trial0004 Sniff Data
TrialNum = 'Trial0004'                  # Selected Trial
GroupName = 'sniff'                     # Selected Group
TrialData = DataFile[TrialNum]
GroupFile = TrialData[GroupName]

## Combine All Packets in Sniff Data
DataArray = GroupFile[0]                                # First array
for num in range(1,241):
    NextArray = GroupFile[num]                          # Next array
    DataArray = np.concatenate((DataArray,NextArray))   # Concatenate
NumVals = len(DataArray)                # Number of Data Points

time = list(range(1,NumVals+1))         # Time array

## Plot Data
fig = Figure(figsize=(12,5),facecolor='white')  # Figure
axis = fig.add_subplot(111)                     # 1 Row, 1 Column
axis.set_ylim(min(DataArray),max(DataArray))    # Y Limits
axis.set_xlim(min(time),max(time))              # X Limits
axis.plot(time,DataArray)

#plt.plot(time,DataArray)
#plt.axis([min(time),max(time),min(DataArray),max(DataArray)])
#plt.xlabel('Time (milliseconds)')
#plt.ylabel('Sniff Values')
#plt.title('Sniff Trace')
#plt.show()
#plt.title(r'$\sigma_i=15$')


## c) Segment Into Individual Sniff Cycles
pastVal = DataArray[0]
i = 0
cycles = []
for val in DataArray:
    if val < -50:                   # If value is below threshold
        if pastVal > -50:           # And prior value is above
            cycle = float(i)        # Mark start of new sniff cycle
            cycles.append(cycle)
    pastVal = val
    i = i+1


# Number of Complete Cycles
numCycles = len(cycles)-1
# Average Duration (of Complete Cycle)
avgDuration = (cycles[numCycles] - cycles[0]) / numCycles

print(numCycles,'cycles')
print(avgDuration,'ms per cycle')