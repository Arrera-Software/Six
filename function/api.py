from src.voice import * 
import datetime
import requests
import geocoder
from tkinter import*
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

def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL= dictionnnaire["url"]
    Titre = dictionnnaire["title"]
    return Sujet,Description,URL,Titre

def Resumer():#Fonction de resumer des actaulités et de la meteo
    speak("Ok je vous prépare votre résumé")
    hour=datetime.datetime.now().hour
    CompleteURLNew = urlNew+"&pageSize="+nombrePageNew2+"&apiKey="+keyNew
    article = requests.get(CompleteURLNew).json()["articles"]
    Sujet1,Description1,URL1,Titre1 = NetoyageActu(article[0])
    Sujet2,Description2,URL2,Titre2 = NetoyageActu(article[1])
    Sujet3,Description3,URL3,Titre3 = NetoyageActu(article[2])
    Sujet4,Description4,URL4,Titre4 = NetoyageActu(article[3])
    Sujet5,Description5,URL5,Titre5 = NetoyageActu(article[4])
    Temparure1,humiditer1,description1,ville1=Meteo(1)
    Temparure2,humiditer2,description2,ville2=Meteo(2)
    speak("La première actualités et " + Titre1 +".")
    speak("La seconde et "+ Titre2+".")
    speak("La troisiéme et "+ Titre3+".")
    speak("La quatriéme et "+ Titre4+" .")
    speak("La derniére et "+ Titre5+".")
    speak("La metéo a votre domicile et "+ description1 )
    speak("avec une température de "+Temparure1+"degrés")
    speak("et un taux d'humiditer de "+humiditer1+" pourcent")
    speak("La metéo a "+ville2+" et "+ description2 )
    speak("avec une température de "+Temparure2+"degrés")
    speak("et un taux d'humiditer de "+humiditer2+" pourcent")
    
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
    
def MeteoParole(nbVille):#Fonction météo avec parole
    Temperature,humiditer,description,ville = Meteo(nbVille)
    speak("La météo à "+ville+ " ,et "+description+".")
    speak("Avec un taux d'humiditer de "+humiditer+" pourcent.")
    speak("Et une température de "+Temperature+" degrés")
def GeoLocGPS():
    myPublic_IP = requests.get("http://wtfismyip.com/text").text.strip()
    ip = geocoder.ip(myPublic_IP)
    loc = ip.latlng
    lat = str(loc[0])
    long = str(loc[1])
    return lat , long

def Trad(genre):#Fonction de Traduction
    langue0= lectureJSON("setting/config.json","lang0")
    langue1= lectureJSON("setting/config.json","lang1")
    langue2= lectureJSON("setting/config.json","lang2")
    ScreenTrad=Tk()
    ScreenTrad.title("Six : Traduction")
    ScreenTrad.maxsize(400,400)
    ScreenTrad.minsize(400,400)
    ScreenTrad.config(bg=Color)
    labelInfo=Label(ScreenTrad,text="Resultat",bg=Color,fg=TextColor,font=("arial","20"))
    trad=Entry(ScreenTrad,width=45)
    def L0versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L0versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue0,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L1versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue0)
        translation = translator.translate(mot)
        speak("Le resultat de votre traduction "+genre+" et "+translation)
        labelInfo.config(text=translation)
    def L1versL2():
        mot = str(trad.get())
        translator= Translator(from_lang=langue1,to_lang=langue2)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    def L2versL0():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue0)
        translation = translator.translate(mot)
        speak("Le resultat de votre traduction "+genre+" et "+translation)
        labelInfo.config(text=translation)
    def L2versL1():
        mot = str(trad.get())
        translator= Translator(from_lang=langue2,to_lang=langue1)
        translation = translator.translate(mot)
        labelInfo.config(text=translation)
    bouttonTraduction=Button(ScreenTrad,text="Traduire",bg=Color,fg=TextColor)
    def Mode1():
        bouttonTraduction.config(command=L0versL1)
    def Mode2():
        bouttonTraduction.config(command=L1versL0)
    def Mode3():
        bouttonTraduction.config(command=L0versL2)
    def Mode4():
        bouttonTraduction.config(command=L2versL0)
    def Mode5():
        bouttonTraduction.config(command=L1versL2)
    def Mode6():
        bouttonTraduction.config(command=L2versL1)
    MenuTrad = Menu(ScreenTrad,bg="white")
    Choix = Menu(MenuTrad,tearoff=0)
    Choix.add_command(label="Langue par défault vers Langue 1",command=Mode1)
    Choix.add_command(label="Langue 1 vers Langue par défault",command=Mode2)
    Choix.add_command(label="Langue par défault vers Langue 2",command=Mode3)
    Choix.add_command(label="Langue 2 vers Langue par défault",command=Mode4)
    Choix.add_command(label="Langue 1 vers Langue 2",command=Mode5)
    Choix.add_command(label="Langue 2 vers Langue 1",command=Mode6)
    MenuTrad.add_cascade(label = "Traduction",menu=Choix)
    ScreenTrad.config(menu=MenuTrad)
    labelInfo.place(x="5",y="25")
    trad.place(relx=.5,rely=.5,anchor ="center")
    bouttonTraduction.pack(side="bottom")
    ScreenTrad.mainloop()