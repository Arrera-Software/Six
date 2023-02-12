import datetime
from src.srcSix import*
from objet.Horloge.AppHorloge import*
from objet.date.objetdate import*

def neuronTime(var,genre,user,name,root,police):
    if "heure" in var :
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        SIXsrc(root,police).speak("Il es "+hour+" heure " +minute)
        return 1
    else : 
        if "date" in var :
            jour = date().jour()
            mois = date().mois()
            annees = date().annes()
            SIXsrc(root,police).speak("Aujourd'hui on es le "+jour+" "+mois+" "+annees)
            return 1
        else : 
            if "horloge" in var :
                SIXsrc(root,police).speak("Ok je vous ouvre l'application horloge "+user,+" "+name)
                AppHorloge("#3c0f14","white","Six : Horloge","acceuil")
                return 1
            else :
                if "chronométre" in var or "chono" in var or "chonometre" in var :
                    SIXsrc(root,police).speak("Ok je t'ouvre le chronometre "+genre+" "+user)
                    AppHorloge("#3c0f14","white","Six : Horloge","chronometre")
                    return 1
                else :
                    if "minuteur" in var :
                        SIXsrc(root,police).speak("Ok je t'ouvre le minuteur "+genre+" "+user)
                        AppHorloge("#3c0f14","white","Six : Horloge","minuteur")
                        return 1
                    else :
                        return 0