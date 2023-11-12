from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from src.SIXGestion import*
from src.SixTK import *
import threading as th

MAXNOTING = 5 
class AssistantSIX :
    def __init__(self):
        #objet
        sixConfig = jsonWork("sixConfig.json")
        self.objetGestion = SIXGestion(sixConfig)
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.sixTK = sixTk(self.objetGestion)
        self.compteurNothing = 0
        #mise en place du theme
        self.objetGestion.setTheme()
        #varriable
        self.etatInternet = self.objetGestion.getEtatInternet()
        self.varSix = 0
        #source six 
        self.srcSIX = SIXsrc(sixConfig)
        #fenetreTkinter       
        self.windows = Tk()
        self.windows.title("Six : Assistant  ")
        self.windows.geometry("500x500+5+30")
        self.windows.overrideredirect(True)

    def bootAssistant(self):
        self.root.mainloop()


    def _assistant(self):
        self.srcSIX.speak(self.arreraAssistant.boot())
        while (self.varSix != 15 ):
            statement = self.srcSIX.micro()
            if ("mute" in statement) or (self.compteurNothing>=MAXNOTING):
                if (self.compteurNothing==MAXNOTING):
                    self.srcSIX.speak("Je me met en pause appeler moi si vous avez besoin de moi")
                else :
                    self.srcSIX.speak("Ok je vous laisse tranquille")
                self.varSix = self.sixTK.muteSix()
                if (self.varSix ==15):
                    self.srcSIX.speak("Au revoir")
                else :
                    self.srcSIX.speak("Je vous ecoute monsieur")
                self.compteurNothing = 0
            else :
                if (statement=="nothing"):
                    self.compteurNothing = self.compteurNothing + 1
    
                else :
                    self.varSix,text = self.arreraAssistant.neuron(statement)
                    if self.varSix == 0 and "parametre" in statement :
                        self.srcSIX.speak("Ok je vous ouvre les parametre")
                        self.sixTK.activePara()
                        self.objetGestion.setTheme()
                        self.interafaceSIX.setGUI()
                        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                        self.srcSIX.speak("Les modification on bien été pris en compte")
                        self.srcSIX.speak("Ok je vous ouvre les parametre")
                    else :
                        self.srcSIX.speak(text)
                        self.compteurNothing = 0 