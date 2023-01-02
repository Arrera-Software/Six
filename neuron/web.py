from operator import ge
from src.voice import *
from function.api import *
from function.search import *
from src.speechRecognition import *
from function.JSON import*
from function.traduction import*

def Web(var,genre,user,root,police):
    if "recherche" in var :
        speak("Vous voulez rechercher quoi "+genre+" ?",root)
        recherche = takeCommand(root,police)
        speak("Ok,je vous recherche sa.",root)
        duckduckgoSearch(recherche)
        return 1
    else :
        if "actualités" in var:
            CompleteURL = urlNew+"&pageSize="+nombrePageNew1+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]
            Sujet,Description,URL,title = NetoyageActu(article[0])
            speak("L'actualités la plus récent est "+title,root)
            speak("Voulez-vous que je vous ouvre le lien de cette actualités "+genre+".",root)
            reponse = takeCommand(root,police)
            if "oui" in reponse:
                speak("Ok je vous l'ouvre",root)
                webbrowser.open(URL)
            if "non" in reponse:
                speak("Ok "+genre+".",root)
            return 1
        else :
            if "ouvre youtube" in var :
                webbrowser.open("https://www.youtube.com/")
                speak("Youtube et ouvert ",root)
                return 1
            else :
                if "lance de la musique" in var or "lancer de la musique" in var:
                    lienMusic =lectureJSON("setting/config.json","appWeb1Lien")
                    webbrowser.open(lienMusic)
                    speak("Votre logiciel de musique est lancer"+genre+".",root)
                    return 1
                else :
                    if "météo" in var:
                        speak("Ou desirez savoir la meteo "+genre+" ?",root)
                        r= takeCommand(root,police)
                        if "maison" in r or "chez moi" in r or "à mon domicile" in r :
                            MeteoParole(1,root)  
                        if  "à mon lieu favori" in r  :
                            MeteoParole(2,root)            
                        if "à mon lieu de travail" in r :
                            MeteoParole(3,root)
                        if "à mon lieu de vacances" in r :
                            MeteoParole(4,root)
                        if "au lieu de bonus" in r  :
                            MeteoParole(5,root)
                        return 1
                    else :
                        if "drive" in var:
                            lienGDrive = lectureJSON("setting/config.json","lien2")
                            speak("Ok voici votre google drive principale"+genre+"",root)
                            webbrowser.open(lienGDrive)
                            return 1
                        else :
                            if "navigateur internet" in var :
                                lienMoteur = lectureJSON("setting/config.json","lienMoteur")
                                nomMoteur = lectureJSON("setting/config.json","nameMoteur")
                                speak("Ok j'ouvre votre navigateur internet avec le moteur de recherche "+nomMoteur,root)
                                webbrowser.open(lienMoteur)
                                return 1
                            else :
                                if "résumé" in var:
                                    Resumer(root)
                                    return 1
                                else :
                                    if "fais une grande recherche" in var:
                                        speak("Que voulez vous que je vous recherche "+genre+"?",root)
                                        r = takeCommand(root,police)
                                        GrandRecherche(r)
                                        return 1
                                    else :
                                        if "dis-moi la température" in var:
                                            lat , long = GeoLocGPS()
                                            temp = str(requests.get(urlWeather+"appid="+keyWeather+"&lat="+lat+"&lon="+long+"&lang=fr"+"&units=metric").json()["main"]["temp"])
                                            speak("La température a votre localisation est de "+temp+" degrés",root)
                                            return 1
                                        else :
                                            if "dis-moi mes coordonnées GPS" in var or "dis-moi où je suis" in var or "dis-moi où je me trouve" in var:
                                                lat , long = GeoLocGPS()
                                                speak("Les coordonnées GPS de votre localisation sont "+lat+" latitude et de longitude "+long+".",root)
                                                return 1
                                            else :
                                                if "traduire" in var or "traduis-moi" in var:
                                                    speak("Ok je vous ouvre l'application de tradution",root)
                                                    Trad(genre)
                                                    return 1
                                                else :
                                                    if "agenda" in var :
                                                        LienAgenda = lectureJSON("setting/config.json","lien1")
                                                        speak("Ok je vous ouvre votre agenda "+genre,root)
                                                        webbrowser.open(LienAgenda)
                                                        return 1
                                                    else :
                                                        if "to do list" in var or "todolist" in var:
                                                            lienToDoList = lectureJSON("setting/config.json","lien4")
                                                            speak("Ok je vous ouvre votre to do list "+genre,root)
                                                            webbrowser.open(lienToDoList)
                                                            return 1
                                                        else :
                                                            if "note" in var or "notes" in var:
                                                                lienNote = lectureJSON("setting/config.json","lien3")
                                                                speak("Ok je vous ouvre vos notes en ligne "+genre,root)
                                                                webbrowser.open(lienNote)
                                                                return 1
                                                            else :
                                                                nameApp1 = lectureJSON("setting/config.json","appWeb2Name")
                                                                nameApp2 = lectureJSON("setting/config.json","appWeb3Name")
                                                                nameApp3 = lectureJSON("setting/config.json","appWeb4Name")
                                                                nameApp4 = lectureJSON("setting/config.json","appWeb5Name")
                                                                if nameApp1 in var:
                                                                    lienApp1 = lectureJSON("setting/config.json","appWeb2Lien")
                                                                    speak("Ok je vous ouvre "+nameApp1+" "+genre+" "+user,root)
                                                                    webbrowser.open(lienApp1)
                                                                    return 1
                                                                else :
                                                                    if nameApp2 in var:
                                                                        lienApp2 = lectureJSON("setting/config.json","appWeb3Lien")
                                                                        speak("Ok je vous ouvre "+nameApp2+" "+genre+" "+user,root)
                                                                        webbrowser.open(lienApp2)
                                                                        return 1
                                                                    else:
                                                                        if nameApp3 in var:
                                                                            lienApp3 = lectureJSON("setting/config.json","appWeb4Lien")
                                                                            speak("Ok je vous ouvre "+nameApp3+" "+genre+" "+user,root)
                                                                            webbrowser.open(lienApp3)
                                                                            return 1
                                                                        else :
                                                                            if nameApp4 in var:
                                                                                lienApp4 = lectureJSON("setting/config.json","appWeb5Lien")
                                                                                speak("Ok je vous ouvre "+nameApp4+" "+genre+" "+user,root)
                                                                                webbrowser.open(lienApp4)
                                                                                return 1
                                                                            else :
                                                                                return 0