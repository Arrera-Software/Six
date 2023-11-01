from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from src.sixInterface import*
from src.SIXGestion import*
from src.SixTK import *
import threading as th

MAXNOTING = 5 
class AssistantSIX :
    def __init__(self):
        #objet
        self.objetGestion = SIXGestion()
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.sixTK = sixTk(self.objetGestion)
        self.compteurNothing = 0
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
            print(self.compteurNothing)
            statement = self.srcSIX.micro()
            if ("mute" in statement) or (self.compteurNothing>=MAXNOTING):
                if (self.compteurNothing==MAXNOTING):
                    self.srcSIX.activeMute("Je me met une pause appeler moi si vous a besoin de moi")
                else :
                    self.srcSIX.activeMute("Ok je vous laisse tranquille")
                self.varSix = self.sixTK.muteSix()
                if (self.varSix ==15):
                    self.srcSIX.quitMute(self.varSix,"Au revoir")
                else :
                    self.srcSIX.quitMute(self.varSix,"Je vous ecoute monsieur")
                self.compteurNothing = 0
            else :
                if (statement=="nothing"):
                    self.compteurNothing = self.compteurNothing + 1
                    self.srcSIX.attent()
                else :
                    self.varSix,text = self.arreraAssistant.neuron(statement)
                    if self.varSix == 0 and "parametre" in statement :
                        self.srcSIX.openParametre("Ok je vous ouvre les parametre")
                        self.sixTK.activePara()
                        self.objetGestion.setTheme()
                        self.interafaceSIX.setGUI()
                        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                        self.srcSIX.closeParametre("Les modification on bien été pris en compte")
                        self.arreraAssistant.sortieParametre("Ok je vous ouvre les parametre","parametre")
                    else :
                        self.srcSIX.speak(text)
                        self.compteurNothing = 0 