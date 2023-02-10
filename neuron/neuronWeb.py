from operator import ge
from src.srcSix import *
from function.api import *
from function.search import *
from function.JSON import*
from function.traduction import*

def NeuronWeb(var,genre,user,root,police):
    if "recherche" in var :
        SIXsrc(root,police).speak("Vous voulez rechercher quoi "+genre+" ?")
        recherche = SIXsrc(root,police).micro()
        SIXsrc(root,police).speak("Ok,je vous recherche sa.")
        duckduckgoSearch(recherche)
        return 1
    else :
        if "actualités" in var:
            CompleteURL = urlNew+"&pageSize="+nombrePageNew1+"&apiKey="+keyNew
            article = requests.get(CompleteURL).json()["articles"]
            Sujet,Description,URL,title = NetoyageActu(article[0])
            SIXsrc(root,police).speak("L'actualités la plus récent est "+title)
            SIXsrc(root,police).speak("Voulez-vous que je vous ouvre le lien de cette actualités "+genre+".")
            reponse = SIXsrc(root,police).micro()
            if "oui" in reponse:
                SIXsrc(root,police).speak("Ok je vous l'ouvre")
                webbrowser.open(URL)
            if "non" in reponse:
                SIXsrc(root,police).speak("Ok "+genre+".")
            return 1
        else :
            if "ouvre youtube" in var :
                webbrowser.open("https://www.youtube.com/")
                SIXsrc(root,police).speak("Youtube et ouvert ")
                return 1
            else :
                if "lance de la musique" in var or "lancer de la musique" in var:
                    lienMusic =lectureJSON("setting/config.json","appWeb1Lien")
                    webbrowser.open(lienMusic)
                    SIXsrc(root,police).speak("Votre logiciel de musique est lancer"+genre+".")
                    return 1
                else :
                    if "météo" in var:
                        SIXsrc(root,police).speak("Ou desirez savoir la meteo "+genre+" ?")
                        r= SIXsrc(root,police).micro()
                        if "maison" in r or "chez moi" in r or "à mon domicile" in r :
                            MeteoParole(1,root,police)  
                        if  "à mon lieu favori" in r  :
                            MeteoParole(2,root,police)            
                        if "à mon lieu de travail" in r :
                            MeteoParole(3,root,police)
                        if "à mon lieu de vacances" in r :
                            MeteoParole(4,root,police)
                        if "au lieu de bonus" in r  :
                            MeteoParole(5,root,police)
                        return 1
                    else :
                        if "drive" in var:
                            lienGDrive = lectureJSON("setting/config.json","lien2")
                            SIXsrc(root,police).speak("Ok voici votre google drive principale"+genre+"")
                            webbrowser.open(lienGDrive)
                            return 1
                        else :
                            if "navigateur internet" in var :
                                lienMoteur = lectureJSON("setting/config.json","lienMoteur")
                                nomMoteur = lectureJSON("setting/config.json","nameMoteur")
                                SIXsrc(root,police).speak("Ok j'ouvre votre navigateur internet avec le moteur de recherche "+nomMoteur)
                                webbrowser.open(lienMoteur)
                                return 1
                            else :
                                if "résumé" in var:
                                    Resumer(root,police)
                                    return 1
                                else :
                                    if "fais une grande recherche" in var:
                                        SIXsrc(root,police).speak("Que voulez vous que je vous recherche "+genre+"?")
                                        r = SIXsrc(root,police).micro()
                                        GrandRecherche(r)
                                        return 1
                                    else :
                                        if "dis-moi la température" in var:
                                            lat , long = GeoLocGPS()
                                            temp = str(requests.get(urlWeather+"appid="+keyWeather+"&lat="+lat+"&lon="+long+"&lang=fr"+"&units=metric").json()["main"]["temp"])
                                            SIXsrc(root,police).speak("La température a votre localisation est de "+temp+" degrés")
                                            return 1
                                        else :
                                            if "dis-moi mes coordonnées GPS" in var or "dis-moi où je suis" in var or "dis-moi où je me trouve" in var:
                                                lat , long = GeoLocGPS()
                                                SIXsrc(root,police).speak("Les coordonnées GPS de votre localisation sont "+lat+" latitude et de longitude "+long+".")
                                                return 1
                                            else :
                                                if "traduire" in var or "traduis-moi" in var:
                                                    SIXsrc(root,police).speak("Ok je vous ouvre l'application de tradution")
                                                    Trad(genre,root,police)
                                                    return 1
                                                else :
                                                    if "agenda" in var :
                                                        LienAgenda = lectureJSON("setting/config.json","lien1")
                                                        SIXsrc(root,police).speak("Ok je vous ouvre votre agenda "+genre)
                                                        webbrowser.open(LienAgenda)
                                                        return 1
                                                    else :
                                                        if "to do list" in var or "todolist" in var:
                                                            lienToDoList = lectureJSON("setting/config.json","lien4")
                                                            SIXsrc(root,police).speak("Ok je vous ouvre votre to do list "+genre)
                                                            webbrowser.open(lienToDoList)
                                                            return 1
                                                        else :
                                                            if "note" in var or "notes" in var:
                                                                lienNote = lectureJSON("setting/config.json","lien3")
                                                                SIXsrc(root,police).speak("Ok je vous ouvre vos notes en ligne "+genre)
                                                                webbrowser.open(lienNote)
                                                                return 1
                                                            else :
                                                                nameApp1 = lectureJSON("setting/config.json","appWeb2Name")
                                                                nameApp2 = lectureJSON("setting/config.json","appWeb3Name")
                                                                nameApp3 = lectureJSON("setting/config.json","appWeb4Name")
                                                                nameApp4 = lectureJSON("setting/config.json","appWeb5Name")
                                                                if nameApp1 in var:
                                                                    lienApp1 = lectureJSON("setting/config.json","appWeb2Lien")
                                                                    SIXsrc(root,police).speak("Ok je vous ouvre "+nameApp1+" "+genre+" "+user)
                                                                    webbrowser.open(lienApp1)
                                                                    return 1
                                                                else :
                                                                    if nameApp2 in var:
                                                                        lienApp2 = lectureJSON("setting/config.json","appWeb3Lien")
                                                                        SIXsrc(root,police).speak("Ok je vous ouvre "+nameApp2+" "+genre+" "+user)
                                                                        webbrowser.open(lienApp2)
                                                                        return 1
                                                                    else:
                                                                        if nameApp3 in var:
                                                                            lienApp3 = lectureJSON("setting/config.json","appWeb4Lien")
                                                                            SIXsrc(root,police).speak("Ok je vous ouvre "+nameApp3+" "+genre+" "+user)
                                                                            webbrowser.open(lienApp3)
                                                                            return 1
                                                                        else :
                                                                            if nameApp4 in var:
                                                                                lienApp4 = lectureJSON("setting/config.json","appWeb5Lien")
                                                                                SIXsrc(root,police).speak("Ok je vous ouvre "+nameApp4+" "+genre+" "+user)
                                                                                webbrowser.open(lienApp4)
                                                                                return 1
                                                                            else :
                                                                                return 0