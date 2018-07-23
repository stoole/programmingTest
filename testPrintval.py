import matplotlib.pyplot as plt

# Print new when new breath (>5)

array = [4,6,7,6,4,2,3,4,7,3,2,6,4,3,2,3,6,3,2,3,4,5,6,3,2,4,6,4]

oldval = 1
time = 0
Cycs = []

for newval in array:
    if newval < 5:
        if oldval > 5:
            Cyc = float(time) # record start time of new cycle
            Cycs.append(Cyc)
    oldval = newval
    time = time+1

# first cycle starts at Cycs[0]
# goes until Cycs[1]


NumCycles = len(Cycs)-1
AvgDur = (Cycs[NumCycles]-Cycs[0])/NumCycles
print(NumCycles,'cycles')
print(AvgDur,'ms per cycle')

#plt.plot(array)
#plt.show()
#plt.close()
