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
        self.interafaceSIX.setGUI()
        #source six 
        self.srcSIX = SIXsrc(self.interafaceSIX)
        
        
    def assistant(self):
        self.interafaceSIX.initialisationFenetre()
        self.srcSIX.booting(self.arreraAssistant.boot())
        while (self.varSix != 15 ):
            statement = self.srcSIX.micro()
            self.varSix,text = self.arreraAssistant.neuron(statement)
            if self.varSix == 0 and "parametre" in statement :
                self.srcSIX.openParametre("Ok je vous ouvre les parametre")
                self.parametre.active()
                self.objetGestion.setTheme()
                self.interafaceSIX.setGUI()
                self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                self.srcSIX.closeParametre("Les modification on bien été pris en compte")
                self.arreraAssistant.sortieParametre("Ok je vous ouvre les parametre","parametre")
            else :
                self.srcSIX.speak(text)
            
        