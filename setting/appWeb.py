from tkinter import *
from function.JSON import*
from setting.view import*


def AppWeb(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6)
    def Actulisation():
        labelAppWeb1.config(text="App 1 :"+lectureJSON("setting/config.json","appWeb1Name"))
        labelAppWeb2.config(text="App 2 :"+lectureJSON("setting/config.json","appWeb2Name"))
        labelAppWeb3.config(text="App 3 :"+lectureJSON("setting/config.json","appWeb3Name"))
        labelAppWeb4.config(text="App 1 :"+lectureJSON("setting/config.json","appWeb4Name"))
        labelAppWeb5.config(text="App 1 :"+lectureJSON("setting/config.json","appWeb5Name"))
    def Affichage():
        labelAppWeb1.place(x=20,y=125)
        labelAppWeb2.place(x=20,y=185)
        labelAppWeb3.place(x=20,y=245)
        labelAppWeb4.place(x=20,y=305)
        labelAppWeb5.place(x=20,y=365)
    
        btnAppWeb1.place(x=265,y=125)
        btnAppWeb2.place(x=265,y=185)
        btnAppWeb3.place(x=265,y=245)
        btnAppWeb4.place(x=265,y=305)
        btnAppWeb5.place(x=265,y=365)
    def NoAffichage():
        labelAppWeb1.place_forget()
        labelAppWeb2.place_forget()
        labelAppWeb3.place_forget()
        labelAppWeb4.place_forget()
        labelAppWeb5.place_forget()
    
        btnAppWeb1.place_forget()
        btnAppWeb2.place_forget()
        btnAppWeb3.place_forget()
        btnAppWeb4.place_forget()
        btnAppWeb5.place_forget()
    def NoViewApp():
        entryLien.place_forget()
        entryName.place_forget()
        btnAppValider.place_forget()
        labelAppWeb6.place_forget()
        labelAppWeb7.place_forget()
    def ViewApp():
        labelAppWeb6.place(x=20,y=125)
        labelAppWeb7.place(x=20,y=225)
        btnAppValider.place(x=225,y=300)
        entryName.place(x=100,y=130)
        entryLien.place(x=100,y=230)
    def ExitModif():
        btnAppWeb7.config(command=exit)
        NoViewApp()
        Affichage()
    def App1():
        btnAppWeb7.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","appWeb1Name",newName)
            EcritureJSON("setting/config.json","appWeb1Lien",newLien)
            ExitModif()
            Actulisation()
        btnAppValider.config(command=valider1)
        NoAffichage()
        ViewApp()
    def App2():
        btnAppWeb7.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","appWeb2Name",newName)
            EcritureJSON("setting/config.json","appWeb2Lien",newLien)
            ExitModif()
            Actulisation()
        btnAppValider.config(command=valider1)
        NoAffichage()
        ViewApp()
    def App3():
        btnAppWeb7.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","appWeb3Name",newName)
            EcritureJSON("setting/config.json","appWeb3Lien",newLien)
            ExitModif()
            Actulisation()
        btnAppValider.config(command=valider1)
        NoAffichage()
        ViewApp()
    def App4():
        btnAppWeb7.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","appWeb4Name",newName)
            EcritureJSON("setting/config.json","appWeb4Lien",newLien)
            ExitModif()
            Actulisation()
        btnAppValider.config(command=valider1)
        NoAffichage()
        ViewApp()
    def App5():
        btnAppWeb7.config(command=ExitModif)
        def valider1():
            newName = entryName.get()
            newLien = entryLien.get()
            EcritureJSON("setting/config.json","appWeb5Name",newName)
            EcritureJSON("setting/config.json","appWeb5Lien",newLien)
            ExitModif()
            Actulisation()
        btnAppValider.config(command=valider1)
        NoAffichage()
        ViewApp()
    #declaration widget
    #btn
    btnAppWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App1)
    btnAppWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App2)
    btnAppWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App3)
    btnAppWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App4)
    btnAppWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=App5)
    btnAppWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    btnAppValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
    #Label
    labelIndication =Label(section,text="Ajouter votre application web ou \nsite internet preférée",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb1 = Label(section,text="App 1 :"+lectureJSON("setting/config.json","appWeb1Name"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb2 = Label(section,text="App 2 :"+lectureJSON("setting/config.json","appWeb2Name"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb3 = Label(section,text="App 3 :"+lectureJSON("setting/config.json","appWeb3Name"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb4 = Label(section,text="App 4 :"+lectureJSON("setting/config.json","appWeb4Name"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb5 = Label(section,text="App 5 :"+lectureJSON("setting/config.json","appWeb5Name"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb6  = Label(section,text="Nom : ",bg="#5e262c",font=("arial","15"),fg="white") 
    labelAppWeb7  = Label(section,text="Lien : ",bg="#5e262c",font=("arial","15"),fg="white") 
    
    #entry
    entryLien = Entry(section,width=30,font=("arial","15"))
    entryName = Entry(section,width=30,font=("arial","15"))
    
    labelIndication.place(x=125,y=0)
    
    Affichage()
    
    btnAppWeb7.place(x=225,y=650)