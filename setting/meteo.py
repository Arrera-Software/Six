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
   #declaration widget
    #btn
    btnMeteo1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnMeteo2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnMeteo3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnMeteo4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnMeteo5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnMeteo6 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Changer votre nom d'utilisateur",bg="#5e262c",font=("arial","15"),fg="white")
    labelMeteo1 = Label(section,text="Lieu de domicile",bg="#5e262c",font=("arial","15"),fg="white")
    labelMeteo2 = Label(section,text="Lieu Favorie",bg="#5e262c",font=("arial","15"),fg="white")
    labelMeteo3 = Label(section,text="Lieu de travail",bg="#5e262c",font=("arial","15"),fg="white")
    labelMeteo4 = Label(section,text="Lieu de vacances",bg="#5e262c",font=("arial","15"),fg="white")
    labelMeteo5 = Label(section,text="Lieu Bonnus",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
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
    btnMeteo6.place(x=225,y=625)