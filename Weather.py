import requests

def weather_forecast(city):

    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bf5e237219d84cac97bac61fe049503c").json()

    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather,f"{temp-273.15}°C",f"{feels_like-273.15}°C"
    
