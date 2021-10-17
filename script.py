#fichier pour creer les voix de l'assistant:

#imortation de module
from gtts import gTTS
from io import BytesIO

#demmande la phrase que l'uttilisateur veut enregister
print("Quelle phrase voulez-vous enregistrer")
phrase=input("Votre phrase :")

#transforamtion de la phrase en voix
tts = gTTS(phrase, lang='fr')
#choix du nom du fichier
fichier=input("Comment voulez-vous appellez ce fichier(ne pas oublier le .mp3): ")
#enregistrement du fichier
tts.save(fichier)
