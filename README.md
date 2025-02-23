# Voice-Assistant
Ohlone Hackathon 5.0 Project 

This submission is for 'education' category, so it is focused on study.

This Voice Assistant:
- Has a GUI with 4 Buttons - Speak, Draw, Help, Exit
- Has a Blackboard Feature for students to take notes or draw. Opens a new pyGame tab where you can draw lines with mouse 1 and erase with mouse 2
- Can open Firefox tabs on Google, DuckDuckGo, and YouTube, enter what you wanted to search for in their respective searchbars, and load the search all hands-free.
- Can open Gmail.com
- Can list all its abilities if you click the Help Button or if you say “Help”
- Has a chat history feature for the User on the GUI. The User’s speech and the Voice Assistant’s responses are logged on.
- Is Linked with Google Gemini to fetch responses to the user for whatever inquiries they have.
- The Voice Assistant repeats its responses in an audible voice in addition to logging it onto the GUI.
- Has a joke feature that takes you to Never Gonna Give You Up by Rick Astley on YouTube if you say “rickroll”

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
