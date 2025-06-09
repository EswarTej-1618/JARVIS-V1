#whatsapp function

import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime
import pyautogui

# Engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for voice as command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 5)  # waits for 5 sec!
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could you please say that again, sir!")
        return "None"
    return query
# Function to send WhatsApp message
def sendMessage():
    contacts = {
        "me": "+91xxxxxxxxxxxx",
        "Tej": "+91xxxxxxxxxx"
    }

    speak("Whom do you want to message, sir?")
    print("Contacts: ", ", ".join(contacts.keys()))
    use_voice_command = input("Use Voice Command for Contact? (yes/no): ").lower() == "yes"
    name = takeCommand().lower() if use_voice_command else input("Enter the name: ").lower()
    
    if name in contacts:
        speak("What's the message?")
        use_voice_command_message = input("Use Voice Command for Message? (yes/no): ").lower() == "yes"
        message = takeCommand() if use_voice_command_message else input("Enter the message: ")
        
        # Open WhatsApp Web
        # pyautogui.hotkey("winleft")  
        # sleep(1)
        # pyautogui.write("Brave")
        # sleep(1)
        # pyautogui.press("enter")
        # sleep(3) 
        
        # url = f"https://web.whatsapp.com/send?phone={contacts[name]}&text={message}"
        webbrowser.open(f"https://web.whatsapp.com/send?phone={contacts[name]}&text={message}", new=2)
        
        # webbrowser.open(url, new=2)
        # Inform user and wait for WhatsApp Web to load
        speak("Please scan the QR code if not already logged in. Message will be sent momentarily.")
        sleep(45)  # Wait for 45 seconds for the page to load and QR code to be scanned if needed
        
        # Press 'Enter' key to send the message with a shorter delay
        speak("Sending message...")
        sleep(20)  
        pyautogui.press('enter')
        
        speak("Message has been sent, sir.")
        sleep(2)
    else:
        speak("Contact not found, sir!")
        