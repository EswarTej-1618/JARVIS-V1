import requests
import json
import pyttsx3
from datetime import datetime

# Engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to fetch and display news
def fetch_news(url):
    r = requests.get(url)
    news = json.loads(r.text)
    speak("Here is the first news")

    # Ensure at least 5 articles are printed
    article_count = 0
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print formatted header for the selected news category
    print(f"**{field.capitalize()} News** - {current_datetime}")
    speak(f"{field.capitalize()} News - {current_datetime}")

    for result in news["results"]:
        title = result.get("title", "No Title")
        description = result.get("description", "No Description")
        news_url = result.get("link", "")

        print(f"**Article {article_count + 1}**")
        print(f"**Title:** {title}")
        print(f"**Description:** {description}")
        print(f"**More Info:** {news_url}")
        print("--------------------------------------------------------------------")

        speak(f"Article {article_count + 1}. The news title is: {title}")
        speak(f"The description is: {description}")
        speak("For more info, visit the link provided.")

        article_count += 1

        if article_count % 5 == 0:
            if input("[Press 'c' to continue] and [Press 's' to stop] in lowercase letters: ") == 's':
                speak("That's a wrap for now, sir! Thank you for your attention and engagement. Until we meet again, stay up to date with the news.")
                return

# Main function to get the latest news
def latestnews():
    api_dict = {
        "business": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=business",
        "entertainment": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=entertainment",
        "crime": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=crime",
        "domestic": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=domestic",
        "education": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=education",
        "environment": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=environment",
        "food": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=food",
        "health": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=health",
        "lifestyle": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=lifestyle",
        "other": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=other",
        "politics": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=politics",
        "science": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=science",
        "sports": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=sports",
        "technology": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=technology",
        "top": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=top",
        "world": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=world",
        "tourism": "https://newsdata.io/api/1/latest?apikey=pub_612989516e6d3a4b6b3d885f0615412b7211c&country=in&domain=The Hindu&category=tourism"
    }
    
    print("Which type of news would you like, sir? [business], [crime], [domestic], [education], [entertainment], [environment], [food], [health], [lifestyle], [other], [politics], [science], [sports], [technology], [top], [tourism], [world]")
    speak("Which type of news you want sir:  [business], [crime], [domestic], [education], [entertainment], [environment], [food], [health], [lifestyle], [other], [politics], [science], [sports], [technology], [top], [tourism], [world] from The Hindu newspaper")

    global field
    field = input("Type the field of news that you want: ")
    print("----------------------------------------------------------------------------------------------")
    
    url = api_dict.get(field.lower())
    
    if url:
        print(url)
        print("URL found")
        fetch_news(url)
    else:
        print("URL not found")
        speak("Sorry, I couldn't find the requested news category.")


