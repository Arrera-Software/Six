import subprocess
from sys import api_version
import webbrowser
from gtts import gTTS
import os
import datetime
import random
import speech_recognition as sr
from ModuleInternet import TestInternet, duckduckgoSearch
import requests
from tkinter import*
nrad = random.randint(1,2)


keyWeather="ecffd157b2cc9eacbd0d35a45c3dc047"
urlWeather="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
nombrePageNew = "5"


def speak(text):
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")
def speakNoInternet():
    os.system("mpg123 " + "sons/speak1.mp3")

def salutation():
    hour=datetime.datetime.now().hour
    if hour>= 0 and hour<=13:
        if nrad == 1 :
            speak("Bonjour monsieur,Je vous souhaite une bonne matinée")
        if nrad == 2 :
            speak("Bonjour monsieur,Je vous souhaite un bon début de journée")
    if hour>=13 and hour<20:
        if nrad == 1 :
            speak("Bonjour monsieur,Je vous souhaite une bonne aprem")
        if nrad == 2 :
            speak("Bonjour monsieur,Je vous souhaite une bonne après-midi")
def NetoyageActu(dictionnnaire):
    Auteur = dictionnnaire["author"]
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL = dictionnnaire["url"]
    return Auteur ,Sujet,Description,URL

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
    complete_url=urlWeather+"appid="+keyWeather+"&q="+ville+"&lang=fr"
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = str(y["temp"])
        current_humidiy = str(y["humidity"])
        weather_description = str(x["weather"][0]["description"])
        speak("La méteo a"+ville+",est"+weather_description+"avec une température de"+current_temperature+" ,et un taux d'humiditer de"+current_humidiy+"pourcent ")



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
        if statement == "mute" or statement == "chut":
            speak("Ok monsieur je vous laisse tranquille")
            screen = Tk()
            def anychar(event):
                if event.keycode == 36 :
                    screen.destroy()
                    speak("Oui monsieur")
            screen.title("SIX")
            screen.wait_visibility(screen)
            screen.wm_attributes('-alpha',0.9)
            screen.config(bg="#08116f")
            screen.maxsize(300,100)
            screen.minsize(300,100)
            LabelMute = Label(screen,text="Mute",font=("arial","24"),bg="#08116f",fg="white").place(relx=.5, rely=.5, anchor="center")
            screen.bind("<Key>",anychar)
            screen.mainloop()
        if "recherche" in statement :
            speak("Vous voulez rechercher quoi ?")
            recherche = takeCommand()
            speak("Ok,Voici le resultat")
            duckduckgoSearch(recherche)
        if "actualités" in statement:

            CompleteURL = urlNew+"&pageSize="+nombrePageNew+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]

            Auteur1,Sujet1,Description1,URL1 = NetoyageActu(article[0])
            Auteur2,Sujet2,Description2,URL2 = NetoyageActu(article[1])
            Auteur3,Sujet3,Description3,URL3 = NetoyageActu(article[2])
            Auteur4,Sujet4,Description4,URL4 = NetoyageActu(article[3])
            Auteur5,Sujet5,Description5,URL5 = NetoyageActu(article[4])

            speak("Les actualités aujourd'hui son"+Sujet1)

        if "toujours là"  in statement  or "es-tu là" in statement or "6" in statement :
            speak("Oui")
        if statement == "tu es qui" or statement == "présente-toi" or "présentation" in statement or "qui es tu" in statement or "qui es-tu" in statement:
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
                city = "Landrethun-le-nord"
                Meteo(city)
            if "Boulogne" in r or "boulogne" in r :
                city = "Boulogne-sur-mer"
                Meteo(city)
            if "carte" in r or "France" in r or "france" in r :
                speak("Ok je vous ouvre meteo france")
                webbrowser.open("https://meteofrance.com/")
            if "région" in r :
                speak("Ok je vous ouvre meteo france")
                webbrowser.open("https://meteofrance.com/previsions-meteo-france/hauts-de-france/1")
        if "un document" in statement :
            speak("Ok j'ouvre libreoffice writer ")
            os.popen("libreoffice --writer")
        if "un diaporama" in statement :
            speak("Ok j'ouvre libreoffice impress ")
            os.popen("libreoffice --impress")
        if "un tableur" in statement :
            speak("Ok j'ouvre libreoffice calc ")
            os.popen("libreoffice --calc")
        if "google drive" in statement:
            speak("Ok voici votre google drive principale")
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
        if "firefox" in statement or "navigateur internet" in statement :
            speak("Ok j'ouvre votre navigateur internet")
            os.popen("/usr/bin/firefox")
        if "mes notes" in statement :
            speak("Ok voici vos note monsieur")
            webbrowser.open("https://www.notion.so/5599107ab8fe4e3d9909f6817cfe1dd4?v=ad3306defd0947aea0b9542029787a2b")
        if "visual studio code" in statement:
            os.popen("/usr/bin/code")
        if "mes fichiers" in statement :
            speak("Ok voici votre explorateur de fichier monsieur")
            os.popen("nautilus")
        if "jupiter" in statement :
            os.popen("jupyter-notebook /home/baptistep/")
        if "steam" in statement :
            speak("Ok bon jeu monsieur")
            os.popen("steam")
        if "arduino" in statement :
            os.popen("flatpak run cc.arduino.arduinoide")
            speak("Desirez vous que j'ouvre le navigateur web pour vous aidez monsieur")
            r = takeCommand()
            if "oui" in r :
                speak("Ok trés bien")
                os.popen("/usr/bin/firefox")
            if "non" in r :
                speak("Ok je reste a votre service si vous avez besoins ")
        if "gimp" in statement:
            os.popen("gimp")
        if "qui passe" in statement or "mots de passe" in statement or "mot de passe" in statement :
            os.popen("keepassxc")
        if "spider" in statement :
            os.popen("spyder")
        if "terminal" in statement:
            os.popen("gnome-terminal")
        if "tout savoir" in statement:
            os.popen("./Script-Bash/toutsavoir.sh")
        if "diabète elle" in statement:
            os.popen("./Script-Bash/diabetehelp.sh")

        if "voix du nord" in statement :
            webbrowser.open("https://www.lavoixdunord.fr/hauts-de-france")
        if "libération" in statement:
            webbrowser.open("https://www.liberation.fr/")
        if "flipboard" in statement :
            webbrowser.open("https://flipboard.com/")
        if "instagram" in statement :
            webbrowser.open("https://www.instagram.com/")
        if "twitter" in statement :
            webbrowser.open("https://twitter.com/home")
        if "signal" in statement:
            os.popen("flatpak run org.signal.Signal")
        if "discorde" in statement:
            os.popen("flatpak run com.discordapp.Discord")
        if "développement" in statement :
            break
        if "répète" in statement or "répéter" in statement or "tu as dit quoi" in statement or "je n'ai pas compris" in statement :
            os.system("mpg123 " + "voc.mp3")
        
else :
    speakNoInternet()
    