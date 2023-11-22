from setting.arreraAssistantSetting import *
from PIL import Image, ImageTk
from src.SIXGestion import*
import re
import threading as th
from arreraLynx.arreraLynx import*

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
    

class interfaceLynx :
    def __init__(self):
        screen = Tk()
        arreraLynx = ArreraLynx(screen,jsonWork("arreraLynx/configLynx.json"),jsonWork("FileUser/configUser.json"),jsonWork("configNeuron.json"))
        arreraLynx.active()
        screen.mainloop()

    

class SixTKMain :
    def __init__(self,gestion:SIXGestion):
        self.__gestionnaire = gestion 
        self.__gestionnaire.setTheme()
        self.__mainGUI = self.__gestionnaire.getGUIMain()
        self.__acceuilIMG = self.__gestionnaire.getGUIAcceuil()
        self.__paroleSmallIMG = self.__gestionnaire.getGUIparoleSmallSmall()
        self.__paroleBigIMG =self.__gestionnaire.getGUIparoleBigSmall()
        listAttendIMG = self.__gestionnaire.getGUIAttent()
        self.__attentIMG1 = str(listAttendIMG[0])
        self.__attentIMG2 = str(listAttendIMG[1])
        self.__attentIMG3 = str(listAttendIMG[2])
        self.__noConnectIMG = self.__gestionnaire.getGUINoConnecte()
        self.__colorTK = self.__gestionnaire.getColorInterface()
        self.__colorLabel = self.__gestionnaire.getColorLabel()
        self.__colorText = self.__gestionnaire.getGUItextColor()
        self.__textMicro = ""
        

    def acticeWindows(self):
        self.windows = Tk()
        self.windows.configure(bg=self.__colorTK)
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
        labelImageMain = Label(self.__frameMain)
        labelImageAcceuil = Label(self.__frameAcceuil)
        labelImageParoleSmall = Label(self.__frameParoleSmall)
        labelImageParoleBig = Label(self.__frameParoleBig)
        labelImageAttend1 = Label(self.__frameAttend1)
        labelImageAttend2 = Label(self.__frameAttend2)
        labelImageAttend3 = Label(self.__frameAttend3)
        labelImageNoConnecte = Label(self.__frameNoConnect)
        #image de fond
        #Main
        mainIMG = PhotoImage(file=self.__mainGUI)
        labelImageMain.configure(image=mainIMG)
        labelImageMain.image = mainIMG
        #Acceuil
        acceuilIMG = PhotoImage(file=self.__acceuilIMG)
        labelImageAcceuil.configure(image=acceuilIMG)
        labelImageAcceuil.image=acceuilIMG
        #ParoleSmall
        paroleSmallIMG = PhotoImage(file=self.__paroleSmallIMG)
        labelImageParoleSmall.configure(image=paroleSmallIMG)
        labelImageParoleSmall.image=paroleSmallIMG
        #ParoleBig
        paroleBigIMG = PhotoImage(file=self.__paroleBigIMG)
        labelImageParoleBig.configure(image=paroleBigIMG)
        labelImageParoleBig.image= paroleBigIMG
        #Attend1
        attend1IMG = PhotoImage(file=self.__attentIMG1)
        labelImageAttend1.configure(image=attend1IMG)
        labelImageAttend1.image=attend1IMG
        #Attend2
        attend2IMG = PhotoImage(file=self.__attentIMG2)
        labelImageAttend2.configure(image=attend2IMG)
        labelImageAttend2.image=attend2IMG
        #Attend3
        attend3IMG = PhotoImage(file=self.__attentIMG3)
        labelImageAttend3.configure(image=attend3IMG)
        labelImageAttend3.image=attend3IMG
        #no connect
        noConnectIMG = PhotoImage(file=self.__noConnectIMG)
        labelImageNoConnecte.configure(image=noConnectIMG)
        labelImageNoConnecte.image=noConnectIMG
        #variable largeur hauteur fenetre 
        largeur = self.__frameMain.winfo_reqwidth()
        #label 
        self.__textcanvasAcceuil = Label(self.__frameAcceuil,font=("arial","15"),text="", bg=self.__colorLabel,fg=self.__colorText,width=36)
        self.__textSmallSix = Label(self.__frameParoleSmall,font=("arial","15"),text="", bg=self.__colorLabel,fg=self.__colorText,width=40)
        self.__textSmallUser = Label(self.__frameParoleSmall,font=("arial","15"),text="", bg=self.__colorLabel,fg=self.__colorText,width=40)
        self.__textBigSix = Label(self.__frameParoleBig,font=("arial","15"),text="", bg=self.__colorLabel,fg=self.__colorText,width=38)
        self.__textBigUser = Label(self.__frameParoleBig,font=("arial","15"),text="", bg=self.__colorLabel,fg=self.__colorText,width=40)
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
        labelImageNoConnecte.place(x=0,y=0)
        # Label Text
        self.__textSmallSix.place(x=140,y=95)
        self.__textSmallUser.place(x=140,y=345)
        self.__textBigSix.place(x=150,y=10)
        self.__textBigUser.place(x=140,y=365)
        self.__textcanvasAcceuil.place(x=((largeur-self.__textcanvasAcceuil.winfo_reqwidth())//2),y=235)
        #Affichage main
        self.__frameMain.pack()
    

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