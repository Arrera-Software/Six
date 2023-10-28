from tkinter import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingInternet :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,textColor:str,color:str):
        #variable 
        self.config = config
        self.varType = StringVar(windows)
        self.varSuppr = StringVar(windows)
        self.listType = ["Autre",
                         "Stokage en ligne"]
        #declaration cadre 
        self.mainFrame = cadre 
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #widget 
        labelTitre = [
            Label(self.acceuilFrame,text="Paramétre d'internet",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ajouter un site",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprFrame,text="Supprimer un site",bg=color,fg=textColor,font=("arial","20"))
        ]
        btnRetour = [
            Button(self.addFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.supprFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        #acceuilFrame
        btnAdd = Button(self.acceuilFrame,text="Ajouter un site",bg=color,fg=textColor,font=("arial","15"),command=self.addView)
        btnSuppr = Button(self.acceuilFrame,text="Supprimer un site",bg=color,fg=textColor,font=("arial","15"),command=self.supprView)
        #frame addFrame
        self.menuType = OptionMenu(self.addFrame,self.varType,*self.listType)
        self.edtName = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        self.edtLien = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnValiderAdd = Button(self.addFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self.add)
        #frame supprFrame
        btnValiderSuppr = Button(self.supprFrame,text="Valider",bg=color,fg=textColor,font=("arial","15"),command=self.suppr)
        #calcule 
        hauteurCadre = self.acceuilFrame.winfo_reqheight()
        largeurCadre = self.acceuilFrame.winfo_reqwidth()
        #affichage 
        #acceuilFrame
        labelTitre[0].place(x=((largeurCadre-(labelTitre[0].winfo_reqwidth()))//2),y=0)
        btnAdd.place(x=((largeurCadre-(btnAdd.winfo_reqwidth()))//2),y=200)
        btnSuppr.place(x=((largeurCadre-(btnSuppr.winfo_reqwidth()))//2),y=275)
        #addFrame
        labelTitre[1].place(x=((largeurCadre-labelTitre[1].winfo_reqwidth())//2),y=0)
        self.menuType.place(x=0,y=((labelTitre[1].winfo_reqheight()+self.menuType.winfo_reqheight())+10))
        self.edtName.place(x=((largeurCadre-self.edtName.winfo_reqwidth())//2),y=200)
        self.edtLien.place(x=((largeurCadre-self.edtLien.winfo_reqwidth())//2),y=275)
        btnValiderAdd.place(x=0,y=(hauteurCadre-btnValiderAdd.winfo_reqheight()))
        btnRetour[0].place(x=(largeurCadre-btnRetour[0].winfo_reqwidth()),y=(hauteurCadre-btnRetour[0].winfo_reqheight()))
        #supprFrame
        labelTitre[2].place(x=((largeurCadre-labelTitre[2].winfo_reqwidth())//2),y=0)
        btnValiderSuppr.place(x=0,y=(hauteurCadre-btnValiderSuppr.winfo_reqheight()))
        btnRetour[1].place(x=(largeurCadre-btnRetour[1].winfo_reqwidth()),y=(hauteurCadre-btnRetour[1].winfo_reqheight()))
        
    def _backAcceuil(self)->bool:
        self.addFrame.place_forget()
        self.supprFrame.place_forget()
        self.acceuilFrame.place(x=0,y=0)
        return True
    
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def addView(self)->bool:
        self.acceuilFrame.place_forget()
        self.varType.set(self.listType[0])
        self.addFrame.place(x=0,y=0)
        return True
        
    
    def add(self)->bool:
        name = self.edtName.get()
        lien = self.edtLien.get()
        varType = self.varType.get()
        if varType == self.listType[1]: 
            if lien:
                self.config.EcritureJSON("lienCloud",lien)
                self.edtName.delete("0",END)
                self.edtLien.delete("0",END)
                self._backAcceuil()
                return True
            else :
                messagebox.showerror("Erreur","Veuiller ecrire le lien de votre stokage could")
                self.edtName.delete("0",END)
                self.edtLien.delete("0",END)
                self._backAcceuil()
                return False
        else :
            if name and lien : 
                nb = int(self.config.lectureJSON("nbSite"))
                self.config.EcritureJSONDictionnaire("dictSite",name,lien)
                self.config.EcritureJSON("nbSite",str(nb+1))
                self.edtName.delete("0",END)
                self.edtLien.delete("0",END)
                self._backAcceuil()
                return True
            else :
                messagebox.showerror("Erreur","Veuiller ecrire le lien et le nom du site")
                self.edtName.delete("0",END)
                self.edtLien.delete("0",END)
                self._backAcceuil()
                return False
    
    def supprView(self)->bool:
        listSite = list((self.config.lectureJSONDict("dictSite").keys()))
        if self.config.lectureJSON("lienCloud") :
            listSite.append("Lien cloud")
        if not listSite :
            messagebox.showerror("Erreur","Aucun site n'est enregistrer")
            return False
        else :        
            self.acceuilFrame.place_forget()
            self.menuSite = OptionMenu(self.supprFrame,self.varSuppr,*listSite)
            self.supprFrame.place(x=0,y=0)
            self.menuSite.place(relx=0.5,rely=0.5,anchor="center")
            return True
            
    def suppr(self)->bool:
        site = self.varSuppr.get()
        if (site == "Lien cloud"):
            self.config.suppressionJson("lienCloud")
        else :
            nb=int(self.config.lectureJSON("nbSite"))
            self.config.EcritureJSON("nbSite",str(nb-1))
            self.config.supprJSONList("dictSite",site)
            messagebox.showinfo("Site supprimer","Le site a ete supprimer")
        self._backAcceuil()
        return True