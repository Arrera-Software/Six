from librairy.travailJSON import *
import requests

class SIXGestion :
    def __init__(self,file:jsonWork) :
        #testInternet
        try:
            requetteInternet = requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        #Emplacement image interface
        self.__acceuil = "IMGAcceuil.png"
        self.__main = "IMGmain.png"
        self.__attent1 = "IMGAttent1.png"
        self.__attent2 = "IMGAttent2.png"
        self.__attent3 = "IMGAttent3.png"
        self.__mute = "IMGMute.png"
        self.__noConnecte = "IMGNoConnection.png"
        self.__speakBigSmall = "IMGSpeak-BIG-Small.png"
        self.__speakSmallSmall = "IMGSpeak-Small-Small.png"
        self.__listColorLabel = ["#ffffff","#000000"]
        self.__listColorInterface = ["#3c0f14","#000000","#ffffff"]
        self.__listColorTextActu = ["#ffffff","#000000"]
        self.__listColor1Para  =  ["#3c0f14","#000000","#ffffff"]
        self.__listColor2Para  =  ["#2b0b0e","#000000","#ffffff"]
        #listUtiliser
        self.__lienAcceuil = str
        self.__lienMute = str
        self.__lienMain = str
        self.__lienAttent = [str]
        self.__lienParole = [str]
        self.__lienNoConnecte = str
        self.__colorText = str
        self.__colorLabel = str
        self.__colorInterface = str
        self.__colorTextActu = str
        self.__color1Para = str
        self.__color2Para = str
        #Creation var de verification
        self.__themeSet = bool
        #Ouverture fichier config Six
        self.__fileSixConfig = file
    
    def getEtatInternet(self):
        return self.__etatConnexion
       
    def setTheme(self):
        varTheme = self.__fileSixConfig.lectureJSON("theme") #Valeur possible "default","white","dark"
        #Non de fichier Image
        if varTheme == "default" :
            chemin = "asset/IMGinterface/default/"
            self.__colorText = "black"
            self.__colorLabel = self.__listColorLabel[0]
            self.__colorInterface = self.__listColorInterface[0]
            self.__colorTextActu = self.__listColorTextActu[0]
            self.__color1Para = self.__listColor1Para[0]
            self.__color2Para = self.__listColor2Para[0]
        else :
            if varTheme == "black" : 
               chemin = "asset/IMGinterface/black/"
               self.__colorText = "black"
               self.__colorLabel = self.__listColorLabel[0]
               self.__colorInterface = self.__listColorInterface[1]
               self.__colorTextActu = self.__listColorTextActu[0]
               self.__color1Para = self.__listColor1Para[1]
               self.__color2Para = self.__listColor2Para[1]
            else :
                if varTheme == "white" :
                    chemin = "asset/IMGinterface/white/"
                    self.__colorText = "white"
                    self.__colorLabel = self.__listColorLabel[1]
                    self.__colorInterface = self.__listColorInterface[2]
                    self.__colorTextActu = self.__listColorTextActu[1]
                    self.__color1Para = self.__listColor1Para[2]
                    self.__color2Para = self.__listColor2Para[2]
                else:
                    chemin = "asset/IMGinterface/default/"
                    self.__colorText = "black"
                    self.__colorLabel = self.__listColorLabel[0]
                    self.__colorInterface = self.__listColorInterface[0]
                    self.__colorTextActu = self.__listColorTextActu[0]
                    self.__color1Para = self.__listColor1Para[0]
                    self.__color2Para = self.__listColor2Para[0]
        self.__lienAcceuil = chemin+self.__acceuil
        self.__lienMute = chemin+self.__mute
        self.__lienMain = chemin+self.__main
        self.__lienAttent = [chemin+self.__attent1,
                            chemin+self.__attent2,
                            chemin+self.__attent3]
        self.__lienParole = [chemin+self.__speakBigSmall,
                            chemin+self.__speakSmallSmall]  
        self.__lienNoConnecte = chemin+self.__noConnecte 
        self.__themeSet = True
    
    def getGUIAcceuil(self):
        if self.__themeSet == True :
            return self.__lienAcceuil
    
    def getGUIMain(self):
        if self.__themeSet == True :
            return self.__lienMain
       
    def getGUIMute(self):
        if self.__themeSet == True :
            return self.__lienMute

    def getGUIparoleBigSmall(self):
        if self.__themeSet == True :
            return self.__lienParole[0]

    def getGUIparoleSmallSmall(self):
        if self.__themeSet == True :
            return self.__lienParole[1]
             
    def getGUItextColor(self):
        if self.__themeSet == True:
            return self.__colorText
        
    def getGUIAttent(self):
        if self.__themeSet == True :
            return [self.__lienAttent[0],self.__lienAttent[1],self.__lienAttent[2]]
    
    def getGUINoConnecte(self):
        if self.__themeSet == True :
            return self.__lienNoConnecte
    
    def getColorInterface(self):
        if self.__themeSet == True :
            return self.__colorInterface
    
    def getColorLabel(self):
        if self.__themeSet == True :
            return self.__colorLabel
    
    def getColorTextActu(self):
        if self.__themeSet == True :
            return self.__colorTextActu
    
    def setColorThemePara(self):
        if self.__themeSet == True :
            filePara = jsonWork("setting/configSetting.json")
            filePara.EcritureJSON("color1",self.__color1Para)
            filePara.EcritureJSON("color1",self.__color2Para)