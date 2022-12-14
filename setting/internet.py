from tkinter import *
from function.JSON import*
from setting.view import*
listMoteur=["duckduckgo","google","qwant","ecosia","brave"]
listLienMoteur=["https://duckduckgo.com/","https://www.google.com/","https://www.qwant.com/","https://www.ecosia.org/","https://search.brave.com/"]
def Web(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6)
   #declaration widget
    #btn
    btnWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Changer les des application de propriété",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb1 = Label(section,text="Moteur de recherche",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb2 = Label(section,text="Lien de l'agenda",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb3 = Label(section,text="Lien Stokage Cloud",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb4 = Label(section,text="Lien de Note",bg="#5e262c",font=("arial","15"),fg="white")
    labelWeb5 = Label(section,text="Lien de votre TO DO LIST",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
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
    
    btnWeb7.place(x=225,y=650)
    