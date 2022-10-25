from tkinter import*
import time
from time import *
import pygame
from  pygame.locals import *
#fichier
from src.voice import*
from neuron.neuronMAIN import *
from neuron.web import *
from neuron.software import *
from function.api import Resumer
from function.search import TestInternet
from src.speechRecognition import *
from src.file import*
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
#Varriable
nrad = random.randint(1,2)
Color = "#3c0f14"
TextColor = "white"
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
listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
varSix = True
HourSleep = int(Lecture("Config/Assistant/hour.txt"))
compteur = 0
fond = pygame.image.load("image/fondMain.png")
fondMute = pygame.image.load("image/fondMute.png")
#Fenetre pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
pygame.init()
pygame.display.set_icon(pygame.image.load("image/logo.png"))
pygame.display.set_caption("Assistant SIX")
root  = pygame.display.set_mode((600,200),pygame.NOFRAME)
police = pygame.font.SysFont("arial", 25)
#Fonction de l'assistant
root.blit(fond.convert(),(0,0))
pygame.display.update()
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
def Mute(Genre,User):
    root.blit(fondMute.convert(),(0,0))
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
                root.blit(fond.convert(),(0,0))
                pygame.display.update()
                return True   

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
    salutation(UserCourt,GenreCourt)
    while varSix == True:
        HourActuel = datetime.datetime.now().hour
        statement = takeCommand().lower()
        if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
            Arret(UserCourt,GenreCourt)
            break
        else :
            if "programmation" in statement :  
                break
            else :
                if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
                    speak("Ok "+GenreCourt+" je vous laisse tranquille")
                    varSix = Mute(GenreCourt,UserCourt)
                    speak("Ravi de vous revoir "+GenreCourt)
                else :
                    if "change de profil" in statement or "change d'utilisateur" in statement:
                        speak("Quelle est votre numero de profile")
                        r = takeCommand()
                        if "le premier" in r or "1" in r :
                            speak("Ok bienvenu " +PrincipalUserGenre+" "+PrincipalUser)
                            UserCourt = PrincipalUser
                            GenreCourt = PrincipalUserGenre
                            speak("En quoi je peux vous étre utile")
                        else :
                            if "le deuxième" in r or "2" in r:
                                speak("Ok bienvenu " +SecondairUserGenre+" "+SecondairUser)
                                UserCourt = SecondairUser
                                GenreCourt = SecondairUserGenre
                                speak("En quoi je peux vous étre utile")
                            else :
                                if "le troisième" in r or "3" in r:
                                    speak("Ok bienvenu " +TroisiemeUserGenre+" "+TroisiemeUser)
                                    UserCourt = TroisiemeUser
                                    GenreCourt = TroisiemeUserGenre
                                    speak("En quoi je peux vous étre utile")
                                else :
                                    speak("Ok bienvenu " +QuatriemeUserGenre+" "+QuatriemeUser)
                                    UserCourt = QuatriemeUser
                                    GenreCourt = QuatriemeUserGenre
                                    speak("En quoi je peux vous étre utile")
                    else :
                        if "ouvre tes paramètre" in statement :
                            speak("Ok j'ouvre mes paramètre")
                            Setting()
                            speak("J'ai enregistrer tout vos modification")
                        else :
                            condition = Main(statement,GenreCourt,UserCourt,CourtNom)
                            if condition == 0 :
                                condition = Web(statement,GenreCourt,UserCourt)
                                if condition == 0 :
                                    condition = Software(statement,GenreCourt,UserCourt,CourtNom)
                                else :
                                    continue
                            else :
                                continue               
else :     
    pygame.quit()