import speech_recognition as sr
import pygame
from  pygame.locals import *
import time
import os
from gtts import gTTS
from playsound import playsound
from unidecode import unidecode
from  pygame.locals import *
from src.SIXGestion import*
import threading as th
from src.sixInterface import*


class SIXsrc :
    def __init__(self,interface:SIXInterface):
        self.interface = interface

    def booting(self,texte:str):
        tts = gTTS(texte, lang="fr")
        theardGUI = th.Thread(target=self.interface.interfaceBoot,args=(texte,))
        tts.save("voc.mp3")
        theardGUI.start()
        playsound("voc.mp3")
        theardGUI.join()
        os.remove("voc.mp3")

    def speak(self,texte:str):
        tts = gTTS(texte, lang="fr")
        theardGUI = th.Thread(target=self.interface.interfaceSpeak,args=(texte,))        
        tts.save("voc.mp3")
        theardGUI.start()
        playsound("voc.mp3")
        theardGUI.join()
        os.remove("voc.mp3")
    
    def micro(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                requette = unidecode(r.recognize_google(audio, language='fr'))
            except sr.WaitTimeoutError as e:
                #print("Erreur : La reconnaissance vocale a expiré. Vérifiez votre microphone.")
                requette = "None"
            except sr.RequestError as e:
                #print(f"Erreur : Impossible de faire la demande : {e}")
                requette = "None"
            except sr.UnknownValueError:
                #print("Erreur : Aucune parole reconnue.")
                requette = "None"
            self.interface.saveValMicro(requette)
            return requette
        
    def openParametre(self,texte:str):
        tts = gTTS(texte, lang="fr")
        theardParole = th.Thread(target=self.interface.interfaceCloseOpenParametre,args=(texte,))
        tts.save("voc.mp3")
        theardParole.start()
        playsound("voc.mp3")
        theardParole.join()
        os.remove("voc.mp3")
        time.sleep(0.5)
        self.interface.quitWindows()

    def closeParametre(self,texte):
        tts = gTTS(texte, lang="fr")
        self.interface.initialisationFenetre()
        theardParole = th.Thread(target=self.interface.interfaceCloseOpenParametre,args=(texte,))
        tts.save("voc.mp3")
        theardParole.start()
        playsound("voc.mp3")
        theardParole.join()
        os.remove("voc.mp3")

    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))