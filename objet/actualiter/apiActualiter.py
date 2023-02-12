import requests
import datetime

class Actualiter :
    def __init__(self):
        self.api_key = "3b43e18afcf945888748071d177b8513"
        nbPage = "5"
        date = str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)
        self.urlActuMondial = "https://newsapi.org/v2/top-headlines?" +"apiKey=" + self.api_key + "&language=fr&from="+date+"&country=fr"+"&pageSize="+nbPage+"&category=general"
        self.urlActuFr = "https://newsapi.org/v2/top-headlines?" +"apiKey=" + self.api_key + "&language=fr&from="+date+"&pageSize="+nbPage+"&category=technology"
        self.urlActuPolitique  =  "https://newsapi.org/v2/top-headlines?" +"apiKey=" + self.api_key + "&language=fr&from="+date+"&country=fr"+"&pageSize="+nbPage+"&category=science"
        self.urlActuCrypto =  "https://newsapi.org/v2/top-headlines?" +"apiKey=" + self.api_key + "&language=fr&from="+date+"&country=fr"+"&pageSize="+nbPage+"&category=sport"
        
    def Netoyage(self,dictionnnaire):
        titre = dictionnnaire["title"]
        return titre
    
    def recuperation(self):#Permet de recuperer les actualiter sous la forme d'une liste
        self.responseMondiale = requests.get(self.urlActuMondial)
        self.responseFr = requests.get(self.urlActuFr)
        self.reponsePoli = requests.get(self.urlActuPolitique)
        self.reponseCrypto = requests.get(self.urlActuCrypto)
        self.listactu = []
        if (self.responseMondiale.status_code == 200)and(self.responseFr.status_code == 200)and(self.reponsePoli.status_code == 200)and(self.reponseCrypto.status_code == 200):
            self.dataMondiale = self.responseMondiale.json()
            self.dataFr = self.responseFr.json()
            self.dataPoli = self.reponsePoli.json()
            self.dataCrypto = self.reponseCrypto.json()
            self.actu1 = self.Netoyage(self.dataMondiale["articles"][0])
            self.actu2 = self.Netoyage(self.dataMondiale["articles"][2])
            self.actu3 = self.Netoyage(self.dataFr["articles"][0])
            self.actu4 = self.Netoyage(self.dataFr["articles"][2])
            self.actu5 = self.Netoyage(self.dataPoli["articles"][0])
            self.actu6 = self.Netoyage(self.dataCrypto["articles"][0])
            self.listactu = [self.actu1 , self.actu2 ,self.actu3,self.actu4,self.actu5,self.actu6]
        else:
            self.listactu=["ereur","ereur","ereur","ereur","ereur","ereur"]
        return self.listactu