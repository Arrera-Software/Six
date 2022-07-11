import subprocess
import webbrowser
from gtts import gTTS
import os
import datetime
import random
import speech_recognition as sr
from ModuleInternet import TestInternet,duckduckgoSearch,GrandRecherche
import requests
from tkinter import*
nrad = random.randint(1,2)


keyWeather="ecffd157b2cc9eacbd0d35a45c3dc047"
urlWeather="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
nombrePageNew1 = "1"
nombrePageNew2 = "5"


def speak(text):
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")
    print("Six =",text)
def speakNoInternet():
    os.system("mpg123 " + "sons/speak1.mp3")
def Resumer():
    speak("Ok je vous prépare votre résumé")
    hour=datetime.datetime.now().hour
    CompleteURLNew = urlNew+"&pageSize="+nombrePageNew2+"&apiKey="+keyNew
    article = requests.get(CompleteURLNew).json()["articles"]
    Sujet1,Description1,URL1,Titre1 = NetoyageActu(article[0])
    Sujet2,Description2,URL2,Titre2 = NetoyageActu(article[1])
    Sujet3,Description3,URL3,Titre3 = NetoyageActu(article[2])
    Sujet4,Description4,URL4,Titre4 = NetoyageActu(article[3])
    Sujet5,Description5,URL5,Titre5 = NetoyageActu(article[4])
    city_name1 = Lecture("villes.txt")
    Temparure1,humiditer1,description1,ville1=Meteo(city_name1)
    Temparure2,humiditer2,description2,ville2=Meteo("Landrethun-le-nord")
    speak("La premier actualités et" + Titre1 +".la second et"+ Titre2+".la troisiéme et"+ Titre3+".la quatriéme"+ Titre4+".et la derniére et"+ Titre5  )
    speak("La metéo a votre lieu favori et "+ description1 + " avec une température de "+Temparure1+" degrés et un taux d'humiditer de "+humiditer1+" pourcent")
    speak("Et la méteo a votre domicile et "+ description2 + " avec une température de "+Temparure2+" degrés et un taux d'humiditer de "+humiditer2+" pourcent")
    speak("Voulez-vous que j'ouvre les lien des actualités ?")
    reponse = takeCommand()
    if "oui" in reponse:
        speak("Ok je vous les ouvre")
        webbrowser.open(URL1)
        webbrowser.open(URL2)
        webbrowser.open(URL3)
        webbrowser.open(URL4)
        webbrowser.open(URL5)
    if "non" in reponse:
        speak("Ok")
def salutation():
    hour=datetime.datetime.now().hour
    if hour == 0 and hour<= 9:
        if nrad == 1 :
            speak("Bonjour monsieur,J'espére que vous passer une bonne nuit.Voulez-vous un petit résumer des actulités?")
        if nrad == 2 :
            speak("Bonjour monsieur,J'espére que vous avez bien dormi.Voulez-vous un petit résumer des actulités? ")
        print("J'attend votre reponse.")
        while True:
            r = takeCommand()
            if "oui" in r:
                Resumer()
                speak("J'espére que sa vous sera utile monsieur")
                break
            if "non" in r:
                speak("Ok passer un exelente journée monsieur")
    if hour >= 10 and hour <=13:
        if nrad == 1 :
            speak("Bonjour monsieur,J'espére que vous passer une bonne matinée")
        if nrad == 2 :
            speak("Bonjour monsieur,J'espére que vous passer un bon début de journée")
    if hour>=13 and hour<=17:
        if nrad == 1 :
            speak("Bonjour monsieur,J'espére que vous passer une bonne aprem")
        if nrad == 2 :
            speak("Bonjour monsieur,J'espére que vous passer une bonne après-midi")
    if  hour>=18 and hour<=20:
        if nrad == 1 :
            speak("Bonsoir monsieu,comment se passe votre début de soirée?")
        if nrad == 2 :
            speak("Bonsoir monsieur,J'espére que votre début de soirée se passe bien")
    if  hour>=21 and hour<=23:
        if nrad == 1 :
            speak("Bonsoir monsieu,comment se passe votre soirée?")
        if nrad == 2 :
            speak("Bonsoir monsieur,J'espére que votre soirée se passe bien")

def Ecriture(file,text):
    doc = open(file,"w")
    doc.truncate()
    doc.write(text)
    doc.close()
    return text,file
def Lecture(file):
    fichier = open(file,"r")
    contenu= fichier.readlines()[0]
    fichier.close()
    return contenu

def NetoyageActu(dictionnnaire):
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL= dictionnnaire["url"]
    Titre = dictionnnaire["title"]
    return Sujet,Description,URL,Titre
def EcritureNote(file):
    speak("Voulez-vous dicter ou ecrire votre note monsieur")
    r = takeCommand()
    if "dictée" in r or "dicter" in r:
        speak("Ok je vous ecoute")
        Note = takeCommand()
        Ecriture(file,Note)
    if "écrire" in r :
        speak("Ok ecrivé votre note monsieur")
        Note = input("Votre note :")
        Ecriture(file,Note)
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
            print("User = ",Requette)
        except Exception as e:
            return "None"
        return Requette

def shutdown():
    subprocess.run("poweroff")
def reboot():
    subprocess.run("reboot")

def Meteo(ville):
    complete_url=urlWeather+"appid="+keyWeather+"&q="+ville+"&lang=fr"+"&units=metric"
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = str(y["temp"])
        current_humidiy = str(y["humidity"])
        weather_description = str(x["weather"][0]["description"])
        return current_temperature , current_humidiy , weather_description , ville
def MeteoParole(city):
    Temperature,humiditer,description,ville = Meteo(city)
    speak("La météo à "+ville+ " ,et "+description +".Avec un taux d'humiditer de "+humiditer+" pourcent et une température de "+Temperature+" degrés")
#Programme principale
internet = TestInternet()
if internet == True :
    salutation()
    while True :
        statement = takeCommand().lower()
        if statement==0:
            continue
        if  statement =="salut"   or statement =="bonjour" or statement =="bonsoir":
            speak(statement+" en quoi je peux vous servir ?")
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
        if "recherche sur internet" in statement :
            speak("Vous voulez rechercher quoi ?")
            recherche = takeCommand()
            speak("Ok,Voici le resultat")
            duckduckgoSearch(recherche)
        if "actualités" in statement:
            CompleteURL = urlNew+"&pageSize="+nombrePageNew1+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]
            Sujet,Description,URL = NetoyageActu(article[0])
            speak("L'actualités la plus récent est "+Description)
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
        if "date" in statement :
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
        if "météo" in statement:
            speak("Ou desirez savoir la meteo monsieur ?")
            r= takeCommand()
            if "maison" in r or "chez moi" in r :
                city = "Landrethun-le-nord"
                MeteoParole(city)              
            if "Boulogne" in r or "boulogne" in r :
                city = "Boulogne-sur-mer"
                MeteoParole(city)
        if "quel temps fait-il" in statement:
            file = open("villes.txt","r")
            city_name= file.readlines()[0]
            MeteoParole(city_name)
        if "change la ville" in statement:
            city = Lecture("villes.txt")
            NewCity = input("Nouvelle ville favorite:")            
            contenu,fichier = Ecriture("villes.txt",NewCity)
            speak("Ok je vous changer votre ville en favorie"+city+",par"+contenu)
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
        if "mes notes internet" in statement :
            speak("Ok voici vos note stoket sur internet monsieur")
            webbrowser.open("https://www.notion.so/5599107ab8fe4e3d9909f6817cfe1dd4?v=ad3306defd0947aea0b9542029787a2b")
        if "mes cahiers des tâches" in statement:
            webbrowser.open("https://www.notion.so/Cahier-de-tache-29b3259503584886b88b24f574f871ba")
        if "ma todolist" in statement or "ma liste de tâches" in statement:
            webbrowser.open("https://www.notion.so/3f037048d43048aa935f74d0700ee0d7?v=6e2e75eb40c94d719f73bbe6e90a52ed")
        if "ma page de projet" in statement:
            webbrowser.open("https://www.notion.so/e6b2105328f34126a0d2527e9fb1c917?v=3af36adfb00a4d29aa12c1187e7004ca")
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
        if "mode nuit" in statement or "mode sombre" in statement:
            os.popen("./Script-Bash/Dark.sh")
        if "mode jour" in statement or "mode clair" in statement:
            os.popen("./Script-Bash/Light.sh")
        if "résumé" in statement:
            Resumer()
        if "écris dans mes notes locales" in statement:
            speak("Quelle note voulez-vous modifier")
            nbNote = takeCommand()
            if "la première" in nbNote:
                file = "note/note1.txt"
                EcritureNote(file)
            if "la deuxième" in nbNote and "la seconde" in nbNote:
                file = "note/note2.txt"
                EcritureNote(file)
            if "la troisième" in nbNote:
                file = "note/note3.txt"
                EcritureNote(file)
            if "la 4e" in nbNote:
                file = "note/note4.txt"
                EcritureNote(file)
            if "la 5e" in nbNote:
                file = "note/note5.txt"
                EcritureNote(file)
        if "lis mes notes local" in statement or "lis-moi mes notes locales" in statement: 
            speak("Quelle note voulez-vous que je vous lise ?")
            nbNote = takeCommand()
            if "la première" in nbNote:
                file = "note/note1.txt"
                note = Lecture(file)
                speak(note)
            if "la deuxième" in nbNote or "la seconde" in nbNote:
                file = "note/note2.txt"
                note = Lecture(file)
                speak(note)
            if "la troisième" in nbNote:
                file = "note/note3.txt"
                note = Lecture(file)
                speak(note)
            if "la 4e" in nbNote:
                file = "note/note4.txt"
                Lecture(file)
            if "la 5e" in nbNote:
                file = "note/note5.txt"
                note = Lecture(file)
                speak(note)
        if "fais une grande recherche" in statement:
            speak("Que voulez vous que je vous recherche ?")
            r = takeCommand()
            GrandRecherche(r)  
else :
    speakNoInternet()
    