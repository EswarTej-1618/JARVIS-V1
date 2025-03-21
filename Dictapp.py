import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)


# functions for text to speech 
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
dictapp ={"vlc media":"vlc","vscode":"code","chrome":"chrome","brave":"brave","media player":"mediaplayer","settings":"ms-settings:","notepad":"notepad","photos":"ms-photos:","whatsapp":"whatsapp:","camera":"microsoft.windows.camera:","paint":"mspaint", "store":"ms-windows-store:","teams":"ms-teams:","this pc":"shell:MyComputerFolder"} # write all apps!

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".in" in query or ".org" in query or ".co.in" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")
def closeappweb(query):
    speak("closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
    elif "five tabs" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed")
        
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
