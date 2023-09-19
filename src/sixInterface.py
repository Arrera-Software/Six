import os 
import pygame 
import time as t
from src.SIXGestion import*


class SIXInterface:
    def __init__(self,objetGestion:SIXGestion):
        self.rootWidht = 600
        self.rootHeight = 200
        self.fond = objetGestion.getGUIMain()
        self.mainFond = objetGestion.getGUIMain()
        self.listFondParole = [objetGestion.getGUIparole1(),
                               objetGestion.getGUIparole2(),
                               objetGestion.getGUIparole3()]
        self.colorText = objetGestion.getGUItextColor()
        
        
    def initialisationFenetre(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
        pygame.init()
        pygame.display.set_icon(pygame.image.load("asset/logo.png"))
        pygame.display.set_caption("Assistant SIX")
        self.root  = pygame.display.set_mode((self.rootWidht,self.rootHeight),pygame.NOFRAME)
        self.police = pygame.font.SysFont("arial", 25)
        self.root.blit(self.fond.convert(),(0,0))
        self.formatSpeak = pygame.font.SysFont("arial", 20)
        pygame.display.update()
        
    def interfaceSpeak(self,text1:str,text2:str,text3:str):
        texte1 = text1
        texte2 = text2
        texte3 = text3
        self.root.blit(self.listFondParole[1].convert(),(0,0))
        pygame.display.update()
        t.sleep(1)
        labelAssistant1 = self.formatSpeak.render(texte1,1,(self.colorText))
        labelAssistant2 = self.formatSpeak.render(texte2,1,(self.colorText))
        labelAssistant3 = self.formatSpeak.render(texte3,1,(self.colorText))
        textRect1 = labelAssistant1.get_rect(center=(600/2 ,55))
        textRect2 = labelAssistant2.get_rect(center=(600/2 ,75))
        textRect3 = labelAssistant3.get_rect(center=(600/2 ,95))
        self.root.blit(self.listFondParole[2].convert(),(0,0))
        self.root.blit(labelAssistant1,textRect1)
        pygame.display.update()
        t.sleep(1)
        self.root.blit(self.listFondParole[0].convert(),(0,0))
        self.root.blit(labelAssistant2,textRect2)
        pygame.display.update()
        t.sleep(1)
        self.root.blit(labelAssistant3,textRect3)
        self.root.blit(self.listFondParole[1].convert(),(0,0))
        pygame.display.update()
        t.sleep(1)
        self.root.blit(self.mainFond.convert(),(0,0))
        pygame.display.update()
        
    def interfaceMicro(self,requette):
        print(requette)
        self.root.blit(self.mainFond.convert(),(0,0))
        pygame.display.update()
        t.sleep(1)
        labelUser = self.police.render(requette,1,(self.colorText))
        text_rect = labelUser.get_rect(center=(self.rootWidht/2 ,self.rootHeight/2))
        self.root.blit(labelUser,text_rect)
        pygame.display.update()
        t.sleep(1)
        
    