from src.voice import *
from function.reading import*
import datetime
import random

def Main(var,genre,user,name,root):
    if  var =="salut"   or var =="bonjour" or var =="bonsoir":
        speak(var+" en quoi je peux vous servir ?",root)
        return 1
    else :
        if "bien" in var or "oui" in var:
            speak("Sa me réjouit de savoir que tout se passe bien pour vous"+genre+" .",root)
            speak("En quoi je peux donc vous servir ?",root)
            return 1
        else :
            if "toujours là"  in var  or "es-tu là" in var or name in var :
                speak("Oui, je suis toujours la"+genre+user+".",root)
                return 1
            else : 
                if "heure" in var :
                    hour = datetime.datetime.now().hour
                    minute = datetime.datetime.now().minute
                    Constrution = "Il es",hour,"heure",minute
                    parole = str(Constrution)
                    speak(parole,root)
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
                        speak("Aujourd'huit on es le "+str(day)+monthSTR+str(years),root)
                        return 1
                    else :
                        if "raconter une blague" in var or "raconte-moi une blague" in var :
                            nb = random.randint(1,10)
                            if nb == 1 :
                                speak("Que dit une noisette quand elle tombe dans l’eau ?",root)
                                speak("Je me noix.",root)
                                return 1
                            else :
                                if nb == 2 :
                                    speak("Comment est-ce que les abeilles communiquent entre elles ?",root)
                                    speak("Par-miel.",root)
                                    return 1
                                else :
                                    if nb == 3 :
                                        speak("Quel est l’arbre préféré du chômeur ?",root)
                                        speak("Le bouleau.",root)
                                        return 1
                                    else :
                                        if nb == 4 :
                                            speak("Qu’est-ce qu’une frite enceinte ?",root)
                                            speak("Une patate sautée.",root)
                                            return 1
                                        else :
                                            if nb == 5 :
                                                speak("Que dit une mère à son fils geek quand le dîner est servi ?",root)
                                                speak("Alt Tab !",root)
                                                return 1
                                            else :
                                                if nb == 6 :
                                                    speak("Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?",root)
                                                    speak("Marcher",root)
                                                    return 1
                                                else :
                                                    if nb == 7 :
                                                        speak("Pourquoi les Ch’tis aiment les fins de vacances au camping ?",root)
                                                        speak("Parce que c’est le moment où ils peuvent démonter leur tente.",root)
                                                        return 1
                                                    else :
                                                        if nb == 8 :
                                                            speak("Quelle est la partie de la voiture la plus dangereuse ?",root)
                                                            speak("La conductrice.",root)
                                                            return 1
                                                        else :
                                                            if nb == 9 :
                                                                speak("Pourquoi dit-on que les poissons travaillent illégalement ?",root)
                                                                speak("Parce qu'ils n'ont pas de FISH de paie",root)
                                                                return 1
                                                            else :
                                                                speak("Mettre du sirop dans son gel douche",root)
                                                                speak("En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible.",root)  
                                                                return 1
                        else :
                            if var == "tu es qui" or var == "présente-toi" or "présentation" in var or "qui es tu" in var or "qui es-tu" in var:
                                speak("Je suis SIX un assistant personnel cree par Baptiste Pauchet. Pour l'assistait dans l'uttilisation de son ordinateur.",root)
                                return 1
                            else :
                                if "peux-tu me lire un truc" in var :
                                    speak("Copier ce que vous voulez  que je vous lise "+genre+".",root)
                                    Reading(root)
                                    return 1
                                else :
                                    return 0

