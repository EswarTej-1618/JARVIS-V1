import pyautogui
import time
import speech_recognition as sr
import pyttsx3


# Engine setup for speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for voice input
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjusts to background noise
        audio = r.listen(source, phrase_time_limit=7)  # Waits until user stops speaking

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could you please say that again?")
        return "None"
    
    return query

# Function to filter out unnecessary words
def clean_query(query):
    stopwords = ["jarvis", "playsong", "spotify search", "search", "on spotify","play"]
    for word in stopwords:
        query = query.replace(word, "")
    return query.strip()


# Function to open Spotify and play song
def play_on_spotify(song_name):
    # Open Start Menu
    pyautogui.press("win")
    time.sleep(1)
    
    # Type "Spotify" and press Enter
    pyautogui.write("Spotify")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(10)  # Wait for Spotify to open

    # Use Ctrl + K to focus on search bar
    pyautogui.hotkey("ctrl", "k")
    time.sleep(1)

    # Type the song name
    pyautogui.write(song_name)
    time.sleep(1)
    speak(f"Searching for {song_name} on Spotify")
    # pyautogui.press("enter")  # Search for the song
    time.sleep(2)
    speak("Enjoy your song sir ")
    # Simulate pressing " Shift + Enter" again to play the song
    time.sleep(1)
    pyautogui.hotkey("shift", "enter")  

# Main execution
if __name__ == "__main__":
    speak("Which song would you like to play? sir")
    query = takeCommand().lower()
    song_name = clean_query(query)
    
    if song_name != "none":
        speak(f"Playing {song_name} on Spotify")
        play_on_spotify(song_name)