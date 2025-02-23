
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
import pyttsx3 
from dotenv import load_dotenv, dotenv_values
from google import genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# GUI Frame
    #Using Tkinter
root = Tk()
frm = ttk.Frame(root, padding = 20)
root.title("My Voice Assistant")
root.configure(bg="grey")
root.geometry(f"372x124")
frm.grid()

# Speech Recognition Functions
r = sr.Recognizer()
#r.energy_threshold = 3000

#Gemini Set Up
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_KEY:
    print("Error: Trouble accessing .env file!")
    raise Exception
client = genai.Client(api_key=GEMINI_KEY)

#TexttoSpeech Set Up

speechEngine = pyttsx3.init()

def textToSpeech(phrase):
    speechEngine.say(phrase)
    speechEngine.runAndWait()

greetingPhrase = "Hello! I am your personal Voice Assistant. Click Speak to get started"

textToSpeech(greetingPhrase)

def open_browser(browserInput):
        browser = webdriver.Firefox()
        browser.get("https://google.com")
        assert "Google" in browser.title
        searchBox = browser.find_element(By.NAME, 'q') 
        searchBox.send_keys(browserInput + Keys.RETURN)

def generate_response(prompt):

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

def listen():
    recognized_phrase = None
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=1)
        print("Please talk...")
        userSpeech = r.listen(source)


        try:
            userSpeech = r.recognize_google(userSpeech)
            print("Your Speech: " + userSpeech)
            recognized_phrase = userSpeech
            #label = ttk.Label(root, text = userSpeech)
        
        except sr.UnknownValueError:
            recognized_phrase = None
            print("I didn't understand that. Please try again?")
            
        except sr.RequestError as e:
            recognized_phrase = None
            print("Google Connection Error")
    
    return recognized_phrase

def main():
        
        lowerCaseUserSpeech = listen().lower()
        print(lowerCaseUserSpeech)

        command = "gemini"
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            response = generate_response(input)
            print(response)
            textToSpeech(response)

        command = "google"
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            open_browser(input)
        
        

    
#GUI Buttons
    # Speak Button (used for Speech to Text)
    # Type Button (Gives alternative option to Type)
    # Exit Button (Terminates Program)
ttk.Button(frm, text = "Speak", command = main).grid(column=0, row=0)
ttk.Button(frm, text = "Type", command = root.destroy).grid(column=0, row=1)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column=0, row=2)


root.mainloop()
