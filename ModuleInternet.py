import webbrowser
import requests
Navigateur =  "/usr/bin/firefox"
def TestInternet():
    try:
        _ = requests.get("https://duckduckgo.com",timeout=5)
        return True
    except requests.ConnectionError :
        return False

def googleSearch(query):
    with requests.session() as c:
        url = 'https://www.google.com/search?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.get(Navigateur).open(liengoogle)

def duckduckgoSearch(query):
    with requests.session() as c:
        url = 'https://duckduckgo.com/?q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienduck = urllink.url
        webbrowser.get(Navigateur).open(lienduck)
    
def QwantSearch(query):
    with requests.session() as c:
        url = 'https://www.qwant.com/?l=fr&q'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienQwant = urllink.url
        webbrowser.get(Navigateur).open(lienQwant)

def EcosiaSearch(query):
    with requests.session() as c:
        url = 'https://www.ecosia.org/search'
        query = {'q': query}
        urllink = requests.get(url,query)
        lienEcosia = urllink.url
        webbrowser.get(Navigateur).open(lienEcosia)
  
def bingSearch(query):
    with requests.session() as c:
        url = "https://www.bing.com/search"
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienbing = urllink.url
        webbrowser.get(Navigateur).open(lienbing)
def LarousseSearch(query):
    with requests.session() as c:
        url = 'https://www.larousse.fr/dictionnaires/francais/'
        lienLarousse = url+query
        webbrowser.get(Navigateur).open(lienLarousse)
def WikipediaSearch(query):
    with requests.session() as c:
        url = 'https://fr.wikipedia.org/wiki/'
        lienWiki = url+query
        webbrowser.get(Navigateur).open(lienWiki)
def googleTrad(query):
    with requests.session() as c:
        url = 'https://translate.google.com/'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        liengoogle = urllink.url
        webbrowser.get(Navigateur).open(liengoogle) 
def WordreferenceSearch(query):
    with requests.session() as c:
        url = 'https://www.wordreference.com/fren/'
        lienWord = url+query
        webbrowser.get(Navigateur).open(lienWord)

def YTmusicSearch(query):
    with requests.session() as c:
        url = 'https://music.youtube.com/search'
        query = {'q': query}
        urllink = requests.get(url, params=query)
        lienYTmusic = urllink.url
        webbrowser.get(Navigateur).open(lienYTmusic)

def GrandRecherche(query):
    duckduckgoSearch(query)
    googleSearch(query)
    EcosiaSearch(query)
    bingSearch(query)
    QwantSearch(query)

def notion():
    webbrowser.get(Navigateur).open("https://www.notion.so")

def note():
    webbrowser.get(Navigateur).open("https://www.notion.so/5599107ab8fe4e3d9909f6817cfe1dd4?v=0e195d1b59674cbe99111a92f9d17f18")


def NotionGithub():
    webbrowser.get(Navigateur).open("https://www.notion.so/Depot-GitHub-d319a52d002642af80294c0553451a5f")

def NotionProjet():
    webbrowser.get(Navigateur).open("https://www.notion.so/e6b2105328f34126a0d2527e9fb1c917?v=3af36adfb00a4d29aa12c1187e7004ca")

def NotionCalendrier():
    webbrowser.get(Navigateur).open("https://www.notion.so/aac15dc1014b4d10ac8586bf4c682330?v=f3d6bd7d0a16479a9743442313e7026d")

def NotionToDo():
    webbrowser.get(Navigateur).open("https://www.notion.so/3f037048d43048aa935f74d0700ee0d7?v=6e2e75eb40c94d719f73bbe6e90a52ed")
def NotionCahierDeTache():
    webbrowser.get(Navigateur).open("https://www.notion.so/Cahier-de-tache-29b3259503584886b88b24f574f871ba")
def Libreview():
    webbrowser.get(Navigateur).open("https://www.libreview.com/glucosereports")

def DocPython():
    webbrowser.get(Navigateur).open("https://docs.python.org/3")
def DocArduino():
    webbrowser.get(Navigateur).open("https://docs.arduino.cc/")


def LeMonde():
    webbrowser.get(Navigateur).open("https://www.lemonde.fr/")

def VoixDuNord():
    webbrowser.get(Navigateur).open("https://www.lavoixdunord.fr/")
    

def ONU():
    webbrowser.get(Navigateur).open("https://news.un.org/fr/")

def Frandroid():
    webbrowser.get(Navigateur).open("https://www.frandroid.com/")

def Liberation():
    webbrowser.get(Navigateur).open("https://www.liberation.fr/")

def Mcarte():
    webbrowser.get(Navigateur).open("https://meteofrance.com/previsions-meteo-france/pas-de-calais/62")

def Mvigilance():
    webbrowser.get(Navigateur).open("https://vigilance.meteofrance.fr/fr")

def FlipBoard():
    webbrowser.get(Navigateur).open("https://flipboard.com/")

def CalendrierDia():
    webbrowser.get(Navigateur).open("https://calendar.google.com/calendar/u/0/gp?hl=fr")
def MAJcapt():
    webbrowser.get(Navigateur).open("https://www.freestylediabete.fr/maj-firmware")
def note():
    webbrowser.get(Navigateur).open("https://www.notion.so/Note-utile-2c163bc4b80c4b76ade427b527ab5704")
def insuline():
    webbrowser.get(Navigateur).open("https://www.notion.so/689dbc0bafea401b9127d72512fd6057?v=a9585f80d1ac4faa8785b21cf18b897a")
def repas():
    webbrowser.get(Navigateur).open("https://www.notion.so/Historique-des-repas-dfd8ab2629dd467c9ab13377dbd64e16")
def github():
    webbrowser.get(Navigateur).open("https://github.com/")
def YTmusic():
    webbrowser.get(Navigateur).open("https://music.youtube.com/")

def DocPython():
    webbrowser.get(Navigateur).open("https://docs.python.org/3")
def DocArduino():
    webbrowser.get(Navigateur).open("https://docs.arduino.cc/")