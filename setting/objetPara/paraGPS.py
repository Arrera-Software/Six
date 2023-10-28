from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingGPS:
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #variable
        self.configFile = config
        #cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addresseDomicile = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addresseWork = Frame(self.mainFrame,bg=color,width=350,height=600)
        #widget
        labelTitre = [
            Label(self.acceuilFrame,text="Parametre GPS",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addresseDomicile,text="Adresse de domicile",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addresseWork,text="Adresse de travail",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.addresseDomicile,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.addresseWork,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        btnSuppr = [
            Button(self.addresseDomicile,text="Supprimer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._supprAdresse("domicile")),
            Button(self.addresseWork,text="Supprimer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._supprAdresse("work"))
        ]
        btnValider = [
            Button(self.addresseDomicile,text="Enregistrer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._addAdresse("domicile")),
            Button(self.addresseWork,text="Enregistrer l'adresse",bg=color,fg=textColor,font=("arial","15"),command=lambda:self._addAdresse("work"))
        ]
        self.entryAdresse = [
            Entry(self.addresseDomicile,font=("arial","15"),borderwidth=2,relief="solid"),
            Entry(self.addresseWork,font=("arial","15"),borderwidth=2,relief="solid")
        ]
        #acceuil frame
        btnDomicile = Button(self.acceuilFrame,text="Adresse de domicile",bg=color,fg=textColor,font=("arial","15"),command=self.domicileView)
        btnWork = Button(self.acceuilFrame,text="Adresse de travail",bg=color,fg=textColor,font=("arial","15"),command=self.workView)
        #recuperartion valeur 
        centrageAcceuil = self.acceuilFrame.winfo_reqwidth()
        hauteurCadre = self.acceuilFrame.winfo_reqheight()
        largeurCadre = self.acceuilFrame.winfo_reqwidth()
        #affichage 
        #acceuilFrame
        labelTitre[0].place(x=((centrageAcceuil-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnDomicile.place(x=((centrageAcceuil-btnDomicile.winfo_reqwidth())//2),y=175)
        btnWork.place(x=((centrageAcceuil-btnWork.winfo_reqwidth())//2),y=275)
        #addresseDomicile
        labelTitre[1].place(x=((centrageAcceuil-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.entryAdresse[0].place(relx=0.5,rely=0.5,anchor="center")
        btnRetour[0].place(x=(largeurCadre-btnRetour[0].winfo_reqwidth()),y=(hauteurCadre-btnRetour[0].winfo_reqheight()))
        btnValider[0].place(x=((centrageAcceuil-btnValider[0].winfo_reqwidth())//2),y=325)
        btnSuppr[0].place(x=((centrageAcceuil-btnSuppr[0].winfo_reqwidth())//2),y=375)
        #addressWork
        labelTitre[2].place(x=((centrageAcceuil-labelTitre[2].winfo_reqwidth())//2),y=0)
        self.entryAdresse[1].place(relx=0.5,rely=0.5,anchor="center")
        btnRetour[1].place(x=(largeurCadre-btnRetour[1].winfo_reqwidth()),y=(hauteurCadre-btnRetour[1].winfo_reqheight()))
        btnValider[1].place(x=((centrageAcceuil-btnValider[0].winfo_reqwidth())//2),y=325)
        btnSuppr[1].place(x=((centrageAcceuil-btnSuppr[0].winfo_reqwidth())//2),y=375)
     
    def _backAcceuil(self)->bool:
        self.addresseDomicile.place_forget()
        self.addresseWork.place_forget()
        self.acceuilFrame.place(x=0,y=0)
        self.acceuilFrame.update()
        return  True    
    
    def view(self)->bool:
        self._backAcceuil()
        self.mainFrame.pack(side="left")
        self._backAcceuil()
        return True
        
    def domicileView(self) ->bool:
        self.acceuilFrame.place_forget()
        self.entryAdresse[0].delete(0,"end")
        self.addresseDomicile.place(x=0,y=0)
        return True
    
    def workView(self) ->bool:
        self.acceuilFrame.place_forget()
        self.entryAdresse[1].delete(0,"end")
        self.addresseWork.place(x=0,y=0)
        return True
    
    def _addAdresse(self,type:str)->bool:
        self._backAcceuil()
        if type == "domicile" :
            adresse = self.entryAdresse[0].get()
            self.configFile.EcritureJSON("adresseDomicile",adresse)
            self.entryAdresse[0].delete(0,"end")
            messagebox.showinfo("Adresse enregistrer","L'adresse de votre domicile a ete enregistrer")
        else :
            if type == "work":
                adresse = self.entryAdresse[1].get()
                self.configFile.EcritureJSON("adresseTravail",adresse)
                self.entryAdresse[1].delete(0,"end")
                messagebox.showinfo("Adresse enregistrer","L'adresse de votre lieu de travail a ete enregistrer")  
        return True 
    
    def _supprAdresse(self,type:str)->bool:
        self._backAcceuil()
        if type == "domicile" :
            self.configFile.suppressionJson("adresseDomicile")
            self.entryAdresse[0].delete(0,"end")
            messagebox.showinfo("Adresse supprimer","L'adresse de votre domicile a ete supprimer")
        else :
            if type == "work":
                self.configFile.suppressionJson("adresseTravail")
                self.entryAdresse[1].delete(0,"end")
                messagebox.showinfo("Adresse enregistrer","L'adresse de votre lieu de travail a ete supprimer")  
        return True  