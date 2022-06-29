from gtts import gTTS
import os
import datetime
import random
import speech_recognition as sr

nrad = random.randint(1,2)

def speak(text):
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")
def speakNoInternet():
    os.system("mpg123 " + "sons/speak1.mp3")

def salutation():
    hour=datetime.datetime.now().hour
    if hour>= 0 and hour<13:
        if nrad == 1 :
            speak("Boujour monsieur,Je vous souhaite une bonne matinée")
        if nrad == 2 :
            speak("Boujour monsieur,Je vous souhaite un bon début de journée")
    if hour>=13 and hour<20:
        if nrad == 1 :
            speak("Bonjour monsieur,Je vous souhaite une bonne aprem")
        if nrad == 2 :
            speak("Bonjour monsieur,Je vous souhaite une bonne après-midi")
    else :
        speak("Bonsoir monsieur")

def Arret():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<20:
       speak("Au revoir monsieur")
    if hour>=13 and hour<20:
        speak("Au revoir monsieur , bonne nuit")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

        try:
            Requette=r.recognize_google(audio,language='fr')

        except Exception as e:
            speak("Desoler Monsieur mais je n'ai pas compris votre requette")
            return "None"
        return Requette
    
