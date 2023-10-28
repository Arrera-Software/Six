from tkinter import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*
from librairy.travailJSON import*
from tkinter import messagebox

class SettingSoftware :
    def __init__(self,windows:Tk,cadre:Frame,config:jsonWork,settingConfig:jsonWork,neuronFile:jsonWork,textColor:str,color:str):
        #varriable
        self.config = config
        self.assistantFile = neuronFile
        self.varType = StringVar(windows)
        self.varSuppr = StringVar(windows)
        self.varSupprSpe = StringVar(windows)
        self.listTypeSoft = [
            "Autre",
            "Traitement de texte",
            "Tableur",
            "Presentation",
            "Navigateur Internet",
            "Note",
            "Musique"
        ]
        self.listTypeSoftSpe = [
            "Traitement de texte",
            "Tableur",
            "Presentation",
            "Navigateur Internet",
            "Note",
            "Musique"
        ]
        #declaration cadre
        self.mainFrame = cadre
        self.acceuilFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.addLinuxFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        self.supprSpeFrame = Frame(self.mainFrame,bg=color,width=350,height=600)
        #objet detction 
        self.dectOS = OS()
        #widget
        labelTitre = [
            Label(self.acceuilFrame,text="Gestion logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.addLinuxFrame,text="Entrer la commande\npour lancer le logiciel",bg=color,fg=textColor,font=("arial","20")),
            Label(self.supprSpeFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","20")),
            ]
        btnRetour = [
            Button(self.addFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.supprFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.addLinuxFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil),
            Button(self.supprSpeFrame,text="Annuler",bg=color,fg=textColor,font=("arial","15"),command=self._backAcceuil)
        ]
        #acceuilFrame
        btnAjout=Button(self.acceuilFrame,text="Ajouter un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.addView) 
        btnSuppr=Button(self.acceuilFrame,text="Supprimer un logiciel",bg=color,fg=textColor,font=("arial","15"),command=self.supprSoft)
        btnSupprSpe =Button(self.acceuilFrame,text="Supprimer logiciel speciaux",bg=color,fg=textColor,font=("arial","15"),command=self._supprSpeciauxViev)
        btnSetEmplacement = Button(self.acceuilFrame,text="Definir emplacement",bg=color,fg=textColor,font=("arial","15"),command=self._setEmplacementWindows)
        #supprFrame
        btnValiderSuppr = Button(self.supprFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self._suppr) 
        #addFrame
        self.entryNameSoft = Entry(self.addFrame,font=("arial","15"),borderwidth=2,relief="solid")
        menuTypeSoft = OptionMenu(self.addFrame,self.varType,*self.listTypeSoft)
        self.varType.set(self.listTypeSoft[0])
        btnValiderAdd = Button(self.addFrame,text="Ajouter",bg=color,fg=textColor,font=("arial","15")) 
        #addLinuxFram
        self.entryCommandSoft = Entry(self.addLinuxFrame,font=("arial","15"),borderwidth=2,relief="solid")
        btnSaveLinux = Button(self.addLinuxFrame,text="Enregistrer",bg=color,fg=textColor,font=("arial","15"),command=self._saveSoftLinux) 
        #supprSpe
        menuSupprSpe = OptionMenu(self.supprSpeFrame,self.varSupprSpe,*self.listTypeSoftSpe)
        btnValiderSupprSpe = Button(self.supprSpeFrame,text="Supprimer",bg=color,fg=textColor,font=("arial","15"),command=self._supprSpeciaux)
        if (self.dectOS.osLinux()==True):
            btnValiderAdd.configure(command=self._addLinuxView)
        else :
            if (self.dectOS.osWindows() == True) :
                btnValiderAdd.configure(command=self._addSoftWindows)
                self.softWin  = gestionSoftWindows(neuronFile.lectureJSON("emplacementSoftWindows"))
        #calcule affichage
        largeurFrame=self.acceuilFrame.winfo_reqwidth()
        hauteurFrame=self.acceuilFrame.winfo_reqheight()
        #Affichage
        #acceuilFrame
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnAjout.place(x=((largeurFrame-btnAjout.winfo_reqwidth())//2),y=175)
        btnSuppr.place(x=((largeurFrame-btnSuppr.winfo_reqwidth())//2),y=250)
        btnSupprSpe.place(x=((largeurFrame-btnSupprSpe.winfo_reqwidth())//2),y=325)
        if (self.dectOS.osWindows()==True):
            btnSetEmplacement.place(x=((largeurFrame-btnSetEmplacement.winfo_reqwidth())//2),y=400)
        #addFrame
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        menuTypeSoft.place(x=10,y=((labelTitre[1].winfo_reqheight()+menuTypeSoft.winfo_reqheight())+5))
        self.entryNameSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderAdd.place(x=0,y=(hauteurFrame-btnValiderAdd.winfo_reqheight()))
        btnRetour[0].place(x=(largeurFrame-btnRetour[0].winfo_reqwidth()),y=(hauteurFrame-btnRetour[0].winfo_reqheight()))
        #suppr Frame
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        btnValiderSuppr.place(x=0,y=(hauteurFrame-btnValiderSuppr.winfo_reqheight()))
        btnRetour[1].place(x=(largeurFrame-btnRetour[1].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
        #addLinuxFrame
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        self.entryCommandSoft.place(relx=0.5,rely=0.5,anchor="center")
        btnSaveLinux.place(x=0,y=(hauteurFrame-btnSaveLinux.winfo_reqheight()))
        btnRetour[2].place(x=(largeurFrame-btnRetour[2].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
        #varSupprSpe
        labelTitre[4].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        menuSupprSpe.place(relx=0.5,rely=0.5,anchor="center")
        btnValiderSupprSpe.place(x=0,y=(hauteurFrame-btnValiderSupprSpe.winfo_reqheight()))
        btnRetour[3].place(x=(largeurFrame-btnRetour[3].winfo_reqwidth()),y=(hauteurFrame-btnRetour[1].winfo_reqheight()))
    
    def view(self)->bool:
        self.mainFrame.pack(side="left")
        self._backAcceuil()
        return True
    
    def _backAcceuil(self)->bool:
        self.addFrame.place_forget()
        self.supprFrame.place_forget()
        self.addLinuxFrame.place_forget()
        self.supprSpeFrame.place_forget()
        self.acceuilFrame.place(x=0,y=0)
        return True
        
    
    def addView(self)->bool:
        self.entryNameSoft.delete(0,END)
        self.varType.set(self.listTypeSoft[0])
        self.acceuilFrame.place_forget()
        self.addFrame.place(x=0,y=0)
        return True
    
    def _saveSoftWindows(self,name:str,flag:str,dict:bool)->bool:
        if name:
            self.softWin.setName(name)
            sortie = self.softWin.saveSoftware()
            if sortie == True :
                if dict == True :
                    self.config.EcritureJSONDictionnaire(flag,name,self.softWin.getName())
                else :
                    self.config.EcritureJSON(flag,self.softWin.getName())
                messagebox.showinfo("Logiciel sauvegarder","Le logiciel a bien etais enregister")
                return True
            else :
                messagebox.showerror("Erreur emplacement","Une erreur c'est produit lors de la selection de l'emplacement")
                return False
        else :
            messagebox.showerror("Erreur nom","Vous pouver pas enregister un logiciel sans nom")
            return False
    
    def _setEmplacementWindows(self)->bool:
        sortie = self.softWin.setEmplacementSoft()
        self.assistantFile.EcritureJSON("emplacementSoftWindows",sortie)
        return True
    
    def _addSoftWindows(self)->bool:
        typeSoft = self.varType.get()
        if typeSoft == self.listTypeSoft[0]:
            self._saveSoftWindows(self.entryNameSoft.get(),"dictSoftWindows",True)
            nbSoft = int(self.config.lectureJSON("nbSoft"))
            self.config.EcritureJSON("nbSoft",str(nbSoft+1))
        else :
            if typeSoft == self.listTypeSoft[1]:
                self._saveSoftWindows("TTexte","wordWindows",False)
            else :
                if typeSoft == self.listTypeSoft[2]:
                    self._saveSoftWindows("tableur","exelWindows",False)
                else :
                    if typeSoft == self.listTypeSoft[3]:
                        self._saveSoftWindows("presentation","diapoWindows",False)
                    else :
                        if typeSoft == self.listTypeSoft[4]:
                            self._saveSoftWindows("internet","browserWindows",False)
                        else :
                            if typeSoft == self.listTypeSoft[5]:
                                self._saveSoftWindows("note","noteWindows",False)
                            else :
                                if typeSoft == self.listTypeSoft[6]:
                                    self._saveSoftWindows("musique","musicWindows",False)
        self.entryNameSoft.delete(0,END)
        self._backAcceuil() 
        return bool
        
    def supprSoft(self)->bool:
        if (self.dectOS.osWindows()==True):
            listSoft= list(self.config.lectureJSONDict("dictSoftWindows").keys())
        else :
            listSoft= list(self.config.lectureJSONDict("dictSoftLinux").keys())
        if not listSoft :
            messagebox.showerror("Erreur","Aucun logiciel n'est enregistrer")
        else :
            self.acceuilFrame.place_forget()
            self.supprFrame.place(x=0,y=0)
            self.menuSuppr = OptionMenu(self.supprFrame,self.varSuppr,*listSoft)
            self.menuSuppr.place(relx=0.5,rely=0.5,anchor="center")
        return True
            
    def _suppr(self)-> bool:
        if (self.dectOS.osWindows()==True):
            name = self.varSuppr.get()
            self.config.supprJSONList("dictSoftWindows",name)
            self.softWin.supprSoft(name)
            nbSoft = int(self.config.lectureJSON("nbSoft"))
            self.config.EcritureJSON("nbSoft",str(nbSoft-1))
        else :
            if (self.dectOS.osLinux()==True):
                self.config.supprJSONList("dictSoftLinux",self.varSuppr.get())
                nbSoft = int(self.config.lectureJSON("nbSoft"))
                self.config.EcritureJSON("nbSoft",str(nbSoft-1))
        self._backAcceuil()
        self.menuSuppr.destroy() 
        return True 
        
        
    def _addLinuxView(self)-> bool:
        self.addFrame.place_forget()
        self.addLinuxFrame.place(x=0,y=0)
        return True 
        
    def _saveSoftLinux(self)-> bool:
        command = self.entryCommandSoft.get()
        typeSoft = self.varType.get()
        if typeSoft == self.listTypeSoft[0]:
            name = self.entryNameSoft.get()
            self.config.EcritureJSONDictionnaire("dictSoftLinux",name,command)
            nbSoft = int(self.config.lectureJSON("nbSoft"))
            self.config.EcritureJSON("nbSoft",str(nbSoft+1))
        else :
            if typeSoft == self.listTypeSoft[1]:
                self.config.EcritureJSON("wordLinux",command)
            else :
                if typeSoft == self.listTypeSoft[2]:
                    self.config.EcritureJSON("exelLinux",command)
                else :
                    if typeSoft == self.listTypeSoft[3]:
                        self.config.EcritureJSON("diapoLinux",command)
                    else :
                        if typeSoft == self.listTypeSoft[4]:
                            self.config.EcritureJSON("browserLinux",command)
                        else :
                            if typeSoft == self.listTypeSoft[5]:
                                self.config.EcritureJSON("noteLinux",command)
                            else :
                                if typeSoft == self.listTypeSoft[6]:
                                    self.config.EcritureJSON("musicLinux",command)
        
        self._backAcceuil()
        self.entryNameSoft.delete("0",END)
        self.entryCommandSoft.delete("0",END)
        return True 
    
    def _supprSpeciauxViev(self)->bool:
        self.acceuilFrame.place_forget()
        self.varSupprSpe.set(self.listTypeSoftSpe[0])
        self.supprSpeFrame.place(x=0,y=0)
        return bool
    
    def _supprSpeciaux(self)->bool:
        typeSoft = self.varSupprSpe.get()
        if typeSoft == self.listTypeSoftSpe[0]:
            if (self.dectOS.osWindows()==True):
                if not self.config.lectureJSON("wordWindows") :
                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                else :
                    self.softWin.supprSoft("TTexte")
                    self.config.suppressionJson("wordWindows")
            else :
                if not self.config.lectureJSON("wordLinux") :
                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                else :
                    self.config.suppressionJson("wordLinux")
        else :
            if typeSoft == self.listTypeSoftSpe[1]:

                if (self.dectOS.osWindows()==True):
                    if not self.config.lectureJSON("exelWindows") :
                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                    else :
                        self.softWin.supprSoft("tableur")
                        self.config.suppressionJson("exelWindows")
                else :
                    if not self.config.lectureJSON("exelLinux") :
                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                    else :
                        self.config.suppressionJson("exelLinux")
            else :
                if typeSoft == self.listTypeSoftSpe[2]:
                    if (self.dectOS.osWindows()==True):
                        if not self.config.lectureJSON("diapoWindows") :
                            messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                        else :
                            self.softWin.supprSoft("presentation")
                            self.config.suppressionJson("diapoWindows")
                    else :
                        if not self.config.lectureJSON("diapoLinux") :
                            messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                        else :
                            self.config.suppressionJson("diapoLinux")
                else :
                    if typeSoft == self.listTypeSoftSpe[3]:
                        if (self.dectOS.osWindows()==True):
                            if not self.config.lectureJSON("browserWindows") :
                                messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                            else :
                                self.softWin.supprSoft("internet")
                                self.config.suppressionJson("browserWindows")
                        else :
                            if not self.config.lectureJSON("browserLinux") :
                                messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                            else :
                                self.config.suppressionJson("browserLinux")
                    else :
                        if typeSoft == self.listTypeSoftSpe[4]:
                            if (self.dectOS.osWindows()==True):
                                if not self.config.lectureJSON("noteWindows") :
                                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                else :
                                    self.softWin.supprSoft("note")
                                    self.config.suppressionJson("noteWindows")
                            else :
                                if not self.config.lectureJSON("noteLinux") :
                                    messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                else :
                                    self.config.suppressionJson("noteLinux")
                        else :
                            if typeSoft == self.listTypeSoftSpe[5]:
                                if (self.dectOS.osWindows()==True):
                                    if not self.config.lectureJSON("musicWindows") :
                                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                    else :
                                        self.softWin.supprSoft("musique")
                                        self.config.suppressionJson("musicWindows")
                                else :
                                    if not self.config.lectureJSON("musicLinux") :
                                        messagebox.showwarning("Erreur","Aucun logiciel n'est enregistrer")
                                    else :
                                        self.config.suppressionJson("musicLinux")
        self._backAcceuil()
        return True