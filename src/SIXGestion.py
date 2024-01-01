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
        #Nom fichier image
        self.__fileNameAcceuil = "acceuil.png"#
        self.__fileNameTriste1 = "triste1.png"#
        self.__fileNameTriste2 = "triste2.png"#
        self.__fileNameSurprit = "sureprit.png"#
        self.__fileNameMute1 = "mute1.png"#
        self.__fileNameMute2 = "mute2.png"#
        self.__fileNameNoConnecte = "noConnect.png"#
        self.__fileNameParole1 = "parole1.png"#
        self.__fileNameParole2 = "parole2.png"#
        self.__fileNameParole3 = "parole3.png"
        self.__fileNameBoot0 = "boot0.png"
        self.__fileNameBoot1 = "boot1.png"
        self.__fileNameBoot2 = "boot2.png"
        self.__fileNameBoot3 = "boot3.png"
        self.__fileNameColere = "colere.png"
        self.__fileNameContent = "content.png"
        self.__fileNameActu =  "actu.png"
        self.__fileNameMicro = "micro.png"
        #Color label
        self.__listColorLabelSix = ["#2b3ceb","#ffffff"]
        self.__listColorTextParole = ["#ffffff","#000000"]
        self.__colorTextLabelUser =  "#ffffff"
        self.__colorLabelUser = "#09179c"
        self.__listColorTextActu = ["#000000","#ffffff"]
        self.__listColorGUI = ["#ebecee","#000000"]
        self.__listColorTextActu = ["#000000","#ffffff"]
        #listUtiliser
        self.__emplacementAcceuil = str
        self.__emplacementMute1 = str
        self.__emplacementMute2 = str
        self.__emplacementTrite1 = str
        self.__emplacementTrite2 = str
        self.__emplacementSurprit = str
        self.__emplacementNoConnect = str
        self.__emplacementParole1 =  str
        self.__emplacementParole2 = str
        self.__emplacementParole3 = str
        self.__emplacementBoot0 = str
        self.__emplacementBoot1 = str
        self.__emplacementBoot2 = str
        self.__emplacementBoot3 = str
        self.__emplacementColere = str
        self.__emplacementContent = str
        self.__emplacementActu = str
        self.__emplacementMicro = str
        self.__colorGUI = str
        self.__colorTexteActu = str
        self.__colorLabelSix = str
        self.__colorTextParole = str
        self.__colorTextActu = str
        self.__colorPara = str
        #Creation var de verification
        self.__themeSet = bool
        #Ouverture fichier config Six
        self.__fileSixConfig = file
    
    def getEtatInternet(self):
        return self.__etatConnexion
       
    def setTheme(self):
        varTheme = self.__fileSixConfig.lectureJSON("theme") #Valeur possible "white" et "dark"
        emplacementGUI  = "asset/IMGinterface/"
        #Non de fichier Image
        if varTheme == "white" :
            chemin = emplacementGUI+"white/"
            self.__emplacementAcceuil = chemin+self.__fileNameAcceuil
            self.__emplacementMute1 = chemin+self.__fileNameMute1
            self.__emplacementMute2 = chemin+self.__fileNameMute2
            self.__emplacementTrite1 = chemin+self.__fileNameTriste1
            self.__emplacementTrite2 = chemin+self.__fileNameTriste2
            self.__emplacementSurprit = chemin+self.__fileNameSurprit
            self.__emplacementNoConnect = chemin+self.__fileNameNoConnecte
            self.__emplacementParole1 =  chemin+self.__fileNameParole1
            self.__emplacementParole2 = chemin+self.__fileNameParole2
            self.__emplacementParole3 = chemin+self.__fileNameParole3
            self.__emplacementBoot0 = chemin+self.__fileNameBoot0
            self.__emplacementBoot1 = chemin+self.__fileNameBoot1
            self.__emplacementBoot2 = chemin+self.__fileNameBoot2
            self.__emplacementBoot3 = chemin+self.__fileNameBoot3
            self.__emplacementColere = chemin+self.__fileNameColere
            self.__emplacementContent = chemin+self.__fileNameContent
            self.__emplacementActu = chemin+self.__fileNameActu
            self.__emplacementMicro = chemin+self.__fileNameMicro
            self.__colorTexteActu = self.__listColorTextActu[0]
            self.__colorTextParole = self.__listColorTextParole[0]
            self.__colorLabelSix = self.__listColorLabelSix[0]
            self.__colorGUI = self.__listColorGUI[0]
            self.__colorTextActu = self.__listColorTextActu[0]
            self.__colorPara = "light"
        else :
            if varTheme == "dark" :
                chemin = emplacementGUI+"dark/"
                self.__emplacementAcceuil = chemin+self.__fileNameAcceuil
                self.__emplacementMute1 = chemin+self.__fileNameMute1
                self.__emplacementMute2 = chemin+self.__fileNameMute2
                self.__emplacementTrite1 = chemin+self.__fileNameTriste1
                self.__emplacementTrite2 = chemin+self.__fileNameTriste2
                self.__emplacementSurprit = chemin+self.__fileNameSurprit
                self.__emplacementNoConnect = chemin+self.__fileNameNoConnecte
                self.__emplacementParole1 =  chemin+self.__fileNameParole1
                self.__emplacementParole2 = chemin+self.__fileNameParole2
                self.__emplacementParole3 = chemin+self.__fileNameParole3
                self.__emplacementBoot0 = chemin+self.__fileNameBoot0
                self.__emplacementBoot1 = chemin+self.__fileNameBoot1
                self.__emplacementBoot2 = chemin+self.__fileNameBoot2
                self.__emplacementBoot3 = chemin+self.__fileNameBoot3
                self.__emplacementColere = chemin+self.__fileNameColere
                self.__emplacementContent = chemin+self.__fileNameContent
                self.__emplacementActu = chemin+self.__fileNameActu
                self.__emplacementMicro = chemin+self.__fileNameMicro
                self.__colorTexteActu = self.__listColorTextActu[1]
                self.__colorTextParole = self.__listColorTextParole[1]
                self.__colorLabelSix = self.__listColorLabelSix[1]
                self.__colorGUI = self.__listColorGUI[1]
                self.__colorTextActu = self.__listColorTextActu[1]
                self.__colorPara = "dark"
            else :
                chemin = emplacementGUI+"white/"
                self.__emplacementAcceuil = chemin+self.__fileNameAcceuil
                self.__emplacementMute1 = chemin+self.__fileNameMute1
                self.__emplacementMute2 = chemin+self.__fileNameMute2
                self.__emplacementTrite1 = chemin+self.__fileNameTriste1
                self.__emplacementTrite2 = chemin+self.__fileNameTriste2
                self.__emplacementSurprit = chemin+self.__fileNameSurprit
                self.__emplacementNoConnect = chemin+self.__fileNameNoConnecte
                self.__emplacementParole1 =  chemin+self.__fileNameParole1
                self.__emplacementParole2 = chemin+self.__fileNameParole2
                self.__emplacementParole3 = chemin+self.__fileNameParole3
                self.__emplacementBoot0 = chemin+self.__fileNameBoot0
                self.__emplacementBoot1 = chemin+self.__fileNameBoot1
                self.__emplacementBoot2 = chemin+self.__fileNameBoot2
                self.__emplacementBoot3 = chemin+self.__fileNameBoot3
                self.__emplacementColere = chemin+self.__fileNameColere
                self.__emplacementContent = chemin+self.__fileNameContent
                self.__emplacementActu = chemin+self.__fileNameActu
                self.__emplacementMicro = chemin+self.__fileNameMicro
                self.__colorTexteActu = self.__listColorTextActu[0]
                self.__colorTextParole = self.__listColorTextParole[0]
                self.__colorLabelSix = self.__listColorLabelSix[0]
                self.__colorGUI = self.__listColorGUI[0]
                self.__colorTextActu = self.__listColorTextActu[0]
                self.__colorPara = "light"
        self.__themeSet = True

    
    def getGUIAcceuil(self):
        if self.__themeSet == True :
            return self.__emplacementAcceuil
    
    def getGUISurprit(self):
        if self.__themeSet == True :
            return self.__emplacementSurprit
       
    def getGUIMute1(self):
        if self.__themeSet == True :
            return self.__emplacementMute1
    
    def getGUIMute2(self):
        if self.__themeSet == True :
            return self.__emplacementMute2

    def getGUITrite1(self):
        if self.__themeSet == True :
            return self.__emplacementTrite1
    
    def getGUITrite2(self):
        if self.__themeSet == True :
            return self.__emplacementTrite2
    
    def getGUINoConnecte(self):
        if self.__themeSet == True :
            return self.__emplacementNoConnect
    
    def getGUIParole1(self):
        if self.__themeSet == True :
            return self.__emplacementParole1
    
    def getGUIParole2(self):
        if self.__themeSet == True :
            return self.__emplacementParole2
        
    def getGUIParole3(self):
        if self.__themeSet == True :
            return self.__emplacementParole3
    
    def getGUIBoot0(self):
        if self.__themeSet == True :
            return self.__emplacementBoot0

    def getGUIBoot1(self):
        if self.__themeSet == True :
            return self.__emplacementBoot1
    
    def getGUIBoot2(self):
        if self.__themeSet == True :
            return self.__emplacementBoot2
    
    def getGUIBoot3(self):
        if self.__themeSet == True :
            return self.__emplacementBoot3
    
    def getGUIColere(self):
        if self.__themeSet == True :
            return self.__emplacementColere
    
    def getGUIContent(self):
        if self.__themeSet == True :
            return self.__emplacementContent
    
    def getIconMicro(self):
        if self.__themeSet == True :
            return self.__emplacementMicro

    def getGUIActu(self):
        if self.__themeSet == True :
            return self.__emplacementActu 
    
    def getTexteColorParole(self):
        if self.__themeSet == True :
            return self.__colorTextParole
    
    def getTexteColorActu(self):
        if self.__themeSet == True :
            return self.__colorTexteActu
    
    def getColorLabelParole(self):
        if self.__themeSet == True :
            return self.__colorLabelSix
    
    def getColorLabelUser(self):
        if self.__themeSet == True :
            return self.__colorLabelUser
    
    def getColorGUI(self):
        if self.__themeSet == True :
            return self.__colorGUI
    
    def getColorTextActu(self):
        if self.__themeSet == True :
            return self.__colorTextActu
    
    def getThemePara(self):
        if self.__themeSet == True :
            return self.__colorPara

    def getcolorTextLabelUser(self):
        if self.__themeSet == True :
            return self.__colorTextLabelUser