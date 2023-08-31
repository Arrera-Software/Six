from src.srcSix import *
from function.api import *
from function.search import *
from function.JSON import*
from function.traduction import*
import random
from objet.meteo.apiMeteo import*
from objet.GPS.apiGPS import*
from objet.actualiter.apiActualiter import*
from function.fenetrePygame import*
class neuroneWeb :
    def __init__(self,name,root,UserCourt,GenreCourt,police):
        self.root = root
        self.police = police
        self.fenetre = pygameFond(root,police,GenreCourt)
        self.sourceSIX = SIXsrc(root,police)
        self.name = name
        self.user = UserCourt
        self.genre = GenreCourt
        
    def neuron(self,var):
        var = str(var)
        if "grande recherche" in var :
            var = var.replace("grande recherche","")
            var = var.replace("fais-moi","")
            var = var.replace("une","")
            var = var.replace("sur ","")
            self.sourceSIX.speak("Ok,Voici ce que trouvent tout les moteur de recherche.")
            search(var).GrandRecherche()
            return 1
        else :
            if "recherche" in var :
                var = var.replace("recherche","")
                var = var.replace("fais-moi","")
                var = var.replace("une","")
                var = var.replace("sur ","")
                self.sourceSIX.speak("Ok,je vous recherche sa.")
                nameMoteur = lectureJSON("setting/config.json","nameMoteur")
                if (nameMoteur=="duckduckgo"):
                    search(var).duckduckgoSearch()
                else :
                    if (nameMoteur=="google"):
                        search(var).googleSearch()
                    else :
                        if (nameMoteur=="qwant"):
                            search(var).QwantSearch()
                        else :
                            if (nameMoteur == "ecosia" ):
                                search(var).EcosiaSearch()
                            else :
                                if (nameMoteur=="brave"):
                                    search(var).braveSearch()
                                else :
                                    if (nameMoteur=="bing"):
                                        search(var).bingSearch()
                                    else :
                                        search(var).duckduckgoSearch()
                return 1
            else :
                if "actualités" in var:
                    if "montre" in var :
                        self.fenetre.OuvertureTK("Voici les actualités du moment")
                        DescriptionActu()
                        self.fenetre.FermetureTK()
                    else :
                        listActu = Actualiter().recuperationTitre()
                        nbRadMonde = random.randint(0,1)
                        nbRandFr = random.randint(2,3)          
                        self.sourceSIX.speak("Les actualités de se moment sont")
                        time.sleep(1)
                        self.sourceSIX.speak(listActu[nbRadMonde])
                        time.sleep(1)
                        self.sourceSIX.speak(listActu[nbRandFr])
                        time.sleep(1)
                        self.sourceSIX.speak("Et enfin")
                        self.sourceSIX.speak(listActu[4])
                
                    return 1
                else :
                    if "ouvre youtube" in var :
                        webbrowser.open("https://www.youtube.com/")
                        self.sourceSIX.speak("Youtube et ouvert ")
                        return 1
                    else :
                        if "météo" in var:
                            
                            if "maison" in var or "chez moi" in var or "à mon domicile" in var or lectureJSON("setting/config.json","ville1") in var :
                                nameVille = lectureJSON("setting/config.json","ville1")
                                gps = ville(nameVille)
                                retourMeteo = meteo(gps.lat(),gps.long())
                                self.sourceSIX.speak("La météo a votre domicile est "+retourMeteo.description())
                                time.sleep(1)
                                self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                time.sleep(1)
                                self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")
                            else :
                                if  "à mon lieu favori" in var  or lectureJSON("setting/config.json","ville2") in var:
                                    nameVille = lectureJSON("setting/config.json","ville2")
                                    gps = ville(nameVille)
                                    retourMeteo = meteo(gps.lat(),gps.long())
                                    self.sourceSIX.speak("La météo a votre lieu favorie est "+retourMeteo.description())
                                    time.sleep(1)
                                    self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                    time.sleep(1)
                                    self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")           
                                else :
                                    if "à mon lieu de travail" in var or lectureJSON("setting/config.json","ville3") in var :
                                        nameVille = lectureJSON("setting/config.json","ville3")
                                        gps = ville(nameVille)
                                        retourMeteo = meteo(gps.lat(),gps.long())
                                        self.sourceSIX.speak("La météo à "+nameVille+" est "+retourMeteo.description())
                                        time.sleep(1)
                                        self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                        time.sleep(1)
                                        self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")
                                    else :
                                        if "à mon lieu de vacances" in var or lectureJSON("setting/config.json","ville4") in var :
                                            nameVille = lectureJSON("setting/config.json","ville4")
                                            gps = ville(nameVille)
                                            retourMeteo = meteo(gps.lat(),gps.long())
                                            self.sourceSIX.speak("La météo à "+nameVille+" est "+retourMeteo.description())
                                            time.sleep(1)
                                            self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                            time.sleep(1)
                                            self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")
                                        else :
                                            if "au lieu bonus" in var or lectureJSON("setting/config.json","ville5") in var :
                                                nameVille = lectureJSON("setting/config.json","ville5")
                                                gps = ville(nameVille)
                                                retourMeteo = meteo(gps.lat(),gps.long())
                                                self.sourceSIX.speak("La météo à "+nameVille+" est "+retourMeteo.description())
                                                time.sleep(1)
                                                self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                                time.sleep(1)
                                                self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")
                                            else : 
                                                nameVille = lectureJSON("setting/config.json","ville1")
                                                gps = ville(nameVille)
                                                retourMeteo = meteo(gps.lat(),gps.long())
                                                self.sourceSIX.speak("La météo à "+nameVille+" est "+retourMeteo.description())
                                                time.sleep(1)
                                                self.sourceSIX.speak("Avec une température de "+retourMeteo.temperature()+" °C")
                                                time.sleep(1)
                                                self.sourceSIX.speak("Et un taux d'humiditer de "+retourMeteo.humiditer()+" %")
                            return 1       
                        else :
                            if "stockage cloud" in var or "stockage Cloud" in var or "drive" in var or "stockage en ligne" in var or "google drive" in var:
                                lienStokageCloud = lectureJSON("setting/config.json","lien2")
                                nrad = random.randint(0,1)
                                listText = ["Voici votre stockage en ligne ","Voici votre stockage en could "]
                                self.sourceSIX.speak(listText[nrad]+self.genre+" ")
                                webbrowser.open(lienStokageCloud)
                                return 1
                            else :
                                if "résumé" in var:
                                    Resumer(self.root,self.police)
                                    return 1
                                else :
                                    if "dis-moi la température" in var:
                                        geoLoc = GeoLocIP()
                                        retourMeteo = meteo(geoLoc.lat(),geoLoc.long())
                                        self.sourceSIX.speak("La température actuel a votre localisation est de "+retourMeteo.temperature()+" °C")
                                        return 1
                                    else :
                                        if "dis-moi mes coordonnées GPS" in var or "dis-moi où je suis" in var or "dis-moi où je me trouve" in var:
                                            geoLoc = GeoLocIP()
                                            self.sourceSIX.speak("Les coordonnées GPS de votre localisation sont "+geoLoc.lat()+" latitude et de longitude "+geoLoc.long()+".")
                                            return 1
                                        else :
                                            if "traduire" in var or "traduis-moi" in var or "traduction" in var :
                                                if "traduis-moi" in var:
                                                    langTrad = lectureJSON("setting/config.json","langTradDefault")
                                                    nom = var.replace("traduis-moi","")
                                                    nomTrad = ArreraTrad("fr",langTrad).Tradution(nom)
                                                    self.sourceSIX.speakOtherLang(langTrad,nomTrad)
                                                else :
                                                    self.fenetre.OuvertureTK("Ok, je vous ouvre l'outil de traduction")
                                                    Trad()
                                                    self.fenetre.FermetureTK()
                                                return 1
                                            else :
                                                nameApp1 = lectureJSON("setting/config.json","appWeb2Name")
                                                nameApp2 = lectureJSON("setting/config.json","appWeb3Name")
                                                nameApp3 = lectureJSON("setting/config.json","appWeb4Name")
                                                nameApp4 = lectureJSON("setting/config.json","appWeb5Name")
                                                if nameApp1 in var:
                                                    lienApp1 = lectureJSON("setting/config.json","appWeb2Lien")
                                                    self.sourceSIX.speak("Ok je vous ouvre "+nameApp1+" "+self.genre+" "+self.user)
                                                    webbrowser.open(lienApp1)
                                                    return 1
                                                else :
                                                    if nameApp2 in var:
                                                        lienApp2 = lectureJSON("setting/config.json","appWeb3Lien")
                                                        self.sourceSIX.speak("Ok je vous ouvre "+nameApp2+" "+self.genre+" "+self.user)
                                                        webbrowser.open(lienApp2)
                                                        return 1
                                                    else:
                                                        if nameApp3 in var:
                                                            lienApp3 = lectureJSON("setting/config.json","appWeb4Lien")
                                                            self.sourceSIX.speak("Ok je vous ouvre "+nameApp3+" "+self.genre+" "+self.user)
                                                            webbrowser.open(lienApp3)
                                                            return 1
                                                        else :
                                                            if nameApp4 in var:
                                                                lienApp4 = lectureJSON("setting/config.json","appWeb5Lien")
                                                                self.sourceSIX.speak("Ok je vous ouvre "+nameApp4+" "+self.genre+" "+self.user)
                                                                webbrowser.open(lienApp4)
                                                                return 1
                                                            else :
                                                                if "dis-moi tout" in var :
                                                                    var = var.replace("dis-moi tout sur","")
                                                                    listRecherche = search(var).rechercheDuckDuckGo
                                                                    self.sourceSIX.speak(listRecherche[0])
                                                                    time.sleep(1)
                                                                    self.sourceSIX.speak(listRecherche[1])
                                                                    time.sleep(1)
                                                                    self.sourceSIX.speak(listRecherche[2])
                                                                    return 1 
                                                                else :
                                                                    return 0
                                                                    