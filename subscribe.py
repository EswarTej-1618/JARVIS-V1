import pyautogui
import pyttsx3
import time
import webbrowser
# Engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def Subscribe():
    speak(" Hello Everyone who are watching this video,please subscribe for amazing content from LEGEND BHAGY PRESENTS channel")
    speak("First go to Youtube")
    webbrowser.open("https://www.youtube.com/")
    speak("click on the search bar ")
    time.sleep(2)
    pyautogui.moveTo(713,161,1)
    time.sleep(2)
    pyautogui.click(x= 713,y=161,clicks=1,interval=0,button='left')
    speak("legend Bhagy Presents")
    pyautogui.write("legend Bhagyam Presents",0.2)
    time.sleep(2)
    speak("press enter")
    pyautogui.press('enter')
    pyautogui.moveTo(971, 370, 1)
    speak("here you will find our channel")
    pyautogui.moveTo(1251,323,1)
    speak("click on the subscribe button")
    pyautogui.click(x= 1251,y=323,clicks=1,interval=0,button='left')
    speak(" And also don't forget to click on the bell icon")
    pyautogui.moveTo(1299, 313, 1)
    pyautogui.click(x= 1299,y=313,clicks=1,interval=0,button='left')
    speak("turn on all notifications")
    pyautogui.click(x=1199,y=363,clicks=1,interval=0,button='left')



# print(pyautogui.position())  # Move your mouse to the search bar and run this

