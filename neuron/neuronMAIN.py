from src.voice import *
from function.reading import*
import datetime
import random

def Main(var,genre,user,name,root):
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
            if "raconter une blague" in var or "raconte-moi une blague" in var :
                nb = random.randint(1,10)
                blague = ["Que dit une noisette quand elle tombe dans l’eau ?"
                          ,"Comment est-ce que les abeilles communiquent entre elles ?"
                          ,"Quel est l’arbre préféré du chômeur ?","Qu’est-ce qu’une frite enceinte ?"
                          ,"Que dit une mère à son fils geek quand le dîner est servi ?"
                          ,"Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?"
                          ,"Pourquoi les Ch’tis aiment les fins de vacances au camping ?"
                          ,"Quelle est la partie de la voiture la plus dangereuse ?"
                          ,"Pourquoi dit-on que les poissons travaillent illégalement ?"
                          ,"Mettre du sirop dans son gel douche"
                          ]
                reponseBlague=["Je me noix."
                               ,"Par-miel."
                               ,"Le bouleau."
                               ,"Une patate sautée."
                               ,"Alt Tab !"
                               ,"Marcher"
                               ,"Parce que c’est le moment où ils peuvent démonter leur tente."
                               ,"La conductrice."
                               ,"Parce qu'ils n'ont pas de FISH de paie"
                               ,"En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible."
                               ]
                speak(blague[nb],root)
                time.sleep(1.5)
                speak(reponseBlague[nb],root)
                return 1
            else :
                if "peux-tu me lire un truc" in var :
                    speak("Copier ce que vous voulez  que je vous lise "+genre+".",root)
                    Reading(root)
                    return 1
                else :
                    return 0

