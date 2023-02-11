import requests

class meteo : 
    def __init__(self,latitude,longitude):
        keyApi="ecffd157b2cc9eacbd0d35a45c3dc047"
        url="https://api.openweathermap.org/data/2.5/weather?"
        self.reponse=requests.get(url+"lat="+str(latitude)+"&lon="+str(longitude)+"&lang=fr&units=metric&appid="+keyApi)
        #print(self.reponse)
        
    def temperature(self):#permet de recuperé la temperature
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            return str(self.reponse.json()["main"]["temp"])
    
    def humiditer(self):#permet de recuperé le taux d'humiditer en %
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            
            return str(self.reponse.json()["main"]["humidity"])
    
    def description(self):#permet de recuperé la description de temp en fr
        if self.reponse.status_code == 400 :
            return "error"
        else : 
            return self.reponse.json()["weather"][0]["description"]