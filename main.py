from tkinter import*
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
from setting.setting import*
from function.temps import*
from src.varInterface import*
#Fonction Varriable

#Varriable
Color = "#3c0f14"
TextColor = "white"
PrincipalUser =  lectureJSON("setting/config.json","user1")
SecondairUser =  lectureJSON("setting/config.json","user2")
TroisiemeUser =  lectureJSON("setting/config.json","user3")
QuatriemeUser =  lectureJSON("setting/config.json","user4")
PrincipalUserGenre = lectureJSON("setting/config.json","userGenre1")
SecondairUserGenre =  lectureJSON("setting/config.json","userGenre2")
TroisiemeUserGenre =  lectureJSON("setting/config.json","userGenre3")
QuatriemeUserGenre =  lectureJSON("setting/config.json","userGenre4")
NomAssistant =   lectureJSON("setting/config.json","nomAssistant")
PrononceAssistant =   lectureJSON("setting/config.json","pronociationAssistant")
varSix = True
compteur = 0

#Fenetre pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
pygame.init()
pygame.display.set_icon(pygame.image.load("image/logo.png"))
pygame.display.set_caption("Assistant SIX")
root  = pygame.display.set_mode((rootWidht,rootHeight),pygame.NOFRAME)
police = pygame.font.SysFont("arial", 25)
#Fonction de l'assistant
root.blit(fond.convert(),(0,0))
pygame.display.update()

def salutation(User,Genre):#Fonction de salutation
    nrad = random.randint(0,1)
    listMatin = [("Bonjour "+Genre+" "+User+",J'espére que vous passer une bonne nuit."),("Bonjour "+Genre+" "+User+",J'espére que vous avez bien dormi.")]
    listDebut = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne matinée"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer un bon début de journée")]
    listAprem = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne aprem"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne après-midi")]
    listSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre début de soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre début de soirée se passe bien")]
    listFinSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre soirée se passe bien")]
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour <= 9:
        speak(listMatin[nrad],root)
        speak("Voulez-vous un petit résumer des actulités? ",root)
        while True:
            r = takeCommand(root,police)
            if "oui" in r:
                Resumer()
                speak("J'espére que sa vous sera utile "+Genre+"",root)
                break
            if "non" in r:
                speak("Ok passer un exélente journée "+Genre+"",root)
                break
    if hour >= 10 and hour <=12:
        speak(listDebut[nrad],root)
    if hour>=13 and hour<=17:
        speak(listAprem[nrad],root)
    if  hour>=18 and hour<=2:
        speak(listSoiree[nrad],root)
    if  hour>=21 and hour<=23:
        speak(listFinSoiree[nrad],root)

def Arret(User,Genre):#Fonction quand l'uttilisateur coup l'assistant
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<3:
       speak("Au revoir" +Genre+" "+User+" ,bonne nuit",root)
    if hour>=3 and hour<9:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne matinée",root)
    if hour>=9 and hour<12:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne journée",root)
    if hour>=12 and hour<16:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne aprem",root)
    if hour>=16 and hour<18:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne fin d'aprés-midi",root)
    if hour>=18 and hour<22:
        speak("Au revoir "+Genre+" "+User+" ,passez une bonne soirée",root)
    if hour>=22 and hour<=23:
        speak("Au revoir "+Genre+" "+User+" , passez une bonne nuit.",root)

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
        statement = takeCommand(root,police).lower()
        if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
            Arret(UserCourt,GenreCourt)
            break
        else :
            if "programmation" in statement :  
                break
            else :
                if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
                    speak("Ok "+GenreCourt+" je vous laisse tranquille",root)
                    varSix = Mute(GenreCourt,UserCourt)
                    speak("Ravi de vous revoir "+GenreCourt,root)
                else :
                    if "change de profil" in statement or "change d'utilisateur" in statement:
                        speak("Quelle est votre numero de profile",root)
                        r = takeCommand()
                        if "le premier" in r or "1" in r :
                            speak("Ok bienvenu " +PrincipalUserGenre+" "+PrincipalUser,root)
                            UserCourt = PrincipalUser
                            GenreCourt = PrincipalUserGenre
                            speak("En quoi je peux vous étre utile",root)
                        else :
                            if "le deuxième" in r or "2" in r:
                                speak("Ok bienvenu " +SecondairUserGenre+" "+SecondairUser,root)
                                UserCourt = SecondairUser
                                GenreCourt = SecondairUserGenre
                                speak("En quoi je peux vous étre utile",root)
                            else :
                                if "le troisième" in r or "3" in r:
                                    speak("Ok bienvenu " +TroisiemeUserGenre+" "+TroisiemeUser,root)
                                    UserCourt = TroisiemeUser
                                    GenreCourt = TroisiemeUserGenre
                                    speak("En quoi je peux vous étre utile",root)
                                else :
                                    speak("Ok bienvenu " +QuatriemeUserGenre+" "+QuatriemeUser,root)
                                    UserCourt = QuatriemeUser
                                    GenreCourt = QuatriemeUserGenre
                                    speak("En quoi je peux vous étre utile",root)
                    else :
                        if "ouvre tes paramètre" in statement :
                            speak("Ok j'ouvre mes paramètre",root)
                            Setting()
                            speak("J'ai enregistrer tout vos modification",root)
                        else :
                            condition = Main(statement,GenreCourt,UserCourt,CourtNom,root)
                            if condition == 0 :
                                condition = Web(statement,GenreCourt,UserCourt,root,police)
                                if condition == 0 :
                                    condition = Software(statement,GenreCourt,UserCourt,CourtNom,root,police)
                                else :
                                    continue
                            else :
                                continue               
else :     
    pygame.quit()