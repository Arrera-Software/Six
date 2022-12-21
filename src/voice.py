import os
from gtts import gTTS
from playsound import playsound
import pygame
from  pygame.locals import *
fond = pygame.image.load("image/fondMain.png")
fondParole = pygame.image.load("image/fondParole.png")
rootWidht = 600
rootHeight = 200


def speak(text,root):#Fonction de parole
    police = pygame.font.SysFont("arial", 15)
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    root.blit(fondParole.convert(),(0,0))
    labelAssistant = police.render(text,1,(255,255,255))
    text_rect = labelAssistant.get_rect(center=(rootWidht/2 ,55))
    root.blit(labelAssistant,text_rect)
    pygame.display.update()
    playsound("voc.mp3")
    os.remove("voc.mp3")
    root.blit(fond.convert(),(0,0))
    pygame.display.update()