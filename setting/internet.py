from tkinter import *
from function.JSON import*
from setting.view import*
listMoteur=["duckduckgo","google","qwant","ecosia","brave"]
listLienMoteur=["https://duckduckgo.com/","https://www.google.com/","https://www.qwant.com/","https://www.ecosia.org/","https://search.brave.com/"]
def ParaWeb(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
    varMoteur = StringVar(screen)
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6)
    def Affichage():
        labelWeb1.place(x=20,y=125)
        labelWeb2.place(x=20,y=185)
        labelWeb3.place(x=20,y=245)
        labelWeb4.place(x=20,y=305)
        labelWeb5.place(x=20,y=365)
    
        btnWeb1.place(x=265,y=125)
        btnWeb2.place(x=265,y=185)
        btnWeb3.place(x=265,y=245)
        btnWeb4.place(x=265,y=305)
        btnWeb5.place(x=265,y=365)
    def NoAffichage():
        labelWeb1.place_forget()
        labelWeb2.place_forget()
        labelWeb3.place_forget()
        labelWeb4.place_forget()
        labelWeb5.place_forget()
    
        btnWeb1.place_forget()
        btnWeb2.place_forget()
        btnWeb3.place_forget()
        btnWeb4.place_forget()
        btnWeb5.place_forget()
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
                EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[0])
            else :
                if newMoteur == "google" :
                    EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[1])
                else :
                    if newMoteur == "qwant" :
                        EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[2])
                    else :
                        if newMoteur == "ecosia" :
                            EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[3])
                        else :
                            EcritureJSON("setting/config.json","lienMoteur",listLienMoteur[4])
            ExitMoteur()
        btnValiderWeb.config(command=valider)
        moteur = lectureJSON("setting/config.json","nameMoteur")
        if moteur == "duckduckgo" :
            varMoteur.set(listMoteur[0])
        else :
            if moteur == "google" :
                varMoteur.set(listMoteur[1])
            else :
                if moteur == "qwant" :
                    varMoteur.set(listMoteur[2])
                else :
                    if moteur == "ecosia" :
                        varMoteur.set(listMoteur[3])
                    else :
                        varMoteur.set(listMoteur[4])
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
        btnValiderWeb.config(command=Valider)
        LienView()
    def Lien2():
        NoAffichage()
        btnWeb7.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lien2",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    def Lien3():
        NoAffichage()
        btnWeb7.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lien3",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    def Lien4():
        NoAffichage()
        btnWeb7.config(command=ExitLien)
        def Valider():
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","lien4",newLien)
            ExitLien()
        btnValiderWeb.config(command=Valider)
        LienView()
    #declaration widget
    #btn
    btnWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Moteur)
    btnWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien1)
    btnWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien2)
    btnWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien3)
    btnWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=Lien4)
    btnWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    btnValiderWeb = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
    #Label
    labelIndication =Label(section,text="Changer les lien de vos site\n qui vous sont utile",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb1 = Label(section,text="Moteur de recherche",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb2 = Label(section,text="Lien de l'agenda",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb3 = Label(section,text="Lien Stokage Cloud",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb4 = Label(section,text="Lien de Note",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb5 = Label(section,text="Lien de votre TO DO LIST",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb6 = Label(section,text="Choisissez-votre moteur de recherche préférer",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb7 = Label(section,text="Lien :",bg="#5e262c",font=("arial","15"),fg="white")
    #entry
    entryLien = Entry(section,width=30,font=("arial","15"))
    #Menu deroulant 
    menuGenre = OptionMenu(section,varMoteur,*listMoteur)
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnWeb7.place(x=225,y=650)
    