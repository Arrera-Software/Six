from setting.arreraAssistantSetting import *
from src.SIXGestion import*
from src.pygamePlaysound import paroleSix
import threading as th

class sixTk :
    def __init__(self,gestionnaire:SIXGestion):
        self.para = ArreraSettingAssistant("setting/configSetting.json","configNeuron.json","sixConfig.json","FileUser/configUser.json") 
        self.gestionnaire = gestionnaire

    
    def activePara(self):
        self.screenPara = Tk()
        self.para.windows(self.screenPara)
        self.para.passageFonctionQuitter(self.fncQuit)
        self.para.mainView()
        self.screenPara.mainloop()

    def muteSix(self)->int:
        self.varOut = 0
        screenMute = Tk()
        screenMute.title("Assistant Mute")
        #screenMute.iconphoto(False,PhotoImage(file="asset/logo.png"))
        screenMute.maxsize(500,500)
        screenMute.minsize(500,500)
        frameMute = Frame(screenMute,width=500,height=500)
        
        fond = Label(frameMute,width=500,height=500)
        photo = PhotoImage(file=self.gestionnaire.getGUIMute(),master=fond)
        fond.image_names = photo
        fond.configure(image=photo)

        btnQuitter = Button(frameMute,text="Quitter",font=("arial","15"),command=lambda:self.quitMute(screenMute))
        btnUmute = Button(frameMute,text="Demuter",font=("arial","15"),command=lambda:self.uMute(screenMute))
        btnUmute.place(x=((frameMute.winfo_reqwidth()-btnUmute.winfo_reqwidth())-20),y=((frameMute.winfo_reqheight()-btnUmute.winfo_reqheight())-20))
        btnQuitter.place(x=20,y=((frameMute.winfo_reqheight()-btnQuitter.winfo_reqheight())-20))
        frameMute.pack()
        fond.place(x=0,y=0)
        screenMute.mainloop()
        return self.varOut
    
    def uMute(self,screen:Tk):
        self.varOut = 0 
        screen.destroy()
    
    def quitMute(self,screen:Tk):
        self.varOut = 15
        screen.destroy()
    
    def fncQuit(self):
        self.screenPara.destroy()

class SixTKMain :
    def __init__(self,gestion:SIXGestion):
        self.__gestionnaire = gestion 
        self.__textMicro = ""
    

    def acticeWindows(self):
        self.windows = Tk()
        self.windows.title("Six : Assistant")
        self.windows.geometry("600x500+5+30")
        self.windows.maxsize(600,500)
        self.windows.minsize(600,500)
        self.windows.overrideredirect(True)
        #Frame
        self.__frameMain = Frame(self.windows,height=500,width=600)
        self.__frameAcceuil = Frame(self.windows,height=500,width=600)
        self.__frameParoleSmall = Frame(self.windows,height=500,width=600)
        self.__frameParoleBig = Frame(self.windows,height=500,width=600)
        self.__frameAttend1 = Frame(self.windows,height=500,width=600)
        self.__frameAttend2 = Frame(self.windows,height=500,width=600)
        self.__frameAttend3 = Frame(self.windows,height=500,width=600)
        self.__frameNoConnect = Frame(self.windows,height=500,width=600)
        #Label Image
        self.__labelImageMain = Label(self.__frameMain)
        self.__labelImageAcceuil = Label(self.__frameAcceuil)
        self.__labelImageParoleSmall = Label(self.__frameParoleSmall)
        self.__labelImageParoleBig = Label(self.__frameParoleBig)
        self.__labelImageAttend1 = Label(self.__frameAttend1)
        self.__labelImageAttend2 = Label(self.__frameAttend2)
        self.__labelImageAttend3 = Label(self.__frameAttend3)
        self.__labelImageNoConnecte = Label(self.__frameNoConnect)
        #variable largeur hauteur fenetre 
        largeur = self.__frameMain.winfo_reqwidth()
        #label 
        self.__textcanvasAcceuil = Label(self.__frameAcceuil,font=("arial","15"),text="",width=36)
        self.__textSmallSix = Label(self.__frameParoleSmall,font=("arial","15"),text="",width=40)
        self.__textSmallUser = Label(self.__frameParoleSmall,font=("arial","15"),text="",width=40)
        self.__textBigSix = Label(self.__frameParoleBig,font=("arial","15"),text="",width=38)
        self.__textBigUser = Label(self.__frameParoleBig,font=("arial","15"),text="",width=40)
        #definition du flag theard
        self.flagBoucle = th.Event()
        self.flagBoucle.set()
        #Mise en place du theme
        self.setTheme()
        #Affichage
        #  Label Image
        self.__labelImageAcceuil.place(x=0,y=0)
        self.__labelImageMain.place(x=0,y=0)
        self.__labelImageParoleSmall.place(x=0,y=0)
        self.__labelImageParoleBig.place(x=0,y=0)
        self.__labelImageAttend1.place(x=0,y=0)
        self.__labelImageAttend2.place(x=0,y=0)
        self.__labelImageAttend3.place(x=0,y=0)
        self.__labelImageNoConnecte.place(x=0,y=0)
        # Label Text
        self.__textSmallSix.place(x=140,y=95)
        self.__textSmallUser.place(x=140,y=345)
        self.__textBigSix.place(x=150,y=10)
        self.__textBigUser.place(x=140,y=365)
        self.__textcanvasAcceuil.place(x=((largeur-self.__textcanvasAcceuil.winfo_reqwidth())//2),y=235)
        #Affichage main
        self.__frameMain.pack()
    
    def setTheme(self):
        self.__gestionnaire.setTheme()
        #image GUI
        mainGUI = self.__gestionnaire.getGUIMain()
        acceuilGUI = self.__gestionnaire.getGUIAcceuil()
        paroleSmallGUI = self.__gestionnaire.getGUIparoleSmallSmall()
        paroleBigGUI =self.__gestionnaire.getGUIparoleBigSmall()
        listAttendGUI = self.__gestionnaire.getGUIAttent()
        attentGUI1 = str(listAttendGUI[0])
        attentGUI2 = str(listAttendGUI[1])
        attentGUI3 = str(listAttendGUI[2])
        noConnectGUI = self.__gestionnaire.getGUINoConnecte()
        colorTK = self.__gestionnaire.getColorInterface()
        colorLabel = self.__gestionnaire.getColorLabel()
        colorText = self.__gestionnaire.getGUItextColor()
        #Couleur fenetre
        self.windows.configure(bg=colorTK)
        #Main
        mainIMG = PhotoImage(file=mainGUI)
        self.__labelImageMain.configure(image=mainIMG)
        self.__labelImageMain.image = mainIMG
        #Acceuil
        acceuilIMG = PhotoImage(file=acceuilGUI)
        self.__labelImageAcceuil.configure(image=acceuilIMG)
        self.__labelImageAcceuil.image=acceuilIMG
        #ParoleSmall
        paroleSmallIMG = PhotoImage(file=paroleSmallGUI)
        self.__labelImageParoleSmall.configure(image=paroleSmallIMG)
        self.__labelImageParoleSmall.image=paroleSmallIMG
        #ParoleBig
        paroleBigIMG = PhotoImage(file=paroleBigGUI)
        self.__labelImageParoleBig.configure(image=paroleBigIMG)
        self.__labelImageParoleBig.image= paroleBigIMG
        #Attend1
        attend1IMG = PhotoImage(file=attentGUI1)
        self.__labelImageAttend1.configure(image=attend1IMG)
        self.__labelImageAttend1.image=attend1IMG
        #Attend2
        attend2IMG = PhotoImage(file=attentGUI2)
        self.__labelImageAttend2.configure(image=attend2IMG)
        self.__labelImageAttend2.image=attend2IMG
        #Attend3
        attend3IMG = PhotoImage(file=attentGUI3)
        self.__labelImageAttend3.configure(image=attend3IMG)
        self.__labelImageAttend3.image=attend3IMG
        #no connect
        noConnectIMG = PhotoImage(file=noConnectGUI)
        self.__labelImageNoConnecte.configure(image=noConnectIMG)
        self.__labelImageNoConnecte.image=noConnectIMG
        #label
        self.__textcanvasAcceuil.configure(bg=colorLabel,fg=colorText)
        self.__textSmallSix.configure(bg=colorLabel,fg=colorText)
        self.__textSmallUser.configure(bg=colorLabel,fg=colorText)
        self.__textBigSix.configure(bg=colorLabel,fg=colorText)
        self.__textBigUser.configure(bg=colorLabel,fg=colorText)
        #Frame 
        self.__frameMain.configure(bg=colorTK)
        self.__frameAcceuil.configure(bg=colorTK)
        self.__frameParoleSmall.configure(bg=colorTK)
        self.__frameParoleBig.configure(bg=colorTK)
        self.__frameAttend1.configure(bg=colorTK)
        self.__frameAttend2.configure(bg=colorTK)
        self.__frameAttend3.configure(bg=colorTK)
        self.__frameNoConnect.configure(bg=colorTK)
        #color parametre
        #self.__gestionnaire.setColorThemePara()
    

    def bootInterface(self):
        self.updateWindows()
        self.windows.mainloop()

    def __clearView(self):
        self.__frameMain.pack_forget()
        self.__frameAcceuil.pack_forget()
        self.__frameParoleSmall.pack_forget()
        self.__frameParoleBig.pack_forget()
        self.__frameAttend1.pack_forget()
        self.__frameAttend2.pack_forget()
        self.__frameAttend3.pack_forget()

    def setTextMicro(self,texte:str):
        self.__textMicro = texte
    
    def viewBigParole(self,texte:str):
        self.__clearView()
        self.windows.lift()
        self.__frameAcceuil.pack()
        if self.__compteur(texte) > 5 :
            texte1,texte2 = self.__division(texte,5)
            if self.__compteur(texte2) > 5 :
                texte2,texte3 =  self.__division(texte2,5)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
            else :
                allTexte = texte1+"\n"+texte2
        else :
            allTexte = texte
        self.__textcanvasAcceuil.configure(text=allTexte)
    
    def noConnectionInterface(self):
        self.__frameMain.pack_forget()
        self.windows.overrideredirect(False)
        self.__frameNoConnect.pack()
        self.updateWindows()

    
    def viewParoleGUI(self,texte:str):
        self.__clearView()
        self.windows.lift()
        if self.__compteur(texte) > 6 :
            texte1,texte2 = self.__division(texte,6)
            if self.__compteur(texte2) > 6 :
                texte2,texte3 =  self.__division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
            else :
                allTexte = texte1+"\n"+texte2
            self.__frameParoleBig.pack()
            self.__textBigSix.configure(text=allTexte)
            self.__textBigUser.configure(text=self.__textMicro)
        else :
            allTexte = texte
            self.__frameParoleSmall.pack()
            self.__textSmallSix.configure(text=allTexte)
            self.__textSmallUser.configure(text=self.__textMicro)
        
        self.windows.update()
    

    def __division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def __compteur(self,s:str):
        mots = s.split()
        return int(len(mots))   

    def updateWindows(self):
        self.windows.after(1000,self.updateWindows) 
    
    def destroyWindows(self):
        self.windows.destroy()

    def __formatageText(self,texte):
        nbMots = 7
        if int(len(texte)) > nbMots  :
            texte1,texte2 = self.__division(texte,nbMots)
            allTexte = texte1+"\n"+texte2
            if int(len(texte2)) > nbMots :
                texte2,texte3 = self.__division(texte2,nbMots)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
                if int(len(texte3)) > nbMots:
                    texte3,texte4 = self.__division(texte3,nbMots)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3+"\n"+texte4
        else :
            allTexte = texte
        return str(allTexte)
    
    def vueActu(self,sortie:list,valeur:int):
        color = self.__gestionnaire.getColorInterface()
        colorLabel = self.__gestionnaire.getColorLabel()
        colorTextLabel = self.__gestionnaire.getGUItextColor()
        colorText = self.__gestionnaire.getColorTextActu()
        if (valeur == 3):
            textOpen = "Voici les actualités du jour."
        else :
            if valeur == 11 :
                textOpen = "Je ne peux pas faire votre resumer une erreur et survenu"
            else :
                if valeur == 12 :
                    textOpen = "Voici votre resumer"
        self.viewBigParole(textOpen)
        paroleSix(textOpen)
        windows = Tk()
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.configure(bg=color)
        labelActu = Label(windows,bg=color,fg=colorText,font=("arial","14"), anchor="w")
        labelActu.place(x="0",y="0")
        btnRead = Button(windows,text ="lire a haute voix",bg=colorLabel,fg=colorTextLabel,font=("arial","15"),width=40)
        btnRead.pack(side="bottom")
        if (valeur==3):
            text = self.__formatageText(sortie[0])+"\n\n"+self.__formatageText(sortie[1])+"\n\n"+self.__formatageText(sortie[2])
            windows.title("Six : Actualites")
            labelActu.configure(text=text, anchor="w")
            btnRead.configure(command=lambda: self.__readActu(text,windows))
            textClose = "J'espere que sa vous a interessez"
        else :
            if valeur == 11 :
                windows.title("Six : Resumer")
                labelActu.configure(text="Une erreur c'est produite", anchor="w")
                btnRead.configure(text="Quitter",command=lambda :windows.destroy())
                textClose = "Desoler pour cette erreur"
            else :
                if valeur == 12 :
                    text = self.__formatageText(sortie[0])+"\n"+self.__formatageText(sortie[1])+"\n La fete du jour est : "+self.__formatageText(sortie[2])+"\n"+self.__formatageText(sortie[3])+"\n"+self.__formatageText(sortie[4])+"\n\n"+self.__formatageText(sortie[5])
                    windows.title("Six : Resumer")
                    labelActu.configure(text=text, anchor="w")
                    btnRead.configure(command=lambda: self.__readActu(text,windows))
                    textClose = "J'espere que votre resumer vous a plu"
        windows.mainloop()
        self.viewBigParole(textClose)
        paroleSix(textClose)

    def __readActu(self,text:str,windows:Tk):
        parole = th.Thread(target= paroleSix,args=(text,))
        parole.start()
        parole.join()
        windows.destroy()
        