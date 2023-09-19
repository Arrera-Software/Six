import speech_recognition as sr
import pygame
from  pygame.locals import *
import time
import os
from gtts import gTTS
from playsound import playsound
from  pygame.locals import *
from src.SIXGestion import*
import threading as th
from src.sixInterface import*


class SIXsrc :
    def __init__(self,interface:SIXInterface):
        self.interface = interface

    def speak(self,texte:str):
        tts = gTTS(texte, lang="fr")
        text1,text2 = self._division(texte,8)
        nbMots2 = self._compteur(text2)
        if (nbMots2 > 8):
            text2,text3 = self._division(text2,8)
        else :
            text3 = " "
        theardGUI = th.Thread(target=self.interface.interfaceSpeak,args=(text1,text2,text3))        
        tts.save("voc.mp3")
        theardGUI.start()
        playsound("voc.mp3")
        theardGUI.join()
        os.remove("voc.mp3")
    
    def micro(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                requette=r.recognize_google(audio,language='fr')
            except Exception as e:
                return "None"
            theardGUIMicro = th.Thread(target=self.interface.interfaceMicro,args=(requette,)) 
            theardGUIMicro.start()
            theardGUIMicro.join()
            return requette
    
    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))