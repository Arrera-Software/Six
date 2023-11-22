from tkinter import *
from tkinter import messagebox
from librairy.travailJSON import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*

class ArreraLynx :
    def __init__(self,windows:Tk,fichierLynx:jsonWork,fichierUser:jsonWork,fichierNeuron:jsonWork):
        #objet
        self.fichierLynx = fichierLynx
        self.fileUser = fichierUser
        self.fileNeuron = fichierNeuron
        self.dectOS = OS()
        if self.dectOS.osWindows()==True:
            self.softWin = gestionSoftWindows(self.fileNeuron.lectureJSON("emplacementSoftWindows"))
        #Variable 
        self.windows = windows
        self.varGenre = StringVar(windows)
        color = self.fichierLynx.lectureJSON("color")
        textColor = self.fichierLynx.lectureJSON("textColor")
        nomSoft = self.fichierLynx.lectureJSON("nameSoft")
        iconLogiciel = PhotoImage(file=str(self.fichierLynx.lectureJSON("iconSoft")))
        listGenre = self.fichierLynx.lectureJSONList("listGenre")
        #modification de la fenetre
        windows.title(nomSoft+": Premier demarage")
        windows.maxsize(700,500)
        windows.iconphoto(False,iconLogiciel)
        #cadre tkinter
        self.frameAcceuil = Frame(windows,width=700,height=500,bg=color)
        self.frameUserName = Frame(windows,width=700,height=500,bg=color)
        self.frameUserGenre = Frame(windows,width=700,height=500,bg=color)
        self.frameWeather = Frame(windows,width=700,height=500,bg=color)
        self.frameAddWeather = Frame(windows,width=700,height=500,bg=color)
        self.frameGPS = Frame(windows,width=700,height=500,bg=color)
        self.frameAddGPS = Frame(windows,width=700,height=500,bg=color)
        self.frameSoft = Frame(windows,width=700,height=500,bg=color)
        self.frameSoftLinux = Frame(windows,width=700,height=500,bg=color)
        self.frameWeb = Frame(windows,width=700,height=500,bg=color)
        self.frameAddWeb = Frame(windows,width=700,height=500,bg=color)
        self.frameEnd =  Frame(windows,width=700,height=500,bg=color)
        #widget 
        labelTitre = [
            Label(self.frameAcceuil,bg=color,fg=textColor,font=("arial","20"),text="Programme de premier demarage de"+nomSoft),
            Label(self.frameUserName,bg=color,fg=textColor,font=("arial","20"),text="Nom d'utilisateur"),
            Label(self.frameUserGenre,bg=color,fg=textColor,font=("arial","20"),text="Genre d'utilisateur"),
            Label(self.frameWeather,bg=color,fg=textColor,font=("arial","20"),text="Meteo"),
            Label(self.frameGPS,bg=color,fg=textColor,font=("arial","20"),text="GPS"),
            Label(self.frameSoft,bg=color,fg=textColor,font=("arial","20"),text="Logiciel"),
            Label(self.frameWeb,bg=color,fg=textColor,font=("arial","20"),text="Site internet"),
            Label(self.frameEnd,bg=color,fg=textColor,font=("arial","20"),text="Configuration terminer")
        ]
        btnSuivant = [
            Button(self.frameAcceuil,bg=color,fg=textColor,font=("arial","15"),text="Commencer",command=self._passUserName),#0
            Button(self.frameUserName,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passUserGenre),#1
            Button(self.frameUserGenre,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passMeteo),#2
            Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passGPS),#3
            Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passSoft),#4
            Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passWeb),#5
            Button(self.frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Suivant",command=self._passEnd),#6
            Button(self.frameEnd,bg=color,fg=textColor,font=("arial","15"),text="Commencer à utiliser "+nomSoft,command=self._end)#7
        ]
        #frameUserName & frameUserGenre
        frameNameUser = Frame(self.frameUserName,bg=color)
        frameGenreUser = Frame(self.frameUserGenre,bg=color)
        labelIndicationUser = [
            Label(frameNameUser,bg=color,fg=textColor,font=("arial","15"),text="Nom :"),
            Label(frameGenreUser,bg=color,fg=textColor,font=("arial","15"),text="Genre :")
            ]
        self.entryName = Entry(frameNameUser,font=("arial","15"),borderwidth=2,relief="solid")
        menuGenre = OptionMenu(frameGenreUser,self.varGenre,*listGenre)
        #frameWeather
        btnDomicile = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile",command=lambda : self._viewAddMeteo("domicile"))
        btnTravail = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Lien de travail",command=lambda : self._viewAddMeteo("travail"))
        btnVille = Button(self.frameWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter une ville",command=lambda : self._viewAddMeteo("ville"))
        #frameAddWeather
        self.labelTitreAdd = [Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Domicile"),
                          Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ville"),
                          Label(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Travail")]
        self.entryVille = Entry(self.frameAddWeather,font=("arial","15"),borderwidth=2,relief="solid")
        self.btnAdd = Button(self.frameAddWeather,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameGPS
        btnAdresseDomicile = Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de domicile",command=lambda :self._viewAddGPS("domicile"))
        btnAdresseTravail = Button(self.frameGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de Travail",command=lambda :self._viewAddGPS("travail"))
        #frameAddGPS
        self.labelTitreGPSAdd = [
            Label(self.frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de votre domicile"),
            Label(self.frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Adresse de votre lieu de travail")
        ]
        self.entryAdresse = Entry(self.frameAddGPS,font=("arial","15"),borderwidth=2,relief="solid")
        self.btnGPSAdd = Button(self.frameAddGPS,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameSoft
        btnWord = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Traitement de texte",command=lambda:self._viewAddSoft("Ttexte"))
        btnExel = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Tableur",command=lambda:self._viewAddSoft("tableur"))
        btnPresentation = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Presentation",command=lambda:self._viewAddSoft("presentation"))
        btnBrowser = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Navigateur",command=lambda:self._viewAddSoft("internet"))
        btnNote = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Note",command=lambda:self._viewAddSoft("note"))
        btnMusic = Button(self.frameSoft,bg=color,fg=textColor,font=("arial","15"),text="Musique",command=lambda:self._viewAddSoft("musique"))
        #frameAddSoft
        self.labelTitreSoft = [
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de traitement de texte"),
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un tableur"),
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de presentation"),
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un navigateur internet"),
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de note"),
            Label(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter un logiciel de musique"),
        ]
        self.entryCommandLinux = Entry(self.frameSoftLinux,font=("arial","15"),borderwidth=2,relief="solid")
        self.btnAddSoft = Button(self.frameSoftLinux,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        #frameWeb
        btnCloud = Button(self.frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Stokage cloud ",command=lambda:self._viewAddWeb("cloud"))
        btnSiteWeb= Button(self.frameWeb,bg=color,fg=textColor,font=("arial","15"),text="Racourcie site",command=lambda:self._viewAddWeb("site"))
        #frameAddWeb
        self.labelIndicationWeb = [Label(self.frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Lien de votre stokage cloud"),
                              Label(self.frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Racourcie d'un site")]
        self.entryNameSite = Entry(self.frameAddWeb,font=("arial","15"),borderwidth=2,relief="solid")
        self.entryLienSite = Entry(self.frameAddWeb,font=("arial","15"),borderwidth=2,relief="solid")
        self.btnAddSite = Button(self.frameAddWeb,bg=color,fg=textColor,font=("arial","15"),text="Ajouter")
        
        #calcule affichage
        largeurFrame = self.frameAcceuil.winfo_reqwidth()
        hauteurFrame = self.frameAcceuil.winfo_reqheight()
        
        #affichage
        #frameAcceuil
        labelTitre[0].place(x=((largeurFrame-labelTitre[0].winfo_reqwidth())//2),y=0)
        btnSuivant[0].place(relx=0.5,rely=0.5,anchor="center")
        #frameUserName
        labelTitre[1].place(x=((largeurFrame-labelTitre[1].winfo_reqwidth())//2),y=0)
        btnSuivant[1].place(x=((largeurFrame-btnSuivant[1].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[1].winfo_reqheight()))
        labelIndicationUser[0].pack(side="left")
        self.entryName.pack(side="left")
        frameNameUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameUserGenre
        labelTitre[2].place(x=((largeurFrame-labelTitre[2].winfo_reqwidth())//2),y=0)
        labelIndicationUser[1].pack(side="left")
        menuGenre.pack(side="left")
        btnSuivant[2].place(x=((largeurFrame-btnSuivant[2].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[2].winfo_reqheight()))
        frameGenreUser.place(relx=0.5,rely=0.5,anchor="center")
        #frameWeather
        labelTitre[3].place(x=((largeurFrame-labelTitre[3].winfo_reqwidth())//2),y=0)
        btnDomicile.place(x=15,y=((hauteurFrame-btnDomicile.winfo_reqheight())//2))
        btnVille.place(relx=0.5,rely=0.5,anchor="center")
        btnTravail.place(x=((largeurFrame-btnTravail.winfo_reqwidth())-15),y=((hauteurFrame-btnTravail.winfo_reqheight())//2))
        btnSuivant[3].place(x=((largeurFrame-btnSuivant[3].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[3].winfo_reqheight()))
        #frameAddWeather
        self.entryVille.place(relx=0.5,rely=0.5,anchor="center")
        self.btnAdd.place(x=((largeurFrame-self.btnAdd.winfo_reqwidth())//2),y=(hauteurFrame-self.btnAdd.winfo_reqheight()))
        #frameGPS
        labelTitre[4].place(x=((largeurFrame-labelTitre[4].winfo_reqwidth())//2),y=0)
        btnAdresseDomicile.place(x=15,y=((hauteurFrame-btnAdresseDomicile.winfo_reqheight())//2))
        btnAdresseTravail.place(x=(largeurFrame-btnAdresseTravail.winfo_reqwidth())-15,y=((hauteurFrame-btnAdresseTravail.winfo_reqheight())//2))
        btnSuivant[4].place(x=((largeurFrame-btnSuivant[4].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[4].winfo_reqheight()))
        #frameAddGPS
        self.entryAdresse.place(relx=0.5,rely=0.5,anchor="center")
        self.btnGPSAdd.place(x=((largeurFrame-self.btnGPSAdd.winfo_reqwidth())//2),y=(hauteurFrame-self.btnGPSAdd.winfo_reqheight()))
        #frameSoft
        labelTitre[5].place(x=((largeurFrame-labelTitre[4].winfo_reqwidth())//2),y=0)
        btnWord.place(x=15,y=100)
        btnExel.place(x=(largeurFrame-btnExel.winfo_reqwidth()-15),y=100)
        btnPresentation.place(x=15,y=200)
        btnBrowser.place(x=(largeurFrame-btnBrowser.winfo_reqwidth()-15),y=200)
        btnNote.place(x=15,y=300)
        btnMusic.place(x=(largeurFrame-btnMusic.winfo_reqwidth()-15),y=300)
        btnSuivant[5].place(x=((largeurFrame-btnSuivant[5].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[4].winfo_reqheight()))
        #frameAddSoft
        if (self.dectOS.osWindows() == False) and (self.dectOS.osLinux()==True):
            self.entryCommandLinux.place(relx=0.5,rely=0.5,anchor="center")
        self.btnAddSoft.place(x=((largeurFrame-self.btnAddSoft.winfo_reqwidth())//2),y=(hauteurFrame-self.btnAddSoft.winfo_reqheight()))
        #frameWeb
        labelTitre[6].place(x=((largeurFrame-labelTitre[6].winfo_reqwidth())//2),y=0)
        btnCloud.place(x=15,y=((hauteurFrame-btnCloud.winfo_reqheight())//2))
        btnSiteWeb.place(x=(largeurFrame-btnSiteWeb.winfo_reqwidth())-15,y=((hauteurFrame-btnSiteWeb.winfo_reqheight())//2))
        btnSuivant[6].place(x=((largeurFrame-btnSuivant[6].winfo_reqwidth())//2),y=(hauteurFrame-btnSuivant[6].winfo_reqheight()))
        #frameAddWeb
        self.btnAddSite.place(x=((largeurFrame-self.btnAddSite.winfo_reqwidth())//2),y=(hauteurFrame-self.btnAddSite.winfo_reqheight()))
        #frameEnd
        labelTitre[7].place(x=((largeurFrame-labelTitre[7].winfo_reqwidth())//2),y=0)
        btnSuivant[7].place(relx=0.5,rely=0.5,anchor="center")
       

    def _clearView(self):
        self.frameAcceuil.pack_forget()
        self.frameUserName.pack_forget()
        self.frameUserGenre.pack_forget()
        self.frameWeather.pack_forget()
        self.frameAddWeather.pack_forget()
        self.frameGPS.pack_forget()
        self.frameAddGPS.pack_forget()
        self.frameSoft.pack_forget()
        self.frameSoftLinux.pack_forget()
        self.frameWeb.pack_forget()
        self.frameAddWeb.pack_forget()
        self.frameEnd.pack_forget()

    def active(self):
        self.frameAcceuil.pack()

    def _passUserName(self):
        self._clearView()
        self.frameUserName.pack()
        
    def _passUserGenre(self):
        if self.entryName.get():
            self._clearView()
            self.frameUserGenre.pack()
            self.fileUser.EcritureJSON("user",self.entryName.get())
        else :
            messagebox.showerror("Erreur","Veuillez entrer un nom d'utilisateur avant de continuer")
    
    def _activeFrameWeather(self):
        self._clearView()
        self.frameWeather.pack()

    def _passMeteo(self):
        if self.varGenre.get():
            self._activeFrameWeather()
            self.fileUser.EcritureJSON("genre",self.varGenre.get())
        else :
           messagebox.showerror("Erreur","Veuillez entrer selectionner un genre avant de continuer") 
    
    def _viewAddMeteo(self,mode):
        self._clearView()
        self.entryVille.delete("0",END)
        self.frameAddWeather.pack()
        self.labelTitreAdd[0].place_forget()
        self.labelTitreAdd[1].place_forget()
        self.labelTitreAdd[2].place_forget()
        if mode == "domicile" :
            self.labelTitreAdd[0].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[0].winfo_reqwidth())//2),y=0)
            self.btnAdd.configure(command=lambda : self._addMeteo(mode))
        else :
            if mode == "travail" :
                self.labelTitreAdd[2].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[2].winfo_reqwidth())//2),y=0)
                self.btnAdd.configure(command=lambda : self._addMeteo(mode))
            else :
                if mode == "ville" :
                    self.labelTitreAdd[1].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreAdd[1].winfo_reqwidth())//2),y=0)
                    self.btnAdd.configure(command=lambda : self._addMeteo(mode))
        
    
    def _addMeteo(self,mode):
        valeur = self.entryVille.get()
        if valeur:
            if mode == "domicile" :
                self.fileUser.EcritureJSON("lieuDomicile",valeur)
            else :
                if mode == "travail" :
                    self.fileUser.EcritureJSON("lieuTravail",valeur)  
                else :
                    if mode == "ville" :
                        self.fileUser.EcritureJSONList("listVille",valeur) 
            self._activeFrameWeather()
        else :
            self._activeFrameWeather()
            messagebox.showerror("Erreur","Aucun ville n'a été marquer dans la zone de texte")
    
    def _passGPS(self):
        self._clearView()
        self.frameGPS.pack()
    
    def _viewAddGPS(self,mode:str):
        self._clearView()
        self.frameAddGPS.pack()
        self.entryAdresse.delete("0",END)
        self.labelTitreGPSAdd[0].place_forget()
        self.labelTitreGPSAdd[1].place_forget()
        if mode == "domicile":
            self.labelTitreGPSAdd[0].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreGPSAdd[0].winfo_reqwidth())//2),y=0)
            self.btnGPSAdd.configure(command=lambda : self._addGPS(mode))
        else :
            if mode == "travail" :
                self.labelTitreGPSAdd[1].place(x=((self.frameAcceuil.winfo_reqwidth()-self.labelTitreGPSAdd[0].winfo_reqwidth())//2),y=0)
                self.btnGPSAdd.configure(command=lambda : self._addGPS(mode))

    def _addGPS(self,mode:str):
        valeur = self.entryAdresse.get()
        if valeur : 
            if mode == "domicile":
                self.fileUser.EcritureJSON("adresseDomicile",valeur)
                self._passGPS()
            else :
                if mode == "travail" :
                    self.fileUser.EcritureJSON("adresseTravail",valeur)
                    self._passGPS()
        else :
            self._passGPS()
            messagebox.showerror("Erreur","Aucun adresse n'a été marquer dans la zone de texte")
   
    def _passSoft(self):
        if (self.dectOS.osWindows() == True) :
            sortie = ""
            while not sortie :
                sortie = self.softWin.setEmplacementSoft()
                self.fileNeuron.EcritureJSON("emplacementSoftWindows",sortie)
        self._clearView()
        self.frameSoft.pack()
    
    def _viewAddSoft(self,mode:str):
        if (self.dectOS.osWindows() == True) :
            if mode == "Ttexte":
                self.softWin.setName("Ttexte")
                self.softWin.saveSoftware()
                self.fileUser.EcritureJSON("wordWindows",self.softWin.getName())
            else :
                if mode == "tableur":
                    self.softWin.setName("tableur")
                    self.softWin.saveSoftware()
                    self.fileUser.EcritureJSON("exelWindows",self.softWin.getName())
                else :
                    if mode == "presentation" :
                        self.softWin.setName("presentation")
                        self.softWin.saveSoftware()
                        self.fileUser.EcritureJSON("diapoWindows",self.softWin.getName())
                    else :
                        if mode == "internet" :
                            self.softWin.setName("internet")
                            self.softWin.saveSoftware()
                            self.fileUser.EcritureJSON("browserWindows",self.softWin.getName())
                        else :
                            if mode == "note" :
                                self.softWin.setName("note")
                                self.softWin.saveSoftware()
                                self.fileUser.EcritureJSON("noteWindows",self.softWin.getName())
                            else :
                                if mode == "musique" :
                                    self.softWin.setName("musique")
                                    self.softWin.saveSoftware()
                                    self.fileUser.EcritureJSON("musicWindows",self.softWin.getName())
        else :
            if (self.dectOS.osLinux() == True) :
                self.entryCommandLinux.delete("0",END)
                self._clearView()
                self.frameSoftLinux.pack()
                largeur = self.frameAcceuil.winfo_reqwidth()
                for i in range(0,5):
                    self.labelTitreSoft[i].place_forget()
                if mode == "Ttexte":
                    self.labelTitreSoft[0].place(x=((largeur-self.labelTitreSoft[0].winfo_reqwidth())//2),y=0)
                else :
                    if mode == "tableur":
                        self.labelTitreSoft[1].place(x=((largeur-self.labelTitreSoft[1].winfo_reqwidth())//2),y=0)
                    else :
                        if mode == "presentation" :
                            self.labelTitreSoft[2].place(x=((largeur-self.labelTitreSoft[2].winfo_reqwidth())//2),y=0)
                        else :
                            if mode == "internet" :
                                self.labelTitreSoft[3].place(x=((largeur-self.labelTitreSoft[3].winfo_reqwidth())//2),y=0)
                            else :
                                if mode == "note" :
                                    self.labelTitreSoft[4].place(x=((largeur-self.labelTitreSoft[4].winfo_reqwidth())//2),y=0)
                                else :
                                    if mode == "musique" :
                                        self.labelTitreSoft[5].place(x=((largeur-self.labelTitreSoft[5].winfo_reqwidth())//2),y=0)
                self.btnAddSoft.configure(command=lambda : self._addSoft(mode))
    
    def _addSoft(self,mode:str):
        command = self.entryCommandLinux.get()
        if command :
            if mode == "Ttexte":
                self.fileUser.EcritureJSON("wordLinux",command)
            else :
                if mode == "tableur":
                    self.fileUser.EcritureJSON("exelLinux",command)
                else :
                    if mode == "presentation" :
                        self.fileUser.EcritureJSON("diapoLinux",command)
                    else :
                        if mode == "internet" :
                            self.fileUser.EcritureJSON("browserLinux",command)
                        else :
                            if mode == "note" :
                                self.fileUser.EcritureJSON("noteLinux",command)
                            else :
                                if mode == "musique" :
                                    self.fileUser.EcritureJSON("musicLinux",command)
            messagebox.showinfo("Enregistrement logiciel","Votre logiciel a ete enregister")
        else :
            messagebox.showerror("Erreur","Veuillez marquer une command pour l'enregistrer le logiciel")
        self._clearView()
        self._passSoft()
                    
    def _passWeb(self):
        self._clearView()
        self.frameWeb.pack()

    def _viewAddWeb(self,mode:str):
        self._clearView()
        self.frameAddWeb.pack()
        self.entryLienSite.delete("0",END)
        self.entryNameSite.delete("0",END)
        self.entryLienSite.place_forget()
        self.entryNameSite.place_forget()
        for i in range(0,1):
            self.labelIndicationWeb[i].place_forget()
        largeurFrame = self.frameAcceuil.winfo_reqwidth()
        if mode == "cloud":
            self.labelIndicationWeb[0].place(x=((largeurFrame-self.labelIndicationWeb[0].winfo_reqwidth())//2),y=0)
            self.entryLienSite.place(rely=0.5,relx=0.5,anchor="center")
            self.btnAddSite.configure(command=lambda:self._addWeb("cloud"))
        else :
            if mode == "site":
                self.labelIndicationWeb[1].place(x=((largeurFrame-self.labelIndicationWeb[0].winfo_reqwidth())//2),y=0)
                self.entryLienSite.place(x=((largeurFrame-self.entryLienSite.winfo_reqwidth())//2),y=200)
                self.entryNameSite.place(x=((largeurFrame-self.entryNameSite.winfo_reqwidth())//2),y=100)
                self.btnAddSite.configure(command=lambda:self._addWeb("site"))
    
    def _addWeb(self,mode:str):
        self._passWeb()
        if mode == "cloud":
            lien = self.entryLienSite.get()
            if lien :
                self.fileUser.EcritureJSON("lienCloud",lien)
                messagebox.showinfo("Lien","Votre lien a ete enregistrer")
            else :
                messagebox.showerror("Erreur","Aucun lien n'a ete marquer dans la zone de texte")
        else :
            if mode == "site":
                name = self.entryNameSite.get()
                lien = self.entryLienSite.get()
                if lien and name :
                    self.fileUser.EcritureJSONDictionnaire("dictSite",name,lien)
                    nbSire = int(self.fileUser.lectureJSON("nbSite"))
                    self.fileUser.EcritureJSON("nbSite",str(nbSire+1))
                    messagebox.showinfo("Lien","Votre lien a ete enregistrer")
                else :
                    messagebox.showerror("Erreur","Aucun lien ou nom n'a ete marquer dans les zones de textes")
        

    def _passEnd(self):
        self._clearView()
        self.frameEnd.pack()
    
    def _end(self):
        self.windows.destroy()