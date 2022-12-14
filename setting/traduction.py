from tkinter import *
from function.JSON import*
from setting.view import*


def Trad(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
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
    btnTrad1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnTrad2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnTrad3 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Modifier la langue de l'outil de traduction de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    labelTrad1 = Label(section,text="Langue 1",bg="#5e262c",font=("arial","15"),fg="white")
    labelTrad2 = Label(section,text="Langue 2",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
    labelTrad1.place(x=20,y=125)
    labelTrad2.place(x=20,y=245)
    
    btnTrad1.place(x=265,y=125)
    btnTrad2.place(x=265,y=245)
 
    
    btnTrad3.place(x=225,y=650)