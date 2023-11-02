import pygame 
from gtts import gTTS
import os

def sixParole(texte:str):
    tts = gTTS(texte, lang="fr")
    pygame.mixer.init()
    tts.save("voc.mp3")
    pygame.mixer.music.load("voc.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    os.remove("voc.mp3")

def playsound(file:str):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()