import os
import pygame
from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from unidecode import unidecode
from src.SIXGestion import*


class AssistantSIX :
    def __init__(self):
        #objet
        self.objetGestion = SIXGestion()
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")      
        #mise en place du theme
        self.objetGestion.setTheme()
        #varriable
        self.fond = self.objetGestion.getGUIMain()
        self.etatInternet = self.objetGestion.getEtatInternet()
        self.varSix = 0
        #Fenetre pygame
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
        pygame.init()
        pygame.display.set_icon(pygame.image.load("asset/logo.png"))
        pygame.display.set_caption("Assistant SIX")
        self.root  = pygame.display.set_mode((600,200),pygame.NOFRAME)
        self.police = pygame.font.SysFont("arial", 25)
        self.root.blit(self.fond.convert(),(0,0))
        pygame.display.update()
        #source six 
        self.srcSIX = SIXsrc(self.root,self.police,self.objetGestion)
        
    def assistant(self):
        self.srcSIX.speak(self.arreraAssistant.boot())
        while self.varSix != 15 :
            statement = self.srcSIX.micro()
            statement = unidecode(statement)
            print(statement)
            self.varSix,text = self.arreraAssistant.neuron(statement)
            self.srcSIX.speak(text)
        