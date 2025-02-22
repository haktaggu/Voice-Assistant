
# Header
#    Imports
from tkinter import *
from tkinter import ttk
import speech_recognition as sr

# GUI Frame
root = Tk()
frm = ttk.Frame(root, padding = 20)
frm.grid()


#GUI Buttons
ttk.Button(frm, text = "Speak", command = root.destroy).grid(column=0, row=0)
ttk.Button(frm, text = "Type", command = root.destroy).grid(column=0, row=1)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column=0, row=2)




root.mainloop()

