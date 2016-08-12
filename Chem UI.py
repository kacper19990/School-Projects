from tkinter import *
from tkinter import ttk
import decimal
from fractions import Fraction

def calculate(*args):																		#The calculating part of the code
		try:
			value = (float(M1.get()) / 1000) * float(V1.get())
			end = (((float(value) * float(Ratio.get())) / float(Used.get())) * 1000)
			end1 = str(round(end,2))
			Conc.set(end1)
		except ValueError:
			pass

root = Tk()
root.title("Calculating Concentration")															#Title of the box


mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

M1 = StringVar()
V1 = StringVar()
Ratio = StringVar()
Used = StringVar()
Conc = StringVar()

M1_entry = ttk.Entry(mainframe, width=5, textvariable=M1)										#Allows the user to input data
M1_entry.grid(column=2, row=1, sticky=(W, E))													#Creates a box for the user to input data to

V1_entry = ttk.Entry(mainframe, width=5, textvariable=V1)
V1_entry.grid(column=2, row=2, sticky=(W, E))

Ratio_entry = ttk.Entry(mainframe, width=5, textvariable=Ratio)
Ratio_entry.grid(column=2, row=3, sticky=(W, E))

Used_entry = ttk.Entry(mainframe, width=5, textvariable=Used)
Used_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=Conc).grid(column=3, row=5, sticky=(W, E))					#Shows the user the output
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=5, sticky=W)		#Creates a button with the word "Calculate" as seen on the screen

ttk.Label(mainframe, text="Molarity of the first substance").grid(column=3, row=1, sticky=W)	#Creates the text that is shown beside each box, to instruct the user what to do
ttk.Label(mainframe, text="Volume of the first substance").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Ratio of the liquids").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="Amount of titrate used").grid(column=3, row=4, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)					#Spaces out the boxes in order to not have them on top of each other

M1_entry.focus()
root.bind('<Return>', calculate)																#

root.mainloop()																					#Loops the whole code to the beginning to allow the user to change the input without restarting the program each time
#╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
