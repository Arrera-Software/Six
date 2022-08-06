import subprocess
from turtle import Screen, color
import webbrowser
from gtts import gTTS
import os
import datetime
import random
import speech_recognition as sr
from ModuleInternet import TestInternet,duckduckgoSearch,GrandRecherche,DocArduino,DocPython
import requests
from tkinter import*
from translate import translate
import time
#Fonction Varriable
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
#Varriable
nrad = random.randint(1,2)
Color = "#08116f"
TextColor = "white"
keyWeather="ecffd157b2cc9eacbd0d35a45c3dc047"
urlWeather="https://api.openweathermap.org/data/2.5/weather?"
urlNew = "https://newsapi.org/v2/top-headlines?sources=google-news-fr"
keyNew = "3b43e18afcf945888748071d177b8513"
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
#Partie Module logiciel
def VisualStudio():
    os.popen("/usr/bin/code")
def terminal():
    os.popen("gnome-terminal")
def arduino():
    os.popen("flatpak run cc.arduino.arduinoide")
#Fonction de l'assistant
def speak(text):#Fonction de parole
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")
    print(NomAssistant+" : "+text)
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
    Temparure1,humiditer1,description1,ville1=Meteo(3)
    Temparure2,humiditer2,description2,ville2=Meteo(1)
    speak("La première actualités et " + Titre1 +".La seconde et "+ Titre2+".La troisiéme et "+ Titre3+".La quatriéme et "+ Titre4+" .La derniére et "+ Titre5  )
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
def salutation(User,Genre):#Fonction de salutation
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <= 9:
        if nrad == 1 :
            speak("Bonjour "+Genre+" "+User+",J'espére que vous passer une bonne nuit.Voulez-vous un petit résumer des actulités?")
        if nrad == 2 :
            speak("Bonjour "+Genre+" "+User+",J'espére que vous avez bien dormi.Voulez-vous un petit résumer des actulités? ")
        while True:
            r = takeCommand()
            if "oui" in r:
                Resumer()
                speak("J'espére que sa vous sera utile "+Genre+"")
                break
            if "non" in r:
                speak("Ok passer un exelente journée "+Genre+"")
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

def NetoyageActu(dictionnnaire):#Fonction qui permet de netoyer les donne recu par l'API
    Sujet = dictionnnaire["content"]
    Description = dictionnnaire["description"]
    URL= dictionnnaire["url"]
    Titre = dictionnnaire["title"]
    return Sujet,Description,URL,Titre
def EcritureNote(file,Genre):#Ecriture dans les fichier note
    speak("Voulez-vous dicter ou ecrire votre note "+Genre+".")
    r = takeCommand()
    if "dictée" in r or "dicter" in r:
        speak("Ok je vous ecoute")
        Note = takeCommand()
        Ecriture(file,Note)
    if "écrire" in r :
        speak("Ok ecrivé votre note "+Genre+".")
        Note = input("Votre note :")
        Ecriture(file,Note)
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
    if hour>=22 and hour<23:
        speak("Au revoir "+Genre+" "+User+" ,bonne nuit")
def takeCommand():#Fonction micro et reconaissance vocal
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            Requette=r.recognize_google(audio,language='fr')
            print("User = ",Requette)
        except Exception as e:
            return "None"
        return Requette
def shutdown():#Fonction d'arrét de l'ordinateur
    subprocess.run("poweroff")
def reboot():#Fonction de redemarage de l'ordinateur
    subprocess.run("reboot")
def Trad(Genre):#Fonction de Traduction
    lang1 = "fr"
    lang2 = Lecture("Config/Langue/Lang1.txt")
    lang3 = Lecture("Config/Langue/Lang2.txt")
    speak("Ok en quelle langue voulez-vous que je vous traduise votre texte "+Genre+"?")
    sortie = input("Choisissez entre 'fr' , 'lang1' ou 'lang2'##: ")
    if sortie == "français" or "fr" == sortie:
        text = input("Entrer votre texte : ")
        textTraduit = translate(text, lang1)
        print(textTraduit)
    if sortie == "lang1":
        text = input("Entrer votre texte : ") 
        textTraduit = translate(text, lang2)
        print(textTraduit)
    if sortie == "lang2":
        text = input("Entrer votre texte : ") 
        textTraduit = translate(text, lang3)
        print(textTraduit)
    
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
    speak("La météo à "+ville+ " ,et "+description +".Avec un taux d'humiditer de "+humiditer+" pourcent et une température de "+Temperature+" degrés")
def Mute(Genre):
        screen = Tk()
        def anychar(event):
            if event.keycode == 36 :
                screen.destroy()
                speak("Oui "+Genre+"")
        screen.title(NomAssistant)
        screen.wait_visibility(screen)
        screen.wm_attributes('-alpha',0.9)
        screen.config(bg=Color)
        screen.maxsize(300,100)
        screen.minsize(300,100)
        LabelMute = Label(screen,text="Mute",font=("arial","24"),bg=Color,fg=TextColor).place(relx=.5, rely=.5, anchor="center")
        screen.bind("<Key>",anychar)
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
    def ParaMeteo():
        CadreLang.pack_forget()
        CadreAssistant.pack_forget()
        CadreMeteo.pack(side="right")
    def ParaLang():
        CadreMeteo.pack_forget()
        CadreAssistant.pack_forget()
        CadreLang.pack(side="right")
    def ParaAssistant():
        CadreLang.pack_forget()
        CadreMeteo.pack_forget()
        CadreAssistant.pack(side="right")
    ScreenPara.title("Six : Paramétre")
    ScreenPara.minsize(500,500)
    ScreenPara.maxsize(500,500)
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
    Lang1 = Label(CadreLang,text="Premier langue",bg=Color,fg=TextColor,font=("arial","20"))
    Lang2 = Label(CadreLang,text="Deuxieme Langue",bg=Color,fg=TextColor,font=("arial","20"))
    BoutonLang1 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange1,font=("arial","15"))
    BoutonLang2 = Button(CadreLang,text="Change",bg=Color,fg=TextColor,command=LangChange2,font=("arial","15"))
    #Cadre Para
    CadrePara = Frame(ScreenPara,bg="black",width=100,height=450)
    LabelIndication = Label(ScreenPara,text="Paramétre",font=("arial","30"),bg=Color,fg=TextColor)
    BoutonPara1 = Button(CadrePara,text="Assistant",bg=Color,fg=TextColor,command=ParaAssistant)
    BoutonPara2= Button(CadrePara,text="Méteo",bg=Color,fg=TextColor,command=ParaMeteo)
    BoutonPara3= Button(CadrePara,text="Traduction",bg=Color,fg=TextColor,command=ParaLang)
    BoutonPara4 = Button(CadrePara,text="Fermer",command=ScreenPara.destroy,bg=Color,fg=TextColor)
    #Cadre Assistant
    CadreAssistant = Frame(ScreenPara,bg=Color,width=350,height=400)
    BoutonAssistant1 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=NomChange)
    BoutonAssistant2 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange1)
    BoutonAssistant3 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange2)
    BoutonAssistant4 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange3)
    BoutonAssistant5 = Button(CadreAssistant,text="Change",bg=Color,fg=TextColor,font=("arial","15"),command=UserChange4)
    Assistant1 = Label(CadreAssistant,text="Nom de l'assistant",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant2 = Label(CadreAssistant,text="Utilisateur Principale",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant3 = Label(CadreAssistant,text="Utilisateur Secondaire",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant4 = Label(CadreAssistant,text="Trosième utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    Assistant5 = Label(CadreAssistant,text="Quatrième utilisateur",bg=Color,fg=TextColor,font=("arial","17"))
    #Affichage
    #Fenetre
    LabelIndication.pack()
    CadrePara.pack(side="left")
    #Cadre Para
    BoutonPara1.place(x="5",y="5")
    BoutonPara2.place(x="10",y="85")
    BoutonPara3.place(x="2",y="165")
    BoutonPara4.place(x="10",y="245")
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
    Lang1.place(x="5",y="5")
    BoutonLang1.place(x="250",y="5")
    Lang2.place(x="5",y="55")
    BoutonLang2.place(x="250",y="55")
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
    ScreenPara.mainloop()
def ModeDev():#Fonction du mode dev
    ScreenDev = Tk()
    ScreenDev.title("Six")
    ScreenDev.minsize(300,600)
    ScreenDev.config(bg=Color)
    CadreEditeur = Frame(ScreenDev,bg=Color)
    CadreDoc = Frame(ScreenDev,bg=Color)
    Labelecart1 = Label(CadreEditeur,width=6,bg=Color)
    Labelecart2 = Label(CadreDoc,width=6,bg=Color)
    Labelecart3 = Label(CadreEditeur,width=6,bg=Color)
    Labelecart4 = Label(CadreDoc,width=6,bg=Color)
    BoutonVisual = Button(CadreEditeur,bg=Color,command=VisualStudio)
    BoutonArduino = Button(CadreEditeur,bg=Color,command=arduino)
    BoutonTerminal = Button(ScreenDev,bg=Color,command=terminal)
    BoutonPython = Button(CadreDoc,bg=Color,command=DocPython)
    BoutonDocArduino = Button(CadreDoc,bg=Color,command=DocArduino)
    IconVisual = PhotoImage(file="image/IconVisual.png",master=BoutonVisual)
    IconArduino = PhotoImage(file="image/IconArduino.png",master=BoutonArduino)
    IconTerminal = PhotoImage(file="image/IconTerminal.png",master=BoutonTerminal)
    IconPython = PhotoImage(file="image/IconDocPython.png",master=BoutonPython)
    IconDocArduino = PhotoImage(file="image/IconDocArduino.png",master=BoutonDocArduino)
    BoutonVisual.image_names = IconVisual
    BoutonArduino.image_names = IconArduino
    BoutonTerminal.image_names = IconTerminal
    BoutonDocArduino.image_names = IconDocArduino
    BoutonPython.image_names = IconPython
    BoutonVisual.config(image = IconVisual)
    BoutonArduino.config(image = IconArduino)
    BoutonTerminal.config(image=IconTerminal)
    BoutonDocArduino.config(image=IconDocArduino)
    BoutonPython.config(image=IconPython)
    CadreEditeur.pack(side="top")
    CadreDoc.pack(side="bottom")
    BoutonTerminal.place(relx=.5, rely=.5, anchor="center")
    BoutonVisual.pack(side="left")
    Labelecart1.pack(side="left")
    BoutonArduino.pack(side="right")
    Labelecart3.pack(side="right")
    BoutonPython.pack(side="left")
    Labelecart2.pack(side="left")
    BoutonDocArduino.pack(side="right")
    Labelecart4.pack(side="right")
    ScreenDev.mainloop()
#Programme principale
internet = TestInternet()
UserCourt = PrincipalUser
GenreCourt = PrincipalUserGenre
CourtNom = NomAssistant
if internet == True :
    salutation(UserCourt,GenreCourt)
    while True :
        statement = takeCommand().lower()
        if statement==0:
            continue
        if  statement =="salut"   or statement =="bonjour" or statement =="bonsoir":
            speak(statement+" en quoi je peux vous servir ?")
        if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
            Arret(UserCourt,GenreCourt)
            break
        if statement == "mute" or statement == "chut":
            speak("Ok "+GenreCourt+" je vous laisse tranquille")
            Mute(GenreCourt)
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
            webbrowser.open("https://music.youtube.com/")
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
            if "maison" in r or "chez moi" in r :
                MeteoParole(1)              
            if "à mon premier lieu de travail" in r or "à mon lieu de travail" in r :
                MeteoParole(2)
            if "à mon deuxième lieu de travail" in r or "à mon second lieu de travail" in r :
                MeteoParole(3)
            if "à mon premier lieu favori" in r or "à mon lieu favori" in r :
                MeteoParole(4)
            if "à mon second lieu favori" in r or "à mon deuxième lieu favori" in r :
                MeteoParole(5)
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
            speak("Ok voici votre google drive principale"+GenreCourt+"")
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
        if "firefox" in statement or "navigateur internet" in statement :
            speak("Ok j'ouvre votre navigateur internet")
            os.popen("/usr/bin/firefox")
        if "mes notes internet" in statement :
            speak("Ok voici vos note stoket sur internet "+GenreCourt+"")
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
            speak("Ok voici votre explorateur de fichier "+GenreCourt+"")
            os.popen("nautilus")
        if "jupiter" in statement :
            os.popen("jupyter-notebook /home/baptistep/")
        if "steam" in statement :
            speak("Ok bon jeu "+GenreCourt+"")
            os.popen("steam")
        if "arduino" in statement :
            os.popen("flatpak run cc.arduino.arduinoide")
            speak("Desirez vous que j'ouvre le navigateur web pour vous aidez "+GenreCourt+"")
            r = takeCommand()
            if "oui" in r :
                speak("Ok trés bien")
                os.popen("/usr/bin/firefox")
            if "non" in r :
                speak("Ok je reste a votre service si vous avez besoins "+GenreCourt+".")
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
        if "programmation" in statement :
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
            speak("Que voulez vous que je vous recherche "+GenreCourt+"?")
            r = takeCommand()
            GrandRecherche(r)
        if "peux-tu me lire un truc" in statement :
            speak("Copier ce que vous voulez  que je vous lise"+GenreCourt+".")
            lecture =str(input("Text :")) 
            speak(lecture)
        if "traduire" in statement:
            Trad()
        if "ouvre tes paramètre" in statement :
            Setting()
            speak("J'ai enregistrer tout vos modification")
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
            speak("Ok j'ouvre mes paramètre")
        if "raconter une blague" in statement or "raconte-moi une blague" in statement :
            nb = random.randint(1,10)
            if nb == 1 :
                speak("Que dit une noisette quand elle tombe dans l’eau ?")
                time.sleep(1)
                speak("Je me noix.")
            if nb == 2 :
                speak("Comment est-ce que les abeilles communiquent entre elles ?")
                time.sleep(1)
                speak("Par-miel.")
            if nb == 3 :
                speak("Quel est l’arbre préféré du chômeur ?")
                time.sleep(1)
                speak("Le bouleau.")
            if nb == 4 :
                speak("Qu’est-ce qu’une frite enceinte ?")
                time.sleep(1)
                speak("Une patate sautée.")
            if nb == 5 :
                speak("Que dit une mère à son fils geek quand le dîner est servi ?")
                time.sleep(1)
                speak("Alt Tab !")
            if nb == 6 :
                speak("Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?")
                time.sleep(1)
                speak("Marcher")
            if nb == 7 :
                speak("Pourquoi les Ch’tis aiment les fins de vacances au camping ?")
                time.sleep(1)
                speak("Parce que c’est le moment où ils peuvent démonter leur tente.")
            if nb == 8 :
                speak("Quelle est la partie de la voiture la plus dangereuse ?")
                time.sleep(1)
                speak("La conductrice.")
            if nb == 9 :
                speak("Pourquoi dit-on que les poissons travaillent illégalement ?")
                time.sleep(1)
                speak("Parce qu'ils n'ont pas de FISH de paie")
            if nb == 10 :
                speak("Mettre du sirop dans son gel douche")
                time.sleep(1)
                speak("En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible.")
        if "active le mode développement" in statement:
            speak("J'active le mode dev")
            ModeDev()
        if "change de profil" in statement or "change d'utilisateur" in statement:
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
else :        
    speakNoInternet()   