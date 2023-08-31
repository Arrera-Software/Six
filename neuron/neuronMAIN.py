from src.srcSix import *
from function.reading import*
from function.fenetrePygame import *
from function.openSofware import ouvertureAide 
import random
import datetime

class neuroneMain :
    def __init__(self,name,root,UserCourt,GenreCourt,police):
        self.root = root
        self.police = police
        self.fenetre = pygameFond(root,police,GenreCourt)
        self.sourceSIX = SIXsrc(root,police)
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt
        
    def neurone(self,var):
        self.var = str(var)
        if "peux-tu me lire un truc" in self.var :
            self.fenetre.OuvertureTK("Copier ce que vous voulez  que je vous lise")
            Reading(self.root,self.police)
            self.fenetre.FermetureTK()
            return 1
        else :
            if "ouvre-moi la page d'aide" in self.var :
                self.sourceSIX.speak("Ok je vous ouvre la page d'aide")
                ouvertureAide()
                return 1
            else :
                if "stop" in var or "bye" in var or "au revoir" in var or "tu peux t'arrêter" in var : 
                    hour=datetime.datetime.now().hour
                    if hour>=0 and hour<3:
                        self.sourceSIX.speak("Au revoir" +self.genre+" "+self.user+" ,bonne nuit")
                    else :
                        if hour>=4 and hour<9:
                            self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" ,passez une bonne matinée")
                        else :
                            if hour>=10 and hour<12:
                                self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" ,passez une bonne journée")
                            else : 
                                if hour>=13 and hour<16:
                                    self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" ,passez une bonne aprem")
                                else :
                                    if hour>=17 and hour <18:
                                        self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" ,passez une bonne fin d'aprés-midi")
                                    else :
                                        if hour>=19 and hour<22:
                                            self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" ,passez une bonne soirée")
                                        else :
                                            self.sourceSIX.speak("Au revoir "+self.genre+" "+self.user+" , passez une bonne nuit.")
                    return 15
                else :
                    return 0                                  