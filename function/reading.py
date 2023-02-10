from tkinter import *
from turtle import color
from src.srcSix import*

Color = "#3c0f14"
TextColor = "white"

def Reading(root,police):
    screenLect = Tk()
    screenLect.title("SIx : Lecture")
    screenLect.minsize("500","200")
    screenLect.maxsize("500","200")
    screenLect.iconphoto(False,PhotoImage(file="image/logo.png"))
    cadreCenter = Frame(screenLect,bg=Color,width=350,height=45)
    entryLect = Entry(cadreCenter,width=50)
    def Lecture():
        texte = entryLect.get()
        screenLect.destroy()
        SIXsrc(root,police).speak(texte)
    screenLect.config(bg=Color)
    labelIndic = Label(screenLect,text="Copier votre texte",bg=Color,fg=TextColor,font=("arial","20"))
    boutonValider  = Button(screenLect,text="Valider",bg=Color,fg=TextColor,font=("arial","20"),command=Lecture)
    labelIndic.pack()
    cadreCenter.place(relx=.5, rely=.5, anchor="center")
    entryLect.place(relx=.5, rely=.5, anchor="center")
    boutonValider.place(x="200",y="125")
    screenLect.mainloop()