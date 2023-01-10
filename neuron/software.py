from software.YoutubeDownlaod import *
from src.voice import*
from objet.Calcule.calcule import *
from function.temps import*

def Software(var,genre,user,name,root,police):
    if "enregistre de la musique" in var or "enregistrement de la musique" in var or "enregistre moi des vidéos" in var or "enregistre-moi une vidéo" in var:
        speak("Ok "+genre+" je vous ouvre le téléchargeur de video Youtube.",root)
        YoutubeDownload()
        return 1
    else :
        if "ouvre l'explorateur de fichier" in var or "ouvre les fichiers" in var or "montre-moi mes fichiers" in var :
            speak("ok je vous ouvre l'explorateur de fichier "+var+".",root)
            os.popen("start explorer")
            return 1
        else :
            if "calcul" in var or "calculer" in var :
                speak("Je vous ouvre ma calculatrice",root)
                Calcule("#3c0f14","white","Six : Calcule")
                return 1
            else :
                if "minuteur" in var :
                    speak("Je vous lance l'application de minuteur "+genre,root)
                    Minuteur()
                    return 1
                else : 
                    if "chronomètre" in var :
                        speak("Je vous lance l'application de chronomètre "+genre,root)
                        Chrono()
                        return 1
                    else :
                        return 0
                    