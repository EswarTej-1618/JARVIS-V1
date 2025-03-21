import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
from Weather import weather_forecast


#password protection for jarvis only 3 chances...
for i in range(3):
    a= input("Enter password to open jarvis :- ")
    pw_file = open("Passwordfile/password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    
    if(a==pw):
        print("Welcome sir ! please speak [Wake up] to get started ")
        break
    elif(i == 2 and a != pw ):
        exit()
    elif(a!= pw):
        print("Try agian ! sir ")

#iron man 
from Intro import play_gif
play_gif

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
        print("could you please say thay again sir!")
        return "None"
    return query


#setting remainders using jarvis
def alarm(query):
    timehere= open("AlarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

#jarvis setup
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greet_me
            greet_me()
            
            while True:
                query = takeCommand().lower()
                
                if "go to sleep" in query:
                    speak("Ok sir, You can Call me anytime")
                    break
                
                ##########   Jarvis Development Phase 2    #############
                
                #change password function 
                elif "change the password" in query:
                    speak("What's the new password sir ?")
                    new_pw = input("Enter the New Password :\n")
                    new_password = open("Passwordfile/password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new Password is {new_pw}")
                
                #Schedule my day function using jarvis...
                elif "schedule my day" in query:
                    tasks = []  #Empty array list
                    speak("Do you want to clear old tasks (Please say YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query :
                        file = open("Tasks/tasks.txt","w")
                        file.write(f"")
                        file.close()
                        noOf_Tasks = int(input("Enter the No.Of Tasks:- "))
                        i=0
                        for i in range(noOf_Tasks):
                            tasks.append(input("Enter the Task :- "))
                            file = open("Tasks/tasks.txt","a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i=0
                        noOf_Tasks = int(input("Enter the No.Of Tasks:- "))
                        for i in range(noOf_Tasks):
                            tasks.append(input("Enter the Task :- "))
                            file = open("Tasks/tasks.txt","a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("Tasks/tasks.txt","r")
                    content = file.read()
                    file.close()
                    #enabling notification sound
                    mixer.init()
                    mixer.music.load("omnitrix.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My Schedule :- ",
                        message = content,
                        timeout = 15
                    )
                
                #Esay method to open app using start
                elif "open app" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    query = query.replace("app","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(4)
                    pyautogui.press("enter")
                
                #speed test function
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576 # 1Mb = 1024*1024 bytes
                    download_net = wifi.download()/1048576
                    print("Wifi upload speed is(in Mbps) : ",upload_net)
                    print("wifi download speed is(in Mbps) : ",download_net)
                    speak(f"wifi upload speed is {upload_net} Mbps")
                    speak(f"wifi downloaf speed is {download_net} Mbps")
                
                elif "ipl score" in query:
                    from GamesSearch import LiveIplScore
                    LiveIplScore()
                #########################################################
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("I am doing Great sir")
                elif "thank you" in query:
                    speak("you are welcome sir")
                elif "love you" in query:
                    speak("I love you too sir ! Together we can make everything done , If you have an Assistant like me ...")
                
                # automating youtube controls like play pause functions
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused sir")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("playing video sir")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted sir")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("decreasing the volume sir")
                    volumedown()
                    
                    
                #opening apps using voice
                elif "explorer" in query:
                    exp= "explorer";
                    os.system(f"{exp}")
                elif "calculator" in query:
                    exp= "calc";
                    os.system(f"{exp}")
                elif "open" in query.lower():
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query.lower():
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                    
                #google youtube wikipedia and perplexity!
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import SearchYoutube
                    SearchYoutube(query)
                elif"perplexity" in query:
                    from SearchNow import searchPerplexity
                    searchPerplexity(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                #News function 
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                
                #calculator function using jarvis 
                elif "calculate" in query:
                    from calculateNum import WolfRamAlpha
                    from calculateNum import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                #Whatsapp function for sending msgs for individuals
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                #Alarm set function call
                elif "set an alarm" in query:
                    print("input time example :- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                
                #weather and temperature
                elif "temperature" in query:
                    search = "temperature in pattiseema"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data =  BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                #modify this 
                elif "weather" in query:
                    from online import find_myip
                    ip_address = find_myip()
                    speak("tell me the name of your city")
                    city = input("Enter your city name: ")
                    speak(f"getting weather forecast for your city {city}")
                    weather , temp , feels_like = weather_forecast(city)
                    speak(f"the current temperature is {temp}, but it feels like {feels_like}")
                    speak(f" Also the weather report talks about {weather}")
                    speak("I am printing weather information on screen")
                    print(f"Description : {weather}\nTemperature : {temp}\nFeels Like : {feels_like}")
                #screenshot function
                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile please sir")
                    pyautogui.press("enter")   
                
                #time function
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")
                
                #Remeber function
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("sir you told me to "+rememberMessage)
                    remember = open("Remember/rememberMe.txt","w") 
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember/rememberMe.txt","r")
                    speak("sir you told me to"+remember.read())
                
                
                #Play my fav songs when i am tired
                elif "tired" in query:
                    speak("Just relax sir, I am playing you're favorite music.")
                    a = (1,2,3,4,5)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=2dBHTz6g5AM")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=_xuI60USDjw")
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=5vsOv_bcnhs")
                    elif b == 4:
                        webbrowser.open("https://www.youtube.com/watch?v=BblraEtrFLI")
                    else :
                        webbrowser.open("https://www.youtube.com/watch?v=MP6SrbIeUWc")
                
                elif "start a game" in query:
                    from game import game_play
                    game_play()
                
                #The best function of JARVIS so called the FOCUS MODE
                elif "focus mode" in query:
                    speak("sir are you sure that you want to enter focus mode! Enter [1 for YES] /[2 for NO]")
                    a = int(input("Enter [1 for YES] / [2 for NO]: "))
                    
                    if a == 1:
                        speak("Entering to the focus mode ....")
                        os.startfile("C:\\Users\\LOGIC\\Desktop\\jarvis\\FocusMode.py")
                        exit()
                    else:
                        pass
                
                #Find my Ip address
                elif "ip address" in query:

                    from online import find_myip
                    # ip=o.find_myip()["ip"]
                    details=find_myip()
                    ip=details['query']
                    speak(f"your IP address is :{ip}")
                    print(f"your ip is {ip}") 
                    location=details['country']+" "+details['regionName']
                    speak(f"your location is {location}")
                    print(f"your location is {location}")
                
                # Graph to show your focus
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                
                #The translator in the Jarvis
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)
                
                #Finally sleep function
                elif "finally sleep" in query:
                    speak("Going to sleep sir, Thank you I'll be back Soon!")
                    exit()