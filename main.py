from tkinter import*
import pygame
from  pygame.locals import *
#fichier
from neuron.neuronMAIN import *
from neuron.neuronWeb import *
from neuron.neuronSoftware import *
from neuron.neuronUser import*
from function.api import Resumer
from function.search import*
from setting.setting import*
from src.varInterface import*
from neuron.neuronTime import*
from src.srcSix import*
class Six :
    def __init__(self):
        #Varriable
        self.Color = "#3c0f14"
        self.TextColor = "white"
        self.varSix = True
        self.NomAssistant =   lectureJSON("setting/config.json","nomAssistant")
        self.PrononceAssistant =   lectureJSON("setting/config.json","pronociationAssistant")   
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
        userCourt = principalUser
        genreCourt = principalUserGenre
        courtNom = self.NomAssistant
        if internet == True :
            self.salutation(userCourt,genreCourt)
            condition = 0
            while (condition < 15):
                #HourActuel = datetime.datetime.now().hour
                statement = SIXsrc(self.root,self.police).micro().lower()
                if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
                    SIXsrc(self.root,self.police).speak("Ok "+genreCourt+" je vous laisse tranquille")
                    condition = self.Mute(genreCourt,userCourt)
                    SIXsrc(self.root,self.police).speak("Ravi de vous revoir "+genreCourt)
                else :
                    if "paramètres" in statement or "paramètre" in statement :
                        SIXsrc(self.root,self.police).speak("Ok j'ouvre mes paramètre")
                        Setting()
                        SIXsrc(self.root,self.police).speak("J'ai enregistrer tout vos modification")
                    else :
                        if "programmation" in statement :  
                            condition = 15
                        else :
                            if "stop" in statement or "bye" in statement or "au revoir" in statement or "tu peux t'arrêter" in statement:
                                self.Arret(userCourt,genreCourt)
                                condition = 15
                            else :
                                condition = Main(statement,genreCourt,userCourt,courtNom,self.root,userCourt,genreCourt,self.police)
                                if condition == 0 :
                                    condition = NeuronWeb(statement,genreCourt,userCourt,self.root,self.police)
                                    if condition == 0 :
                                        condition = Software(statement,genreCourt,userCourt,courtNom,self.root,self.police)
                                        if condition == 0 :
                                            condition = neuronTime(statement,genreCourt,userCourt,courtNom,self.root,self.police)
                                            if condition == 0 :
                                                nbUser,condition = neuronUser(statement)
                                                if nbUser == 0 :
                                                    condition = 0
                                                else :
                                                    if nbUser == 1:
                                                        userCourt = principalUser
                                                        genreCourt = principalUserGenre
                                                        SIXsrc(self.root,self.police).speak("Rebonjour "+genreCourt+" "+userCourt)
                                                        condition = 0
                                                    else :
                                                        if nbUser == 2:
                                                            userCourt = secondairUser
                                                            genreCourt = secondairUserGenre
                                                            SIXsrc(self.root,self.police).speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                            condition = 0  
                                                        else :
                                                            if nbUser == 3 :
                                                                userCourt = troisiemeUser
                                                                genreCourt = troisiemeUserGenre
                                                                SIXsrc(self.root,self.police).speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                            else :
                                                                if nbUser == 4 :
                                                                    userCourt = quatriemeUser
                                                                    genreCourt = quatriemeUserGenre
                                                                    SIXsrc(self.root,self.police).speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                                    condition = 0
                                                                                                              
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
                        return 15
                    if tkey[pygame.K_RETURN] :
                        mute = False
                        self.root.blit(fond.convert(),(0,0))
                        pygame.display.update()
                        return 0       
        
    
    
    
    def salutation(self,User,Genre):#Fonction de salutation
        nrad = random.randint(0,1)
        listMatin = [("Bonjour "+Genre+" "+User+",J'espére que vous passer une bonne nuit."),("Bonjour "+Genre+" "+User+",J'espére que vous avez bien dormi.")]
        listDebut = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne matinée"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer un bon début de journée")]
        listAprem = [("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne aprem"),("Bonjour "+Genre+" "+User+" ,J'espére que vous passer une bonne après-midi")]
        listSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre début de soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre début de soirée se passe bien")]
        listFinSoiree = [("Bonsoir "+Genre+" "+User+" ,comment se passe votre soirée?"),("Bonsoir "+Genre+" "+User+" ,J'espére que votre soirée se passe bien")]
        hour=datetime.datetime.now().hour
        if hour >= 0 and hour <= 9:
            SIXsrc(self.root,self.police).speak(listMatin[nrad])
            SIXsrc(self.root,self.police).speak("Voulez-vous un petit résumer des actulités? ")
        else :
            if hour >= 10 and hour <=12:
                SIXsrc(self.root,self.police).speak(listDebut[nrad])
            else :
                if hour>=13 and hour<=17:
                    SIXsrc(self.root,self.police).speak(listAprem[nrad])
                else :
                    if  hour>=18 and hour<=20:
                        SIXsrc(self.root,self.police).speak(listSoiree[nrad])
                    else :
                        SIXsrc(self.root,self.police).speak(listFinSoiree[nrad])  
        
    def Arret(self,User,Genre):#Fonction quand l'uttilisateur coup l'assistant
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<3:
            SIXsrc(self.root,self.police).speak("Au revoir" +Genre+" "+User+" ,bonne nuit")
        else :
            if hour>=3 and hour<9:
                SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" ,passez une bonne matinée")
            else :
                if hour>=9 and hour<12:
                    SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" ,passez une bonne journée")
                else : 
                    if hour>=12 and hour<16:
                        SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" ,passez une bonne aprem")
                    else :
                        if hour>=16 and hour<18:
                            SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" ,passez une bonne fin d'aprés-midi")
                        else :
                            if hour>=18 and hour<22:
                                SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" ,passez une bonne soirée")
                            else :
                                SIXsrc(self.root,self.police).speak("Au revoir "+Genre+" "+User+" , passez une bonne nuit.")
        

Six()    