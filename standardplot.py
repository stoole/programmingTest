import matplotlib.pyplot as plt 
import matplotlib as mpl  
import numpy as np 

x = np.linspace(0,20,100)   # List of evenly spaced numbers over the range
plt.plot(x,np.sin(x))       # Plot sine of each x 
plt.show()                  # Display plot