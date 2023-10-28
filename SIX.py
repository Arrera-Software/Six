from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from src.sixInterface import*
from src.SIXGestion import*
from setting.SixSetting import *
import threading as th


class AssistantSIX :
    def __init__(self):
        #objet
        self.objetGestion = SIXGestion()
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.parametre = SIXSetting()  
        #mise en place du theme
        self.objetGestion.setTheme()
        #varriable
        self.etatInternet = self.objetGestion.getEtatInternet()
        self.varSix = 0
        #objet interface
        self.interafaceSIX = SIXInterface(self.objetGestion)
        #source six 
        self.srcSIX = SIXsrc(self.interafaceSIX)
        
        
    def assistant(self):
        self.interafaceSIX.initialisationFenetre()
        self.srcSIX.booting(self.arreraAssistant.boot())
        while (self.varSix != 15 ):
            statement = self.srcSIX.micro()
            self.varSix,text = self.arreraAssistant.neuron(statement)
            if self.varSix == 0 and "parametre" in statement :
                self.srcSIX.speak("Ok je vous ouvre les parametre")
                self.parametre.active()
            else :
                self.srcSIX.speak(text)
            
        