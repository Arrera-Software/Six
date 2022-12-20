from tkinter import*
from src.speechRecognition import*
from src.voice import*
from setting.user import*
from setting.assistant import*
from setting.view import*
from setting.internet import*
from setting.meteo import*
from setting.appWeb import*
from setting.traduction import *


listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
    
def Setting(root,police):#fonction parametre
    ScreenPara = Tk()
    ScreenPara.title("SIX : Parametre")
    ScreenPara.iconphoto(False,PhotoImage(file="image/logo.png"))
    ScreenPara.maxsize(700,700)
    ScreenPara.minsize(700,700)
    left = Frame(ScreenPara,width=200,height=700,bg="#3c0b10") 
    right = Frame(ScreenPara,width=500,height=700,bg="#5e262c")
    #fonction
    def web():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        ParaWeb(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    def user():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        User(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    def assistant():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        Assistant(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,root,police)
    def meteo():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        Meteo(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    def appweb():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        AppWeb(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    def trad():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
        Trad(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    #widget
    #label
    labelTitre = Label(left,text="Paramètre",font=("arial","30"),bg="#3c0b10",fg="white")
    #bouton
    btnAssistant = Button(left,text="Assistant",bg="white",fg="black",font=("arial","15"),command=assistant)
    btnUttilisateur = Button(left,text="Utilisateurs",bg="white",fg="black",font=("arial","15"),command=user)
    btnInternet = Button(left,text="Internet",bg="white",fg="black",font=("arial","15"),command=web)
    btnMeteo = Button(left,text="Météo",bg="white",fg="black",font=("arial","15"),command=meteo)
    btnTraducteur = Button(left,text="Traducteur",bg="white",fg="black",font=("arial","15"),command=trad)
    btnAppWeb = Button(left,text="Application Web",bg="white",fg="black",font=("arial","15"),command=appweb)
    #affichage
    left.pack(side="left")
    right.pack(side="right")
    ViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo)
    labelTitre.place(x=5,y=5)
    ScreenPara.mainloop()