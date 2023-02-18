from tkinter import*
from setting.user import*
from setting.assistant import*
from setting.view import*
from setting.internet import*
from setting.meteo import*
from setting.appWeb import*
from setting.traduction import *
from setting.GUITheme import*
from setting.application import*

listMoteur = "google" , "duckduckgo" , "ecosia" , "qwant" , "bing"
    
def Setting():#fonction parametre
    ScreenPara = Tk()
    ScreenPara.title("SIX : Parametre")
    ScreenPara.iconphoto(False,PhotoImage(file="image/logo.png"))
    ScreenPara.maxsize(700,700)
    ScreenPara.minsize(700,700)
    left = Frame(ScreenPara,width=200,height=700,bg="#3c0b10") 
    right = Frame(ScreenPara,width=500,height=700,bg="#5e262c")
    #fonction
    def web():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        ParaWeb(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def user():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        User(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def assistant():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        Assistant(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def meteo():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        Meteo(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme)
    def appweb():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        AppWeb(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def trad():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        Trad(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def interface():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        GUI(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    def app():
        NoViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
        Application(right,ScreenPara,btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    
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
    btnTheme = Button(left,text="Theme GUI",bg="white",fg="black",font=("arial","15"),command=interface)
    btnApp = Button(left,text="Application",bg="white",fg="black",font=("arial","15"),command=app)
    #affichage
    left.pack(side="left")
    right.pack(side="right")
    ViewBTN(btnAssistant,btnUttilisateur,btnInternet,btnAppWeb,btnTraducteur,btnMeteo,btnTheme,btnApp)
    labelTitre.place(x=5,y=5)
    ScreenPara.mainloop()