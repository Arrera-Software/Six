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
   #declaration widget
    #btn
    btnAppWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAppWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAppWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAppWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAppWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAppWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Ajouter votre application web ou \nsite internet preférée",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb1 = Label(section,text="Application 1",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb2 = Label(section,text="Application 2",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb3 = Label(section,text="Application 3",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb4 = Label(section,text="Application 4",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb5 = Label(section,text="Application 5",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
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
    
    btnAppWeb7.place(x=225,y=650)