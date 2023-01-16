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
from src.varInterface import*
from neuron.neuronTime import*

class Six :
    def __init__(self):
        #Varriable
        self.Color = "#3c0f14"
        self.TextColor = "white"
        self.PrincipalUser =  lectureJSON("setting/config.json","user1")
        self.SecondairUser =  lectureJSON("setting/config.json","user2")
        self.TroisiemeUser =  lectureJSON("setting/config.json","user3")
        self.QuatriemeUser =  lectureJSON("setting/config.json","user4")
        self.PrincipalUserGenre = lectureJSON("setting/config.json","userGenre1")
        self.SecondairUserGenre =  lectureJSON("setting/config.json","userGenre2")
        self.TroisiemeUserGenre =  lectureJSON("setting/config.json","userGenre3")
        self.QuatriemeUserGenre =  lectureJSON("setting/config.json","userGenre4")
        self.NomAssistant =   lectureJSON("setting/config.json","nomAssistant")
        self.PrononceAssistant =   lectureJSON("setting/config.json","pronociationAssistant")
        self.varSix = True
        #Fenetre pygame
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
        pygame.init()
        pygame.display.set_icon(pygame.image.load("image/logo.png"))
        pygame.display.set_caption("Assistant SIX")
        self.root  = pygame.display.set_mode((rootWidht,rootHeight),pygame.NOFRAME)
        self.police = pygame.font.SysFont("arial", 25)
        self.root.blit(fond.convert(),(0,0))
        pygame.display.update()
        #Programme principale
        internet = TestInternet()
        UserCourt = self.PrincipalUser
        GenreCourt = self.PrincipalUserGenre
        CourtNom = self.NomAssistant
        if internet == True :
            self.salutation(UserCourt,GenreCourt)
        while True:
            HourActuel = datetime.datetime.now().hour
            statement = takeCommand(self.root,self.police).lower()
            if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
                self.Arret(UserCourt,GenreCourt)
                break
            else :
                if "programmation" in statement :  
                    break
                else :
                    if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
                        speak("Ok "+GenreCourt+" je vous laisse tranquille",self.root)
                        varSix = self.Mute(GenreCourt,UserCourt)
                        speak("Ravi de vous revoir "+GenreCourt,self.root)
                    else :
                        if "change de profil" in statement or "change d'utilisateur" in statement:
                            speak("Quelle est votre numero de profile",self.root)
                            r = takeCommand()
                            if "le premier" in r or "1" in r :
                                speak("Ok bienvenu " +self.PrincipalUserGenre+" "+self.PrincipalUser,self.root)
                                UserCourt = self.PrincipalUser
                                GenreCourt = self.PrincipalUserGenre
                                speak("En quoi je peux vous étre utile",self.root)
                            else :
                                if "le deuxième" in r or "2" in r:
                                    speak("Ok bienvenu " +self.SecondairUserGenre+" "+self.SecondairUser,self.root)
                                    UserCourt = self.SecondairUser
                                    GenreCourt = self.SecondairUserGenre
                                    speak("En quoi je peux vous étre utile",self.root)
                                else :
                                    if "le troisième" in r or "3" in r:
                                        speak("Ok bienvenu " +self.TroisiemeUserGenre+" "+self.TroisiemeUser,self.root)
                                        UserCourt = self.TroisiemeUser
                                        GenreCourt = self.TroisiemeUserGenre
                                        speak("En quoi je peux vous étre utile",self.root)
                                    else :
                                        speak("Ok bienvenu " +self.QuatriemeUserGenre+" "+self.QuatriemeUser,self.root)
                                        UserCourt = self.QuatriemeUser
                                        GenreCourt = self.QuatriemeUserGenre
                                        speak("En quoi je peux vous étre utile",self.root)
                        else :
                            if "paramètres" in statement or "paramètre" in statement :
                                speak("Ok j'ouvre mes paramètre",self.root)
                                Setting()
                                speak("J'ai enregistrer tout vos modification",self.root)
                            else :
                                condition = Main(statement,GenreCourt,UserCourt,CourtNom,self.root)
                                if condition == 0 :
                                    condition = Web(statement,GenreCourt,UserCourt,self.root,self.police)
                                    if condition == 0 :
                                        condition = Software(statement,GenreCourt,UserCourt,CourtNom,self.root,self.police)
                                        if condition == 0 :
                                            condition = Time(statement,GenreCourt,UserCourt,CourtNom,self.root,self.police)
                                        else :
                                            continue
                                    else :
                                        continue
                                else :
                                    continue               
        else :     
            pygame.quit()
        
    def Mute(self,Genre,User):
            self.root.blit(fondMute.convert(),(0,0))
            pygame.display.update()
            mute = True
            while mute == True :
                tkey = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.Arret(User,Genre)
                        time.sleep(1.25)
                        pygame.quit()
                        return False
                    if tkey[pygame.K_RETURN] :
                        mute = False
                        self.root.blit(fond.convert(),(0,0))
                        pygame.display.update()
                        return True       
        
    
    
    
    def salutation(self,User,Genre):#Fonction de salutation
        nrad = random.randint(0,1)
        listMatin = [("Bonjour "+Genre+" "+User+",J'espére que vous passer une bonne nuit."),("Bonjour "+Genre+" "+User+",J'espére que vous avez bien dormi.")]
        listDebut = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne matinée"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer un bon début de journée")]
        listAprem = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne aprem"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne après-midi")]
        listSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre début de soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre début de soirée se passe bien")]
        listFinSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre soirée se passe bien")]
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour <= 9:
            speak(listMatin[nrad],self.root)
            speak("Voulez-vous un petit résumer des actulités? ",self.root)
        else :
            if hour >= 10 and hour <=12:
                speak(listDebut[nrad],self.root)
            else :
                if hour>=13 and hour<=17:
                    speak(listAprem[nrad],self.root)
                else :
                    if  hour>=18 and hour<=20:
                        speak(listSoiree[nrad],self.root)
                    else :
                        speak(listFinSoiree[nrad],self.root)  
        
    def Arret(self,User,Genre):#Fonction quand l'uttilisateur coup l'assistant
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<3:
            speak("Au revoir" +Genre+" "+User+" ,bonne nuit",self.root)
        else :
            if hour>=3 and hour<9:
                speak("Au revoir "+Genre+" "+User+" ,passez une bonne matinée",self.root)
            else :
                if hour>=9 and hour<12:
                    speak("Au revoir "+Genre+" "+User+" ,passez une bonne journée",self.root)
                else : 
                    if hour>=12 and hour<16:
                        speak("Au revoir "+Genre+" "+User+" ,passez une bonne aprem",self.root)
                    else :
                        if hour>=16 and hour<18:
                            speak("Au revoir "+Genre+" "+User+" ,passez une bonne fin d'aprés-midi",self.root)
                        else :
                            if hour>=18 and hour<22:
                                speak("Au revoir "+Genre+" "+User+" ,passez une bonne soirée",self.root)
                            else :
                                speak("Au revoir "+Genre+" "+User+" , passez une bonne nuit.",self.root)
        
        