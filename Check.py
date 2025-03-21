import pyttsx3
import imdb

# Engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set female voice (you can change this)
engine.setProperty('rate', 170)  # Adjust speech rate

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# IMDb setup
movies_db = imdb.IMDb()

# Get movie information
def get_movie_info():
    speak("Please enter the name of the movie:")
    text = input("Please enter the name of the movie: ")
    speak(f"Searching for {text}...")

    # Search for the movie
    movies = movies_db.search_movie(text)
    if movies:  # Ensure search results exist
        # Fetch the first movie in the search results
        first_match = movies[0]
        title = first_match["title"]
        year = first_match.get("year", "Unknown year")
        info = first_match.getID()
        movie_info = movies_db.get_movie(info)

        # Safely retrieve movie details
        rating = movie_info.get("rating", "No rating available")
        cast = movie_info.get("cast", [])
        actor_names = [person["name"] for person in cast[:5]]  # Extract top 5 names
        actor_names_str = ", ".join(actor_names)  # Format names as a single string
        plot = movie_info.get('plot outline', 'Plot summary not available')

        # Speak and display the movie information
        speak(f"{title} was released in {year} and has an IMDb rating of {rating}.")
        speak(f"It features a cast of {actor_names_str}. The plot summary of the movie is: {plot}.")
        print(f"{title} was released in {year} and has an IMDb rating of {rating}.")
        print(f"It features a cast of: {actor_names_str}.")
        print(f"The plot summary of the movie is: {plot}.")
    else:
        # Handle no search results
        speak("Sorry, no results found!")
        print("Sorry, no results found!")

# Run the program
get_movie_info()
