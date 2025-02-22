
# Header VA.py (Voice Assistant)
#    Imports
        # Tkinter Package (used for GUI)
        # Speech Recognition Package (used for Speech Recognition)
        # PyAudio Package (Used for Audio)
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import PyAudio as pa

# GUI Frame
    #Using Tkinter
root = Tk()
frm = ttk.Frame(root, padding = 20)
frm.grid()


#GUI Buttons
    # Speak Button (used for Speech to Text)
    # Type Button (Gives alternative option to Type)
    # Exit Button (Terminates Program)
ttk.Button(frm, text = "Speak", command = root.destroy).grid(column=0, row=0)
ttk.Button(frm, text = "Type", command = root.destroy).grid(column=0, row=1)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column=0, row=2)




root.mainloop()

