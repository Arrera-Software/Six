
from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingMeteo :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #varriable
        self.varSuppr = StringVar(windows)
        self.varChoixLieu = StringVar(windows)
        self.configFile = config
        self.listChoixLieu = ["Simple","Domicile","Travail"]
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.listFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        labelTitre = [
            Label(self.acceuilFrame,text="Parametre Meteo",bg=color,fg=textColor,font=("arial","20")),
            Label(self.listFrame,text="Liste de ville enregistrer",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ecrivez la ville\nque vous voulez rajouter",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprFrame,text="Selectionner la ville\nque vous voulez supprimer",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.listFrame,text="Retour",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15")),
            Button(self.addFrame,text="Annuler",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15")),
            Button(self.supprFrame,text="Annuler",bg=color,fg=textColor,command=self._backAcceuil,font=("arial","15"))
        ]
        #Frame acceuilFrame
        btnListMeteo =  Button(self.acceuilFrame,text="      Liste meteo      ",bg=color,fg=textColor,font=("arial","15"),command=self.viewListMeteo)
        btnAddVille =   Button(self.acceuilFrame,text="   Ajouter une ville   ",bg=color,fg=textColor,font=("arial","15"),command=self.addView)
        btnSupprVille = Button(self.acceuilFrame,text="   Supprimer une ville ",bg=color,fg=textColor,font=("arial","15"),command=self.supprView)
        #frame listFrame
        self.labelListe = Label(self.listFrame,bg=color,fg=textColor,font=("arial","15"))
        #frame addFrame
        menuChoixLieu = OptionMenu(self.addFrame,self.varChoixLieu,*self.listChoixLieu)
        self.entryVille = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnAddValidate = Button(self.addFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self._add)
        #frame supprFrame
        btnSupprValidate = Button(self.supprFrame,font=("arial","15"),text="Valider",bg=color,fg=textColor,command=self._suppr)
        #recuperartion valeur 
        centrageAcceuil = self.acceuilFrame.winfo_reqwidth()
        centrageAddVille = self.addFrame.winfo_reqwidth()
        hauteurRetour = btnRetour[0].winfo_reqheight()
        largeurRetour = btnRetour[0].winfo_reqwidth()
        hauteurCadre = self.acceuilFrame.winfo_reqheight()
        largeurCadre = self.acceuilFrame.winfo_reqwidth()
        #affichage
        # acceuilFrame
        labelTitre[0].place(x=((centrageAcceuil-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnListMeteo.place(x=((centrageAcceuil-btnListMeteo.winfo_reqwidth())//2),y=200)
        btnAddVille.place(x=((centrageAcceuil-btnAddVille.winfo_reqwidth())//2),y=275)
        btnSupprVille.place(x=((centrageAcceuil-btnSupprVille.winfo_reqwidth())//2),y=350)
        # listFrame
        labelTitre[1].place(x=((self.listFrame.winfo_reqwidth()-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.labelListe.place(x=0,y=(labelTitre[1].winfo_reqheight()+10))
        btnRetour[0].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        # addVilleFrame
        labelTitre[2].place(x=((centrageAddVille-labelTitre[2].winfo_reqwidth())//2),y=0)
        menuChoixLieu.place(x=15,y=((labelTitre[2].winfo_reqheight()+menuChoixLieu.winfo_reqheight())+15))
        self.entryVille.place(relx=0.5,rely=0.5,anchor="center")
        btnAddValidate.place(x=0,y=(hauteurCadre-btnAddValidate.winfo_reqheight()))
        btnRetour[1].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        # supprFrame
        labelTitre[3].place(x=((centrageAddVille-labelTitre[3].winfo_reqwidth())//2),y=0)
        btnSupprValidate.place(x=0,y=(hauteurCadre-btnSupprValidate.winfo_reqheight()))
        btnRetour[2].place(x=(largeurCadre-largeurRetour),y=(hauteurCadre-hauteurRetour))
        
        
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self.acceuilFrame.place(x=0,y=0)
        self._backAcceuil()
        return True
    
    def _backAcceuil(self)->bool:
        self.listFrame.place_forget()
        self.addFrame.place_forget()
        self.supprFrame.place_forget()
        self.acceuilFrame.place(x=0,y=0)
        self.acceuilFrame.update()
        return True 
    
    def viewListMeteo(self) ->bool:
        self.acceuilFrame.place_forget()
        self.listFrame.place(x=0,y=0)
        if self.labelListe.cget("text"):
            self.listFrame.config(text="")
        listeVille = []
        if not self.configFile.lectureJSON("lieuDomicile")  :
            listeVille.append("Pas de lieu domicile enregistrer")
        else :
            listeVille.append("Lieu domicile enregistrer")
        if not self.configFile.lectureJSON("lieuTravail") :
            listeVille.append("Pas de lieu travail enregistrer")
        else :
            listeVille.append("Lieu travail enregistrer")   
        listeVille = listeVille + self.configFile.lectureJSONList("listVille")
        for i in range(0,len(listeVille)):
            self.labelListe.configure(text=self.labelListe.cget("text")+listeVille[i]+"\n")
        return True
            
    def addView(self)->bool:
        self.acceuilFrame.place_forget()
        self.entryVille.delete(0,"end")
        self.varChoixLieu.set(self.listChoixLieu[0])
        self.addFrame.place(x=0,y=0)
        return True
    
    def _add(self)->bool:
        typeVille  = self.varChoixLieu.get()
        if (typeVille == self.listChoixLieu[0]):
            self.configFile.EcritureJSONList("listVille",str(self.entryVille.get()))
        else :
            if (typeVille == self.listChoixLieu[1]):
                self.configFile.EcritureJSON("lieuDomicile",str(self.entryVille.get()))
            else :
                if (typeVille == self.listChoixLieu[2]):
                    self.configFile.EcritureJSON("lieuTravail",str(self.entryVille.get()))
        self._backAcceuil()
        messagebox.showinfo("Ecriture terminer","Votre ville a été enregister")
        return True
    
    def supprView(self)->bool:
        if (len(str(self.configFile.lectureJSON("lieuDomicile")))==0 ) and (len(str(self.configFile.lectureJSON("lieuTravail")))==0) and (len(self.configFile.lectureJSONList("listVille"))==0) :
            self._backAcceuil()
            messagebox.showerror("Aucun donner enregister","Ajouter des villes dans la meteo avant d'en supprimer")
        else :
            self.supprFrame.place(x=0,y=0)
            listeVille = []
            if len(str(self.configFile.lectureJSON("lieuDomicile")))>0 :
                listeVille.append("Domicile")
            if len(str(self.configFile.lectureJSON("lieuTravail")))>0 :
                listeVille.append("Travail")
            listeVille = listeVille + self.configFile.lectureJSONList("listVille")
            print(listeVille)
            self.menuVille = OptionMenu(self.supprFrame,self.varSuppr,*listeVille)
            self.menuVille.place(relx=0.5,rely=0.5,anchor="center")
            self.varSuppr.set(listeVille[0])
            self.menuVille.update()
        return True
    
    def _suppr(self)->bool:
        valeur = self.varSuppr.get()
        if valeur == "Domicile" :
            self.configFile.suppressionJson("lieuDomicile")
        else :
            if valeur == "Travail" :
                self.configFile.suppressionJson("lieuTravail")
            else :
                self.configFile.suppressionJsonList("listVille",valeur)
        self.menuVille.destroy()
        self._backAcceuil() 