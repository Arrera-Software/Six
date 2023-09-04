from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from unidecode import unidecode
from src.SIXGestion import*
import threading

class AssistantSIX :
    def __init__(self):
        #objet
        self.objetGestion = SIXGestion()
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")      
        self.srcSIX = SIXsrc(self.objetGestion)
        #theard
        self.theardMicro = threading.Event()
        #Varriable
        self.etatInternet = self.objetGestion.getEtatInternet()
        self.varSix = 0
        
        
    def _assistant(self):
        self.srcSIX.speak(self.arreraAssistant.boot())
        while self.varSix != 15 :
            statement =self.srcSIX.Micro()
            statement = unidecode(statement)
            print(statement)
            self.varSix,text = self.arreraAssistant.neuron(statement)
            self.srcSIX.speak(text)
            
    def bootAssistant(self):
        theardAssistant = threading.Thread(target=self._assistant())
        theardAssistant.start()        