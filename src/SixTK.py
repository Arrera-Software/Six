from setting.arreraAssistantSetting import *
from PIL import Image, ImageTk
from src.SIXGestion import*
import re
import threading as th

class sixTk :
    def __init__(self,gestionnaire:SIXGestion):
        self.para = ArreraSettingAssistant("setting/configSetting.json","configNeuron.json","sixConfig.json","FileUser/configUser.json") 
        self.gestionnaire = gestionnaire

    
    def activePara(self):
        self.screenPara = Tk()
        self.screenPara.iconphoto(False,PhotoImage(file="asset/logo.png"))
        self.para.windows(self.screenPara)
        self.para.passageFonctionQuitter(self.fncQuit)
        self.para.mainView()
        self.screenPara.mainloop()

    def muteSix(self)->int:
        self.varOut = 0
        screenMute = Tk()
        image = Image.open(self.gestionnaire.getGUIMute())
        photo = PhotoImage(image)
        screenMute.title("Assistant Mute")
        screenMute.iconphoto(False,PhotoImage(file="asset/logo.png"))
        screenMute.maxsize(500,500)
        screenMute.minsize(500,500)
        fond = Canvas(screenMute,width=500,height=500)
        fond.create_image(0, 0, anchor=NW, image=photo)
        btnQuitter = Button(fond,text="Quitter",font=("arial","15"),command=lambda:self.quitMute(screenMute))
        btnUmute = Button(fond,text="Demuter",font=("arial","15"),command=lambda:self.uMute(screenMute))
        btnUmute.place(x=((fond.winfo_reqwidth()-btnUmute.winfo_reqwidth())-20),y=((fond.winfo_reqheight()-btnUmute.winfo_reqheight())-20))
        btnQuitter.place(x=20,y=((fond.winfo_reqheight()-btnQuitter.winfo_reqheight())-20))
        fond.pack()
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
        self.gestionnaire = gestion 
        self.gestionnaire.setTheme()
        self.mainGUI = self.gestionnaire.getGUIMain()
        self.acceuilIMG = self.gestionnaire.getGUIAcceuil()
        self.paroleSmallIMG = self.gestionnaire.getGUIparoleSmallSmall()
        self.paroleBigIMG =self.gestionnaire.getGUIparoleBigSmall()
        listAttendIMG = self.gestionnaire.getGUIAttent()
        self.attentIMG1 = str(listAttendIMG[0])
        self.attentIMG2 = str(listAttendIMG[1])
        self.attentIMG3 = str(listAttendIMG[2])
        self.colorTK = self.gestionnaire.getColorInterface()
        self.colorLabel = self.gestionnaire.getColorLabel()
        self.colorText = self.gestionnaire.getGUItextColor()
        self.textMicro = ""
        

    def acticeWindows(self):
        self.windows = Tk()
        self.windows.configure(bg=self.colorTK)
        self.windows.title("Six : Assistant")
        self.windows.geometry("600x500+5+30")
        self.windows.maxsize(600,500)
        self.windows.minsize(600,500)
        self.windows.overrideredirect(True)
        #Frame
        self.frameMain = Frame(self.windows,height=500,width=600)
        self.frameAcceuil = Frame(self.windows,height=500,width=600)
        self.frameParoleSmall = Frame(self.windows,height=500,width=600)
        self.frameParoleBig = Frame(self.windows,height=500,width=600)
        self.frameAttend1 = Frame(self.windows,height=500,width=600)
        self.frameAttend2 = Frame(self.windows,height=500,width=600)
        self.frameAttend3 = Frame(self.windows,height=500,width=600)
        #Label Image
        labelImageMain = Label(self.frameMain)
        labelImageAcceuil = Label(self.frameAcceuil)
        labelImageParoleSmall = Label(self.frameParoleSmall)
        labelImageParoleBig = Label(self.frameParoleBig)
        labelImageAttend1 = Label(self.frameAttend1)
        labelImageAttend2 = Label(self.frameAttend2)
        labelImageAttend3 = Label(self.frameAttend3)
        #image de fond
        #Main
        mainIMG = PhotoImage(file=self.mainGUI)
        labelImageMain.configure(image=mainIMG)
        labelImageMain.image = mainIMG
        #Acceuil
        acceuilIMG = PhotoImage(file=self.acceuilIMG)
        labelImageAcceuil.configure(image=acceuilIMG)
        labelImageAcceuil.image=acceuilIMG
        #ParoleSmall
        paroleSmallIMG = PhotoImage(file=self.paroleSmallIMG)
        labelImageParoleSmall.configure(image=paroleSmallIMG)
        labelImageParoleSmall.image=paroleSmallIMG
        #ParoleBig
        paroleBigIMG = PhotoImage(file=self.paroleBigIMG)
        labelImageParoleBig.configure(image=paroleBigIMG)
        labelImageParoleBig.image= paroleBigIMG
        #Attend1
        attend1IMG = PhotoImage(file=self.attentIMG1)
        labelImageAttend1.configure(image=attend1IMG)
        labelImageAttend1.image=attend1IMG
        #Attend2
        attend2IMG = PhotoImage(file=self.attentIMG2)
        labelImageAttend2.configure(image=attend2IMG)
        labelImageAttend2.image=attend2IMG
        #Attend3
        attend3IMG = PhotoImage(file=self.attentIMG3)
        labelImageAttend3.configure(image=attend3IMG)
        labelImageAttend3.image=attend3IMG
        #variable largeur hauteur fenetre 
        largeur = self.frameMain.winfo_reqwidth()
        #label 
        self.textcanvasAcceuil = Label(self.frameAcceuil,font=("arial","15"),text="", bg=self.colorLabel,fg=self.colorText,width=36)
        self.textSmallSix = Label(self.frameParoleSmall,font=("arial","15"),text="", bg=self.colorLabel,fg=self.colorText,width=40)
        self.textSmallUser = Label(self.frameParoleSmall,font=("arial","15"),text="", bg=self.colorLabel,fg=self.colorText,width=40)
        self.textBigSix = Label(self.frameParoleBig,font=("arial","15"),text="", bg=self.colorLabel,fg=self.colorText,width=38)
        self.textBigUser = Label(self.frameParoleBig,font=("arial","15"),text="", bg=self.colorLabel,fg=self.colorText,width=40)
        #definition du flag theard
        self.flagBoucle = th.Event()
        self.flagBoucle.set()
        #Affichage
        #  Label Image
        labelImageAcceuil.place(x=0,y=0)
        labelImageMain.place(x=0,y=0)
        labelImageParoleSmall.place(x=0,y=0)
        labelImageParoleBig.place(x=0,y=0)
        labelImageAttend1.place(x=0,y=0)
        labelImageAttend2.place(x=0,y=0)
        labelImageAttend3.place(x=0,y=0)
        # Label Text
        self.textSmallSix.place(x=140,y=95)
        self.textSmallUser.place(x=140,y=345)
        self.textBigSix.place(x=150,y=10)
        self.textBigUser.place(x=140,y=365)
        self.textcanvasAcceuil.place(x=((largeur-self.textcanvasAcceuil.winfo_reqwidth())//2),y=235)
        #Affichage main
        self.frameMain.pack()
    

    def bootInterface(self):
        self.updateWindows()
        self.windows.mainloop()

    def _clearView(self):
        self.frameMain.pack_forget()
        self.frameAcceuil.pack_forget()
        self.frameParoleSmall.pack_forget()
        self.frameParoleBig.pack_forget()
        self.frameAttend1.pack_forget()
        self.frameAttend2.pack_forget()
        self.frameAttend3.pack_forget()

    def setTextMicro(self,texte:str):
        self.textMicro = texte
    
    def viewBigParole(self,texte:str):
        self._clearView()
        self.frameAcceuil.pack()
        if self._compteur(texte) > 6 :
            texte1,texte2 = self._division(texte,6)
            if self._compteur(texte2) > 6 :
                texte2,texte3 =  self._division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
            else :
                allTexte = texte1+"\n"+texte2
        else :
            allTexte = texte
        self.textcanvasAcceuil.configure(text=allTexte)

    
    def viewParoleGUI(self,texte:str):
        self._clearView()
        if self._compteur(texte) > 6 :
            texte1,texte2 = self._division(texte,6)
            if self._compteur(texte2) > 6 :
                texte2,texte3 =  self._division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
            else :
                allTexte = texte1+"\n"+texte2
            self.frameParoleBig.pack()
            self.textBigSix.configure(text=allTexte)
            self.textBigUser.configure(text=self.textMicro)
        else :
            allTexte = texte
            self.frameParoleSmall.pack()
            self.textSmallSix.configure(text=allTexte)
            self.textBigUser.configure(text=self.textMicro)
        
        self.windows.update()
    

    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))   

    def _sautLigne(texte:str, nbMots:int):
        mots = re.findall(r'\S+\s*', texte)
        lignes = []  
        ligne_actuelle = [] 
        for mot in mots:
            ligne_actuelle.append(mot)
            if len(ligne_actuelle) >= nbMots:
                lignes.append(" ".join(ligne_actuelle))
                ligne_actuelle = []
        if ligne_actuelle:
            lignes.append(" ".join(ligne_actuelle))

        return "\n".join(lignes)

    def updateWindows(self):
        self.windows.after(1000,self.updateWindows) 