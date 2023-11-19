from librairy.travailJSON import *
import requests

class SIXGestion :
    def __init__(self,file:jsonWork) :
        #testInternet
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            self.etatConnexion = True
        except requests.ConnectionError :
            self.etatConnexion = False
        #Emplacement image interface
        self.acceuil = "IMGAcceuil.png"
        self.main = "IMGmain.png"
        self.attent1 = "IMGAttent1.png"
        self.attent2 = "IMGAttent2.png"
        self.attent3 = "IMGAttent3.png"
        self.mute = "IMGMute.png"
        self.speakBigSmall = "IMGSpeak-BIG-Small.png"
        self.speakSmallSmall = "IMGSpeak-Small-Small.png"
        self.listColorLabel = ["#ffffff","#000000"]
        self.listColorInterface = ["#3c0f14","#000000","#ffffff"]
        #listUtiliser
        self.lienAcceuil = str
        self.lienMute = str
        self.lienMain = str
        self.lienAttent = [str]
        self.lienParole = [str]
        self.colorText = str
        self.colorLabel = str
        self.colorInterface = str
        #Creation var de verification
        self.themeSet = bool
        #Ouverture fichier config Six
        self.fileSixConfig = file
        #varriable theme
        self.varTheme =  str
    
    def getEtatInternet(self):
        return self.etatConnexion
       
    def setTheme(self):
        varTheme = self.fileSixConfig.lectureJSON("theme") #Valeur possible "default","white","dark"
        #Non de fichier Image
        if varTheme == "default" :
            chemin = "asset/IMGinterface/default/"
            self.colorText = "black"
            self.colorLabel = self.listColorLabel[0]
            self.colorInterface = self.listColorInterface[0]
        else :
            if varTheme == "black" : 
               chemin = "asset/IMGinterface/black/"
               self.colorText = "black"
               self.colorLabel = self.listColorLabel[0]
               self.colorInterface = self.listColorInterface[1]
            else :
                if varTheme == "white" :
                    chemin = "asset/IMGinterface/white/"
                    self.colorText = "white"
                    self.colorLabel = self.listColorLabel[1]
                    self.colorInterface = self.listColorInterface[2]
                else:
                    chemin = "asset/IMGinterface/default/"
                    self.colorText = "black"
                    self.colorLabel = self.listColorLabel[0]
                    self.colorInterface = self.listColorInterface[0]
        self.lienAcceuil = chemin+self.acceuil
        self.lienMute = chemin+self.mute
        self.lienMain = chemin+self.main
        self.lienAttent = [chemin+self.attent1,
                            chemin+self.attent2,
                            chemin+self.attent3]
        self.lienParole = [chemin+self.speakBigSmall,
                            chemin+self.speakSmallSmall]   
        self.themeSet = True
    
    def getGUIAcceuil(self):
        if self.themeSet == True :
            return self.lienAcceuil
    
    def getGUIMain(self):
        if self.themeSet == True :
            return self.lienMain
       
    def getGUIMute(self):
        if self.themeSet == True :
            return self.lienMute

    def getGUIparoleBigSmall(self):
        if self.themeSet == True :
            return self.lienParole[0]

    def getGUIparoleSmallSmall(self):
        if self.themeSet == True :
            return self.lienParole[1]
             
    def getGUItextColor(self):
        if self.themeSet == True:
            return self.colorText
        
    def getGUIAttent(self):
        if self.themeSet == True :
            return [self.lienAttent[0],self.lienAttent[1],self.lienAttent[2]]
    
    def getColorInterface(self):
        if self.themeSet == True :
            return self.colorInterface
    
    def getColorLabel(self):
        if self.themeSet == True :
            return self.colorLabel