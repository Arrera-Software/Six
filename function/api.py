from src.srcSix import* 
from objet.actualiter.apiActualiter import*
from objet.meteo.apiMeteo import*
from function.JSON import*
from objet.date.objetdate import*
from objet.GPS.apiGPS import*

def Resumer(root,police):#Fonction de resumer des actaulités et de la meteo
    varGPSDomicile = ville(lectureJSON("setting/config.json","ville1"))
    varCapitale = ville("Paris")
    ListActu = Actualiter().recuperation()
    varMeteoDomicile = meteo(varGPSDomicile.lat(),varGPSDomicile.long())
    dateJour = date().jour() + " " + date().mois() + " "+date().annes()
    heureActuel = date().heure()+" Heure "+date().minute()
    six = SIXsrc(root,police)
    
    six.speak("On est le "+dateJour+" a "+heureActuel+" ")
    time.sleep(1)
    six.speak("La météo a "+lectureJSON("setting/config.json","ville1")+" est "+varMeteoDomicile.description()+" avec une température de "+varMeteoDomicile.temperature()+"°C")
    time.sleep(1)
    six.speak("Les actualités du jour sont :")
    time.sleep(1)
    six.speak(ListActu[0])
    time.sleep(1)
    six.speak(ListActu[1])
    time.sleep(1)
    six.speak(ListActu[2])
    time.sleep(1)
    six.speak(ListActu[3])
    time.sleep(1)
    six.speak(ListActu[4])
    
    
    


