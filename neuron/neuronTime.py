import datetime
from src.voice import*
from objet.Horloge.AppHorloge import*

def neuronTime(var,genre,user,name,root,police):
    if "heure" in var :
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        speak("Il es "+hour+" heure " +minute,root)
        return 1
    else : 
        if "date" in var :
            monthSTR = "Janvier"
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            years = datetime.datetime.now().year
            if month == 1 :
                monthSTR = "Janvier"
            else :
                if month == 2 :
                    monthSTR = "Fevrier"
                else :
                    if month == 3 :
                        monthSTR = "Mars"
                    else :
                        if month == 4 :
                            monthSTR = "Avril"
                        else :
                            if month == 5 :
                                monthSTR = "Mai"
                            else:
                                if month == 6 :
                                    monthSTR = "Juin"
                                else:
                                    if month == 7 :
                                        monthSTR = "Juillet"
                                    else :
                                        if month == 8 :
                                            monthSTR = "Aout"
                                        else :
                                            if month == 9 :
                                                monthSTR = "Septembre"
                                            else :
                                                if month == 10 :
                                                    monthSTR = "Octobre"
                                                else:
                                                    if month == 11 :
                                                        monthSTR = "Novembre"
                                                    else :
                                                         monthSTR = "Décembre"
            speak("Aujourd'hui on es le "+str(day)+" "+monthSTR+" "+str(years),root)
            return 1
        else : 
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