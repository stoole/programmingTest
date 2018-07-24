
import tkinter as tk
#import tkinter.ttk as ttk 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.title("welcome")
window.geometry('350x200')      # 350x200 pixels
#combo = ttk.Combobox(window)
#combo['values'] = (1,2,3,4,5,"text")
#combo.current()     # set the selected item
#combo.grid(column=0,row=0)
lbl = tk.Label(window,text="hey", font=("arial bold",10))
lbl.grid(column=0,row=0)        # need to call for it to show up
txt = tk.Entry(window,width=10)
txt.grid(column=1,row=0)
txt.focus()     # automatically set focus 
def clicked():
    res = "nice " + txt.get()
    lbl.configure(text=res)
btn = tk.Button(window,text="click",command=clicked)
btn.grid(column=2,row=0)        # second column, not on top of label
window.mainloop()               # endless loop, wait for user interaction until close
# if you forget mainloop, nothing will appear



"""
fig = plt.figure()      # Define figure
x = [1,2,3]
y = [3,4,5]
plt.plot(x,y)

def _destroyWindow():   # Destroy window
    root.quit()         # Exit main loop
    root.destroy()      # Destroy widget

root = tk.Tk()          # Root
root.withdraw()         # Remove default window
root.protocol("WM_DELETE_WINDOW",_destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)        # Create drawing area
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)    

root.update()           # Update display
root.deiconify()        # Redraw widget
root.mainloop()


"""
