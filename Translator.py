from time import sleep
import googletrans
from gtts import gTTS
from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
#engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#function for voice as commond
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5) #waits for 5 sec!
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could you please say that again, sir!")
        return "None"
    return query

#function for translate from English to any language
def translategl(query):
    speak("sure sir!")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    
    chooseLang = input("To the Language :- ")
    text_to_translate = translator.translate(query,src = "auto", dest = chooseLang)
    text = text_to_translate.text
    
    try:
        speakgl = gTTS(text = text ,lang = chooseLang, slow = False )
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        sleep(10)
        os.remove("voice.mp3")
    except:
        print("Unable to Translate sir")