import speech_recognition as sr
from unidecode import*
import time
import pygame as p
from src.pygamePlaysound import*
from gtts import gTTS
import os
from src.SIXGestion import*
import threading as th


class SIXsrc :
    def __init__(self,sixAssistant:jsonWork):
        self.configSix=sixAssistant
       

    def speak(self,texte:str):
        tts = gTTS(texte, lang="fr")
        p.mixer.init()
        tts.save("voc.mp3")
        p.mixer.music.load("voc.mp3")
        p.mixer.music.play()
        while p.mixer.music.get_busy():
            p.time.Clock().tick(10)
        p.mixer.quit()
        os.remove("voc.mp3")
        
    
    def micro(self):
        valeur = self.configSix.lectureJSON("soundMicro")
        objetReconnaissance = sr.Recognizer()
        with sr.Microphone() as micro:
            if valeur == "1" :
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