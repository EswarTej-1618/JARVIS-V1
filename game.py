import pyttsx3
import speech_recognition as sr
import random


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

#Rock paper scissors game
def game_play():
    speak("Let's play Rock, paper and scissors sir")
    print("let's play!")
    i= 0
    My_score= 0
    Com_score =0
    
    while(i<5):
        choose = ("rock","paper","scissors")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if(com_choose=="rock"):
                speak("rock")
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            elif(com_choose=="paper"):
                speak("paper")
                Com_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            else:
                speak("scissors")
                My_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
        
        elif (query =="paper"):
            if(com_choose=="paper"):
                speak("paper")
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            elif(com_choose=="scissors"):
                speak("scissors")
                Com_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            else:
                speak("rock")
                My_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
        
        elif (query == "scissors" or query =="scissor"):
            if(com_choose=="scissors"):
                speak("scissors")
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            elif(com_choose=="rock"):
                speak("rock")
                Com_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
            else:
                speak("paper")
                My_score+=1
                print(f"Score: Me:-{My_score}, Com:- {Com_score}")
        i += 1 #update the variable
    print(f"Final Score: \nMe:-{My_score}\nCom:-{Com_score}")