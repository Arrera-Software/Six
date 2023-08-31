from tkinter import*
from function.JSON import*
import speech_recognition as sr
from gtts import gTTS
import os 
from playsound import playsound
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *

class Setting :  
    def __init__(self):#fonction parametre
        self.screen = Tk()
        self.screen.title("SIX : Parametre")
        self.screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        self.screen.maxsize(700,700)
        self.screen.minsize(700,700)
        self.left = Frame(self.screen,width=200,height=700,bg="#3c0b10") 
        self.right = Frame(self.screen,width=500,height=700,bg="#5e262c")
        self.listMoteur=["duckduckgo","google","qwant","ecosia","brave","bing"]
        self.listLienMoteur=["https://duckduckgo.com/","https://www.google.com/","https://www.qwant.com/","https://www.ecosia.org/","https://search.brave.com/","https://www.bing.com/search"]
        self.listGenre = ["monsieur","madame","maitre"]
        self.listTheme = ["default","white","black"]
        self.listLang = list(lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json").values())
        #fonction
        def web():
            self.NoViewBTN()
            self.ParaWeb()
        def user():
            self.NoViewBTN()
            self.User()
        def assistant():
            self.NoViewBTN()
            self.Assistant()
        def meteo():
            self.NoViewBTN()
            self.Meteo()
        def appweb():
            self.NoViewBTN()
            self.AppWeb()
        def trad():
            self.NoViewBTN()
            self.Trad()
        def interface():
            self.NoViewBTN()
            self.GUI()
        def app():
            self.NoViewBTN()
            self.Application()
        
        #widget
        #label
        self.labelTitre = Label(self.left,text="Paramètre",font=("arial","30"),bg="#3c0b10",fg="white")
        #bouton
        self.btnAssistant = Button(self.left,text="Assistant",bg="white",fg="black",font=("arial","15"),command=assistant)
        self.btnUttilisateur = Button(self.left,text="Utilisateurs",bg="white",fg="black",font=("arial","15"),command=user)
        self.btnInternet = Button(self.left,text="Internet",bg="white",fg="black",font=("arial","15"),command=web)
        self.btnMeteo = Button(self.left,text="Météo",bg="white",fg="black",font=("arial","15"),command=meteo)
        self.btnTraducteur = Button(self.left,text="Traducteur",bg="white",fg="black",font=("arial","15"),command=trad)
        self.btnAppWeb = Button(self.left,text="Application Web",bg="white",fg="black",font=("arial","15"),command=appweb)
        self.btnTheme = Button(self.left,text="Theme GUI",bg="white",fg="black",font=("arial","15"),command=interface)
        self.btnApp = Button(self.left,text="Application",bg="white",fg="black",font=("arial","15"),command=app)
        #affichage
        self.left.pack(side="left")
        self.right.pack(side="right")
        self.ViewBTN()
        self.labelTitre.place(x=5,y=5)
        self.screen.mainloop()
        
    def ViewBTN(self):
        self.btnAssistant.place(x=20,y=70)
        self.btnUttilisateur.place(x=20,y=140)
        self.btnInternet.place(x=20,y=210)
        self.btnAppWeb.place(x=20,y=280)
        self.btnTraducteur.place(x=20,y=350)
        self.btnMeteo.place(x=20,y=420)
        self.btnTheme.place(x=20,y=490)
        self.btnApp.place(x=20,y=560)
        
    def NoViewBTN(self):
        self.btnAssistant.place_forget()
        self.btnUttilisateur.place_forget()
        self.btnInternet.place_forget()
        self.btnAppWeb.place_forget()
        self.btnTraducteur.place_forget()
        self.btnMeteo.place_forget()
        self.btnTheme.place_forget()
        self.btnApp.place_forget()
        
    def ParaWeb(self):
        varMoteur = StringVar(self.screen)
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Affichage():
            labelWeb1.place(x=20,y=125)
            labelWeb2.place(x=20,y=185)
            labelWeb3.place(x=20,y=245)
            #labelWeb4.place(x=20,y=305)
            #labelWeb5.place(x=20,y=365)
        
            btnWeb1.place(x=265,y=125)
            btnWeb2.place(x=265,y=185)
            btnWeb3.place(x=265,y=245)
            #btnWeb4.place(x=265,y=305)
            #btnWeb5.place(x=265,y=365)
        def NoAffichage():
            labelWeb1.place_forget()
            labelWeb2.place_forget()
            labelWeb3.place_forget()
            #labelWeb4.place_forget()
            #labelWeb5.place_forget()
        
            btnWeb1.place_forget()
            btnWeb2.place_forget()
            btnWeb3.place_forget()
            #btnWeb4.place_forget()
            #btnWeb5.place_forget()
        def MoteurView():
            labelWeb6.place(x=20,y=125)
            menuGenre.place(x=100,y=230)
            btnValiderWeb.place(x=225,y=300)
        def NoMoteurView():
            labelWeb6.place_forget()
            menuGenre.place_forget()
            btnValiderWeb.place_forget()
        def ExitMoteur():
            NoMoteurView()
            btnWeb7.config(command=exit)
            Affichage()
        def Moteur():
            btnWeb7.config(command=ExitMoteur)
            def valider():
                newMoteur = varMoteur.get()
                EcritureJSON("setting/config.json","nameMoteur",newMoteur)
                if newMoteur == "duckduckgo" :
                    EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[0])
                else :
                    if newMoteur == "google" :
                        EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[1])
                    else :
                        if newMoteur == "qwant" :
                            EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[2])
                        else :
                            if newMoteur == "ecosia" :
                                EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[3])
                            else :
                                if newMoteur == "brave":
                                    EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[4])
                                else :
                                    EcritureJSON("setting/config.json","lienMoteur",self.listLienMoteur[5])
                ExitMoteur()
            btnValiderWeb.config(command=valider)
            moteur = lectureJSON("setting/config.json","nameMoteur")
            if moteur == "duckduckgo" :
                varMoteur.set(self.listMoteur[0])
            else :
                if moteur == "google" :
                    varMoteur.set(self.listMoteur[1])
                else :
                    if moteur == "qwant" :
                        varMoteur.set(self.listMoteur[2])
                    else :
                        if moteur == "ecosia" :
                            varMoteur.set(self.listMoteur[3])
                        else :
                            varMoteur.set(self.listMoteur[4])
            NoAffichage()
            MoteurView()
        def LienView():
            labelWeb7.place(x=20,y=125)
            entryLien.place(x=100,y=230)
            btnValiderWeb.place(x=225,y=300)
        def NoLienView():
            labelWeb7.place_forget()
            entryLien.place_forget()
            btnValiderWeb.place_forget()
        def ExitLien():
            NoLienView()
            Affichage()
            btnWeb7.config(command=exit)
        def Lien1():
            NoAffichage()
            btnWeb7.config(command=ExitLien)
            def Valider():
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","lien1",newLien)
                ExitLien()
                entryLien.delete(0, "end")
            btnValiderWeb.config(command=Valider)
            LienView()
        def Lien2():
            NoAffichage()
            btnWeb7.config(command=ExitLien)
            def Valider():
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","lien2",newLien)
                ExitLien()
                entryLien.delete(0, "end")
            btnValiderWeb.config(command=Valider)
            LienView()
        #declaration widget
        #btn
        btnWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Moteur)
        btnWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien1)
        btnWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien2)
        btnWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnValiderWeb = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
        #Label
        labelIndication =Label(section,text="Changer les lien de vos site\n qui vous sont utile",bg="#5e262c",font=("arial","15"),fg="white")
        labelWeb1 = Label(section,text="Moteur de recherche",bg="#5e262c",font=("arial","15"),fg="white")
        labelWeb2 = Label(section,text="Lien de l'agenda",bg="#5e262c",font=("arial","15"),fg="white")
        labelWeb3 = Label(section,text="Lien Stokage Cloud",bg="#5e262c",font=("arial","15"),fg="white")
        labelWeb6 = Label(section,text="Choisissez-votre moteur de recherche préférer",bg="#5e262c",font=("arial","15"),fg="white")
        labelWeb7 = Label(section,text="Lien :",bg="#5e262c",font=("arial","15"),fg="white")
        #entry
        entryLien = Entry(section,width=30,font=("arial","15"))
        #Menu deroulant 
        menuGenre = OptionMenu(section,varMoteur,*self.listMoteur)
        
        labelIndication.place(x=125,y=0)
        
        Affichage()
        
        btnWeb7.place(x=225,y=650)
        
    def prononciationMicro(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                Requette=r.recognize_google(audio,language='fr')
            except Exception as e:
                return "None" 
            return Requette
        
    def Assistant(self):
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Actualisation():
            labelAssistant1.config(text="Nom :"+lectureJSON("setting/config.json","nomAssistant"))
        def Afficher():
            labelAssistant1.place(x=20,y=125)
            labelAssistant2.place(x=20,y=225)
            btnAssistant1.place(x=250,y=125)
            btnAssistant2.place(x=250,y=225)
        def NoAfficher():
            labelAssistant1.place_forget()
            labelAssistant2.place_forget()
            btnAssistant1.place_forget()
            btnAssistant2.place_forget()
        def ExitName():
            labelAssistant3.place_forget()
            entryName.place_forget()
            btnAssistantValider.place_forget()
            btnAssistant3.config(command=exit)
            Afficher()
        def ExitPrononciation():
            labelAssistant4.place_forget()
            btnAssistant4.place_forget()
            btnAssistant5.place_forget()
            btnAssistantValider.place_forget()
            btnAssistant3.config(command=exit)
            Afficher()
        def AssistantName():
            NoAfficher()
            def ValiderName():
                newName = entryName.get()
                EcritureJSON("setting/config.json","nomAssistant",newName)
                ExitName()
                Afficher()
                Actualisation()
                entryName.delete(0, "end")
            btnAssistant3.config(command=ExitName)
            btnAssistantValider.config(command=ValiderName)
            labelAssistant3.place(x=20,y=125)
            entryName.place(x=100,y=230)
            btnAssistantValider.place(x=225,y=300)
        def AssistantPronociation():
            NoAfficher()
            btnAssistant3.config(command=ExitPrononciation)
            def ValiderPronociation():
                ExitPrononciation()
            def Ecoute():
                tts = gTTS(lectureJSON("setting/config.json","pronociationAssistant"), lang="fr")
                tts.save("voc.mp3")
                playsound("voc.mp3")
                os.remove("voc.mp3")
            def micro():
                var = self.prononciationMicro()
                EcritureJSON("setting/config.json","pronociationAssistant",var)
            btnAssistantValider.config(command=ValiderPronociation)
            btnAssistant4.config(command=micro)
            btnAssistant5.config(command=Ecoute)
            labelAssistant4.place(x=20,y=125)
            btnAssistant4.place(x=50,y=230)
            btnAssistant5.place(x=50,y=330)
            btnAssistantValider.place(x=225,y=400)
        #declaration widget
        #btn
        btnAssistant1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=AssistantName)
        btnAssistant2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=AssistantPronociation)
        btnAssistant3 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnAssistant4 = Button(section,text="Appuyer pour parler",bg="#3c0b10",font=("arial","15"),fg="white")
        btnAssistant5 = Button(section,text="Ecouter",bg="#3c0b10",font=("arial","15"),fg="white")
        btnAssistantValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
        #Label
        labelIndication =Label(section,text="Changer le nom de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
        labelAssistant1 = Label(section,text="Nom :"+lectureJSON("setting/config.json","nomAssistant"),bg="#5e262c",font=("arial","15"),fg="white")
        labelAssistant2 = Label(section,text="Pronociation",bg="#5e262c",font=("arial","15"),fg="white")
        labelAssistant3 = Label(section,text="Nouveau nom :",bg="#5e262c",font=("arial","15"),fg="white")
        labelAssistant4 = Label(section,text="Pronication du nom de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
        labelIndication.place(x=125,y=0)
        #entry
        entryName = Entry(section,width=30,font=("arial","15"))
        Afficher()
        
        btnAssistant3.place(x=225,y=525)
        
    def User(self):
        varGenre = StringVar(self.screen)
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def Actulisaton():
            labelUser1.config(text=lectureJSON("setting/config.json","userGenre1")+" "+lectureJSON("setting/config.json","user1"))
            labelUser2.config(text=lectureJSON("setting/config.json","userGenre2")+" "+lectureJSON("setting/config.json","user2"))
            labelUser3.config(text=lectureJSON("setting/config.json","userGenre3")+" "+lectureJSON("setting/config.json","user3"))
            labelUser4.config(text=lectureJSON("setting/config.json","userGenre4")+" "+lectureJSON("setting/config.json","user4"))
        def userView():
            labelUserGenre.place(x=20,y=125)
            labelUserName.place(x=20,y=225)
            entryName.place(x=100,y=230)
            menuGenre.place(x=100,y=130)
            btnUserValider.place(x=225,y=300)
        def userNoView():
            labelUserGenre.place_forget()
            labelUserName.place_forget()
            entryName.place_forget()
            menuGenre.place_forget()
            btnUserValider.place_forget()
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def exitModif():
            Afficher()
            userNoView()
            btnUser5.config(command=exit)
        def User1():
            btnUser5.config(command=exitModif)
            def Valider1():
                newName=entryName.get()
                newGenre = varGenre.get()
                EcritureJSON("setting/config.json","user1",newName)
                EcritureJSON("setting/config.json","userGenre1",newGenre)
                exitModif()
                Actulisaton()
                entryName.delete(0, "end")
            genre = lectureJSON("setting/config.json","userGenre1")
            if genre == "monsieur" :
                varGenre.set(self.listGenre[0])
            else :
                if genre == "madame" :
                    varGenre.set(self.listGenre[1])
                else :
                    varGenre.set(self.listGenre[2])
            btnUserValider.config(command=Valider1)  
            NoAfficher()
            userView()
        def User2():
            btnUser5.config(command=exitModif)
            def Valider1():
                newName=entryName.get()
                newGenre = varGenre.get()
                EcritureJSON("setting/config.json","user2",newName)
                EcritureJSON("setting/config.json","userGenre2",newGenre)
                exitModif()
                Actulisaton()
                entryName.delete(0, "end")
            genre = lectureJSON("setting/config.json","userGenre2")
            if genre == "monsieur" :
                varGenre.set(self.listGenre[0])
            else :
                if genre == "madame" :
                    varGenre.set(self.listGenre[1])
                else :
                    varGenre.set(self.listGenre[2])
            btnUserValider.config(command=Valider1)  
            NoAfficher()
            userView()
        def User3():
            btnUser5.config(command=exitModif)
            def Valider1():
                newName=entryName.get()
                newGenre = varGenre.get()
                EcritureJSON("setting/config.json","user3",newName)
                EcritureJSON("setting/config.json","userGenre3",newGenre)
                exitModif()
                Actulisaton()
                entryName.delete(0, "end")
            genre = lectureJSON("setting/config.json","userGenre3")
            if genre == "monsieur" :
                varGenre.set(self.listGenre[0])
            else :
                if genre == "madame" :
                    varGenre.set(self.listGenre[1])
                else :
                    varGenre.set(self.listGenre[2])
            btnUserValider.config(command=Valider1)  
            NoAfficher()
            userView()
        def User4():
            btnUser5.config(command=exitModif)
            def Valider1():
                newName=entryName.get()
                newGenre = varGenre.get()
                EcritureJSON("setting/config.json","user4",newName)
                EcritureJSON("setting/config.json","userGenre4",newGenre)
                exitModif()
                Actulisaton()
                entryName.delete(0, "end")
            genre = lectureJSON("setting/config.json","userGenre4")
            if genre == "monsieur" :
                varGenre.set(self.listGenre[0])
            else :
                if genre == "madame" :
                    varGenre.set(self.listGenre[1])
                else :
                    varGenre.set(self.listGenre[2])
            btnUserValider.config(command=Valider1)  
            NoAfficher()
            userView()
        #declaration widget
        #btn
        btnUser1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User1)
        btnUser2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User2)
        btnUser3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User3)
        btnUser4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User4)
        btnUser5 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnUserValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
        #Label
        labelIndication =Label(section,text="Changer votre nom d'utilisateur",bg="#5e262c",font=("arial","15"),fg="white")
        labelUser1 = Label(section,text=lectureJSON("setting/config.json","userGenre1")+" "+lectureJSON("setting/config.json","user1"),bg="#5e262c",font=("arial","15"),fg="white")
        labelUser2 = Label(section,text=lectureJSON("setting/config.json","userGenre2")+" "+lectureJSON("setting/config.json","user2"),bg="#5e262c",font=("arial","15"),fg="white")
        labelUser3 = Label(section,text=lectureJSON("setting/config.json","userGenre3")+" "+lectureJSON("setting/config.json","user3"),bg="#5e262c",font=("arial","15"),fg="white")
        labelUser4 = Label(section,text=lectureJSON("setting/config.json","userGenre4")+" "+lectureJSON("setting/config.json","user4"),bg="#5e262c",font=("arial","15"),fg="white")
        
        labelUserGenre = Label(section,text="Genre : ",bg="#5e262c",font=("arial","15"),fg="white")
        labelUserName = Label(section,text="Nom : ",bg="#5e262c",font=("arial","15"),fg="white")
        
        labelIndication.place(x=125,y=0)
        #entry
        entryName = Entry(section,width=30,font=("arial","15"))
        #Menu deroulant 
        menuGenre = OptionMenu(section,varGenre,*self.listGenre)
        def Afficher():
            labelUser1.place(x=20,y=125)
            labelUser2.place(x=20,y=225)
            labelUser3.place(x=20,y=325)
            labelUser4.place(x=20,y=425)
        
            btnUser1.place(x=250,y=125)
            btnUser2.place(x=250,y=225)
            btnUser3.place(x=250,y=325)
            btnUser4.place(x=250,y=425)
            btnUser5.place(x=225,y=525)
        def NoAfficher():
            labelUser1.place_forget()
            labelUser2.place_forget()
            labelUser3.place_forget()
            labelUser4.place_forget()
        
            btnUser1.place_forget()
            btnUser2.place_forget()
            btnUser3.place_forget()
            btnUser4.place_forget()
        
        Afficher()
    
    def Meteo(self):
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Affichage():
            labelMeteo1.place(x=20,y=125)
            labelMeteo2.place(x=20,y=225)
            labelMeteo3.place(x=20,y=325)
            labelMeteo4.place(x=20,y=425)
            labelMeteo5.place(x=20,y=525)
        
            btnMeteo1.place(x=195,y=125)
            btnMeteo2.place(x=195,y=225)
            btnMeteo3.place(x=195,y=325)
            btnMeteo4.place(x=195,y=425)
            btnMeteo5.place(x=195,y=525)
        def NoAffichage():
            labelMeteo1.place_forget()
            labelMeteo2.place_forget()
            labelMeteo3.place_forget()
            labelMeteo4.place_forget()
            labelMeteo5.place_forget()
            btnMeteo1.place_forget()
            btnMeteo2.place_forget()
            btnMeteo3.place_forget()
            btnMeteo4.place_forget()
            btnMeteo5.place_forget()
        def MeteoView():
            labelMeteo6.place(x=20,y=125)
            entryVille.place(x=100,y=230)
            btnMeteoValider.place(x=225,y=300)
        def NoMeteoView():
            labelMeteo6.place_forget()
            entryVille.place_forget()
            btnMeteoValider.place_forget()
        def ExitModif():
            btnMeteo6.config(command=exit)
            Affichage()
            NoMeteoView()
        def Meteo1():
            NoAffichage()
            btnMeteo6.config(command=ExitModif)
            def valider():
                newVille = entryVille.get()
                EcritureJSON("setting/config.json","ville1",newVille)
                ExitModif()
                entryVille.delete(0, "end")
            btnMeteoValider.config(command=valider)
            MeteoView()
        def Meteo2():
            NoAffichage()
            btnMeteo6.config(command=ExitModif)
            def valider():
                newVille = entryVille.get()
                EcritureJSON("setting/config.json","ville2",newVille)
                ExitModif()
                entryVille.delete(0, "end")
            btnMeteoValider.config(command=valider)
            MeteoView()
        def Meteo3():
            NoAffichage()
            btnMeteo6.config(command=ExitModif)
            def valider():
                newVille = entryVille.get()
                EcritureJSON("setting/config.json","ville3",newVille)
                ExitModif()
                entryVille.delete(0, "end")
            btnMeteoValider.config(command=valider)
            MeteoView()
        def Meteo4():
            NoAffichage()
            btnMeteo6.config(command=ExitModif)
            def valider():
                newVille = entryVille.get()
                EcritureJSON("setting/config.json","ville4",newVille)
                ExitModif()
                entryVille.delete(0, "end")
            btnMeteoValider.config(command=valider)
            MeteoView()
        def Meteo5():
            NoAffichage()
            btnMeteo6.config(command=ExitModif)
            def valider():
                newVille = entryVille.get()
                EcritureJSON("setting/config.json","ville5",newVille)
                ExitModif()
                entryVille.delete(0, "end")
            btnMeteoValider.config(command=valider)
            MeteoView()
    #declaration widget
        #btn
        btnMeteo1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Meteo1)
        btnMeteo2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Meteo2)
        btnMeteo3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Meteo3)
        btnMeteo4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Meteo4)
        btnMeteo5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Meteo5)
        btnMeteo6 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnMeteoValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
        #Label
        labelIndication =Label(section,text="Changer la localisation \nde vos lieu",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo1 = Label(section,text="Lieu de domicile",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo2 = Label(section,text="Lieu Favorie",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo3 = Label(section,text="Lieu de travail",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo4 = Label(section,text="Lieu de vacances",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo5 = Label(section,text="Lieu Bonnus",bg="#5e262c",font=("arial","15"),fg="white")
        labelMeteo6 = Label(section,text="Nom de la ville :",bg="#5e262c",font=("arial","15"),fg="white") 
        #entry
        entryVille = Entry(section,width=30,font=("arial","15"))
        
        labelIndication.place(x=125,y=0)
        
        Affichage()
        
        btnMeteo6.place(x=225,y=625)
        
    def AppWeb(self):
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Actulisation():
        
            labelAppWeb1.config(text="App 2 :"+lectureJSON("setting/config.json","appWeb2Name"))
            labelAppWeb2.config(text="App 3 :"+lectureJSON("setting/config.json","appWeb3Name"))
            labelAppWeb3.config(text="App 1 :"+lectureJSON("setting/config.json","appWeb4Name"))
            labelAppWeb4.config(text="App 1 :"+lectureJSON("setting/config.json","appWeb5Name"))
        def Affichage():
            
            labelAppWeb1.place(x=20,y=125)
            labelAppWeb2.place(x=20,y=185)
            labelAppWeb3.place(x=20,y=245)
            labelAppWeb4.place(x=20,y=305)
        
        
            btnAppWeb1.place(x=265,y=125)
            btnAppWeb2.place(x=265,y=185)
            btnAppWeb3.place(x=265,y=245)
            btnAppWeb4.place(x=265,y=305)
        def NoAffichage():
            
            labelAppWeb1.place_forget()
            labelAppWeb2.place_forget()
            labelAppWeb3.place_forget()
            labelAppWeb4.place_forget()
        
            
            btnAppWeb1.place_forget()
            btnAppWeb2.place_forget()
            btnAppWeb3.place_forget()
            btnAppWeb4.place_forget()
        def NoViewApp():
            entryLien.place_forget()
            entryName.place_forget()
            btnAppValider.place_forget()
            labelAppWeb5.place_forget()
            labelAppWeb6.place_forget()
        def ViewApp():
            labelAppWeb5.place(x=20,y=125)
            labelAppWeb6.place(x=20,y=225)
            btnAppValider.place(x=225,y=300)
            entryName.place(x=100,y=130)
            entryLien.place(x=100,y=230)
        def ExitModif():
            btnAppWeb5.config(command=exit)
            NoViewApp()
            Affichage()
        
        def App1():
            btnAppWeb5.config(command=ExitModif)
            def valider1():
                newName = entryName.get()
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","appWeb2Name",newName)
                EcritureJSON("setting/config.json","appWeb2Lien",newLien)
                ExitModif()
                Actulisation()
                entryLien.delete(0, "end")
                entryName.delete(0, "end")
            btnAppValider.config(command=valider1)
            NoAffichage()
            ViewApp()
        def App2():
            btnAppWeb5.config(command=ExitModif)
            def valider1():
                newName = entryName.get()
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","appWeb3Name",newName)
                EcritureJSON("setting/config.json","appWeb3Lien",newLien)
                ExitModif()
                Actulisation()
                entryLien.delete(0, "end")
                entryName.delete(0, "end")
            btnAppValider.config(command=valider1)
            NoAffichage()
            ViewApp()
        def App3():
            btnAppWeb5.config(command=ExitModif)
            def valider1():
                newName = entryName.get()
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","appWeb4Name",newName)
                EcritureJSON("setting/config.json","appWeb4Lien",newLien)
                ExitModif()
                Actulisation()
                entryLien.delete(0, "end")
                entryName.delete(0, "end")
            btnAppValider.config(command=valider1)
            NoAffichage()
            ViewApp()
        def App4():
            btnAppWeb5.config(command=ExitModif)
            def valider1():
                newName = entryName.get()
                newLien = entryLien.get()
                EcritureJSON("setting/config.json","appWeb5Name",newName)
                EcritureJSON("setting/config.json","appWeb5Lien",newLien)
                ExitModif()
                Actulisation()
                entryLien.delete(0, "end")
                entryName.delete(0, "end")
            btnAppValider.config(command=valider1)
            NoAffichage()
            ViewApp()
        #declaration widget
        #btn
        btnAppWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App1)
        btnAppWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App2)
        btnAppWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App3)
        btnAppWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App4)
        btnAppWeb5 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnAppValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
        #Label
        labelIndication =Label(section,text="Ajouter votre application web ou \nsite internet preférée",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb1 = Label(section,text="App 1 :"+lectureJSON("setting/config.json","appWeb2Name"),bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb2 = Label(section,text="App 2 :"+lectureJSON("setting/config.json","appWeb3Name"),bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb3 = Label(section,text="App 3 :"+lectureJSON("setting/config.json","appWeb4Name"),bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb4 = Label(section,text="App 4 :"+lectureJSON("setting/config.json","appWeb5Name"),bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb5  = Label(section,text="Nom : ",bg="#5e262c",font=("arial","15"),fg="white") 
        labelAppWeb6  = Label(section,text="Lien : ",bg="#5e262c",font=("arial","15"),fg="white") 
        
        #entry
        entryLien = Entry(section,width=30,font=("arial","15"))
        entryName = Entry(section,width=30,font=("arial","15"))
        
        labelIndication.place(x=125,y=0)
        
        Affichage()
        
        btnAppWeb5.place(x=225,y=650)
        
    def Trad(self):
        varLang = StringVar(self.screen)
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        #fonction
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Valider():
                nameLang = varLang.get()
                newLang = searchKey(nameLang,lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json"))
                EcritureJSON("setting/config.json","langTradDefault",newLang)
                exit()
                
        def tradView():
            labelTrad1.place(x=20,y=125)
            menuLangue.place(x=100,y=230)
            btnTradValider.place(x=225,y=300)
            listLang = list(lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json").values())
            langSortieDefault = lectureJSON("setting/config.json","langTradDefault")
            dictTrad = lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json")
            
            i=0
            while i < len(listLang):
                if (dictTrad[langSortieDefault]==listLang[i]):
                    varLang.set(listLang[i])
                    i=len(listLang)
                else :
                    i = i + 1
            
        #declaration widget
        #btn
        btnTrad1 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        btnTradValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white",command=Valider)
        #Label
        labelIndication =Label(section,text="Modifier la langue de l'outil \nde traduction de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
        labelTrad1 = Label(section,text="Langue :",bg="#5e262c",font=("arial","15"),fg="white")
        #Menu deroulant 
        menuLangue = OptionMenu(section,varLang,*self.listLang)
        
        labelIndication.place(x=125,y=0)
        
        tradView()
        
        btnTrad1.place(x=225,y=650)
        
    def GUI(self):
        self.right.pack_forget()
        varTheme = StringVar(self.screen)
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        def Affichage():
            btnGUIValider.place(x=195,y=125) 
            menuTheme.place(x=20,y=125)
        def valider():
            newTheme = varTheme.get()
            EcritureJSON("setting/config.json","theme",newTheme)
            showinfo(title="SIX : Parametre",message="Vous devez redemarré l'assistant pour\nvoir le changement de l'interface")
            exit()
        #declaration widget
        #btn
        btnGUIValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white",command=valider)
        btnGUI1 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        #label
        labelIndication =Label(section,text="Modifier le theme de l'interface \nde principal de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
        #menu
        menuTheme = OptionMenu(section,varTheme,*self.listTheme)
        if lectureJSON("setting/config.json","theme") == "default" :
            varTheme.set(self.listTheme[0])
        else :
            if lectureJSON("setting/config.json","theme") == "white":
                varTheme.set(self.listTheme[1])
            else :
                varTheme.set(self.listTheme[2])
        
        Affichage()
        
        btnGUI1.place(x=225,y=625)
        labelIndication.place(x=125,y=0)
        
    def Application(self):
        self.right.pack_forget()
        section= Frame(self.screen,width=500,height=700,bg="#5e262c")
        section.pack(side="right")
        def exit():
            section.pack_forget()
            self.right.pack(side="right")
            self.ViewBTN()
        
        def Affichage():
            labelAppWeb1.place(x=20,y=125)
            labelAppWeb2.place(x=20,y=185)
            labelAppWeb3.place(x=20,y=245)
            labelAppWeb4.place(x=20,y=305)
            labelAppWeb5.place(x=20,y=365)
            labelAppWeb6.place(x=20,y=425)
        
            btnAppWeb1.place(x=265,y=125)
            btnAppWeb2.place(x=265,y=185)
            btnAppWeb3.place(x=265,y=245)
            btnAppWeb4.place(x=265,y=305)
            btnAppWeb5.place(x=265,y=365)
            btnAppWeb6.place(x=265,y=425)
        
        def NoAffichage():
            labelAppWeb1.place_forget()
            labelAppWeb2.place_forget()
            labelAppWeb3.place_forget()
            labelAppWeb4.place_forget()
            labelAppWeb5.place_forget()
            labelAppWeb6.place_forget()
        
            btnAppWeb1.place_forget()
            btnAppWeb2.place_forget()
            btnAppWeb3.place_forget()
            btnAppWeb4.place_forget()
            btnAppWeb5.place_forget()
            btnAppWeb6.place_forget()
        
        def note():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","appNote",str(var))
            exit()
        
        def navigateurInternet():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","navigateurInternet",str(var))
            exit()
            
        def editeurtext():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","editeurtexte",str(var))
            exit()
        
        def presentation():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","editeurpresentation",str(var))
            exit()
            
        def tableur():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","tableur",str(var))
            exit()
            
        def musique():
            messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
            var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
            EcritureJSON("setting/config.json","appMusique",str(var))
            exit()
            
        #btn
        btnAppWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=note)
        btnAppWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=navigateurInternet)
        btnAppWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=editeurtext)
        btnAppWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=presentation)
        btnAppWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=tableur)
        btnAppWeb6 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=musique)
        btnAppWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
        #Label
        labelIndication =Label(section,text="Selectionner les racourcie qui correspont au\napplication suivante:",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb1 = Label(section,text="Application note",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb2 = Label(section,text="Navigateur internet",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb3 = Label(section,text="Editeur de texte",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb4 = Label(section,text="Editeur de presentation",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb5 = Label(section,text="Tableur",bg="#5e262c",font=("arial","15"),fg="white")
        labelAppWeb6  = Label(section,text="Musique",bg="#5e262c",font=("arial","15"),fg="white") 

        labelIndication.place(x=95,y=0)
        
        Affichage()
        
        btnAppWeb7.place(x=225,y=650)