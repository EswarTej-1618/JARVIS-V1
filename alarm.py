import pyttsx3
import datetime
import os

#define engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

extractedtime = open("AlarmText.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("AlarmText.txt","r+")
deletetime.truncate(0)
deletetime.close()

#automise time or alarm function
def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timeset.replace("set an alarm","")
    timenow = timeset.replace(" and ",":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir")
            os.startfile("nokia.mp3")
        elif currenttime+"00:00:30" == Alarmtime:
            exit()

#function call 
ring(time)
