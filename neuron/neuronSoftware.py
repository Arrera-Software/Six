from software.YoutubeDownload import *
from src.srcSix import*
from objet.Calcule.calcule import *
from function.openSofware import*
from function.fenetrePygame import*
class neuroneSoftware:
    def __init__(self,name,root,UserCourt,GenreCourt,police):
        self.root = root
        self.police = police
        self.fenetre = pygameFond(root,police,GenreCourt)
        self.sourceSIX = SIXsrc(root,police)
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt
        
    def neurone(self,var):
        var = str(var)
        if "enregistre de la musique" in var or "enregistrement de la musique" in var or "enregistre moi des vidéos" in var or "enregistre-moi une vidéo" in var:
            self.fenetre.OuvertureTK("Ok "+self.genre+" je vous ouvre le téléchargeur de video Youtube.")
            ArreraVideoDownload("#3c0b10","white","#3c0b10","white")
            self.fenetre.FermetureTK()
            return 1
        else :
            if "ouvre l'explorateur de fichier" in var or "ouvre les fichiers" in var or "montre-moi mes fichiers" in var :
                self.sourceSIX.speak("ok je vous ouvre l'explorateur de fichier ")
                os.popen("start explorer")
                return 1
            else :
                if "calcul" in var or "calculer" in var :
                    self.fenetre.OuvertureTK("Je vous ouvre ma calculatrice")
                    Calcule("#3c0f14","white","Six : Calcule")
                    self.fenetre.FermetureTK()
                    return 1
                else :
                    if "ouvre mes notes" in var or "ouvre les notes" in var or "ouvre-moi mes notes" in var :
                        navigateur = lectureJSON("setting/config.json","appNote")
                        if navigateur == "":
                            self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                        else :
                            self.sourceSIX.speak("Ok je vous vos notes "+self.genre+" "+self.user)
                            openSoftware(navigateur)
                        return 1
                    else :
                        if "ouvre-moi mon navigateur internet" in var or "navigateur internet" in var or "navigateur" in var :
                            navigateur = lectureJSON("setting/config.json","navigateurInternet")
                            if navigateur == "":
                                self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                            else :
                                self.sourceSIX.speak("Ok je vous votre navigateur "+self.genre+" "+self.user)
                                openSoftware(navigateur)
                            return 1
                        else :
                            if "lance de la musique" in var or "application musique" in var :
                                navigateur = lectureJSON("setting/config.json","appMusique")
                                if navigateur == "":
                                    self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                                else :
                                    self.sourceSIX.speak("Ok je vous votre application de musique "+self.genre+" "+self.user)
                                    openSoftware(navigateur)
                                return 1
                            else : 
                                if "powerpoint" in var or "éditeur de diaporama" in var :
                                    navigateur = lectureJSON("setting/config.json","editeurpresentation")
                                    if navigateur == "":
                                        self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                                    else :
                                        self.sourceSIX.speak("Ok je vous votre éditeur de présentation "+self.genre+" "+self.user)
                                        openSoftware(navigateur)
                                    return 1
                                else :
                                    if "traitement de texte" in var or "word" in var :
                                        navigateur = lectureJSON("setting/config.json","editeurtexte")
                                        if navigateur == "":
                                            self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                                        else :
                                            self.sourceSIX.speak("Ok je vous votre traitement de texte "+self.genre+" "+self.user)
                                            openSoftware(navigateur)
                                        return 1
                                    else :
                                        if "tableur" in var or "exel" in var :
                                            navigateur = lectureJSON("setting/config.json","tableur")
                                            if navigateur == "":
                                                self.sourceSIX.speak("Vous n'avez pas dit ou se trouve votre racourcie "+self.genre)
                                            else :
                                                self.sourceSIX.speak("Ok je vous votre tableur "+self.genre+" "+self.user)
                                                openSoftware(navigateur)
                                            return 1
                                        else :
                                            return 0
                    