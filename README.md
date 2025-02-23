# Voice-Assistant
Ohlone Hackathon 5.0 Project 

This submittion is for 'education' categroy, so it is focused on study.

This Voice Assistant:
 - Creates a GUI for the user to use.
 - Can open browser for you and google search, open youtube, and gmail
 - Can ask Gemini
 - Has a blackboard feature for taking notes

This project uses Gemini API to run, so you need a Gemini API key
Create a .env file in the main project folder and write 
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"

This project was developed on VSCode for Mac OS X, so there will be different 
instructions for Windows. Homebrew is required on OS X. 

It also requires the packages:
* Pygame
* PyAudio
* speech_recognition
* pyttsx3
* selenium
* python-dotenv
* google-genai

Also required:
 - Firefox (only supported browser as of this version)
 - GeckoDriver from the mozila repository (place in usr/local/bin and run)
