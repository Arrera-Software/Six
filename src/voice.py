import os
import time
from gtts import gTTS
from playsound import playsound
import pygame
from  pygame.locals import *
from src.varInterface import*


def speak(text,root):#Fonction de parole
    root.blit(fondParole2.convert(),(0,0))
    pygame.display.update()
    police = pygame.font.SysFont("arial", 15)
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    root.blit(fondParole1.convert(),(0,0))
    pygame.display.update()
    time.sleep(0.5)
    labelAssistant = police.render(text,1,(ColorText))
    text_rect = labelAssistant.get_rect(center=(rootWidht/2 ,55))
    root.blit(fondParole3.convert(),(0,0))
    root.blit(labelAssistant,text_rect)
    pygame.display.update()
    playsound("voc.mp3")
    os.remove("voc.mp3")
    root.blit(fond.convert(),(0,0))
    pygame.display.update()