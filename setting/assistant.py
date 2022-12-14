from tkinter import *
from function.JSON import*
from setting.view import*

def Assistant(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
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
    btnAssistant1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAssistant2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAssistant3 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Changer le nom de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant1 = Label(section,text="Nom :"+lectureJSON("setting/config.json","nomAssistant"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant2 = Label(section,text="Pronociation",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
    labelAssistant1.place(x=20,y=125)
    labelAssistant2.place(x=20,y=225)
    
    btnAssistant1.place(x=250,y=125)
    btnAssistant2.place(x=250,y=225)
    btnAssistant3.place(x=225,y=525)