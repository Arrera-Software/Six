import subprocess
from gtts import gTTS
import webbrowser
import requests
import os
import datetime
import random
import speech_recognition as sr
from tkinter import*
from tkinter.messagebox import *
from translate import*
import time
from pytube import YouTube , Playlist
from playsound import playsound
from time import *
import pygame
from  pygame.locals import *
import geocoder
#Fonction Varriable
def HourSup(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT >= h1:
        return True
    else :
        return False
def HourInf(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT <= h1:
        return True
    else :
        return False
#Fontion du module internet
def TestInternet():
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        return True
    except requests.ConnectionError :
        return False
def braveSearch(query):
    with requests.session() as c:
        url = 'https://search.brave.com/search?q='
        urllink = requests.get(url+query+"&source=web")
        lienBrave = urllink.url
        webbrowser.open(lienBrave)
def AmazonSearch(query):
    with requests.session() as c:
        url = 'https://www.amazon.fr/s?k='
        urllink = requests.get(url+query)
        lienAmazon = urllink.url
        webbrowser.open(lienAmazon)
def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle)
def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.open(lienduck)   
def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.open(lienQwant)

def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.open(lienEcosia) 
def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.open(lienbing)
def WikipediaSearch(query):
    with requests.session() as c:
        url = 'https://fr.wikipedia.org/wiki/'
        lienWiki = url+query
        webbrowser.open(lienWiki)
def ReversoSeacrch(query):
    with requests.session() as c:
        url = 'https://www.reverso.net/traduction-texte#sl=fra&tl=eng&text='
        urllink = requests.get(url+query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle) 
def WordreferenceSearch(query):
    with requests.session() as c:
        url = 'https://www.wordreference.com/fren/'
        lienWord = url+query
        webbrowser.open(lienWord)
def YTmusicSearch(query):
    with requests.session() as c:
        url = 'https://music.youtube.com/search'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienYTmusic = urllink.url
        webbrowser.open(lienYTmusic)
def DocPython():
    webbrowser.open("https://docs.python.org/3")
def DocArduino():
    webbrowser.open("https://docs.python.org/3")
def GrandRecherche(query):
    googleSearch(query)
    duckduckgoSearch(query)
    QwantSearch(query)
    EcosiaSearch(query)
    bingSearch(query) 
    braveSearch(query)

#______________________
def Ecriture(file,text):#Fonction d'écriture sur un fichier texte
    doc = open(file,"w")
    doc.truncate()
    doc.write(text)
    doc.close()
    return text,file
def Lecture(file):#Fonction de lecture d'un fichier texte et stokage dans une varriable
    fichier = open(file,"r")
    contenu= fichier.readlines()[0]
    fichier.close()
    return contenu
def ThemeFonc():
    if HourInf(21) == False and HourSup(6) == True:
        return "day"
    else :
        return "night"
#Varriable
nrad = random.randint(1,2)
Color = "#3c0f14"
TextColor = "white"
keyWeather="ecffd157b2cc9eacbd0d35a45c3dc047"
urlWeather="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
urlGeoLoc = "http://api.ipstack.com/check"
KeyGeoLoc = "b8f00cfb49bfdaf40a317f98314ddc63"
nombrePageNew1 = "1"
nombrePageNew2 = "5"
listGenre = ["monsieur","madame"]
PrincipalUser =  str(Lecture("Config/Assistant/User1.txt"))
SecondairUser =  str(Lecture("Config/Assistant/User2.txt"))
TroisiemeUser =  str(Lecture("Config/Assistant/User3.txt"))
QuatriemeUser =  str(Lecture("Config/Assistant/User4.txt"))
PrincipalUserGenre =  str(Lecture("Config/Assistant/Genre1.txt"))
SecondairUserGenre =  str(Lecture("Config/Assistant/Genre2.txt"))
TroisiemeUserGenre =  str(Lecture("Config/Assistant/Genre3.txt"))
QuatriemeUserGenre =  str(Lecture("Config/Assistant/Genre4.txt"))
NomAssistant =   str(Lecture("Config/Assistant/Nom.txt"))
PrononceAssistant =   str(Lecture("Config/Assistant/NomPrononciation.txt"))
NameMoteur = str(Lecture("Config/MoteurRecherche/LienMoteur.txt"))
LienMoteur = str(Lecture("Config/MoteurRecherche/LienMoteur.txt"))
listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
varSix = True
FileMusic = str(Lecture("Config/file/emplacementMusic.txt"))
FileVideo = str(Lecture("Config/file/emplacementVideo.txt"))
HourSleep = int(Lecture("Config/Assistant/hour.txt"))
LienGDrive = str(Lecture("Config/Lien/GDrive.txt"))
LienMusic = str(Lecture("Config/Lien/music.txt"))
LienAgenda = str(Lecture("Config/Lien/Agenda.txt"))
LienNote = str(Lecture("Config/Lien/Note.txt"))
LienToDoList = str(Lecture("Config/Lien/ToDoList.txt"))
LienResaux1 = str(Lecture("Config/reseau/lien/Reseau1.txt"))
LienResaux2 = str(Lecture("Config/reseau/lien/Reseau2.txt"))
LienResaux3 = str(Lecture("Config/reseau/lien/Reseau3.txt"))
NameResaux1 = str(Lecture("Config/reseau/name/NameReseau1.txt"))
NameResaux2 = str(Lecture("Config/reseau/name/NameReseau2.txt"))
NameResaux3 = str(Lecture("Config/reseau/name/NameReseau3.txt"))
hourDark = 21
hourLight = 6
compteur = 0
light = pygame.image.load("image/interfaceLIght.png")
lightMute = pygame.image.load("image/interfaceLIghtMute.png")
dark = pygame.image.load("image/interfaceDark.png")
darkMute = pygame.image.load("image/interfaceDarkMute.png")
#Fenetre pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
pygame.init()
pygame.display.set_icon(pygame.image.load("image/logo.png"))
pygame.display.set_caption("Assistant SIX")
root  = pygame.display.set_mode((600,200),pygame.NOFRAME)
police = pygame.font.SysFont("arial", 25)
#Fonction de l'assistant
def ThemeFonc():
    if HourInf(hourDark) == True and HourSup(hourLight) == True:
        root.blit(light.convert(),(0,0))
        pygame.display.update()
    else :
        root.blit(dark.convert(),(0,0))
        pygame.display.update()
def speak(text):#Fonction de parole
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    playsound("voc.mp3")
    os.remove("voc.mp3")
    texte = str(NomAssistant+": "+text)
    pygame.display.update()
    print(texte)
def takeCommand():#Fonction micro et reconaissance vocal
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            Requette=r.recognize_google(audio,language='fr')
            ThemeFonc()
            if HourInf(hourDark) == True and HourSup(hourLight) == True:
                labelMicro = police.render(Requette, 1,(255,255,255))
            else :
                 labelMicro = police.render(Requette, 1,(255,255,255))
            root.blit(labelMicro,(5, 100))
            pygame.display.update()
            texte = str("User: "+Requette)
            print(texte)
        except Exception as e:
            return "None" 
        return Requette
def speakNoInternet():#Fonctiion pas internet
    os.system("mpg123 " + "sons/speak1.mp3")
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
def salutation(User,Genre):#Fonction de salutation
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <= 9:
        if nrad == 1 :
            speak("Bonjour "+Genre+" "+User+",J'espére que vous passer une bonne nuit.")
            speak("Voulez-vous un petit résumer des actulités? ")
        if nrad == 2 :
            speak("Bonjour "+Genre+" "+User+",J'espére que vous avez bien dormi.")
            speak("Voulez-vous un petit résumer des actulités? ")
        while True:
            r = takeCommand()
            if "oui" in r:
                Resumer()
                speak("J'espére que sa vous sera utile "+Genre+"")
                break
            if "non" in r:
                speak("Ok passer un exélente journée "+Genre+"")
                break
    if hour >= 10 and hour <=12:
        if nrad == 1 :
            speak("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne matinée")
        if nrad == 2 :
            speak("Bonjour "+Genre+" "+User+" ,J'espére que vous passer un bon début de journée")
    if hour>=13 and hour<=17:
        if nrad == 1 :
            speak("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne aprem")
        if nrad == 2 :
            speak("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne après-midi")
    if  hour>=18 and hour<=20:
        if nrad == 1 :
            speak("Bonsoir "+Genre+" "+User+" ,comment se passe votre début de soirée?")
        if nrad == 2 :
            speak("Bonsoir "+Genre+" "+User+" ,J'espére que votre début de soirée se passe bien")
    if  hour>=21 and hour<=23:
        if nrad == 1 :
            speak("Bonsoir "+Genre+" "+User+" ,comment se passe votre soirée?")
        if nrad == 2 :
            speak("Bonsoir "+Genre+" "+User+" ,J'espére que votre soirée se passe bien")

def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL= dictionnnaire["url"]
    Titre = dictionnnaire["title"]
    return Sujet,Description,URL,Titre
def Arret(User,Genre):#Fonction quand l'uttilisateur coup l'assistant
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<3:
       speak("Au revoir" +Genre+" "+User+" ,bonne nuit")
    if hour>=3 and hour<9:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne matinée")
    if hour>=9 and hour<12:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne journée")
    if hour>=12 and hour<16:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne aprem")
    if hour>=16 and hour<18:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne fin d'aprés-midi")
    if hour>=18 and hour<22:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne soirée")
    if hour>=22 and hour<=23:
        speak("Au revoir "+Genre+" "+User+" , passez une bonne nuit.")
def shutdown():#Fonction d'arrét de l'ordinateur
    subprocess.run("poweroff")
def reboot():#Fonction de redemarage de l'ordinateur
    subprocess.run("reboot")
def Trad(genre):#Fonction de Traduction
    langue0=str(Lecture("Config/Langue/Lang0.txt"))
    langue1=str(Lecture("Config/Langue/Lang1.txt"))
    langue2=str(Lecture("Config/Langue/Lang2.txt"))
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
def Meteo(nbVille):#Fonction de recuperation des donne de l'api openweather
    Nomfile = "Config/meteo/ville"+str(nbVille)+".txt"   
    fichier = open(Nomfile,"r")
    ville = fichier.readlines()[0]
    fichier.close()
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
def Mute(Genre,User):
    root.blit(pygame.image.load("image/interfaceLIghtMute.png").convert(),(0,0))
    pygame.display.update()
    mute = True
    while mute == True :
        tkey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Arret(User,Genre)
                time.sleep(1.25)
                pygame.quit()
                return False
            if tkey[pygame.K_RETURN] :
                mute = False
                ThemeFonc()
                return True   
def YoutubeDownload():
    screen = Tk()
    screen.title("Youtube Downloader")
    screen.config(bg=Color)
    screen.maxsize(500,600)
    screen.minsize(500,600)
    LabelVideo = Label(screen,text= "Video",bg=Color,fg="white",font=("arial","25"))
    CadreVideo = Frame(screen,bg=Color,width=400,height=100)
    LabelVideo2 = Label(screen,text= "Playlist Video",bg=Color,fg="white",font=("arial","25"))
    CadreVideo2 = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic = Label(screen,text= "Musique",bg=Color,fg="white",font=("arial","25"))
    CadreMusic = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic2 = Label(screen,text= "Playlist Musique",bg=Color,fg="white",font=("arial","25"))
    CadreMusic2 = Frame(screen,bg=Color,width=400,height=100)
    #Label
    LabelURL1 = Label(CadreVideo,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL2 = Label(CadreVideo2,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL3 = Label(CadreMusic,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL4 = Label(CadreMusic2,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    #Entry
    EntryURL1 = Entry(CadreVideo,width=45)
    EntryURL2 = Entry(CadreVideo2,width=45)
    EntryURL3 = Entry(CadreMusic,width=45)
    EntryURL4 = Entry(CadreMusic2,width=45)
    #Fonction
    def AffichageCadre():
        LabelVideo.pack()
        CadreVideo.pack()
        LabelVideo2.pack()
        CadreVideo2.pack()
        LabelMusic.pack()
        CadreMusic.pack()
        LabelMusic2.pack()
        CadreMusic2.pack()
    def NoAffichageCadre():
        LabelVideo.pack_forget()
        CadreVideo.pack_forget()
        LabelVideo2.pack_forget()
        CadreVideo2.pack_forget()
        LabelMusic.pack_forget()
        CadreMusic.pack_forget()
        LabelMusic2.pack_forget()
        CadreMusic2.pack_forget()
    def Download1():
        URL = str(EntryURL1.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download("video")
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        
    def Download2():
        URL = str(EntryURL2.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download("video")
        showinfo(title="Youtube Downloader",message="Videos Télécharger")
    
    def Download3():
        URL = str(EntryURL3.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download("musique")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        showinfo(title="Youtube Downloader",message="Musique Télécharger")

    def Download4():
        URL = str(EntryURL4.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download("musique")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Musiques Télécharger")
    #Bouton
    BoutonDownload1 = Button(CadreVideo,text="Télécharger",bg=Color,fg="white",command=Download1)
    BoutonDownload2 = Button(CadreVideo2,text="Télécharger",bg=Color,fg="white",command=Download2)
    BoutonDownload3 = Button(CadreMusic,text="Télécharger",bg=Color,fg="white",command=Download3)
    BoutonDownload4 = Button(CadreMusic2,text="Télécharger",bg=Color,fg="white",command=Download4)
    #Affichage
    AffichageCadre()
    LabelURL1.place(x="150",y="0")
    LabelURL2.place(x="150",y="0")
    LabelURL3.place(x="150",y="0")
    LabelURL4.place(x="150",y="0")
    EntryURL1.place(x="10",y="30")
    EntryURL2.place(x="10",y="30")
    EntryURL3.place(x="10",y="30")
    EntryURL4.place(x="10",y="30")
    BoutonDownload1.place(x="150",y="60")
    BoutonDownload2.place(x="150",y="60")
    BoutonDownload3.place(x="150",y="60")
    BoutonDownload4.place(x="150",y="60")
    screen.mainloop()
def Setting():#fonction parametre
    ScreenPara = Tk()
    def FoncModif(file):
        Contenu = Lecture(file)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(300,150)
        ScreenModif.minsize(300,150)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        LabelContenu = Label(ScreenModif,text=Contenu,font=("arial","20"),bg=Color,fg=TextColor).pack()
        entry = Entry(ScreenModif)
        def Modif():
            Var = str(entry.get())
            Ecriture(file,Var)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).pack(side="right",anchor="s")
        entry.pack(side="left",anchor="s")
    def FoncModifName(file,file2):
        Contenu1 = Lecture(file)
        Contenu2 = Lecture(file2)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(400,150)
        ScreenModif.minsize(400,150)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        LabelContenuNom = Label(ScreenModif,text="Nom:"+Contenu1,font=("arial","15"),bg=Color,fg=TextColor).place(x="10",y="0")
        LabelContenuPro = Label(ScreenModif,text="Pronociation:"+Contenu2,font=("arial","15"),bg=Color,fg=TextColor).place(x="150",y="0")
        entry = Entry(ScreenModif)
        def ModifNom():
            Var = str(entry.get())
            Ecriture(file,Var)
        def ModifPrononce():
            Var = takeCommand()
            Ecriture(file2,Var)
            speak(Var)
        ModifNomB = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=ModifNom).pack(side="left",anchor="s")
        ModifPrononceB = Button(ScreenModif,text="Prononciation",bg=Color,fg=TextColor,command=ModifPrononce).pack(side="right",anchor="s")
        entry.place(relx=.5, rely=.5, anchor="center")
    def FoncModifUser(User,Genre):
        user = Lecture(User)
        genre = Lecture(Genre)
        ScreenModif = Toplevel()
        NewGenre =  StringVar(ScreenModif)
        if genre == "monsieur":
            NewGenre.set(listGenre[0])
        if genre == "madame":
            NewGenre.set(listGenre[1])
        ScreenModif.maxsize(550,200)
        ScreenModif.minsize(550,200)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        Labelgenre = Label(ScreenModif,text="genre: "+genre,font=("arial","20"),bg=Color,fg=TextColor).place(x="0",y="40")
        Labeluser = Label(ScreenModif,text="Utilisateur: "+user,font=("arial","20"),bg=Color,fg=TextColor).place(x="0",y="0")
        entry = Entry(ScreenModif)
        ListGenre = OptionMenu(ScreenModif,NewGenre, *listGenre)
        def Modif():
            VarUser = str(entry.get())
            VarGenre = NewGenre.get()
            Ecriture(User,VarUser)
            Ecriture(Genre,VarGenre)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).place(x="0",y="80")
        entry.place(x="380",y="5")
        ListGenre.place(x="380",y="45")
    def FoncModifSite(file,file2):
        Contenu = Lecture(file2)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(400,250)
        ScreenModif.minsize(400,250)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        LabelContenu = Label(ScreenModif,text="Nom: "+Contenu,font=("arial","20"),bg=Color,fg=TextColor)
        frameName = Frame(ScreenModif,width=350,height=100,bg=Color)
        labelName = Label(frameName,text="Nom :",bg=Color,fg=TextColor)
        entryName = Entry(frameName,width=30)
        labelLien = Label(frameName,text="Lien :",bg=Color,fg=TextColor)
        entryLien = Entry(frameName,width=30)
        def Modif():
            Var1 = str(entryName.get())
            Var2 = str(entryLien.get())
            Ecriture(file,Var2)
            Ecriture(file2,Var1)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).pack(side="bottom")
        LabelContenu.pack()
        frameName.place(relx=.5,rely=.5,anchor ="center")
        labelName.place(x="5",y="5")
        entryName.place(x="65",y="5")
        labelLien.place(x="5",y="65")
        entryLien.place(x="65",y="65")
    def FoncModifSiteLien(file):
        Contenu = Lecture(file)
        ScreenModif = Toplevel()
        ScreenModif.maxsize(400,250)
        ScreenModif.minsize(400,250)
        ScreenModif.wait_visibility(ScreenModif)
        ScreenModif.wm_attributes('-alpha',0.9)
        ScreenModif.config(bg=Color)
        LabelContenu = Label(ScreenModif,text="Lien Actuel: "+Contenu,font=("arial","11"),bg=Color,fg=TextColor)
        frameName = Frame(ScreenModif,width=350,height=100,bg=Color)
        labelLien = Label(frameName,text="Lien :",bg=Color,fg=TextColor)
        entryLien = Entry(frameName,width=30)
        def Modif():
            Var2 = str(entryLien.get())
            Ecriture(file,Var2)
            ScreenModif.destroy()
        Modif = Button(ScreenModif,text="Modifier",bg=Color,fg=TextColor,command=Modif).pack(side="bottom")
        LabelContenu.pack()
        frameName.place(relx=.5,rely=.5,anchor ="center")
        labelLien.place(x="5",y="30")
        entryLien.place(x="65",y="30")
    def MeteoChange1():
        FoncModif("Config/meteo/ville1.txt")
    def MeteoChange2():
        FoncModif("Config/meteo/ville2.txt")
    def MeteoChange3():
        FoncModif("Config/meteo/ville3.txt")
    def MeteoChange4():
        FoncModif("Config/meteo/ville4.txt")
    def MeteoChange5():
        FoncModif("Config/meteo/ville5.txt")
    def LangChange0():
        FoncModif("Config/Langue/Lang0.txt")
    def LangChange1():
        FoncModif("Config/Langue/Lang1.txt")
    def LangChange2():
        FoncModif("Config/Langue/Lang2.txt")
    def NomChange():
        FoncModifName("Config/Assistant/Nom.txt","Config/Assistant/NomPrononciation.txt")
    def UserChange1():
        FoncModifUser("Config/Assistant/User1.txt","Config/Assistant/Genre1.txt")
    def UserChange2():
        FoncModifUser("Config/Assistant/User2.txt","Config/Assistant/Genre2.txt")
    def UserChange3():
        FoncModifUser("Config/Assistant/User3.txt","Config/Assistant/Genre3.txt")
    def UserChange4():
        FoncModifUser("Config/Assistant/User4.txt","Config/Assistant/Genre4.txt")
    def FileChange1():
        FoncModif("Config/file/emplacementMusic.txt")
    def FileChange2():
        FoncModif("Config/file/emplacementVideo.txt")
    def HourSleepChange():
        FoncModif("Config/Assistant/hour.txt")
    def ReseauChange1():
        FoncModifSite("Config/Lien/Reseau1.txt","Config/Name/NameReseau1.txt")
    def ReseauChange2():
        FoncModifSite("Config/Lien/Reseau2.txt","Config/Name/NameReseau2.txt")
    def ReseauChange3():
        FoncModifSite("Config/Lien/Reseau3.txt","Config/Name/NameReseau3.txt")
    def GDrive():
        FoncModifSiteLien("Config/Lien/GDrive.txt")
    def Music():
        FoncModifSiteLien("Config/Lien/music.txt")
    def Note():
        FoncModifSiteLien("Config/Lien/Note.txt")
    def Agenda():
        FoncModifSiteLien("Config/Lien/Agenda.txt")
    def ToDoList():
        FoncModifSiteLien("Config/Lien/ToDoList.txt")
    def ReseauChange1():
        FoncModifSite("Config/reseau/lien/Reseau1.txt","Config/reseau/name/NameReseau1.txt")
    def ReseauChange2():
        FoncModifSite("Config/reseau/lien/Reseau2.txt","Config/reseau/name/NameReseau2.txt")
    def ReseauChange3():
        FoncModifSite("Config/reseau/lien/Reseau3.txt","Config/reseau/name/NameReseau3.txt")
    def MoteurChange():
        fileName = "Config/MoteurRecherche/NameMoteur.txt"
        fileLien = "Config/MoteurRecherche/LienMoteur.txt"
        moteur = str(Lecture(fileName))
        ScreenModifM = Toplevel()
        ScreenModifM.maxsize(300,150)
        ScreenModifM.minsize(300,150)
        NewMoteur = StringVar(ScreenModifM)
        if moteur == "google":
            NewMoteur.set(listMoteur[0])
        if moteur == "duckduckgo":
            NewMoteur.set(listMoteur[1])
        if moteur == "ecosia":
            NewMoteur.set(listMoteur[2])
        if moteur == "qwant":
            NewMoteur.set(listMoteur[3])
        if moteur == "bing":
            NewMoteur.set(listMoteur[4])
        ScreenModifM.wait_visibility(ScreenModifM)
        ScreenModifM.wm_attributes('-alpha',0.9)
        ScreenModifM.config(bg=Color)
        LabelInfo = Label(ScreenModifM,text="Moteur de recherche\n par défault",font=("arial","20"),bg=Color,fg=TextColor).pack()
        Moteur = OptionMenu(ScreenModifM,NewMoteur, *listMoteur)
        def Modif():
            VarMoteur = NewMoteur.get()
            if VarMoteur == "google":
                NewLien = "https://www.google.fr/"
                Ecriture(fileName,VarMoteur)
                Ecriture(fileLien,NewLien)
                ScreenModifM.destroy()
            if moteur == "duckduckgo":
                NewLien = "https://duckduckgo.com/"
                Ecriture(fileName,VarMoteur)
                Ecriture(fileLien,NewLien)
                ScreenModifM.destroy()
            if moteur == "ecosia":
                NewLien = "https://www.ecosia.org/?c=fr"
                Ecriture(fileName,VarMoteur)
                Ecriture(fileLien,NewLien)
                ScreenModifM.destroy()
            if moteur == "qwant":
                NewLien = "https://www.qwant.com/"
                Ecriture(fileName,VarMoteur)
                Ecriture(fileLien,NewLien)
                ScreenModifM.destroy()
            if moteur == "bing":
                NewLien = "https://www.bing.com/"
                Ecriture(fileName,VarMoteur)
                Ecriture(fileLien,NewLien)
                ScreenModifM.destroy()
        BoutonValider = Button(ScreenModifM,text="Valider",command=Modif,bg=Color,fg=TextColor)
        BoutonValider.pack(side="right")
        Moteur.pack(side="left")
    def ParaMeteo():
        CadreLang.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreMeteo.pack(side="right")
    def ParaLang():
        CadreMeteo.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack_forget()
        CadreLang.pack(side="right")
    def ParaAssistant():
        CadreLang.pack_forget()
        CadreMeteo.pack_forget()
        CadreLien.pack_forget()
        CadreAssistant.pack(side="right")
    def ParaLien():
        CadreLang.pack_forget()
        CadreMeteo.pack_forget()
        CadreAssistant.pack_forget()
        CadreLien.pack(side="right")
    ScreenPara.title("Six : Paramétre")
    ScreenPara.minsize(500,500)
    ScreenPara.maxsize(500,500)
    ScreenPara.iconphoto(False,PhotoImage(file="image/logo.png"))
    ScreenPara.wait_visibility(ScreenPara)
    ScreenPara.wm_attributes('-alpha',0.9)
    ScreenPara.config(bg=Color)
    #Cadre Meteo
    CadreMeteo = Frame(ScreenPara,bg=Color,width=350,height=400)
    Meteo1 = Label(CadreMeteo,text="Lieu Domicile",bg=Color,fg=TextColor,font=("arial","20"))
    Meteo2 = Label(CadreMeteo,text="Lieu Favorie ",bg=Color,fg=TextColor,font=("arial","20"))
    Meteo3 = Label(CadreMeteo,text="Lieu Travail ",bg=Color,fg=TextColor,font=("arial","20"))
    Meteo4 = Label(CadreMeteo,text="Lieu Vacance ",bg=Color,fg=TextColor,font=("arial","20"))
    Meteo5 = Label(CadreMeteo,text="Lieu Bonnus  ",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonMeteo1 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange1,font=("arial","15"))
    BoutonMeteo2 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange2,font=("arial","15"))
    BoutonMeteo3 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange3,font=("arial","15"))
    BoutonMeteo4 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange4,font=("arial","15"))
    BoutonMeteo5 = Button(CadreMeteo,text="Change",bg=Color,fg=TextColor,command=MeteoChange5,font=("arial","15"))
    #Cadre Langue
    CadreLang = Frame(ScreenPara,bg=Color,width=350,height=400)
    Lang0 = Label(CadreLang,text="Langue par défault",bg=Color,fg=TextColor,font=("arial","20"))
    Lang1 = Label(CadreLang,text="Premier Langue",bg=Color,fg=TextColor,font=("arial","20"))
    Lang2 = Label(CadreLang,text="Deuxiéme Langue",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonLang0 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange0,font=("arial","15"))
    BoutonLang1 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange1,font=("arial","15"))
    BoutonLang2 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange2,font=("arial","15"))
    #Cadre Para
    CadrePara = Frame(ScreenPara,bg="black",width=100,height=450)
    LabelIndication = Label(ScreenPara,text="Paramétre",font=("arial","30"),bg=Color,fg=TextColor)
    BoutonPara1 = Button(CadrePara,text="Assistant",bg=Color,fg=TextColor,command=ParaAssistant,font=("arial","12"))
    BoutonPara2= Button(CadrePara,text="Méteo",bg=Color,fg=TextColor,command=ParaMeteo,font=("arial","12"))
    BoutonPara3= Button(CadrePara,text="Traduction",bg=Color,fg=TextColor,command=ParaLang,font=("arial","12"))
    BoutonPara5 = Button(CadrePara,text="Lien",command=ParaLien,bg=Color,fg=TextColor,font=("arial","12"))
    BoutonPara6 = Button(CadrePara,text="Fermer",command=ScreenPara.destroy,bg=Color,fg=TextColor,font=("arial","12"))
    #Cadre Assistant
    CadreAssistant = Frame(ScreenPara,bg=Color,width=350,height=400)
    BoutonAssistant1 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=NomChange)
    BoutonAssistant2 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange1)
    BoutonAssistant3 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange2)
    BoutonAssistant4 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange3)
    BoutonAssistant5 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange4)
    BoutonAssistant6 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=HourSleepChange)
    BoutonAssistant7 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,command=MoteurChange,font=("arial","15"))
    Assistant1 = Label(CadreAssistant,text="Nom de l'assistant",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant2 = Label(CadreAssistant,text="Utilisateur Principale",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant3 = Label(CadreAssistant,text="Utilisateur Secondaire",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant4 = Label(CadreAssistant,text="Trosième utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant5 = Label(CadreAssistant,text="Quatrième utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant6 = Label(CadreAssistant,text="Heure de coucher",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant7 = Label(CadreAssistant,text="Recherche",bg=Color,fg=TextColor,font=("arial","20"))
    #Cadre Lien
    CadreLien = Frame(ScreenPara,bg=Color,width=350,height=400)
    BoutonLien1 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=GDrive)
    BoutonLien2 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=Music)
    BoutonLien3 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=Agenda)
    BoutonLien4 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ToDoList)
    BoutonLien5 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=Note)
    BoutonLien6 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ReseauChange1)
    BoutonLien7 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ReseauChange2)
    BoutonLien8 = Button(CadreLien,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=ReseauChange3)
    Lien1 = Label(CadreLien,text="Google Drive",bg=Color,fg=TextColor,font=("arial","17"))
    Lien2 = Label(CadreLien,text="Musique",bg=Color,fg=TextColor,font=("arial","17"))
    Lien3 = Label(CadreLien,text="Agenda",bg=Color,fg=TextColor,font=("arial","17"))
    Lien4 = Label(CadreLien,text="ToDoList",bg=Color,fg=TextColor,font=("arial","17"))
    Lien5 = Label(CadreLien,text="Note",bg=Color,fg=TextColor,font=("arial","17"))
    Lien6 = Label(CadreLien,text="Resaux Sociaux 1",bg=Color,fg=TextColor,font=("arial","17"))
    Lien7 = Label(CadreLien,text="Resaux Sociaux 2",bg=Color,fg=TextColor,font=("arial","17"))
    Lien8 = Label(CadreLien,text="Resaux Sociaux 3",bg=Color,fg=TextColor,font=("arial","17"))
    #Affichage
    #Fenetre
    LabelIndication.pack()
    CadrePara.pack(side="left")
    #Cadre Para
    BoutonPara1.place(x="5",y="5")
    BoutonPara2.place(x="10",y="85")
    BoutonPara3.place(x="2",y="165")
    BoutonPara5.place(x="10",y="245")
    BoutonPara6.place(x="10",y="325")
    #Cadre Meteo
    Meteo1.place(x="5",y="5")
    BoutonMeteo1.place(x="250",y="5")
    Meteo2.place(x="5",y="55")
    BoutonMeteo2.place(x="250",y="55")
    Meteo3.place(x="5",y="105")
    BoutonMeteo3.place(x="250",y="105")
    Meteo4.place(x="5",y="155")
    BoutonMeteo4.place(x="250",y="155")
    Meteo5.place(x="5",y="205")
    BoutonMeteo5.place(x="250",y="205")
    #Cadre Lang
    Lang0.place(x="5",y="5")
    BoutonLang0.place(x="250",y="5")
    Lang1.place(x="5",y="55")
    BoutonLang1.place(x="250",y="55")
    Lang2.place(x="5",y="105")
    BoutonLang2.place(x="250",y="105")
    #Cadre Assistant
    Assistant1.place(x="5",y="5")
    BoutonAssistant1.place(x="250",y="5")
    Assistant2.place(x="5",y="55")
    BoutonAssistant2.place(x="250",y="55")
    Assistant3.place(x="5",y="105")
    BoutonAssistant3.place(x="250",y="105")
    Assistant4.place(x="5",y="155")
    BoutonAssistant4.place(x="250",y="155")
    Assistant5.place(x="5",y="205")
    BoutonAssistant5.place(x="250",y="205")
    Assistant6.place(x="5",y="255")
    BoutonAssistant6.place(x="250",y="255")
    Assistant7.place(x="5",y="305")
    BoutonAssistant7.place(x="250",y="305")
    #Cadre Lien
    Lien1.place(x="5",y="5")
    BoutonLien1.place(x="250",y="5")
    Lien2.place(x="5",y="55")
    BoutonLien2.place(x="250",y="55")
    Lien3.place(x="5",y="105")
    BoutonLien3.place(x="250",y="105")
    Lien4.place(x="5",y="155")
    BoutonLien4.place(x="250",y="155")
    Lien5.place(x="5",y="205")
    BoutonLien5.place(x="250",y="205")
    Lien6.place(x="5",y="255")
    BoutonLien6.place(x="250",y="255")
    Lien7.place(x="5",y="305")
    BoutonLien7.place(x="250",y="305")
    Lien8.place(x="5",y="355")
    BoutonLien8.place(x="250",y="355")
    #Boucle Tkinter
    ScreenPara.mainloop()
#Programme principale
internet = TestInternet()
UserCourt = PrincipalUser
GenreCourt = PrincipalUserGenre
CourtNom = NomAssistant
if internet == True :
    ThemeFonc()
    salutation(UserCourt,GenreCourt)
    while varSix == True:
        HourActuel = datetime.datetime.now().hour
        statement = takeCommand().lower()
        if "bien" in statement or "oui" in statement:
            speak("Sa me réjouit de savoir que tout se passe bien pour vous"+GenreCourt+" .")
            speak("En quoi je peux donc vous servir ?")
        if statement==0:
            continue
        if HourActuel == HourSleep :
            speak("Vous devrai aller vous coucher "+ GenreCourt+".")
        if  statement =="salut"   or statement =="bonjour" or statement =="bonsoir":
            speak(statement+" en quoi je peux vous servir ?")
        if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
            Arret(UserCourt,GenreCourt)
            break
        if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
            speak("Ok "+GenreCourt+" je vous laisse tranquille")
            varSix = Mute(GenreCourt,UserCourt)
            speak("Ravi de vous revoir "+GenreCourt)
        if "recherche sur internet" in statement :
            speak("Vous voulez rechercher quoi ?")
            recherche = takeCommand()
            speak("Ok,Voici le resultat")
            duckduckgoSearch(recherche)
        if "actualités" in statement:
            CompleteURL = urlNew+"&pageSize="+nombrePageNew1+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]
            Sujet,Description,URL,title = NetoyageActu(article[0])
            speak("L'actualités la plus récent est "+title)
            speak("Voulez-vous que je vous ouvre le lien de cette actualités "+GenreCourt+".")
            reponse = takeCommand()
            if "oui" in reponse:
                speak("Ok je vous l'ouvre")
                webbrowser.open(URL)
            if "non" in reponse:
                speak("Ok "+GenreCourt+".")
        if "toujours là"  in statement  or "es-tu là" in statement or CourtNom in statement :
            speak("Oui")
        if statement == "tu es qui" or statement == "présente-toi" or "présentation" in statement or "qui es tu" in statement or "qui es-tu" in statement:
            speak("Je suis SIX un assistant personnel cree par Baptiste Pauchet. Pour l'assistait dans l'uttilisation de son ordinateur.")
        if "fin de journée" in statement :
            Arret()
            shutdown()
        if "redémarre" in statement :
            speak("Ok a tout de suite "+GenreCourt+"")
            reboot()
        if "ouvre youtube" in statement :
            webbrowser.open("https://www.youtube.com/")
            speak("Youtube et ouvert ")
        if "lance de la musique" in statement or "lancer de la musique" in statement:
            webbrowser.open(LienMusic)
            speak("Votre logiciel de musique est lancer"+GenreCourt+".")
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
                monthSTR = "Octobre"
            if month == 11 :
                monthSTR = "Novembre"
            if month == 12 :
                monthSTR = "Décembre"
            speak("Aujourd'huit on es le "+str(day)+monthSTR+str(years))
        if "météo" in statement:
            speak("Ou desirez savoir la meteo "+GenreCourt+" ?")
            r= takeCommand()
            if "maison" in r or "chez moi" in r or "à mon domicile" in r :
                MeteoParole(1)  
            if  "à mon lieu favori" in r  :
                MeteoParole(2)            
            if "à mon lieu de travail" in r :
                MeteoParole(3)
            if "à mon lieu de vacances" in r :
                 MeteoParole(4)
            if "au lieu de bonus" in r  :
                MeteoParole(5)
        if "un document" in statement :
            compteur = 0
            speak("Ok j'ouvre libreoffice writer ")
            os.popen("libreoffice --writer")
        if "un diaporama" in statement :   
            speak("Ok j'ouvre libreoffice impress ")
            os.popen("libreoffice --impress")
        if "un tableur" in statement :
            speak("Ok j'ouvre libreoffice calc ")
            os.popen("libreoffice --calc")
        if "google drive" in statement:
            speak("Ok voici votre google drive principale"+GenreCourt+"")
            webbrowser.open(LienGDrive)
        if "navigateur internet" in statement :
            speak("Ok j'ouvre votre navigateur internet")
            webbrowser.open(LienMoteur)
        if "programmation" in statement :  
            break
        if "résumé" in statement:
            Resumer()
        if "fais une grande recherche" in statement:
            speak("Que voulez vous que je vous recherche "+GenreCourt+"?")
            r = takeCommand()
            GrandRecherche(r)
        if "peux-tu me lire un truc" in statement :
            speak("Copier ce que vous voulez  que je vous lise "+GenreCourt+".")
            screenLect = Tk()
            screenLect.title("SIx : Lecture")
            screenLect.minsize("500","200")
            screenLect.maxsize("500","200")
            screenLect.iconphoto(False,PhotoImage(file="image/logo.png"))
            cadreCenter = Frame(screenLect,bg="grey",width=350,height=45)
            entryLect = Entry(cadreCenter,width=50)
            def Lecture():
                texte = entryLect.get()
                screenLect.destroy()
                speak(texte)
            if HourInf(hourDark) == True and HourSup(hourLight) == True:
                screenLect.config(bg="white")
                labelIndic = Label(screenLect,text="Copier votre texte",bg="white",fg="black",font=("arial","20"))
                boutonValider  = Button(screenLect,text="Valider",bg="white",fg="black",font=("arial","20"),command=Lecture)
            else :
                screenLect.config(bg="black")
                labelIndic = Label(screenLect,text="Copier votre texte",bg="black",fg="white",font=("arial","20"))
                boutonValider  = Button(screenLect,text="Valider",bg="black",fg="white",font=("arial","20"),command=Lecture)
            labelIndic.pack()
            cadreCenter.place(relx=.5, rely=.5, anchor="center")
            entryLect.place(relx=.5, rely=.5, anchor="center")
            boutonValider.place(x="200",y="125")
            screenLect.mainloop()
        if "ouvre tes paramètre" in statement :
            speak("Ok j'ouvre mes paramètre")
            Setting()
            PrincipalUser =  str(Lecture("Config/Assistant/User1.txt"))
            SecondairUser =  str(Lecture("Config/Assistant/User2.txt"))
            TroisiemeUser =  str(Lecture("Config/Assistant/User3.txt"))
            QuatriemeUser =  str(Lecture("Config/Assistant/User4.txt"))
            PrincipalUserGenre =  str(Lecture("Config/Assistant/Genre1.txt"))
            SecondairUserGenre =  str(Lecture("Config/Assistant/Genre2.txt"))
            TroisiemeUserGenre =  str(Lecture("Config/Assistant/Genre3.txt"))
            QuatriemeUserGenre =  str(Lecture("Config/Assistant/Genre4.txt"))
            NomAssistant =   str(Lecture("Config/Assistant/Nom.txt"))
            PrononceAssistant =   str(Lecture("Config/Assistant/NomPrononciation.txt"))
            FileMusic = str(Lecture("Config/file/emplacementMusic.txt"))
            FileVideo = str(Lecture("Config/file/emplacementVideo.txt"))
            HourSleep = int(Lecture("Config/Assistant/hour.txt"))
            NameMoteur = str(Lecture("Config/MoteurRecherche/NameMoteur.txt"))
            LienMoteur = str(Lecture("Config/MoteurRecherche/LienMoteur.txt"))
            LienGDrive = str(Lecture("Config/Lien/GDrive.txt"))
            LienMusic = str(Lecture("Config/Lien/music.txt"))
            LienAgenda = str(Lecture("Config/Lien/Agenda.txt"))
            LienNote = str(Lecture("Config/Lien/Note.txt"))
            LienToDoList = str(Lecture("Config/Lien/ToDoList.txt"))
            LienResaux1 = str(Lecture("Config/reseau/lien/Reseau1.txt"))
            LienResaux2 = str(Lecture("Config/reseau/lien/Reseau2.txt"))
            LienResaux3 = str(Lecture("Config/reseau/lien/Reseau3.txt"))
            NameResaux1 = str(Lecture("Config/reseau/name/NameReseau1.txt"))
            NameResaux2 = str(Lecture("Config/reseau/name/NameReseau2.txt"))
            NameResaux3 = str(Lecture("Config/reseau/name/NameReseau3.txt"))
            speak("J'ai enregistrer tout vos modification")
        if "raconter une blague" in statement or "raconte-moi une blague" in statement :
            nb = random.randint(1,10)
            if nb == 1 :
                speak("Que dit une noisette quand elle tombe dans l’eau ?")
                speak("Je me noix.")
            if nb == 2 :
                speak("Comment est-ce que les abeilles communiquent entre elles ?")
                speak("Par-miel.")
            if nb == 3 :
                speak("Quel est l’arbre préféré du chômeur ?")
                speak("Le bouleau.")
            if nb == 4 :
                speak("Qu’est-ce qu’une frite enceinte ?")
                speak("Une patate sautée.")
            if nb == 5 :
                speak("Que dit une mère à son fils geek quand le dîner est servi ?")
                speak("Alt Tab !")
            if nb == 6 :
                speak("Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?")
                speak("Marcher")
            if nb == 7 :
                speak("Pourquoi les Ch’tis aiment les fins de vacances au camping ?")
                speak("Parce que c’est le moment où ils peuvent démonter leur tente.")
            if nb == 8 :
                speak("Quelle est la partie de la voiture la plus dangereuse ?")
                speak("La conductrice.")
            if nb == 9 :
                speak("Pourquoi dit-on que les poissons travaillent illégalement ?")
                speak("Parce qu'ils n'ont pas de FISH de paie")
            if nb == 10 :
                speak("Mettre du sirop dans son gel douche")
                speak("En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible.")
        if "change de profil" in statement or "change d'utilisateur" in statement:
            compteur = 0
            speak("Quelle est votre numero de profile")
            r = takeCommand()
            if "le premier" in r or "1" in r :
                speak("Ok bienvenu " +PrincipalUserGenre+" "+PrincipalUser)
                UserCourt = PrincipalUser
                GenreCourt = PrincipalUserGenre
                speak("En quoi je peux vous étre utile")
            if "le deuxième" in r or "2" in r:
                speak("Ok bienvenu " +SecondairUserGenre+" "+SecondairUser)
                UserCourt = SecondairUser
                GenreCourt = SecondairUserGenre
                speak("En quoi je peux vous étre utile")
            if "le troisième" in r or "3" in r:
                speak("Ok bienvenu " +TroisiemeUserGenre+" "+TroisiemeUser)
                UserCourt = TroisiemeUser
                GenreCourt = TroisiemeUserGenre
                speak("En quoi je peux vous étre utile")
            if "le 4e" in r or "4" in r:
                speak("Ok bienvenu " +QuatriemeUserGenre+" "+QuatriemeUser)
                UserCourt = QuatriemeUser
                GenreCourt = QuatriemeUserGenre
                speak("En quoi je peux vous étre utile")
        if "dis-moi la température" in statement:
            lat , long = GeoLocGPS()
            temp = str(requests.get(urlWeather+"appid="+keyWeather+"&lat="+lat+"&lon="+long+"&lang=fr"+"&units=metric").json()["main"]["temp"])
            speak("La température a votre localisation est de "+temp+" degrés")
        if "dis-moi mes coordonnées GPS" in statement or "dis-moi où je suis" in statement or "dis-moi où je me trouve" in statement:
            lat , long = GeoLocGPS()
            speak("Les coordonnées GPS de votre localisation sont "+lat+" latitude et de longitude "+long+".") 
        if "enregistre de la musique" in statement or "enregistrement de la musique" in statement or "enregistre moi des vidéos" in statement or "enregistre-moi une vidéo" in statement:
            speak("Ok "+GenreCourt+" je vous ouvre le téléchargeur de video Youtube.")
            YoutubeDownload()
        if "traduire" in statement or "traduis-moi" in statement:
            speak("Ok je vous ouvre l'application de tradution")
            Trad(GenreCourt)
        if "agenda" in statement :
            speak("Ok je vous ouvre votre agenda "+GenreCourt)
            webbrowser.open(LienAgenda)
        if "to do list" in statement or "todolist" in statement:
            speak("Ok je vous ouvre votre to do list "+GenreCourt)
            webbrowser.open(LienToDoList)
        if "note" in statement or "notes" in statement:
            speak("Ok je vous ouvre vos notes en ligne "+GenreCourt)
            webbrowser.open(LienNote)
        if NameResaux1 in statement:
            compteur = 0
            speak("Ok je vous ouvre "+NameResaux1+" "+GenreCourt+" "+UserCourt)
            webbrowser.open(LienResaux1)
        if NameResaux2 in statement:
            speak("Ok je vous ouvre "+NameResaux2+" "+GenreCourt+" "+UserCourt)
            webbrowser.open(LienResaux2)
        if NameResaux3 in statement:
            speak("Ok je vous ouvre "+NameResaux3+" "+GenreCourt+" "+UserCourt)
            webbrowser.open(LienResaux3)
        if "ouvre l'explorateur de fichier" in statement or "ouvre les fichiers" in statement or "montre-moi mes fichiers" in statement :
            speak("ok je vous ouvre l'explorateur de fichier "+GenreCourt+".")
            os.popen("start explorer")
            
else :     
    pygame.quit()