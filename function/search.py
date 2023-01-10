import webbrowser
import requests

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
def WikipediaSearch(query):
    with requests.session() as c:
        url = 'https://fr.wikipedia.org/wiki/'
        lienWiki = url+query
        webbrowser.open(lienWiki)
def ReversoSeacrch(query):
    with requests.session() as c:
        url = 'https://www.reverso.net/traduction-texte#sl=fra&tl=eng&text='
        urllink = requests.get(url+query)
        liengoogle = urllink.url
        webbrowser.open(liengoogle) 
def WordreferenceSearch(query):
    with requests.session() as c:
        url = 'https://www.wordreference.com/fren/'
        lienWord = url+query
        webbrowser.open(lienWord)
def YTmusicSearch(query):
    with requests.session() as c:
        url = 'https://music.youtube.com/search'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienYTmusic = urllink.url
        webbrowser.open(lienYTmusic)
def DocPython():
    webbrowser.open("https://docs.python.org/3")
def DocArduino():
    webbrowser.open("https://docs.python.org/3")
def GrandRecherche(query):
    i = 0
    while(i!=6):
        if (i==1) :
            googleSearch(query)
        else :
            if (i==2):                
                QwantSearch(query)
            else :
                if(i==3):
                    duckduckgoSearch(query)
                else :
                    if(i==4):
                        EcosiaSearch(query)
                    else :
                        if(i==5):
                            braveSearch(query)
        i = i + 1