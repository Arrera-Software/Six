from tkinter import *
from turtle import color
from src.srcSix import*

Color = "#3c0f14"
TextColor = "white"

class Reading:
    def __init__(self,root,police):
        self.dictLang = lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json")
        self.listLang = list(self.dictLang.values())
        self.soureSIX = SIXsrc(root,police)
        self.screen = Tk()
        self.varLang = StringVar(self.screen)
        self.screen.title("SIX : Lecture")
        self.screen.minsize(600,500)
        self.screen.maxsize(600,500)
        self.screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        self.screen.config(bg=Color)
        self.entryLect = Text(self.screen,width=50)
        menuLang = OptionMenu(self.screen,self.varLang,*self.listLang)
        self.varLang.set(self.listLang[28])
        menuLang.place(x=0,y=20)
        boutonValider  = Button(self.screen,text="Valider",bg=Color,fg=TextColor,font=("arial",15),command=self.Lecture)
        self.entryLect.pack(side="left")
        boutonValider.pack(side="right")
        self.screen.mainloop()
        
    def Lecture(self):
        lang = searchKey(self.varLang.get(),self.dictLang)
        texte = self.entryLect.get("1.0",END)
        self.screen.destroy()
        self.soureSIX.speakOtherLang(lang,texte)