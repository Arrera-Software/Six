import datetime
from src.srcSix import*
from objet.Horloge.AppHorloge import*
from objet.date.objetdate import*
from function.calendar import *
from function.fenetrePygame import*

class neuronTime :
    def __init__(self,name,root,UserCourt,GenreCourt,police):
        self.root = root
        self.police = police
        self.fenetre = pygameFond(root,police,GenreCourt)
        self.sourceSIX = SIXsrc(root,police)
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt

    def neuron(self,var):
        self.fenetre = pygameFond(self.root,self.police,self.genre)
        self.sourceSIX = SIXsrc(self.root,self.police)
        var = str(var)
        if "heure" in var :
            hour = str(datetime.datetime.now().hour)
            minute = str(datetime.datetime.now().minute)
            self.sourceSIX.speak("Il es "+hour+" heure " +minute)
            return 1
        else : 
            if "date" in var :
                jour = dateToday().jour()
                mois = dateToday().moisSTR()
                annees = dateToday().annes()
                self.sourceSIX.speak("Aujourd'hui on es le "+jour+" "+mois+" "+annees)
                return 1
            else : 
                if "horloge" in var :
                    self.fenetre.OuvertureTK("Ok je vous ouvre l'application horloge "+self.genre+" "+self.user)
                    AppHorloge("#3c0f14","white","Six : Horloge","acceuil")
                    self.fenetre.FermetureTK()
                    return 1
                else :
                    if "chronomètre" in var or "chrono" in var :
                        self.fenetre.OuvertureTK("Ok je vous ouvre le chronomètre "+self.genre+" "+self.user)
                        AppHorloge("#3c0f14","white","Six : Horloge","chronometre")
                        self.fenetre.FermetureTK()
                        return 1
                    else :
                        if "minuteur" in var :
                            self.fenetre.OuvertureTK("Ok je vous ouvre le minuteur "+self.genre+" "+self.user)
                            AppHorloge("#3c0f14","white","Six : Horloge","minuteur")
                            self.fenetre.FermetureTK()
                            return 1
                        else :
                            if "agenda" in var :
                                if "ouvre" in var :
                                    self.fenetre.OuvertureTK("Je vous ouvre mon calendrier")
                                    SixCalendar()
                                    self.fenetre.FermetureTK()
                                else :
                                    texte = SortieEvenementTexte()
                                    self.sourceSIX.speak(texte)
                                return 1
                            else :
                                return 0