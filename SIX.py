import os
import pygame
from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from unidecode import unidecode
from src.sixInterface import*
from src.SIXGestion import*


class AssistantSIX :
    def __init__(self):
        #objet
        self.objetGestion = SIXGestion()
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")      
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
        self.srcSIX.speak(self.arreraAssistant.boot())
        while (self.varSix != 15 ):
            statement = self.srcSIX.micro()
            statement = unidecode(statement)
            self.varSix,text = self.arreraAssistant.neuron(statement)
            
            self.srcSIX.speak(text)
        