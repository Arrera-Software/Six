from operator import ge
from src.voice import *
from function.api import *
from function.search import *
from src.speechRecognition import *
from src.file import*

def Web(var,genre,user):
    if "recherche" in var :
        speak("Vous voulez rechercher quoi ",genre,"?")
        recherche = takeCommand()
        speak("Ok,je vous recherche sa.")
        duckduckgoSearch(recherche)
        return 1
    else :
        if "actualités" in var:
            CompleteURL = urlNew+"&pageSize="+nombrePageNew1+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]
            Sujet,Description,URL,title = NetoyageActu(article[0])
            speak("L'actualités la plus récent est "+title)
            speak("Voulez-vous que je vous ouvre le lien de cette actualités "+genre+".")
            reponse = takeCommand()
            if "oui" in reponse:
                speak("Ok je vous l'ouvre")
                webbrowser.open(URL)
            if "non" in reponse:
                speak("Ok "+genre+".")
            return 1
        else :
            if "ouvre youtube" in var :
                webbrowser.open("https://www.youtube.com/")
                speak("Youtube et ouvert ")
                return 1
            else :
                if "lance de la musique" in var or "lancer de la musique" in var:
                    lienMusic = str(Lecture("config/lienMusic.txt"))
                    webbrowser.open(lienMusic)
                    speak("Votre logiciel de musique est lancer"+genre+".")
                    return 1
                else :
                    if "météo" in var:
                        speak("Ou desirez savoir la meteo "+genre+" ?")
                        r= takeCommand()
                        if "maison" in r or "chez moi" in r or "à mon domicile" in r :
                            MeteoParole(1)  
                        if  "à mon lieu favori" in r  :
                            MeteoParole(2)            
                        if "à mon lieu de travail" in r :
                            MeteoParole(3)
                        if "à mon lieu de vacances" in r :
                            MeteoParole(4)
                        if "au lieu de bonus" in r  :
                            MeteoParole(5)
                        return 1
                    else :
                        if "google drive" in var:
                            lienGDrive = str(Lecture("Config/lienGDrive.txt"))
                            speak("Ok voici votre google drive principale"+genre+"")
                            webbrowser.open(lienGDrive)
                            return 1
                        else :
                            if "navigateur internet" in var :
                                lienMoteur = str(Lecture("config/MoteurRecherche/LienMoteur.txt"))
                                speak("Ok j'ouvre votre navigateur internet")
                                webbrowser.open(lienMoteur)
                                return 1
                            else :
                                if "résumé" in var:
                                    Resumer()
                                    return 1
                                else :
                                    if "fais une grande recherche" in var:
                                        speak("Que voulez vous que je vous recherche "+genre+"?")
                                        r = takeCommand()
                                        GrandRecherche(r)
                                        return 1
                                    else :
                                        if "dis-moi la température" in var:
                                            lat , long = GeoLocGPS()
                                            temp = str(requests.get(urlWeather+"appid="+keyWeather+"&lat="+lat+"&lon="+long+"&lang=fr"+"&units=metric").json()["main"]["temp"])
                                            speak("La température a votre localisation est de "+temp+" degrés")
                                            return 1
                                        else :
                                            if "dis-moi mes coordonnées GPS" in var or "dis-moi où je suis" in var or "dis-moi où je me trouve" in var:
                                                lat , long = GeoLocGPS()
                                                speak("Les coordonnées GPS de votre localisation sont "+lat+" latitude et de longitude "+long+".")
                                                return 1
                                            else :
                                                if "traduire" in var or "traduis-moi" in var:
                                                    speak("Ok je vous ouvre l'application de tradution")
                                                    Trad(genre)
                                                    return 1
                                                else :
                                                    if "agenda" in var :
                                                        LienAgenda = str(Lecture("config/lienAgenda.txt"))
                                                        speak("Ok je vous ouvre votre agenda "+genre)
                                                        webbrowser.open(LienAgenda)
                                                        return 1
                                                    else :
                                                        if "to do list" in var or "todolist" in var:
                                                            lienToDoList = str(Lecture("config/lienToDoList.txt"))
                                                            speak("Ok je vous ouvre votre to do list "+genre)
                                                            webbrowser.open(lienToDoList)
                                                            return 1
                                                        else :
                                                            if "note" in var or "notes" in var:
                                                                lienNote = str(Lecture("config/lienNote.txt"))
                                                                speak("Ok je vous ouvre vos notes en ligne "+genre)
                                                                webbrowser.open(lienNote)
                                                                return 1
                                                            else :
                                                                nameResaux1 = str(Lecture("neuron/config/reseau/name/NameReseau1.txt"))
                                                                nameResaux2 = str(Lecture("neuron/config/reseau/name/NameReseau2.txt"))
                                                                nameResaux3 = str(Lecture("neuron/config/reseau/name/NameReseau3.txt"))
                                                                if nameResaux1 in var:
                                                                    lienResaux1 = str(Lecture("neuron/config/reseau/lien/Reseau1.txt"))
                                                                    speak("Ok je vous ouvre "+nameResaux1+" "+genre+" "+user)
                                                                    webbrowser.open(lienResaux1)
                                                                    return 1
                                                                else :
                                                                    if nameResaux2 in var:
                                                                        lienResaux2 = str(Lecture("neuron/config/reseau/lien/Reseau2.txt"))
                                                                        speak("Ok je vous ouvre "+nameResaux2+" "+genre+" "+user)
                                                                        webbrowser.open(lienResaux2)
                                                                        return 1
                                                                    else:
                                                                        if nameResaux1 in var:
                                                                            lienResaux3 = str(Lecture("neuron/config/reseau/lien/Reseau1.txt"))
                                                                            speak("Ok je vous ouvre "+nameResaux3+" "+genre+" "+user)
                                                                            webbrowser.open(lienResaux3)
                                                                            return 1
                                                                        else :
                                                                            return 0