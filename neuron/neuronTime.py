from src.voice import*
from objet.Horloge.AppHorloge import*

def Time(var,genre,user,name,root,police):
    if "horloge" in var :
        speak("Ok je vous ouvre l'application horloge "+user,+" "+name,root)
        AppHorloge("#3c0f14","white","Six : Horloge","acceuil")
        return 1
    else :
        if "chronométre" in var or "chono" in var or "chonometre" in var :
            speak("Ok je t'ouvre le chronometre "+genre+" "+user,root)
            AppHorloge("#3c0f14","white","Six : Horloge","chronometre")
            return 1
        else :
            if "minuteur" in var :
                speak("Ok je t'ouvre le minuteur "+genre+" "+user,root)
                AppHorloge("#3c0f14","white","Six : Horloge","minuteur")
                return 1
            else :
                return 0