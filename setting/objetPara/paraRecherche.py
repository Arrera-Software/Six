from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingRecherche :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str,liste:list):
        #varriable
        self.configFile = config
        self.listMoteur = liste
        self.choixVar = StringVar(windows)
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = Label(self.acceuilFrame,text="Choisisser\nle moteur de recherche",bg=color,fg=textColor,font=("arial","20"))
        menuMoteur = OptionMenu(self.acceuilFrame,self.choixVar,*self.listMoteur)
        btnValider = Button(self.acceuilFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self._moteurRecherche)
        #calcule affichage
        largeurAcceuilFrame = self.acceuilFrame.winfo_reqwidth()
        #Affichage 
        labelTitre.place(x=((largeurAcceuilFrame-labelTitre.winfo_reqwidth())//2),y=0)
        menuMoteur.place(relx=0.5,rely=0.5,anchor="center")
        btnValider.place(x=((largeurAcceuilFrame-btnValider.winfo_reqwidth())//2),y=(self.acceuilFrame.winfo_reqheight()-btnValider.winfo_reqheight()))
        
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self.acceuilFrame.place(x=0,y=0)
        
    def writeMoteur(self,moteur:StringVar):
        valeur = moteur.get()
        self.configFile.EcritureJSON("moteurRecherche",valeur)
        messagebox.showinfo("Moteur de recherche","Le moteur de chercheche a ete changer")
    
    def _moteurRecherche(self):
        self.writeMoteur(self.choixVar)