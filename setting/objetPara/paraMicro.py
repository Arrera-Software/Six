from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingMicro :
    def __init__(self,cadre:Frame,SixConfig:jsonWork,textColor:str,color:str):
        #variable
        self.config = SixConfig
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.acceuilFrame,text="Sons au declanchement du micro",bg=color,fg=textColor,font=("arial","20"))
        self.btnOnOff = Button(self.acceuilFrame,bg=color,fg=textColor,font=("arial","20"))
        #calcule Affichage
        largeur = self.acceuilFrame.winfo_reqwidth()
        hauteur = self.acceuilFrame.winfo_reqheight()
        self.setTextButton()
        #affichage
        labelTitre.place(x=(largeur-labelTitre.winfo_reqwidth()),y=0)
        self.btnOnOff.place(relx=0.5,rely=0.5,anchor="center")

    def view(self):
        self.mainFrame.pack(side="left")
        self.acceuilFrame.place(x=0,y=0)

    def setTextButton(self):
        valeur = int(self.config.lectureJSON("soundMicro"))
        if valeur == 1 :
            self.btnOnOff.configure(text="OFF",command=self.commandOff)
        else :
            if valeur == 0 :
                self.btnOnOff.configure(text="ON",command=self.commandOn)

    def commandOff(self):
        self.config.EcritureJSON("soundMicro","0")
        self.setTextButton()
    
    def commandOn(self):
        self.config.EcritureJSON("soundMicro","1")
        self.setTextButton()