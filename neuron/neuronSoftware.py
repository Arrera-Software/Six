from software.YoutubeDownlaod import *
from src.srcSix import*
from objet.Calcule.calcule import *

def Software(var,genre,user,name,root,police):
    if "enregistre de la musique" in var or "enregistrement de la musique" in var or "enregistre moi des vidéos" in var or "enregistre-moi une vidéo" in var:
        SIXsrc(root,police).speak("Ok "+genre+" je vous ouvre le téléchargeur de video Youtube.")
        YoutubeDownload()
        return 1
    else :
        if "ouvre l'explorateur de fichier" in var or "ouvre les fichiers" in var or "montre-moi mes fichiers" in var :
            SIXsrc(root,police).speak("ok je vous ouvre l'explorateur de fichier ")
            os.popen("start explorer")
            return 1
        else :
            if "calcul" in var or "calculer" in var :
                SIXsrc(root,police).speak("Je vous ouvre ma calculatrice")
                Calcule("#3c0f14","white","Six : Calcule")
                return 1
            else :
                return 0
                    