from tkinter import *
from tkinter.messagebox import *
from function.JSON import*
from setting.view import*

listTheme = ["default","white","black"]

def GUI(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6,btn7):
    cadre.pack_forget()
    varTheme = StringVar(screen)
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
    def Affichage():
        btnGUIValider.place(x=195,y=125) 
        menuTheme.place(x=20,y=125)
    def valider():
        newTheme = varTheme.get()
        EcritureJSON("setting/config.json","theme",newTheme)
        showinfo(title="SIX : Parametre",message="Vous devez redemarré l'assistant pour\nvoir le changement de l'interface")
        exit()
    #declaration widget
    #btn
    btnGUIValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white",command=valider)
    btnGUI1 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #label
    labelIndication =Label(section,text="Modifier le theme de l'interface \nde principal de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    #menu
    menuTheme = OptionMenu(section,varTheme,*listTheme)
    
    if lectureJSON("setting/config.json","theme") == "default" :
        varTheme.set(listTheme[0])
    else :
        if lectureJSON("setting/config.json","theme") == "white":
            varTheme.set(listTheme[1])
        else :
            varTheme.set(listTheme[2])
    
    Affichage()
    
    btnGUI1.place(x=225,y=625)
    labelIndication.place(x=125,y=0)