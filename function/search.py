import webbrowser
import requests
import time
from translate import*

def TestInternet():
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        return True
    except requests.ConnectionError :
        return False
    
def braveSearch(query):
    with requests.session() as c:
        url = 'https://search.brave.com/search?q='
        urllink = requests.get(url+query+"&source=web")
        lienBrave = urllink.url
        webbrowser.open(lienBrave)

def AmazonSearch(query):
    with requests.session() as c:
        url = 'https://www.amazon.fr/s?k='
        urllink = requests.get(url+query)
        lienAmazon = urllink.url
        webbrowser.open(lienAmazon)

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle)

def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.open(lienduck)   

def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.open(lienQwant)


def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.open(lienEcosia) 

def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.open(lienbing)

 
def rechercheDuckDuckGo(query):
    listReponse = []
    url = "https://api.duckduckgo.com/?q="
    fullUrl = url+query+"&format=json"
    response = requests.get(fullUrl)
    results = response.json()["RelatedTopics"]
    i = 0
    while i <= 2 :
        result_text = results[i]["Text"]
        translation = Translator(from_lang="en",to_lang="fr").translate(result_text)  
        i = i + 1
        listReponse.append(translation)
    
    return listReponse
    
def GrandRecherche(query):
    i = 0
    while(i!=7):
        if (i==1) :
            googleSearch(query)
            time.sleep(1.5)
        else :
            if (i==2):                
                QwantSearch(query)
                time.sleep(1.5)
            else :
                if(i==3):
                    duckduckgoSearch(query)
                    time.sleep(1.5)
                else :
                    if(i==4):
                        EcosiaSearch(query)
                        time.sleep(1.5)
                    else :
                        if(i==5):
                            braveSearch(query)
                            time.sleep(1.5)
                        else :
                            if(i==6):
                                bingSearch(query)
                                time.sleep(1.5)
        i = i + 1