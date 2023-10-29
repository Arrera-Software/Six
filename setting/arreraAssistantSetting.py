from tkinter import *
from librairy.travailJSON import*
from setting.objetPara.paraUser import*
from setting.objetPara.paraMeteo import*
from setting.objetPara.paraGPS import*
from setting.objetPara.paraRecherche import *
from setting.objetPara.paraSoftware import*
from setting.objetPara.paraInternet import *
from setting.objetPara.paraTheme import*

class ArreraSettingAssistant :
    def __init__(self,configSettingFile:str,configFile:str,configAssistant:str,fichierConfigUser:str):
        self.changeColor = bool 
        self.icon = bool 
        self.fileIcon = str
        self.fnc = None
         
        #overture des fichier
        self.settingFile = jsonWork(configSettingFile)
        self.fileNeuronConfig = jsonWork(configFile)
        self.assistantFile = jsonWork(configAssistant)
        self.fileUser = jsonWork(fichierConfigUser)
        #Recuperarton donner
        #fichier settingFile
        self.colorPrimaire = self.settingFile.lectureJSON("color1")
        self.colorSecondaire = self.settingFile.lectureJSON("color2")
        self.textColorPrimaire = self.settingFile.lectureJSON("textColor1")
        self.textColorSecondaire = self.settingFile.lectureJSON("textColor2")
        if self.settingFile.lectureJSON("colorInterface") == "1" :
            self.changeColor =  True 
            self.listTheme = self.settingFile.lectureJSONList("listeTheme")
        else :
            self.changeColor = False
        if self.settingFile.lectureJSON("setIcon") == "1" : 
            self.icon = True
        else :
            self.icon = False
        #fichier fileconfig 
        self.icon = self.fileNeuronConfig.lectureJSON("iconAssistant")
        self.nameAssistant = self.fileNeuronConfig.lectureJSON("name")
        if self.icon == True :
            self.fileIcon = self.assistantFile.lectureJSON("iconAssistant")
         
       
            
    def windows(self,windows:Tk) ->bool :
        #variable
        xlabel2 = int 
        yBTNQuitter = int 
        listMoteur = ["duckduckgo","google","bing","brave","ecosia","qwant"]
        self.varRecherche = StringVar(windows)
        self.varTheme = StringVar(windows)
        #widget
        #Cadre
        self.cadreMenu = Frame(windows,width=150,height=600,bg=self.colorSecondaire)
        self.cadreAcceuil = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreUser = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreMeteo = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreGPS = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreRecherche = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreSoft = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreInternet = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        self.cadreTheme = Frame(windows,width=350,height=600,bg=self.colorPrimaire)
        #initilisation objet para
        self.paraUser = SettingUser(windows,self.cadreUser,self.fileUser,self.settingFile,self.textColorPrimaire,self.colorPrimaire)
        self.paraMeteo = SettingMeteo(windows,self.cadreMeteo,self.fileUser,self.textColorPrimaire,self.colorPrimaire)
        self.paraGPS = SettingGPS(windows,self.cadreGPS,self.fileUser,self.textColorPrimaire,self.colorPrimaire)
        self.paraRecherche = SettingRecherche(windows,self.cadreRecherche,self.fileUser,self.textColorPrimaire,self.colorPrimaire,listMoteur)
        self.paraSoftware = SettingSoftware(windows,self.cadreSoft,self.fileUser,self.settingFile, self.fileNeuronConfig,self.textColorPrimaire,self.colorPrimaire)
        self.paraInternet = SettingInternet(windows,self.cadreInternet,self.fileUser,self.textColorPrimaire,self.colorPrimaire)
        if self.changeColor == True:
            self.paraTheme = SettingTheme(windows,self.cadreTheme,self.listTheme,self.assistantFile,self.textColorPrimaire,self.colorPrimaire)
        #cadre interne a l'acceuil
        cadresPresentations = [
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid"),
            Frame(self.cadreAcceuil,width=175,height=200,bg=self.colorPrimaire,borderwidth=1, relief="solid")]
        #Label
        labelTitreMenu = Label(self.cadreMenu,text="Menu",font=("arial","20"),bg=self.colorSecondaire,fg=self.textColorSecondaire)
        labelcadresPresentations = [
            Label(cadresPresentations[0],text="Gestion recherche",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[1],text="Gestion meteo",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[2],text="Gestion GPS",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[3],text="Gestion software",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[4],text="Gestion Site internet",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire),
            Label(cadresPresentations[5],text="Gestion theme",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire)]
        if self.changeColor == False :
            labelcadresPresentations[5].configure(text="Cette fonction\nn'est pas\ndisponible sur\ncette assistant")
        #cadresPresentations
        #0
        menuRecherche1 = OptionMenu(cadresPresentations[0],self.varRecherche,*listMoteur)
        btnValiderMoteur1 = Button(cadresPresentations[0],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.rechercheChange)
        #1
        btnMeteo1 = Button(cadresPresentations[1],text="Ajouter\nune ville",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.meteoViewAdd)
        #2
        btnGPSHome = Button(cadresPresentations[2],text="Adresse\nde domicile",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.gpsViewDomicile)
        btnGPSWork = Button(cadresPresentations[2],text="Adresse\nde travail",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.gpsViewWork)
        #3
        btnSoftware1 = Button(cadresPresentations[3],text="Ajouter\nun logiciel",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.softwareAddView)
        #4
        buttonAddSite = Button(cadresPresentations[4],text="Ajouter",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.internetViewAdd)
        buttonSupprSite = Button(cadresPresentations[4],text="Supprimer",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.internetViewSuppr)
        #5
        if self.changeColor == True:
            menuTheme1 = OptionMenu(cadresPresentations[5],self.varTheme,*self.listTheme)
            btnValiderTheme1 = Button(cadresPresentations[5],text="Valider",font=("arial","13"),bg=self.colorPrimaire,fg=self.textColorPrimaire,command=self.setThemeAcceuil)
        #bouton
        #cadre menu
        boutonMenu1 = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Acceuil",command=lambda : self.mainView())
        boutonMenu2 = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Utilisateur",command=lambda :self.userView())
        boutonMenu3 = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Meteo",command=lambda : self.meteoView())
        boutonMenu4=Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="GPS",command=lambda :self.gpsView())
        boutonMenu5=Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Recherche",command=lambda :self.rechercheView())
        boutonMenu6=Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Software",command=lambda :self.softwareView())
        boutonMenu7 = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Internet",command=lambda :self.internetView())
        boutonMenu8=Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Theme",command=lambda :self.themeView())
        boutonQuitter = Button(self.cadreMenu,font=("arial","15"),bg=self.colorPrimaire,fg=self.textColorPrimaire,text="Quitter",command=lambda :self.quittePara())
        #formatage de la fenetre
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.title(self.nameAssistant+": Parametre")
        if self.icon == True :
            windows.iconphoto(False,PhotoImage(file=self.fileIcon))
        #Calcule position
        xlabel2 = int(self.cadreMenu.winfo_width()/2)
        xBoutonMenu = xlabel2 + 5
        yBTNQuitter = int(self.cadreMenu.winfo_reqheight()-boutonQuitter.winfo_reqheight())
        #Cadre acceuil
        cadresPresentations[0].place(x=0,y=0)
        cadresPresentations[1].place(x=180,y=0)
        cadresPresentations[2].place(x=0,y=200)
        cadresPresentations[3].place(x=180,y=200)
        cadresPresentations[4].place(x=0,y=400)
        cadresPresentations[5].place(x=180,y=400)
        #Affichage des cadre composant du cadre acceuil
        labelcadresPresentations[0].place(x=0,y=0)
        menuRecherche1.place(relx=0.5,y=(labelcadresPresentations[0].winfo_reqheight()+45), anchor="center")
        btnValiderMoteur1.place(relx=0.5, rely=1.0, anchor="s")
        labelcadresPresentations[1].place(x=0,y=0)
        btnMeteo1.place(relx=0.5, rely=0.5, anchor="center")
        labelcadresPresentations[2].place(x=0,y=0)
        btnGPSHome.place(relx=0.5, rely=1.0, anchor="s")
        btnGPSWork.place(relx=0.5,y=(labelcadresPresentations[2].winfo_reqheight()+45), anchor="center")
        labelcadresPresentations[3].place(x=0,y=0)
        btnSoftware1.place(relx=0.5, rely=0.5, anchor="center")
        labelcadresPresentations[4].place(x=0,y=0)
        buttonSupprSite.place(relx=0.5, rely=0.5, anchor="center")
        buttonAddSite.place(relx=0.5,y=(labelcadresPresentations[4].winfo_reqheight()+45), anchor="s")
        
        if self.changeColor == True :   
            labelcadresPresentations[5].place(x=0,y=0)
            menuTheme1.place(relx=0.5,y=(labelcadresPresentations[1].winfo_reqheight()+45), anchor="center")
            btnValiderTheme1.place(relx=0.5, rely=1.0, anchor="s")
        else :
            labelcadresPresentations[5].place(relx=0.5, rely=0.5, anchor="center")
        #Affichage cadre menu 
        labelTitreMenu.place(x=xBoutonMenu,y=0)
        boutonMenu1.place(x=xBoutonMenu,y=50)
        boutonMenu2.place(x=xBoutonMenu,y=100)
        boutonMenu3.place(x=xBoutonMenu,y=150)
        boutonMenu4.place(x=xBoutonMenu,y=200)
        boutonMenu5.place(x=xBoutonMenu,y=250)
        boutonMenu6.place(x=xBoutonMenu,y=300)
        boutonMenu7.place(x=xBoutonMenu,y=350)
        if self.changeColor == True :
            boutonMenu8.place(x=xBoutonMenu,y=400)

        boutonQuitter.place(x=xBoutonMenu,y=yBTNQuitter)
        #Affichage cadre principal
        self.cadreMenu.pack(side="left")
        return True 
    
    def _unView(self):
        self.cadreAcceuil.pack_forget()
        self.cadreUser.pack_forget()
        self.cadreMeteo.pack_forget()  
        self.cadreGPS.pack_forget()
        self.cadreRecherche.pack_forget()
        self.cadreSoft.pack_forget()
        self.cadreInternet.pack_forget()
        self.cadreTheme.pack_forget()
        
              
    def mainView(self) -> bool :
        self._unView()
        self.cadreAcceuil.pack(side="left")
        self.cadreAcceuil.update()
        return True 
    
    def userView(self)->bool:
        self._unView()
        self.paraUser.view()
        self.cadreUser.update()
        return True
    
    def meteoView(self) -> bool : 
        self._unView()
        self.paraMeteo.view()
        self.cadreMeteo.update()
        return True 

    def meteoViewAdd(self)->bool:
        self._unView()
        self.paraMeteo.view()
        self.paraMeteo.addView()
        self.cadreMeteo.update()
        return True
    
    def gpsView(self)->bool:
        self._unView()
        self.paraGPS.view()
        self.cadreGPS.update()
        return True 
    
    def gpsViewDomicile(self)->bool:
        self._unView()
        self.paraGPS.view()
        self.paraGPS.domicileView()
        return True

    def gpsViewWork(self)->bool:
        self._unView()
        self.paraGPS.view()
        self.paraGPS.workView()
        return True
    
    def rechercheView(self)->bool  :
        self._unView()
        self.paraRecherche.view()
        return True 

    def rechercheChange(self)->bool:
        self.paraRecherche.writeMoteur(self.varRecherche)
        return True
    
    def softwareView(self)->bool  :
        self._unView()
        self.paraSoftware.view()
        return True 
    
    def softwareAddView(self)->bool:
        self._unView()
        self.paraSoftware.view()
        self.paraSoftware.addView()
        return True
    
    def internetView(self)->bool :
        self._unView()
        self.paraInternet.view()
        return True
    
    def internetViewAdd(self)->bool  :
        self._unView()
        self.paraInternet.view()
        self.paraInternet.addView()
        return True 
    
    def internetViewSuppr(self)->bool  :
        self._unView()
        self.paraInternet.view()
        self.paraInternet.supprView()
        return True 
    
    def themeView(self)->bool  :
        if self.changeColor == True :
            self._unView()
            self.paraTheme.view()
            return True 
        else :
            return False
        
    def setThemeAcceuil(self):
        valeur = self.varTheme.get()
        if valeur :
            self.assistantFile.EcritureJSON("theme",valeur)
        else :
            messagebox.showerror("Erreur","Veuillez selectionner un theme")

    def passageFonctionQuitter(self,fonctionQuitter):
        self.fnc = fonctionQuitter
    
        
    def quittePara(self)->bool :
        self.cadreAcceuil.destroy()
        self.cadreUser.destroy()
        self.cadreMeteo.destroy()
        self.cadreMenu.destroy()
        self.cadreGPS.destroy()
        self.cadreRecherche.destroy()
        self.cadreSoft.destroy()
        self.fnc()    
        return True 
        