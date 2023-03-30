import webbrowser
import requests
import time
from translate import*

class internet :
    def testInternet():
        try:
            _ = requests.get("https://duckduckgo.com",timeout=5)
            return True
        except requests.ConnectionError :
            return False
class search :
    def __init__(self,query):
        self.query = str(query)
    
    def braveSearch(self):
        url = 'https://search.brave.com/search?q='
        urllink = requests.get(url+self.query+"&source=web")
        lienBrave = urllink.url
        webbrowser.open(lienBrave)

    def AmazonSearch(self):
        url = 'https://www.amazon.fr/s?k='
        urllink = requests.get(url+self.query)
        lienAmazon = urllink.url
        webbrowser.open(lienAmazon)

    def googleSearch(self):
        url = 'https://www.google.com/search?q'
        query = {'q': self.query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle)

    def duckduckgoSearch(self):
        url = 'https://duckduckgo.com/?q='
        lienduck = url+self.query
        webbrowser.open(lienduck)   

    def QwantSearch(self):
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': self.query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.open(lienQwant)


    def EcosiaSearch(self):
        url = 'https://www.ecosia.org/search'
        query = {'q': self.query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.open(lienEcosia) 

    def bingSearch(self):
        url = "https://www.bing.com/search"
        query = {'q': self.query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.open(lienbing)

    
    def rechercheDuckDuckGo(self):
        listReponse = []
        url = "https://api.duckduckgo.com/?q="
        fullUrl = url+self.query+"&format=json"
        response = requests.get(fullUrl)
        results = response.json()["RelatedTopics"]
        i = 0
        while i <= 2 :
            result_text = results[i]["Text"]
            translation = Translator(from_lang="en",to_lang="fr").translate(result_text)  
            i = i + 1
            listReponse.append(translation)
        
        return listReponse
    
    def GrandRecherche(self):
        i = 0
        while(i!=7):
            if (i==1) :
                self.googleSearch()
                time.sleep(1.5)
            else :
                if (i==2):                
                    self.QwantSearch()
                    time.sleep(1.5)
                else :
                    if(i==3):
                        self.duckduckgoSearch()
                        time.sleep(1.5)
                    else :
                        if(i==4):
                            self.EcosiaSearch()
                            time.sleep(1.5)
                        else :
                            if(i==5):
                                self.braveSearch()
                                time.sleep(1.5)
                            else :
                                if(i==6):
                                    self.bingSearch()
                                    time.sleep(1.5)
            i = i + 1