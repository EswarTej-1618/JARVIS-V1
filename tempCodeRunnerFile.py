import pyttsx3
import imdb
import speech_recognition as sr
import wolframalpha

#engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,7) #waits for 5 sec!
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("could you please say thay again sir!")
        return "None"
    return query

def Calculate():
    try:
        app_id = "285WT9-6J2888TKRW"
        client = wolframalpha.Client(app_id)
    except Exception as e:
        speak("Failed to initialize Wolfram Alpha client.")
        print(f"Failed to initialize Wolfram Alpha client: {str(e)}")
        return

    try:
        ind = query.lower().split().index('calculate')
    except ValueError:
        speak("Invalid calculate command. Please use 'calculate' followed by your query.")
        print("Invalid calculate command. Please use 'calculate' followed by your query.")
        return

    text = query.split()[ind + 1:]
    
    try:
        result = client.query(' '.join(text))
    except wolframalpha.exceptions.WolframAlphaError as e:
        speak("Wolfram Alpha error: " + str(e))
        print("Wolfram Alpha error: " + str(e))
    except Exception as e:
        speak("Failed to query Wolfram Alpha. Please try again later.")
        print(f"Failed to query Wolfram Alpha: {str(e)}")
        return

    try:
        ans = next(result.results).text
    except StopIteration:
        speak("I couldn't find the answer, Please Try Again")
        print("I couldn't find the answer, Please Try Again")
    except AttributeError:
        speak("Unable to parse result. Please check the query and try again.")
        print("Unable to parse result. Please check the query and try again.")
    else:
        speak("The answer is: " + ans)
        print("The answer is: " + ans)
def Whois():
    app_id = "285WT9-6J2888TKRW"
    client = wolframalpha.Client(app_id)
    try:
        ind = query.lower().index('what is') if 'what is' in query.lower() else \
            query.lower().index('who is') if 'who is' in query.lower() else \
                query.lower().index('which is') if 'which is' in query.lower() else None

        if ind is not None:
            text = query.split()[ind + 2:]
            res = client.query(" ".join(text))
            ans = next(res.results).text
            speak("The answer is " + ans)
            print("The answer is " + ans)
        else:
            speak("I couldn't find that. Please try again.")
    except StopIteration:
        speak("I couldn't find that. Please try again.")
    except Exception as e:
        if "ReadTimeout" in str(e):
            speak("Timeout error occurred. Please check your internet connection and try again.")
            print("Timeout error occurred. Please check your internet connection and try again.")
        else:
            speak("An unexpected error occurred. Please try again later.")
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    speak("Hello sir, I am Jarvis. How can I help you?")
    while True:    
        query = takeCommand().lower()
        if "calculate" in query:
            Calculate()                   
        elif any(keyword in query for keyword in ("who is", "what is", "which is")):
            Whois()
        elif"exit" in query:
            exit()