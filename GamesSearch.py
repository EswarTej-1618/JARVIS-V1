import speech_recognition as sr
import pyttsx3
import webbrowser
from bs4 import BeautifulSoup
from plyer import notification
from pygame import mixer
import requests



def LiveIplScore():
    #webscraping using beautiful soup ! that's it  enhance the code for cricket and kabbadi in future!!1 imp 
                    #todo do same for kabbadi
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
                    
                    a = print(f"{team1}:{team1_score}")
                    a = print(f"{team2}:{team2_score}")
                    #enabling notification sound
                    mixer.init()
                    mixer.music.load("omnitrix.mp3")
                    mixer.music.play()
                    #for notification
                    notification.notify(
                        title = "IPL Score :- ",
                        message = f"{team1}:{team1_score}\n {team2}:{team2_score}",
                        timeout = 10
                    )