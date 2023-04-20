#from tkinter import*
import pygame
from  pygame.locals import *
#fichier
from neuron.neuronMAIN import *
from neuron.neuronWeb import *
from neuron.neuronSoftware import *
from neuron.neuronUser import*
from function.search import internet 
from setting.setting import*
from neuron.neuronTime import*
from neuron.neuronDiscution import *
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
        #declaration objet
        self.sourceSix =  SIXsrc(self.root,self.police)
        #Programme principale
        etatInternet = internet.testInternet()
        courtNom = self.NomAssistant
        if etatInternet == True :
            webNeuron = neuroneWeb(self.NomAssistant,self.root,principalUser,principalUserGenre,self.police)
            mainNeuron=neuroneMain(self.NomAssistant,self.root,principalUser,principalUserGenre,self.police)
            softwareNeuron = neuroneSoftware(self.NomAssistant,self.root,principalUser,principalUserGenre,self.police)
            timeNeuron = neuroneTime(self.NomAssistant,self.root,principalUser,principalUserGenre,self.police)
            self.salutation(principalUser,principalUserGenre)
            condition = 0
            while (condition < 15):
                #HourActuel = datetime.datetime.now().hour
                statement = self.sourceSix.micro().lower()
                if statement == "mute" or statement == "chut" or "ferme ta gueule" in statement:
                    self.sourceSix.speak("Ok "+genreCourt+" je vous laisse tranquille")
                    condition = self.Mute(genreCourt,userCourt)
                    self.sourceSix.speak("Ravi de vous revoir "+genreCourt)
                else :
                    if "paramètres" in statement or "paramètre" in statement :
                        self.sourceSix.speak("Ok j'ouvre mes paramètre")
                        Setting()
                        self.sourceSix.speak("J'ai enregistrer tout vos modification")
                    else :
                        if "programmation" in statement :  
                            condition = 15
                        else :
                                condition = mainNeuron.neurone(statement)
                                if condition == 0 :
                                    condition = webNeuron.neuron(statement)
                                    if condition == 0 :
                                        condition = softwareNeuron.neurone(statement)
                                        if condition == 0 :
                                            condition = timeNeuron.neurone(statement)
                                            if condition == 0 :
                                                nbUser,condition = neuroneUser(statement)
                                                if nbUser == 0 :
                                                    condition = 0
                                                else :
                                                    if nbUser == 1:
                                                        userCourt = principalUser
                                                        genreCourt = principalUserGenre
                                                        self.sourceSix.speak("Rebonjour "+genreCourt+" "+userCourt)
                                                        webNeuron = neuroneWeb(courtNom,self.root,userCourt,genreCourt,self.police)
                                                        mainNeuron=neuroneMain(courtNom,self.root,userCourt,genreCourt,self.police)
                                                        softwareNeuron = neuroneSoftware(courtNom,self.root,userCourt,genreCourt,self.police)
                                                        timeNeuron = neuroneTime(courtNom,self.root,userCourt,genreCourt,self.police)
                                                        condition = 0
                                                    else :
                                                        if nbUser == 2:
                                                            userCourt = secondairUser
                                                            genreCourt = secondairUserGenre
                                                            self.sourceSix.speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                            webNeuron = neuroneWeb(courtNom,self.root,userCourt,genreCourt,self.police)
                                                            mainNeuron=neuroneMain(courtNom,self.root,userCourt,genreCourt,self.police)
                                                            softwareNeuron = neuroneSoftware(courtNom,self.root,userCourt,genreCourt,self.police)
                                                            timeNeuron = neuroneTime(courtNom,self.root,userCourt,genreCourt,self.police)
                                                            condition = 0  
                                                        else :
                                                            if nbUser == 3 :
                                                                userCourt = troisiemeUser
                                                                genreCourt = troisiemeUserGenre
                                                                self.sourceSix.speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                                webNeuron = neuroneWeb(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                mainNeuron=neuroneMain(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                softwareNeuron = neuroneSoftware(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                timeNeuron = neuroneTime(courtNom,self.root,userCourt,genreCourt,self.police)
                                                            else :
                                                                if nbUser == 4 :
                                                                    userCourt = quatriemeUser
                                                                    genreCourt = quatriemeUserGenre
                                                                    self.sourceSix.speak("Bonjour "+genreCourt+" "+userCourt+" en quoi je peux vous aidez ?")
                                                                    webNeuron = neuroneWeb(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                    mainNeuron=neuroneMain(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                    softwareNeuron = neuroneSoftware(courtNom,self.root,userCourt,genreCourt,self.police)
                                                                    timeNeuron = neuroneTime(courtNom,self.root,userCourt,genreCourt,self.police)
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
            self.sourceSix.speak(listMatin[nrad])
            self.sourceSix.speak("Voulez-vous un petit résumer des actulités? ")
        else :
            if hour >= 10 and hour <=12:
                self.sourceSix.speak(listDebut[nrad])
            else :
                if hour>=13 and hour<=17:
                    self.sourceSix.speak(listAprem[nrad])
                else :
                    if  hour>=18 and hour<=20:
                        self.sourceSix.speak(listSoiree[nrad])
                    else :
                        self.sourceSix.speak(listFinSoiree[nrad])  
        
    
        

#Six()    