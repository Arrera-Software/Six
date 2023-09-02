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
        self.lienMain = ["asset/IMGinterface/interfaceDefault.png","asset/IMGinterface/interfaceLIght.png","asset/IMGinterface/interfaceDark.png"]
        self.lienMute = ["asset/IMGinterface/interfaceDefaultMute.png","asset/IMGinterface/interfaceLIghtMute.png","asset/IMGinterface/interfaceDarkMute.png"]
        self.lienParole1 = ["asset/IMGinterface/interfaceDefaultVoice1.png","asset/IMGinterface/interfaceLIghtVoice1.png","asset/IMGinterface/interfaceDarkVoice1.png"]
        self.lienParole2 = ["asset/IMGinterface/interfaceDefaultVoice2.png","asset/IMGinterface/interfaceLIghtVoice2.png","asset/IMGinterface/interfaceDarkVoice2.png"]
        self.lienParole3 = ["asset/IMGinterface/interfaceDefaultVoice3.png","asset/IMGinterface/interfaceLIghtVoice3.png","asset/IMGinterface/interfaceDarkVoice3.png"]
        self.lienFenetre = ["asset/IMGinterface/interfaceDefaultFenetre.png","asset/IMGinterface/interfaceLIghtFenetre.png","asset/IMGinterface/interfaceDarkFenetre.png"]
        #Ouverture fichier config Six
        self.fileSixConfig = jsonWork("sixConfig.json")
        #varriable theme
        self.varTheme =  str
    
    def getEtatInternet(self):
        return self.etatConnexion
       
    def setTheme(self):
        self.varTheme = self.fileSixConfig.lectureJSON("theme") #Valeur possible "default","white","dark"
    
    def getGUIMain(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienMain[0])
        else :
            if self.varTheme == "white" :
                return pygame.image.load(self.lienMain[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienMain[2])
                else :
                    return pygame.image.load(self.lienMain[0])


    def getGUIMute(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienMute[0])
        else :
            if self.varTheme == "white" :
                return pygame.image.load(self.lienMute[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienMute[2])
                else :
                    return pygame.image.load(self.lienMute[0])

    def getGUIparole1(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienParole1[0])
        else :
            if self.varTheme == "white" :
                return pygame.image.load(self.lienParole1[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienParole1[2])
                else :
                    return pygame.image.load(self.lienParole1[0])   

    def getGUIparole2(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienParole2[0])
        else :
            if self.varTheme == "white" :
                return pygame.image.load(self.lienParole2[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienParole2[2])  
                else :
                    return pygame.image.load(self.lienParole2[0])

    def getGUIparole3(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienParole3[0])
        else :
            if self.varTheme == "white" :
                return pygame.image.load(self.lienParole3[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienParole3[2])
                else :
                    return pygame.image.load(self.lienParole3[0]) 
                

    def getGUItextColor(self):
        if self.varTheme == "default" :
            return (255,255,255)
        else :
            if self.varTheme == "white" :
                return (0,0,0)
            else :
                if self.varTheme == "dark" :
                    return (255,255,255)
                else :
                    return (255,255,255)
                    

    def getGUIOpenFentreTkinter(self):
        if self.varTheme == "default" :
            return pygame.image.load(self.lienFenetre[0])
        else :
            if self.varTheme == "white":
                return pygame.image.load(self.lienFenetre[1])
            else :
                if self.varTheme == "dark" :
                    return pygame.image.load(self.lienFenetre[2])
                else :
                    return pygame.image.load(self.lienFenetre[0])
"""
rootWidht = 600
rootHeight = 200
fondMute = GUIMute()
fond = GUIMain()
fondFenetre = GUIOpenFentreTkinter()
fondParole1 = GUIparole1()
fondParole2 = GUIparole2()
fondParole3 = GUIparole3()
ColorText = GUItextColor()
"""
