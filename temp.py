import pyttsx3
from online import find_myip


#engine setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


# functions for text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
import requests
from online import find_myip

def weather_forecast(city):

    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf5e237219d84cac97bac61fe049503c").json()

    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    wind_speed = res["wind"]["speed"]
    return weather,f"{round(temp-273.15,2)}°C",f"{round(feels_like-273.15,2)}°C",f"{wind_speed} m/s"
    

if __name__ == "__main__":
    ip_address = find_myip()
    speak("tell me the name of your city")
    city = input("Enter your city name: ")
    speak(f"getting weather forecast for your city {city}")
    weather , temp , feels_like , wind_speed = weather_forecast(city)
    speak(f"the current temperature is {temp}, but it feels like {feels_like}")
    speak(f" Also the weather report talks about {weather}")
    speak(f"The wind speed is {wind_speed}")
    speak("I am printing weather information on screen")
    print(f"Description : {weather}\nTemperature : {temp}\nFeels Like : {feels_like}\nWind Speed : {wind_speed}")


