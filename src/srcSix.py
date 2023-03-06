import speech_recognition as sr
import pygame
from  pygame.locals import *
import time
import os
from gtts import gTTS
from playsound import playsound
from  pygame.locals import *
from src.varInterface import*


class SIXsrc :
    def __init__(self,root,police):
        self.rootWidht = 600
        self.rootHeight = 200
        self.fenetre = root
        self.formatText = police
        self.formatSpeak = pygame.font.SysFont("arial", 20)
        
    def speak(self,texte):
        self.fenetre.blit(fondParole2.convert(),(0,0))
        #text1,text2,text3 = ""
        pygame.display.update()
        tts = gTTS(texte, lang="fr")
        text1,text2 = self.division(texte,8)
        nbMots2 = self.compteur(text2)
        if (nbMots2 > 8):
            text2,text3 = self.division(text2,8)
        else :
            text3 = " "
        tts.save("voc.mp3")
        self.fenetre.blit(fondParole1.convert(),(0,0))
        pygame.display.update()
        time.sleep(0.5)
        labelAssistant1 = self.formatSpeak.render(text1,1,(ColorText))
        labelAssistant2 = self.formatSpeak.render(text2,1,(ColorText))
        labelAssistant3 = self.formatSpeak.render(text3,1,(ColorText))
        textRect1 = labelAssistant1.get_rect(center=(rootWidht/2 ,55))
        textRect2 = labelAssistant2.get_rect(center=(rootWidht/2 ,75))
        textRect3 = labelAssistant3.get_rect(center=(rootWidht/2 ,95))
        self.fenetre.blit(fondParole3.convert(),(0,0))
        self.fenetre.blit(labelAssistant1,textRect1)
        self.fenetre.blit(labelAssistant2,textRect2)
        self.fenetre.blit(labelAssistant3,textRect3)
        pygame.display.update()
        playsound("voc.mp3")
        os.remove("voc.mp3")
        self.fenetre.blit(fond.convert(),(0,0))
        pygame.display.update()
    
    def division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def compteur(self,s):
        mots = s.split()
        return int(len(mots))
    
    def micro(self):
        self.fenetre.blit(fond.convert(),(0,0))
        pygame.display.update()
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                Requette=r.recognize_google(audio,language='fr')
                #print(Requette)
                labelUser = self.formatText.render(Requette,1,(255,255,255))
                text_rect = labelUser.get_rect(center=(self.rootWidht/2 ,self.rootHeight/2))
                self.fenetre.blit(labelUser,text_rect)
                pygame.display.update()
            except Exception as e:
                return "None" 
            time.sleep(1)
            return Requette