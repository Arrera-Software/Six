from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingTheme :
    def __init__(self,windows:Tk,cadre:Frame,listeTheme:list,configAssistant:jsonWork,textColor:str,color:str):
        #varriable
        self.varTheme = StringVar(windows)
        self.configAssistant = configAssistant
        self.listTheme = listeTheme
        #cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.acceuilFrame,text="Choix du theme",bg=color,fg=textColor,font=("arial","20"))
        self.menuTheme = OptionMenu(self.acceuilFrame,self.varTheme,*self.listTheme)
        btnValider = Button(self.acceuilFrame,text="Choix du theme",bg=color,fg=textColor,font=("arial","15"),command=self.setTheme)
        #Calcule affichage
        largeur = self.acceuilFrame.winfo_reqwidth()
        hauteur = self.acceuilFrame.winfo_reqheight()
        #affichage
        labelTitre.place(x=((largeur-labelTitre.winfo_reqwidth())//2),y=0)
        self.menuTheme.place(relx=0.5,rely=0.5,anchor="center")
        btnValider.place(x=((largeur-labelTitre.winfo_reqwidth())//2),y=(hauteur-labelTitre.winfo_reqheight()))
        
        
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self.acceuilFrame.place(x=0,y=0)
        return True
    
    def setTheme(self)->bool:
        valeur = self.varTheme.get()
        if valeur :
            self.configAssistant.EcritureJSON("theme",valeur)
        else :
            messagebox.showerror("Erreur","Veuillez selectionner un theme")