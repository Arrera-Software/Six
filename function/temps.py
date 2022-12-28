import time as t
from tkinter import*
from time import *
from objet.Chronometre import*
from objet.Minuteur import*

Color = "#3c0f14"
TextColor = "white"

def HourSup(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT >= h1:
        return True
    else :
        return False
def HourInf(h1):
    hour = strftime("%H")
    h1 = int(h1)
    hourINT = int(hour)
    if hourINT <= h1:
        return True
    else :
        return False
   

def Minuteur():
    screen = Tk()
    screen.title("Six : Horloge")
    screen.config(bg=Color)
    screen.iconphoto(False,PhotoImage(file="image/logo.png"))
    screen.maxsize(500,250)
    screen.minsize(500,250)
    def valider():
        min = int(entryMin.get())*60
        sec = int(entrySec.get())       
        temps = min + sec
        minuteur = MINUTEUR(bottom,temps)    
    top = Frame(screen,bg=Color,width=500,height=125)
    bottom = Frame(screen,bg=Color,width=500,height=125)
    top.pack(side="top")
    bottom.pack(side="bottom")
    entryMin = Entry(top,width=5,font=("arial","15"))
    entrySec = Entry(top,width=5,font=("arial","15"))
    labelMin = Label(top,text="min",font=("arial","15"),bg=Color,fg=TextColor)
    labelSec = Label(top,text="s",font=("arial","15"),bg=Color,fg=TextColor)
    btnValider = Button(top,text="Valider",bg=Color,fg=TextColor,font=("arial","15"),command=valider)
    entryMin.place(x=170,y=50)
    labelMin.place(x=230,y=50)
    entrySec.place(x=270,y=50)
    labelSec.place(x=330,y=50)
    btnValider.place(x=225,y=85)
    screen.mainloop()
    
def Chrono():
    screen = Tk()
    screen.title("Six : Horloge")
    screen.iconphoto(False,PhotoImage(file="image/logo.png"))
    screen.config(bg=Color)
    screen.maxsize(500,250)
    screen.minsize(500,250)
    chrono = CHRONOMETRE(screen)
    screen.mainloop()    