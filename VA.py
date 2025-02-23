
# Header VA.py (Voice Assistant)
#    Imports
        # Tkinter Package (used for GUI)
        # Speech Recognition Package (used for Speech Recognition)
        # PyAudio Package (Used for Audio)
        
from tkinter import *
from tkinter import ttk
import pygame
import speech_recognition as sr
import pyaudio as pa
from datetime import datetime 
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
#root.configure(bg="grey")
root.geometry(f"425x500")
frm.grid()


current_time = datetime.now()
#Pygame Frame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

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

speech_engine = pyttsx3.init()

def textToSpeech(phrase):
    speech_engine.say(phrase)
    speech_engine.runAndWait()

greeting_phrase = "Hello! I am your personal Voice Assistant. Click Speak to get started"
greeting_label = Label(root, text="Hello! I am your personal Voice Assistant. Click Speak to get started!")
greeting_label.grid() 

textToSpeech(greeting_phrase)

def open_browser(browserInput):
        browser = webdriver.Firefox()
        browser.get("https://google.com")
        assert "Google" in browser.title
        searchBox = browser.find_element(By.NAME, 'q') 
        searchBox.send_keys(browserInput + Keys.RETURN)
        status_for_user = "Searched Google for " + browserInput
        textToSpeech(status_for_user)
        browser_report_label = Label(root, text=status_for_user)
        browser_report_label.grid()


def open_youtube(browserInput):
        browser = webdriver.Firefox()
        browser.get("https://youtube.com")
        #assert "Google" in browser.title
        searchBox = browser.find_element(By.NAME, 'search_query') 
        searchBox.send_keys(browserInput + Keys.RETURN)
        status_for_user = "Searched Youtube for " + browserInput
        textToSpeech(status_for_user)
        browser_report_label = Label(root, text=status_for_user)
        browser_report_label.grid()

def open_gmail(browserInput):
        browser = webdriver.Firefox()
        browser.get("https://gmail.com")
        status_for_user = "Opened Gmail. Please enter your login credentials!"
        textToSpeech(status_for_user)
        browser_report_label = Label(root, text=status_for_user)
        browser_report_label.grid()
        #assert "Google" in browser.title
        #searchBox = browser.find_element(By.NAME, 'search_query') 
        #searchBox.send_keys(browserInput + Keys.RETURN)

def rick_roll():
        browser = webdriver.Firefox()
        browser.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        status_for_user = "Get rickrolled you Son of a Gun"
        textToSpeech(status_for_user)
        browser_report_label = Label(root, text=status_for_user)
        browser_report_label.grid()

def generate_response(prompt):

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    
    return response.text

def create_label(txt):
     label = Label(root, text=txt)
     label.grid()
     

def listen():
    recognized_phrase = None
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=1)
        listening_report = "Please talk..."
        textToSpeech(listening_report)
        userSpeech = r.listen(source)


        try:
            userSpeech = r.recognize_google(userSpeech)
            user_speech_report = "Your Speech: " + userSpeech
            create_label(user_speech_report)
            textToSpeech(user_speech_report)
            recognized_phrase = userSpeech
            #label = ttk.Label(root, text = userSpeech)
        
        except sr.UnknownValueError:
            recognized_phrase = None
            print("I didn't understand that. Please try again?")
            
        except sr.RequestError as e:
            recognized_phrase = None
            print("Google Connection Error")
    
    return recognized_phrase

def drawing_app():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0,0,0))
    pygame.display.set_caption('Blackboard')
    running = True
    drawing = True
    erasing = True
    last_pos_x = None 
    last_pos_y = None
    while running:
        drawing = pygame.mouse.get_pressed()[0]
        erasing = pygame.mouse.get_pressed()[2]
        x,y = pygame.mouse.get_pos()
        # Draw if mouse is down
        if(drawing):
            pygame.draw.line(screen, (255,255,255), (x,y), (last_pos_x, last_pos_y), 3)
        if(erasing):
            pygame.draw.line(screen, (0,0,0), (x,y), (last_pos_x, last_pos_y), 50)
        last_pos_x = x
        last_pos_y = y

        for event in pygame.event.get():
            # if (event.type == pygame.mouse.get_pressed()[0]):
            #     drawing = pygame.mouse.get_pressed()[0]
            if (event.type == pygame.QUIT):
                running = False
        
        pygame.display.update()
    pygame.quit()

def main():
        
        phrase = listen()
        if(not phrase):
            return
        lowerCaseUserSpeech = phrase.lower()
        print(lowerCaseUserSpeech)

        #lowerCaseUserSpeech = listen().lower()
        #print(lowerCaseUserSpeech)

        command = "gemini"
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            response = generate_response(input)
            print(response)
            create_label(response)
            textToSpeech(response)


        command = "google"
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            open_browser(input)
        
        command = "youtube" 
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            open_youtube(input)

        command = "gmail" 
        command_length = len(command)
        if(lowerCaseUserSpeech[0:command_length])==command: 
            input = lowerCaseUserSpeech[command_length+1:]
            open_gmail(input)
        
        if(lowerCaseUserSpeech == "rickroll" or lowerCaseUserSpeech == "rick roll"):
            rick_roll()
  
#GUI Buttons
    # Speak Button (used for Speech to Text)
    # Type Button (Gives alternative option to Type)
    # Exit Button (Terminates Program)
ttk.Button(frm, text = "Speak", command = main).grid(column=0, row=0)
ttk.Button(frm, text = "Draw", command = drawing_app).grid(column=0, row=1)
ttk.Button(frm, text = "Exit", command = root.destroy).grid(column=0, row=2)


root.mainloop()