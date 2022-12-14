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
from setting.setting import*
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