import speech_recognition as sr
import pygame
from  pygame.locals import *
import time
from src.pygamePlaysound import*
from unidecode import unidecode
from  pygame.locals import *
from src.SIXGestion import*
import threading as th
from src.sixInterface import*


class SIXsrc :
    def __init__(self,interface:SIXInterface):
        self.interface = interface

    def booting(self,texte:str):
        theardGUI = th.Thread(target=self.interface.interfaceBoot,args=(texte,))
        theardParole = th.Thread(target=sixParole,args=(texte,))
        theardGUI.start()
        theardParole.start()
        theardGUI.join()
        theardParole.join()
       

    def speak(self,texte:str):
        theardGUI = th.Thread(target=self.interface.interfaceSpeak,args=(texte,))
        theardParole = th.Thread(target=sixParole,args=(texte,))        
        theardGUI.start()
        theardParole.start()
        theardGUI.join()
        theardParole.join()
        
    
    def micro(self):
        objetReconnaissance = sr.Recognizer()
        with sr.Microphone() as micro:
            playsound("asset/Sound/bootMicro.mp3")
            entrer = objetReconnaissance.listen(micro)
            try:
                requette = unidecode(objetReconnaissance.recognize_google(entrer, language='fr'))
            except sr.WaitTimeoutError as e:
                requette = "nothing"
            except sr.RequestError as e:
                requette = "nothing"
            except sr.UnknownValueError:
                requette = "nothing"
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
        theardGUI = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
        theardParole = th.Thread(target=sixParole,args=(texte,))
        theardGUI.start()
        theardParole.start()
        theardGUI.join()
        theardParole.join()
        time.sleep(0.5)
        self.interface.quitWindows()

    def closeParametre(self,texte):
        self.interface.initialisationFenetre()
        theardGUI = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
        theardParole = th.Thread(target=sixParole,args=(texte,))
        theardGUI.start()
        theardParole.start()
        theardGUI.join()
        theardParole.join()

    def activeMute(self,texte)->int:
        theardGUI = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
        theardParole = th.Thread(target=sixParole,args=(texte,))
        theardGUI.start()
        theardParole.start()
        theardGUI.join()
        theardParole.join()
        self.interface.quitWindows()

    def quitMute(self,var:int,texte:str):
        theardParole = th.Thread(target=sixParole,args=(texte,))
        if var == 15 :
           theardParole.start()
           theardParole.join()
        else :
            self.interface.initialisationFenetre()
            theardGUI = th.Thread(target=self.interface.interfaceCloseOpenTKInterface,args=(texte,))
            theardGUI.start()
            theardParole.start()
            theardGUI.join()
            theardParole.join()

    def attent(self):
        self.interface.interfaceAttente()
        pygame.display.update()
        

    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))