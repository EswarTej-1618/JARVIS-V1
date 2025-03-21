import pyttsx3
import imdb
import speech_recognition as sr



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
        audio = r.listen(source,0,5) #waits for 5 sec!
        
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("could you please say thay again sir!")
        return "None"
    return query


movies_db = imdb.IMDb()
#text = takeCommand()
speak("Please Enter the name of the movie:")
text = input("Please Enter the name of the movie:")
movie = movies_db.search_movie(text)
speak("searching for "+text)
speak("I found the following movies")
for movie in movie:
    title = movie["title"]
    year = movie["year"]
    speak(f"{title} released in {year}")
    info = movie.getID()
    movie_info = movies_db.get_movie(info)
    rating = movie_info["rating"]
    cast = movie_info["cast"]
    actor = cast[0:5]
    plot = movie_info.get('plot outline','plot summary not available')
    speak(f"{title} was released in {year} has imdb rating of {rating}. It has a cast of {actor}.The plot summary if the movie is {plot} ")
    print(f"{title} was released in {year} has imdb rating of {rating}.\nIt has a cast of {actor}.\nThe plot summary if the movie is {plot} ")