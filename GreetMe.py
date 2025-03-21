import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    

def greet_me():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning, Sir!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon, Sir!")
    elif hour >=16 and hour <19:
        speak("Good Evening, Sir!")
        
    speak("I am Jarvis. How may I assist you?")