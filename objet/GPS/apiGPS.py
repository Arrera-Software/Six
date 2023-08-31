import requests
import geocoder

class ville:
    def __init__(self,ville):
        url = "http://api.openweathermap.org/geo/1.0/direct?q="
        keyApi="19bfbee6112be5b3d9a64d4ccec72602"
        self.reponse = requests.get(url+ville+"&appid="+keyApi)
    def lat(self):#permet de recuperé la latitude
        if self.reponse.status_code == 400 :
            return "error"
        else :
            return str(self.reponse.json()[0]["lat"])
    
    def long(self):#permet de recuperé la longitude
        if self.reponse.status_code == 400 :
            return "error"
        else :
            return str(self.reponse.json()[0]["lon"])
        
    
class GeoLocIP:
    def __init__(self):
        self.ipPublic = requests.get("http://wtfismyip.com/text").text.strip()
        ip = geocoder.ip(self.ipPublic)
        self.loc = ip.latlng
    
    def lat(self):
        return str(self.loc[0])

    def long(self):
        return str(self.loc[1])
    
