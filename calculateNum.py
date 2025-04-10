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
    # Remove "jarvis" from the query
    Term = str(query)
    Term = Term.replace("jarvis", "")  
    Term = Term.strip()  # Remove leading/trailing whitespaces

    try:
        app_id = "285WT9-6J2888TKRW"
        client = wolframalpha.Client(app_id)
    except Exception as e:
        speak("Failed to initialize Wolfram Alpha client.")
        print(f"Failed to initialize Wolfram Alpha client: {str(e)}")
        return

    try:
        result = client.query(Term)
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
        speak(f"Sir, the answer is: {ans}")
        print(f"Sir, the answer is: {ans}")

def Whois(query):
    # Remove "jarvis" from the query
    Term = str(query)
    Term = Term.replace("jarvis", "")  
    Term = Term.strip()  # Remove leading/trailing whitespaces

    try:
        app_id = "285WT9-6J2888TKRW"
        client = wolframalpha.Client(app_id)
    except Exception as e:
        speak("Failed to initialize Wolfram Alpha client.")
        print(f"Failed to initialize Wolfram Alpha client: {str(e)}")
        return

    # Check for "what is," "who is," or "which is" in the query
    question_keywords = ["what is", "who is", "which is"]
    question_keyword = next((keyword for keyword in question_keywords if keyword in Term.lower()), None)

    if question_keyword:
        # Remove the question keyword from the query
        Term = Term.lower().replace(question_keyword, "").strip()
        
        try:
            result = client.query(Term)
            ans = next(result.results).text
            speak(f"Sir, the answer is: {ans}")
            print(f"Sir, the answer is: {ans}")
        except StopIteration:
            speak("I couldn't find the answer, Please Try Again")
            print("I couldn't find the answer, Please Try Again")
        except Exception as e:
            if "ReadTimeout" in str(e):
                speak("Timeout error occurred. Please check your internet connection and try again.")
                print("Timeout error occurred. Please check your internet connection and try again.")
            else:
                speak("An unexpected error occurred. Please try again later.")
                print(f"An unexpected error occurred: {str(e)}")
    else:
        speak("I couldn't find that. Please try again with a 'what is,' 'who is,' or 'which is' question.")
        print("I couldn't find that. Please try again with a 'what is,' 'who is,' or 'which is' question.")