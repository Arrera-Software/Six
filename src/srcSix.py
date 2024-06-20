import speech_recognition as sr
from unidecode import*
from src.pygamePlaysound import*
from librairy.travailJSON import*
import threading as th


class SIXsrc :
    def __init__(self,sixAssistant:jsonWork):
        self.__configSix=sixAssistant
       

    def speak(self,texte:str):
        paroleSix(texte)
        
    
    def micro(self):
        valeur = self.__configSix.lectureJSON("soundMicro")
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
            return requette