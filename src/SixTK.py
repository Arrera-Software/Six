from setting.arreraAssistantSetting import *
from src.SIXGestion import*
from src.srcSix import *
from src.pygamePlaysound import paroleSix
import time
import threading as th
import random

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
        self.__varOut = 0
        screenMute = Tk()
        screenMute.title("Assistant Mute")
        #screenMute.iconphoto(False,PhotoImage(file="asset/logo.png"))
        screenMute.maxsize(500,350)
        screenMute.minsize(500,350)
        screenMute.configure(bg="red")
        frameMute = Canvas(screenMute,width=500,height=350)
        if random.randint(0,1) == 0 :
            photo = PhotoImage(file=self.gestionnaire.getGUIMute1(),master=frameMute)
        else :
           photo = PhotoImage(file=self.gestionnaire.getGUIMute2(),master=frameMute) 
        frameMute.image_names = photo
        frameMute.create_image( 0, 0, image =photo , anchor = "nw")
        btnQuitter = Button(frameMute,text="Quitter",font=("arial","15"),command=lambda:self.quitMute(screenMute))
        btnUmute = Button(frameMute,text="Demuter",font=("arial","15"),command=lambda:self.uMute(screenMute))
        btnUmute.place(x=((frameMute.winfo_reqwidth()-btnUmute.winfo_reqwidth())-20),y=((frameMute.winfo_reqheight()-btnUmute.winfo_reqheight())-20))
        btnQuitter.place(x=20,y=((frameMute.winfo_reqheight()-btnQuitter.winfo_reqheight())-20))
        frameMute.pack()
        frameMute.place(x=0,y=0)
        screenMute.mainloop()
        return self.__varOut
    
    def uMute(self,screen:Tk):
        self.__varOut = 0 
        screen.destroy()
    
    def quitMute(self,screen:Tk):
        self.__varOut = 15
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
        self.windows.geometry("500x350+5+30")
        self.windows.maxsize(500,350)
        self.windows.minsize(500,350)
        self.windows.overrideredirect(True)
        #Canvas
        self.__canvasAcceuil = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasBoot0 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasBoot1 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasBoot2 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasBoot3 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasParole1 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasParole2 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasParole3 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasNoConnect = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasContent = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasColere = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasSurprit = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasTriste1 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        self.__canvasTriste2 = Canvas( self.windows, width = 500,height = 400, highlightthickness=0)
        #label 
        self.__labelTextParole2 = Label(self.__canvasParole2,font=("arial","15"),bg="red")
        self.__labelTextParole1Six = Label(self.__canvasParole1,font=("arial","15"),bg="red")
        self.__labelTextParole1User = Label(self.__canvasParole1,font=("arial","15"),bg="red")
        self.__labelTextParole3Six = Label(self.__canvasParole3,font=("arial","15"),bg="red")
        self.__labelTextParole3User = Label(self.__canvasParole3,font=("arial","15"),bg="red")
        #label Micro
        self.__labelMicro = Label(self.windows)
        #definition du flag theard
        self.flagBoucle = th.Event()
        self.flagBoucle.set()
        #Mise en place du theme
        self.setTheme()
        #Emplacement label
        self.__labelTextParole1Six.place(x=120,y=60)
        self.__labelTextParole1User.place(x=15,y=240)
        self.__labelTextParole3Six.place(x=120,y=60)
        self.__labelTextParole3User.place(x=15,y=240)
        self.__labelTextParole2.place(x=40,y=125)
        
    
    def setTheme(self):
        #Mise en place du theme
        self.__gestionnaire.setTheme()
        #Recuperation des image
        bgAcceuil = PhotoImage(file=self.__gestionnaire.getGUIAcceuil(),master=self.__canvasAcceuil)
        bgBoot0 = PhotoImage(file=self.__gestionnaire.getGUIBoot0(),master=self.__canvasBoot0)
        bgBoot1 = PhotoImage(file=self.__gestionnaire.getGUIBoot1(),master=self.__canvasBoot1)
        bgBoot2 = PhotoImage(file=self.__gestionnaire.getGUIBoot2(),master=self.__canvasBoot2)
        bgBoot3 = PhotoImage(file=self.__gestionnaire.getGUIBoot3(),master=self.__canvasBoot3)
        bgParole1 = PhotoImage(file=self.__gestionnaire.getGUIParole1(),master=self.__canvasParole1) 
        bgParole2  = PhotoImage(file=self.__gestionnaire.getGUIParole2(),master=self.__canvasParole2)
        bgParole3  = PhotoImage(file=self.__gestionnaire.getGUIParole3(),master=self.__canvasParole3)
        bgNoConnect = PhotoImage(file=self.__gestionnaire.getGUINoConnecte(),master=self.__canvasNoConnect)
        bgContent = PhotoImage(file=self.__gestionnaire.getGUIContent(),master=self.__canvasContent)
        bgColere = PhotoImage(file=self.__gestionnaire.getGUIColere(),master=self.__canvasColere)
        bgSurprit = PhotoImage(file=self.__gestionnaire.getGUISurprit(),master=self.__canvasSurprit)
        bgTriste1 = PhotoImage(file=self.__gestionnaire.getGUITrite1(),master=self.__canvasTriste1)
        bgTriste2 = PhotoImage(file=self.__gestionnaire.getGUITrite2(),master=self.__canvasTriste2)
        bgMicro = PhotoImage(file=self.__gestionnaire.getIconMicro(),master=self.__labelMicro)
        #Recuperation coleur
        colorLabelParole = self.__gestionnaire.getColorLabelParole()
        colorLabelParoleUser = self.__gestionnaire.getColorLabelUser()
        colorTextParole = self.__gestionnaire.getTexteColorParole()
        #Formatage des canvas avec leurs image
        self.__canvasAcceuil.image_names = bgAcceuil
        self.__canvasBoot0.image_names = bgBoot0
        self.__canvasBoot1.image_names = bgBoot1
        self.__canvasBoot2.image_names = bgBoot2
        self.__canvasBoot3.image_names = bgBoot3
        self.__canvasParole1.image_names = bgParole1
        self.__canvasParole2.image_names = bgParole2
        self.__canvasParole3.image_names = bgParole3
        self.__canvasNoConnect.image_names = bgNoConnect
        self.__canvasContent.image_names=bgContent
        self.__canvasColere.image_names = bgColere
        self.__canvasSurprit.image_names = bgSurprit
        self.__canvasTriste1.image_names = bgTriste1
        self.__canvasTriste2.image_names = bgTriste2
        self.__labelMicro.image_names =  bgMicro
        #Mise des image dans les canvas
        self.__canvasAcceuil.create_image( 0, 0, image =bgAcceuil , anchor = "nw")
        self.__canvasBoot0.create_image( 0, 0, image =bgBoot0 , anchor = "nw")
        self.__canvasBoot1.create_image( 0, 0, image =bgBoot1 , anchor = "nw")
        self.__canvasBoot2.create_image( 0, 0, image =bgBoot2 , anchor = "nw")
        self.__canvasBoot3.create_image( 0, 0, image =bgBoot3 , anchor = "nw")
        self.__canvasParole1.create_image( 0, 0, image =bgParole1 , anchor = "nw")
        self.__canvasParole2.create_image( 0, 0, image =bgParole2 , anchor = "nw")
        self.__canvasParole3.create_image( 0, 0, image =bgParole3 , anchor = "nw")
        self.__canvasNoConnect.create_image( 0, 0, image =bgNoConnect , anchor = "nw")
        self.__canvasContent.create_image( 0, 0, image =bgContent , anchor = "nw")
        self.__canvasColere.create_image( 0, 0, image =bgColere , anchor = "nw")
        self.__canvasSurprit.create_image( 0, 0, image =bgSurprit , anchor = "nw")
        self.__canvasTriste1.create_image( 0, 0, image =bgTriste1 , anchor = "nw")
        self.__canvasTriste2.create_image( 0, 0, image =bgTriste2 , anchor = "nw")
        #Mise en place de coleur pour les label
        self.__labelTextParole1Six.configure(bg=colorLabelParole,fg=colorTextParole)
        self.__labelTextParole1User.configure(bg=colorLabelParoleUser,fg=colorTextParole)
        self.__labelTextParole3Six.configure(bg=colorLabelParole,fg=colorTextParole)
        self.__labelTextParole3User.configure(bg=colorLabelParoleUser,fg=colorTextParole)
        self.__labelTextParole2.configure(bg=colorLabelParole,fg=colorTextParole)
        self.__labelMicro.configure(image=bgMicro)

    def sequenceBoot(self,src:SIXsrc,texte:str):
        self.__canvasBoot0.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot0.place_forget()
        self.__canvasBoot1.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot1.place_forget()
        self.__canvasBoot2.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot2.place_forget()
        self.__canvasBoot3.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot3.place_forget()
        allTexte = self.__formatageText(texte)
        self.__labelTextParole2.configure(text=allTexte)
        self.__canvasParole2.place(x=0,y=0)
        time.sleep(0.2)
        src.speak(texte)
        self.__canvasParole2.place_forget()
        self.__canvasAcceuil.place(x=0,y=0)
    
    def sequenceArret(self,src:SIXsrc,texte:str):
        self.__clearView()
        allTexte = self.__formatageText(texte)
        self.__labelTextParole2.configure(text=allTexte)
        self.__canvasParole2.place(x=0,y=0)
        src.speak(texte)
        self.__canvasParole2.place_forget()
        self.__canvasBoot3.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot3.place_forget()
        self.__canvasBoot2.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot2.place_forget()
        self.__canvasBoot3.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot3.place_forget()
        self.__canvasBoot0.place(x=0,y=0)
        time.sleep(0.2)
        self.__canvasBoot0.place_forget()

    
    def guiMicro(self,src:SIXsrc):
        self.__labelMicro.place(x=(self.windows.winfo_width()-self.__labelMicro.winfo_reqwidth()),y=(self.windows.winfo_height()-self.__labelMicro.winfo_reqheight()))
        texte = src.micro()
        self.setTextMicro(texte)
        return texte

    def bootInterface(self):
        self.updateWindows()
        self.windows.mainloop()

    def __clearView(self):
        self.__labelMicro.place_forget()
        self.__canvasAcceuil.place_forget()
        self.__canvasBoot0.place_forget()
        self.__canvasBoot1.place_forget()
        self.__canvasBoot2.place_forget()
        self.__canvasBoot3.place_forget()
        self.__canvasParole1.place_forget()
        self.__canvasParole2.place_forget()
        self.__canvasParole3.place_forget()
        self.__canvasNoConnect.place_forget()
        self.__canvasContent.place_forget()
        self.__canvasColere.place_forget()
        self.__canvasSurprit.place_forget()
        self.__canvasTriste1.place_forget()
        self.__canvasTriste2.place_forget()

    def setTextMicro(self,texte:str):
        self.__textMicro = texte
        self.__labelTextParole1User.configure(text=self.__textMicro)
        self.__labelTextParole3User.configure(text=self.__textMicro)
    
    def noConnectionInterface(self):
        self.__clearView()
        self.windows.overrideredirect(False)
        self.__canvasNoConnect.place(x=0,y=0)
        self.updateWindows()

    
    def viewParoleGUI(self,mode:int,texte:str):
        self.__clearView()
        self.windows.lift()
        if mode == 1 :
            if self.__compteur(texte) > 6 :
                texte1,texte2 = self.__division(texte,6)
                if self.__compteur(texte2) > 6 :
                    texte2,texte3 =  self.__division(texte2,6)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3
                    self.__labelTextParole3Six.configure(text=allTexte)
                    self.__canvasParole3.place(x=0,y=0)
                else :
                    allTexte = texte1+"\n"+texte2
                    self.__labelTextParole3Six.configure(text=allTexte)
                    self.__canvasParole3.place(x=0,y=0)
            else :
                allTexte = texte
                self.__labelTextParole1Six.configure(text=allTexte)
                self.__canvasParole1.place(x=0,y=0)
        else :
            allTexte = self.__formatageText(texte)
            self.__labelTextParole2.configure(text=allTexte)
            self.__canvasParole2.place(x=0,y=0)
        self.windows.update()
    
    def activeMute(self):
        self.__clearView()
        if (random.randint(0,1)==1) :
            self.__canvasTriste1.place(x=0,y=0)
        else :
            self.__canvasTriste1.place(x=0,y=0)
    
    def guiNoParole(self):
        self.__clearView()
        if (random.randint(0,1)==1) :
            self.__canvasContent.place(x=0,y=0)
        else :
            self.__canvasAcceuil.place(x=0,y=0)

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

    def __formatageTextActu(self,texte):
        nbMots = 5
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
        color = self.__gestionnaire.getColorGUI()
        textColor = self.__gestionnaire.getColorTextActu()
        if (valeur == 3):
            textOpen = "Voici les actualités du jour."
        else :
            if valeur == 11 :
                textOpen = "Je ne peux pas faire votre resumer une erreur et survenu"
            else :
                if valeur == 12 :
                    textOpen = "Voici votre resumer"
        self.viewParoleGUI(0,textOpen)
        paroleSix(textOpen)
        windows = Tk()
        windows.maxsize(500,600)
        windows.minsize(500,600)
        windows.configure(bg=color)
        #canvas actu
        canvasActu = Canvas(windows, width=500,height=600, highlightthickness=0)
        guiActu = PhotoImage(file=self.__gestionnaire.getGUIActu(),master=canvasActu)
        canvasActu.image_names = guiActu
        canvasActu.create_image( 0, 0, image =guiActu , anchor = "nw")
        canvasActu.place(x=0,y=0)
        #widget
        labelActu = Label(canvasActu,bg=color,fg=textColor,font=("arial","13"), anchor="w")
        labelActu.place(x="75",y="0")
        btnRead = Button(canvasActu,text ="lire a haute voix",bg=color,fg=textColor,font=("arial","15"),width=40)
        btnRead.place(x=((canvasActu.winfo_reqwidth()-btnRead.winfo_reqwidth())//2),y=(canvasActu.winfo_reqheight()-btnRead.winfo_reqheight()))
        if (valeur==3):
            text = self.__formatageTextActu(sortie[0])+"\n\n"+self.__formatageTextActu(sortie[1])+"\n\n"+self.__formatageTextActu(sortie[2])
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
                    text = self.__formatageTextActu(sortie[0])+"\n"+self.__formatageTextActu(sortie[1])+"\n La fete du jour est : "+self.__formatageTextActu(sortie[2])+"\n"+self.__formatageTextActu(sortie[3])+"\n"+self.__formatageTextActu(sortie[4])+"\n\n"+self.__formatageTextActu(sortie[5])
                    windows.title("Six : Resumer")
                    labelActu.configure(text=text, anchor="w")
                    btnRead.configure(command=lambda: self.__readActu(text,windows))
                    textClose = "J'espere que votre resumer vous a plu"
        windows.mainloop()
        self.viewParoleGUI(0,textClose)
        paroleSix(textClose)
        

    def __readActu(self,text:str,windows:Tk):
        parole = th.Thread(target= paroleSix,args=(text,))
        parole.start()
        parole.join()
        windows.destroy()