import speech_recognition as sr
import pygame
from  pygame.locals import *
fond = pygame.image.load("image/fondMain.png")
rootWidht = 600
rootHeight = 200
def takeCommand(root,police):#Fonction micro et reconaissance vocal
    root.blit(fond.convert(),(0,0))
    pygame.display.update()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            Requette=r.recognize_google(audio,language='fr')
            labelUser = police.render(Requette,1,(255,255,255))
            text_rect = labelUser.get_rect(center=(rootWidht/2 ,rootHeight/2))
            root.blit(labelUser,text_rect)
            pygame.display.update()
        except Exception as e:
            return "None" 
        return Requette