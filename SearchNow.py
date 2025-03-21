import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

#query here!
query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on Google")
        
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,5)
            speak(result)
        
        except:
            speak("No speakable output available")
            

def SearchYoutube(query):
    if "youtube" in query:
        speak("This is what I found in your search!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchPerplexity(query):
    if "perplexity" in query:
        speak("This is what i found in our search!")
        query = query.replace("jarvis","")
        query = query.replace("perplexity search","")
        query = query.replace("perplexity","")
        web="https://www.perplexity.ai/search//hello-0A5bIFD4S1yn8c8tP9R..Q"+query
        webbrowser.open(web)
        speak("Done sir!")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Serach from wikipedia....")
        query = query.replace("jarvis","")
        query = query.replace("search wikipedia","")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=5)
        speak("According to wikipedia...")
        print(results)
        speak(results)
        