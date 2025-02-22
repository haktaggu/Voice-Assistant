import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
from google import genai
# importing gemini AI
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

recognized_phrase = None

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    recognized_phrase = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + recognized_phrase)
except sr.UnknownValueError:
    recognized_phrase = None
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    recognized_phrase = None
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

load_dotenv() 

# accessing gemini API key
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    print("It seems that you don't have the .env file configured!")
    raise Exception
client = genai.Client(api_key=GEMINI_KEY)



input_text = recognized_phrase


response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input_text
)

print(response.text)
