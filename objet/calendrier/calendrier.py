import holidays
import datetime
import json
from function.JSON import *

class CalendrierToday :
    def __init__(self):
        self.anneeEnCours = str(datetime.date.today().year)
        self.moisEnCours = str(datetime.date.today().month)
        self.jourEnCours = str(datetime.date.today().day)
        
        
    def SaintDujour(self):
        jourSaint = json.load(open(file="objet/calendrier/listFete.json", encoding='utf-8'))[self.moisEnCours][self.jourEnCours]
        return str(jourSaint)
    
    def jourFerier(self):
        joursFeries = dict(holidays.FRA(years=datetime.date.today().year))
        if self.anneeEnCours+"-"+self.moisEnCours+"-"+self.jourEnCours in  joursFeries :
            ferier = True 
            nameJour = joursFeries[self.anneeEnCours+"-"+self.moisEnCours+"-"+self.jourEnCours]
        else :
            ferier = False
            nameJour = "none"
            
        return ferier,nameJour
    
    
class Agenda : 
    def __init__(self,file) :
        self.fichier = file
        
    def addEvent(self,name,date):
        baseDict = {"name":"","date":""}
        nombre = compteurJSON(self.fichier)
        nombre = nombre + 1
        baseDict["name"] = str(name)
        baseDict["date"] = date
        EcritureSansEcrasement(self.fichier, baseDict, str(nombre))
        
    def ListEventName(self):
        nombre = compteurJSON(self.fichier)
        i = 1
        dictEnvent = {}
        while i <= nombre :
            var = lectureJSONDict(self.fichier,str(i))    
            var = var["name"]
            dictEnvent[str(i)] = var  
            i = i + 1
        return dictEnvent
    
    def ListEventDate(self):
        nombre = compteurJSON(self.fichier)
        i = 1
        dictEnvent = {}
        while i <= nombre :
            var = lectureJSONDict(self.fichier,str(i))    
            var = var["date"]
            dictEnvent[str(i)] = var  
            i = i + 1
        return dictEnvent
    
    
    def SupprEnvent(self,nbEnvent):
        var = lectureSimpleJSON(self.fichier)
        # Conversion du numéro de clé en string
        num_cle_str = str(nbEnvent)
        # Suppression de la clé et mise à jour des numéros de clé
        del var[num_cle_str]
        for i in range(nbEnvent + 1, len(var) + 2):
            var[str(i-1)] = var.pop(str(i))
        EcritureEcrasement(self.fichier, var)