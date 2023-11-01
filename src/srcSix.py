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
            playsound("asset/Sound/bootMicro.mp3")
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
    
    def trigerWord(self):
        theardGUIMain = th.Thread(target=self.interface.interfaceMain)
        theardGUIMain.start()
        theardGUIMain.join()
        micro = sr.Recognizer()
        theardGUI = th.Thread(target=self.interface.interfaceAttente)
        with sr.Microphone() as source:
            audio = micro.listen(source)
        try:
            microOut = micro.recognize_google(audio)
            print(microOut)
            if "6" in microOut or "dit" in microOut:
                return True
            else :
                theardGUI.start()
                theardGUI.join()
                return False
        except sr.UnknownValueError:
            return False
        

        
    def openParametre(self,texte:str):
        tts = gTTS(texte, lang="fr")
        theardParole = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
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
        theardParole = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
        tts.save("voc.mp3")
        theardParole.start()
        playsound("voc.mp3")
        theardParole.join()
        os.remove("voc.mp3")

    def activeMute(self,texte)->int:
        tts = gTTS(texte, lang="fr")
        theardParole = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
        tts.save("voc.mp3")
        theardParole.start()
        playsound("voc.mp3")
        theardParole.join()
        os.remove("voc.mp3")
        self.interface.quitWindows()

    def quitMute(self,var:int,texte:str):
        tts = gTTS(texte, lang="fr")
        tts.save("voc.mp3")
        if var == 15 :
            playsound("voc.mp3")
            os.remove("voc.mp3")
        else :
            self.interface.initialisationFenetre()
            theardParole = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
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