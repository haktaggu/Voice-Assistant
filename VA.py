
# Header VA.py (Voice Assistant)
#    Imports
        # Tkinter Package (used for GUI)
        # Speech Recognition Package (used for Speech Recognition)
        # PyAudio Package (Used for Audio)
        
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
import pyaudio as pa
import os
from dotenv import load_dotenv, dotenv_values
from google import genai

# GUI Frame
    #Using Tkinter
root = Tk()
frm = ttk.Frame(root, padding = 20)
frm.grid()

# Speech Recognition Functions
r = sr.Recognizer()
#r.energy_threshold = 3000

#Gemini SetUp
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    print("Error: Trouble accessing .env file!")
    raise Exception
client = genai.Client(api_key=GEMINI_KEY)

def listen():
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=1)
        print("Please talk...")
        userSpeech = r.listen(source)

        try:
            userSpeech = r.recognize_google(userSpeech)
            print("Your Speech: " + userSpeech)
            label = ttk.Label(root, text = userSpeech)
        
        except sr.UnknownValueError:
            print("I didn't understand that. Please try again?")
            

        except sr.RequestError as e:
            print("Google Connection Error")

        lowerCaseUserSpeech = userSpeech.lower()

        if(lowerCaseUserSpeech[0:14])=="ask gemini for": 
            _,_, geminiInput = userSpeech.partition("ask gemini for ")
            print(geminiInput)
            response = client.models.generate_content(
                 model="gemini-2.0-flash", contents=geminiInput
            )
        

    
#GUI Buttons
    # Speak Button (used for Speech to Text)
    # Type Button (Gives alternative option to Type)
    # Exit Button (Terminates Program)
ttk.Button(frm, text = "Speak", command = listen).grid(column=0, row=0)
ttk.Button(frm, text = "Type", command = root.destroy).grid(column=0, row=1)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column=0, row=2)


root.mainloop()

