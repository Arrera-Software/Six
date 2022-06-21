from gtts import gTTS
from io import BytesIO
import os

def parole(text):
    tts = gTTS(text, lang="fr")
    tts.save("voc.mp3")
    os.system("mpg123 " + "voc.mp3")

def lecture(fichier):
    os.system("mpg123 " + fichier)