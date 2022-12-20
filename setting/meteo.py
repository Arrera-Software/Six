from tkinter import *
from function.JSON import*
from setting.view import*

def Meteo(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6)
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
        btnMeteoValider.config(command=valider)
        MeteoView()
    def Meteo2():
        NoAffichage()
        btnMeteo6.config(command=ExitModif)
        def valider():
            newVille = entryVille.get()
            EcritureJSON("setting/config.json","ville2",newVille)
            ExitModif()
        btnMeteoValider.config(command=valider)
        MeteoView()
    def Meteo3():
        NoAffichage()
        btnMeteo6.config(command=ExitModif)
        def valider():
            newVille = entryVille.get()
            EcritureJSON("setting/config.json","ville3",newVille)
            ExitModif()
        btnMeteoValider.config(command=valider)
        MeteoView()
    def Meteo4():
        NoAffichage()
        btnMeteo6.config(command=ExitModif)
        def valider():
            newVille = entryVille.get()
            EcritureJSON("setting/config.json","ville4",newVille)
            ExitModif()
        btnMeteoValider.config(command=valider)
        MeteoView()
    def Meteo5():
        NoAffichage()
        btnMeteo6.config(command=ExitModif)
        def valider():
            newVille = entryVille.get()
            EcritureJSON("setting/config.json","ville5",newVille)
            ExitModif()
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