import wolframalpha
import pyttsx3
import speech_recognition


#engine setup for jarvis
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def WolfRamAlpha(query):
    apikey = "285WT9-6J2888TKRW"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer
    
    except:
        speak("the value is not answerable sir !")


def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    
    Final = str(Term)
    
    try:
        result = WolfRamAlpha(Final)
        print(f"sir the Answer is : {result}")
        speak(f"sir the answer is :{result}")
    except:
        speak("The value is not answerable sir!")