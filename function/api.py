from src.voice import * 
import datetime
import requests
import geocoder

from translate import*
from function.JSON import*

keyWeather="ecffd157b2cc9eacbd0d35a45c3dc047"
urlWeather="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
urlGeoLoc = "http://api.ipstack.com/check"
KeyGeoLoc = "b8f00cfb49bfdaf40a317f98314ddc63"
nombrePageNew1 = "1"
nombrePageNew2 = "5"
Color = "#3c0f14"
TextColor = "white"

def ClearActu(dictionnnaire):
    var = dictionnnaire["title"]
    return var

def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL= dictionnnaire["url"]
    Titre = dictionnnaire["title"]
    return Sujet,Description,URL,Titre

def Resumer(root):#Fonction de resumer des actaulités et de la meteo
    speak("Ok je vous prépare votre résumé",root)
    hour=datetime.datetime.now().hour
    CompleteURLNew = urlNew+"&pageSize="+nombrePageNew2+"&apiKey="+keyNew
    article = requests.get(CompleteURLNew).json()["articles"]
    titre1 = ClearActu(article[0])
    titre2 = ClearActu(article[1])
    titre3 = ClearActu(article[2])
    titre4 = ClearActu(article[3])
    titre5 = ClearActu(article[4])
    temparure1,humiditer1,description1,ville1=Meteo(1)
    temparure2,humiditer2,description2,ville2=Meteo(2)
    speak("La première actualités et " + titre1 +".",root)
    speak("La seconde et "+ titre2+".",root)
    speak("La troisiéme et "+ titre3+".",root)
    speak("La quatriéme et "+ titre4+" .",root)
    speak("La derniére et "+ titre5+".",root)
    speak("La metéo a votre domicile et "+ description1,root )
    speak("avec une température de "+temparure1+"degrés",root)
    speak("et un taux d'humiditer de "+humiditer1+" pourcent",root)
    speak("La metéo a "+ville2+" et "+ description2,root )
    speak("avec une température de "+temparure2+"degrés",root)
    speak("et un taux d'humiditer de "+humiditer2+" pourcent",root)
    
def Meteo(nbVille):#Fonction de recuperation des donne de l'api openweather
    flagVille = "ville"+str(nbVille)   
    ville = lectureJSON("setting/config.json",flagVille)
    complete_url=urlWeather+"appid="+keyWeather+"&q="+ville+"&lang=fr"+"&units=metric"
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = str(y["temp"])
        current_humidiy = str(y["humidity"])
        weather_description = str(x["weather"][0]["description"])
        return current_temperature , current_humidiy , weather_description , ville
    
def MeteoParole(nbVille,root):#Fonction météo avec parole
    Temperature,humiditer,description,ville = Meteo(nbVille)
    speak("La météo à "+ville+ " ,et "+description+".",root)
    speak("Avec un taux d'humiditer de "+humiditer+" pourcent.",root)
    speak("Et une température de "+Temperature+" degrés",root)

def GeoLocGPS():
    myPublic_IP = requests.get("http://wtfismyip.com/text").text.strip()
    ip = geocoder.ip(myPublic_IP)
    loc = ip.latlng
    lat = str(loc[0])
    long = str(loc[1])
    return lat , long
