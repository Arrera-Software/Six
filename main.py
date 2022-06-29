import subprocess
from turtle import speed, st
import webbrowser
from gtts import gTTS
import os
import datetime
import random
import meteofrance_api
from numpy import take
import speech_recognition as sr
from ModuleInternet import TestInternet, duckduckgoSearch
nrad = random.randint(1,2)
import requests
from translate import Translator

api_key="ecffd157b2cc9eacbd0d35a45c3dc047"
base_url="https://api.openweathermap.org/data/2.5/weather?"
translator= Translator(to_lang="French")

House = "Landrethun-le-nord"
work = "Boulogne-sur-mer"

def speak(text):
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")
def speakNoInternet():
    os.system("mpg123 " + "sons/speak1.mp3")

def salutation():
    hour=datetime.datetime.now().hour
    if hour>= 0 and hour<13:
        if nrad == 1 :
            speak("Boujour monsieur,Je vous souhaite une bonne matinée")
        if nrad == 2 :
            speak("Boujour monsieur,Je vous souhaite un bon début de journée")
    if hour>=13 and hour<20:
        if nrad == 1 :
            speak("Bonjour monsieur,Je vous souhaite une bonne aprem")
        if nrad == 2 :
            speak("Bonjour monsieur,Je vous souhaite une bonne après-midi")
    else :
        speak("Bonsoir monsieur")

def Arret():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<22:
       speak("Au revoir monsieur")
    
    if hour>=22 and hour<23:
        speak("Au revoir monsieur , bonne nuit")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

        try:
            Requette=r.recognize_google(audio,language='fr')
            print(Requette)

        except Exception as e:
            return "None"
        return Requette

def shutdown():
    subprocess.run("poweroff")
def reboot():
    subprocess.run("reboot")

def Meteo(ville):
    complete_url=base_url+"appid="+api_key+"&q="+ville
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = int(y["temp"]-273.15)
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        fr_weather_description = translator.translate(weather_description)

        speak("La température a"+ville+",est de "+str(current_temperature)+"degrés."+"Le taux d'humiditer est de"+str(current_humidiy)+"pourcent"+"Et il fait actuellement"+fr_weather_description)



#Programme principale
internet = TestInternet()
if internet == True :
    salutation()
    while True :
        statement = takeCommand().lower()
        if statement==0:
            continue
    
        if "stop" in statement or "bye" in statement or "au revoir" in statement:
            Arret()
            break
        
        if "recherche" in statement :
            speak("Vous voulez rechercher quoi ?")
            recherche = takeCommand()
            speak("Ok,Voici le resultat")
            duckduckgoSearch(recherche)
        
        if "toujours là"  in statement  or "es-tu là" in statement :
            speak("Oui")
        if statement == "tu es qui" or statement == "présente-toi" or "présentation" in statement or "qui es tu" in statement:
            speak("Je suis SIX un assistant personnel cree par Baptiste Pauchet. Pour l'assistait dans l'uttilisation de son ordinateur.")
        if "fin de journée" in statement :
            Arret()
            shutdown()
        if "redémarre" in statement :
            speak("Ok a tout de suite monsieur")
            reboot()
        if "ouvre youtube" in statement :
            webbrowser.open("https://www.youtube.com/")
            speak("Youtube et ouvert ")
        if "lance de la musique" in statement or "lancer de la musique" in statement:
            webbrowser.open("https://music.youtube.com/")
            speak("Votre logiciel de musique est lancer")
        if "heure" in statement :
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            Constrution = "Il es",hour,"heure",minute
            parole = str(Constrution)
            speak(parole)
        if "jour" in statement :
            monthSTR = "Janvier"
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            years = datetime.datetime.now().year
            
            if month == 1 :
                monthSTR = "Janvier"
            if month == 2 :
                monthSTR = "Fevrier"
            if month == 3 :
                monthSTR = "Mars"
            if month == 4 :
                monthSTR = "Avril"
            if month == 5 :
                monthSTR = "Mai"
            if month == 6 :
                monthSTR = "Juin"
            if month == 7 :
                monthSTR = "Juillet"
            if month == 8 :
                monthSTR = "Aout"
            if month == 9 :
                monthSTR = "Septembre"
            if month == 10 :
                monthSTR = "Novembre"
            if month == 11 :
                monthSTR = "Decembre"
            if month == 11 :
                monthSTR = "Janvier"
            
            Constrution = "Aujourd'hui on est le",day,monthSTR,years
            parole = str(Constrution)
            speak(parole)
        if statement == "quel temps fait-il" or "météo" in statement:
            speak("Ou desirez savoir la meteo monsieur ?")
            r= takeCommand()
            if "maison" in r or "chez moi" in r :
                city = House
                Meteo(city)
            if "Boulogne" in r or "boulogne" in r :
                city = work
                Meteo(city)
            if "carte" in r or "France" in r or "france" in r :
                speak("Ok je vous ouvre meteo france")
                webbrowser.open("https://meteofrance.com/")
            if "région" in r :
                speak("Ok je vous ouvre meteo france")
                webbrowser.open("https://meteofrance.com/previsions-meteo-france/hauts-de-france/1")
        
        if "développement" in statement :
            break

else :
    speakNoInternet()
    