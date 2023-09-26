import pygame
from  pygame.locals import *
from librairy.travailJSON import *
import requests

class SIXGestion :
    def __init__(self) :
        #testInternet
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            self.etatConnexion = True
        except requests.ConnectionError :
            self.etatConnexion = False
        #Emplacement image interface
        self.lienAcceuil = str
        self.lienMute = str
        self.lienMain = str
        self.lienAttent = [str]
        self.lienParole = [str]
        self.lienMicro = [str]
        self.colorText = (int,int,int)
        #Creation var de verification
        self.themeSet = bool
        #Ouverture fichier config Six
        self.fileSixConfig = jsonWork("sixConfig.json")
        #varriable theme
        self.varTheme =  str
    
    def getEtatInternet(self):
        return self.etatConnexion
       
    def setTheme(self):
        varTheme = self.fileSixConfig.lectureJSON("theme") #Valeur possible "default","white","dark"
        #Non de fichier Image
        acceuil = "IMGAcceuil.png"
        main = "IMGmain.png"
        attent1 = "IMGAttent1.png"
        attent2 = "IMGAttent2.png"
        attent3 = "IMGAttent3.png"
        microSmallSmall = "IMGMicro-Small-Small.png" 
        microSmallBig = "IMGMicroSmall-Big.png"
        mute = "IMGMute.png"
        speakBigSmall = "IMGSpeak-BIG-Small.png"
        speakSmallSmall = "IMGSpeak-Small-Small.png"
        if varTheme == "default" :
            chemin = "asset/IMGinterface/default/"
            self.colorText = (0,0,0)
        else :
            if varTheme == "black" : 
               chemin = "asset/IMGinterface/black/"
               self.colorText = (0,0,0)
            else :
                if varTheme == "white" :
                    chemin = "asset/IMGinterface/white/"
                    self.colorText = (255,255,255)
                else:
                    chemin = "asset/IMGinterface/default/"
                    self.colorText = (0,0,0)
        self.lienAcceuil = chemin+acceuil
        self.lienMute = chemin+mute
        self.lienMain = chemin+main
        self.lienAttent = [chemin+attent1,
                            chemin+attent2,
                            chemin+attent3]
        self.lienParole = [chemin+speakBigSmall,
                            chemin+speakSmallSmall]
        self.lienMicro = [chemin+microSmallBig,
                            chemin+microSmallSmall]
        
        self.themeSet = True
    
    def getGUIAcceuil(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienAcceuil)
    
    def getGUIMain(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienMain)
       
    def getGUIMute(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienMute)

    def getGUIparoleBigSmall(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienParole[0])

        
    def getGUIparoleSmallSmall(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienParole[1])
    

    def getGUImicroSmallBig(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienMicro[0])
        
    def getGUImicroSmallSmall(self):
        if self.themeSet == True :
            return pygame.image.load(self.lienMicro[1])          

    def getGUItextColor(self):
        if self.themeSet == True:
            return self.colorText
