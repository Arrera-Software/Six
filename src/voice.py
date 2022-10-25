import os
from gtts import gTTS
from playsound import playsound

def speak(text):#Fonction de parole
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    playsound("voc.mp3")
    os.remove("voc.mp3")