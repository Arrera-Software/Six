from tkinter import*
from objet.Horloge.Chronometre import *
from objet.Horloge.Minuteur import*
from objet.Horloge.HorlogeAcceuil import*
from objet.Horloge.ObjetHorloge import*

class AppHorloge :
    def __init__(self,mainColor,textColor,title,mode):
        self.mainColor = mainColor
        self.textColor = textColor
        self.screen = Toplevel()
        self.screen.iconphoto(False,PhotoImage(file="image/Ryley.png"))
        self.img = PhotoImage(file="image/horloge.png")
        self.screen.title(title)
        self.screen.minsize(500,500)
        self.screen.maxsize(500,500)
        self.screen.config(bg=mainColor)
        self.frameBottom = Frame(self.screen,bg=mainColor,width=500,height=35)
        self.frameAcceuil = Frame(self.screen,bg=mainColor,height=465,width=500)
        self.frameChrono = Frame(self.screen,bg=mainColor,height=465,width=500)
        self.frameMinuteur = Frame(self.screen,bg=mainColor,height=465,width=500)
        self.frameHorloge = Frame(self.screen,bg=mainColor,height=465,width=500)
        self.btn1 = Button(self.frameBottom,text="Acceuil",font=("arial","13"),bg=mainColor,command=self.affichageAcceuil)
        self.btn2 = Button(self.frameBottom,text="Chronometre",font=("arial","13"),bg=mainColor,command=self.affichageChrono)
        self.btn3 = Button(self.frameBottom,text="Minuteur",font=("arial","13"),bg=mainColor,command=self.affichageMinuteur)
        self.btn4 = Button(self.frameBottom,text="Horloge",font=("arial","13"),bg=mainColor,command=self.affichageHorloge)
        if mode == "acceuil" :
            self.affichageAcceuil()
        else : 
            if mode == "chronometre":
                self.affichageChrono()
            else : 
                if mode == "minuteur":
                   self.affichageMinuteur()
                else : 
                    if mode == "horloge":
                        self.affichageHorloge() 
                    else : 
                        self.affichageAcceuil()
        self.btn1.place(x=10,y=0)
        self.btn2.place(x=90,y=0)
        self.btn3.place(x=210,y=0)
        self.btn4.place(x=300,y=0)
        self.frameBottom.pack(side="bottom")
        self.screen.mainloop()
    
    def resetAffichage(self):
        self.frameAcceuil.place_forget()
        self.frameChrono.place_forget()
        self.frameHorloge.place_forget()
        self.frameMinuteur.place_forget()
    
    def affichageAcceuil(self):
        self.resetAffichage() 
        Acceuil(self.frameAcceuil,self.mainColor,self.textColor,self.img)
        self.frameAcceuil.place(x=0,y=0) 
    
    def affichageChrono(self):
        self.resetAffichage() 
        CHRONOMETRE(self.frameChrono,self.mainColor,self.textColor)
        self.frameChrono.place(x=0,y=0)
    
    def affichageMinuteur(self):
        self.resetAffichage()
        AppMinuteur(self.frameMinuteur,self.mainColor,self.textColor)
        self.frameMinuteur.place(x=0,y=0)
    
    def affichageHorloge(self):
        self.resetAffichage()
        Clock(self.frameHorloge,self.mainColor,self.textColor)
        self.frameHorloge.place(x=0,y=0)