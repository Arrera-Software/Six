import time
from src.AssistantSix import*
from src.pygamePlaysound import*
from librairy.travailJSON import *
import requests
import threading as th
import random
import os
from librairy.dectectionOS import*
from src.CArreraTrigerWord import*
from src.srcSix import*
import signal
from tkinter import*
from tkinter.messagebox import*
from setting.ArreraGazelleUIOld import*
from PIL import Image, ImageTk

VERSION = ""

class SixGUI :
    def __init__(self,icon:str,jsonConfAssistant:str,jsonUser:str,jsonNeuronNetwork:str,jsonConfSetting:str,jsonListeFete:str):
        # var
        self.__emplacementIcon = icon
        self.__nameSoft = "Arrera Six"
        self.__themeNB = int # 0 : white 1 : black
        self.__darkModeEnable = bool
        # Teste de la connextion internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        # Instantation de l'objet Six
        self.__six = CArreraSix(jsonUser,
                                jsonNeuronNetwork,
                                jsonListeFete)
        # Instentation de l'objet Arrera Triger
        self.__objTriger = CArreraTrigerWord("6")
        # Instantation de l'objet srcSix
        self.__objSRCSix = SIXsrc(jsonWork(jsonConfAssistant))
        # Objet 
        self.__objetDectOS = OS()
        # Creation du theard Trigger word
        self.__TriggerWorkStop = th.Event()
        # Creation du theard Minuteur Actu 
        self.__thMinuteurActu = th.Thread(target=self.__minuteurActu)
        # initilisation fenetre
        self.__screen = Tk()
        self.__screen.title(self.__nameSoft)
        self.__screen.geometry("500x350+5+30")
        self.__screen.maxsize(500,400)
        self.__screen.minsize(500,400)
        self.__screen.protocol("WM_DELETE_WINDOW",self.__onClose)
        self.__screen.iconphoto(False,PhotoImage(file=self.__emplacementIcon))
        # Declaration de l'objet Arrera Gazelle 
        self.__gazelleUI = CArreraGazelleUIOld(self.__screen,jsonUser,jsonNeuronNetwork,jsonConfAssistant,jsonConfSetting)
        self.__gazelleUI.passQuitFnc(self.__quitParametre)
        # Fichier json
        self.__fileSixConfig = jsonWork(jsonConfAssistant)
        # Teste de de la connection internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        # initilisation du menu six
        sixMenu = Menu(self.__screen)
        sixMenu.add_command(label="Parametre",command=self.__activeParametre)
        sixMenu.add_command(label="A propos",command=self.__Apropop )
        self.__screen.configure(menu=sixMenu)
        # widget et canvas
        # canvas
        self.__canvasAcceuil = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasBoot0 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasBoot1 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasBoot2 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasBoot3 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasParole1 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasParole2 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasParole3 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasNoConnect = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasContent = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasColere = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasSurprit = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasTriste1 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)
        self.__canvasTriste2 = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasParaOpen = Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)

        self.__canvasActu = Canvas(self.__screen,width=500,height=600,highlightthickness=0)

        self.__canvasMute = [Canvas(self.__screen, width = 500,height = 350, highlightthickness=0),
                             Canvas(self.__screen, width = 500,height = 350, highlightthickness=0)]
        # widget 
        self.__entryUser = Entry(self.__screen,font=("Arial","20"),width=25,relief=SOLID)
        self.__labelTextDuringSpeak = Label(self.__canvasParole2,font=("arial","15"),bg="red", bd=0)
        self.__labelTextAfterSpeak = Label(self.__canvasParole3,font=("arial","15"),bg="red", bd=0)
        # Label Micro 
        self.__labelTriggerMicro = Label(self.__screen,width=50,height=40)
        self.__labelMicroRequette = Label(self.__screen,width=50,height=40)
        # Canvas Actu
        self.__labelActu = Label(self.__canvasActu,font=("arial","15"),bg="red", bd=0)
        self.__btnQuitActu = Button(self.__canvasActu,text="Quitter",font=("arial","15"),bg="red",command=self.__quitActu)
        self.__btnReadActu =  Button(self.__canvasActu,text="Lire a voix haute",font=("arial","15"),bg="red")
        self.__btnStopMute = [Button(self.__canvasMute[0],text="Demute",font=("arial","15"),bg="red",command=self.__quitMute),
                             Button(self.__canvasMute[1],text="Demute",font=("arial","15"),bg="red",command=self.__quitMute)]
        self.__btnQuitMute = [Button(self.__canvasMute[0],text="Quitter",font=("arial","15"),bg="red",command=self.__quit),
                             Button(self.__canvasMute[1],text="Quitter",font=("arial","15"),bg="red",command=self.__quit)]   
        # appelle de la methode pour initiliser le gui
        self.__setTheme()
        #Affichage label parole
        self.__labelTextDuringSpeak.place(x=30,y=110)
        self.__labelTextAfterSpeak.place(x=10,y=80)
        self.__labelActu.place(x=70,y=0)
        self.__btnReadActu.place(relx=0, rely=1, anchor='sw')
        self.__btnQuitActu.place(relx=1, rely=1, anchor='se')
        self.__btnStopMute[0].place(relx=0, rely=1, anchor='sw')
        self.__btnQuitMute[0].place(relx=1, rely=1, anchor='se')
        self.__btnStopMute[1].place(relx=0, rely=1, anchor='sw')
        self.__btnQuitMute[1].place(relx=1, rely=1, anchor='se')
        # Mise a place de la touche entree
        if (self.__objetDectOS.osWindows()==True) and (self.__objetDectOS.osLinux()==False) : 
            self.__detectionTouche(self.__envoie,13)
        else :
            if (self.__objetDectOS.osWindows()==False) and (self.__objetDectOS.osLinux()==True) :
                self.__detectionTouche(self.__envoie,36)
    
    def __setTheme(self):
        fileImage = ["acceuil.png","triste1.png","triste2.png","sureprit.png","mute1.png",
                           "mute2.png","noConnect.png","parole1.png","parole2.png","parole3.png",
                           "boot0.png","boot1.png","boot2.png","boot3.png","colere.png","content.png",
                           "actu.png","micro.png","microIcon.png","parametreOpen.png"]
        theme = self.__fileSixConfig.lectureJSON("theme") #Valeur possible "white" et "dark"
        emplacementGUI  = "asset/IMGinterface/"
        cheminImage = str
        if theme == "white" :
            cheminImage = emplacementGUI+"white/"
            self.__screen.configure(bg="white")
            self.__labelTextAfterSpeak.configure(bg="#ffffff",fg="#000000")
            self.__labelActu.configure(bg="#ffffff",fg="#000000")
            self.__btnReadActu.configure(bg="#ffffff",fg="#000000")
            self.__btnQuitActu.configure(bg="#ffffff",fg="#000000")
            self.__btnStopMute[0].configure(bg="#ffffff",fg="#000000")
            self.__btnQuitMute[0].configure(bg="#ffffff",fg="#000000")
            self.__btnStopMute[1].configure(bg="#ffffff",fg="#000000")
            self.__btnQuitMute[1].configure(bg="#ffffff",fg="#000000")
            self.__labelTriggerMicro.configure(bg="#ffffff")
            self.__labelMicroRequette.configure(bg="#ffffff")
            self.__themeNB = 0 
            self.__darkModeEnable = False
        else :
            if theme == "dark" :
                cheminImage = emplacementGUI+"dark/"
                self.__screen.configure(bg="black")
                self.__labelTextAfterSpeak.configure(bg="#000000",fg="#ffffff")
                self.__labelActu.configure(bg="#000000",fg="#ffffff")
                self.__btnReadActu.configure(bg="#000000",fg="#ffffff")
                self.__btnQuitActu.configure(bg="#000000",fg="#ffffff")
                self.__btnStopMute[0].configure(bg="#000000",fg="#ffffff")
                self.__btnQuitMute[0].configure(bg="#000000",fg="#ffffff")
                self.__btnStopMute[1].configure(bg="#000000",fg="#ffffff")
                self.__btnQuitMute[1].configure(bg="#000000",fg="#ffffff")
                self.__labelTriggerMicro.configure(bg="#000000")
                self.__labelMicroRequette.configure(bg="#000000")
                self.__themeNB = 1
                self.__darkModeEnable = True
            else :
                cheminImage = emplacementGUI+"white/"
                self.__screen.configure(bg="white")
                self.__labelTextAfterSpeak.configure(bg="#ffffff",fg="#000000")
                self.__labelActu.configure(bg="#ffffff",fg="#000000")
                self.__btnReadActu.configure(bg="#ffffff",fg="#000000")
                self.__btnQuitActu.configure(bg="#ffffff",fg="#000000")
                self.__btnStopMute[0].configure(bg="#ffffff",fg="#000000")
                self.__btnQuitMute[0].configure(bg="#ffffff",fg="#000000")
                self.__btnStopMute[1].configure(bg="#ffffff",fg="#000000")
                self.__btnQuitMute[1].configure(bg="#ffffff",fg="#000000")
                self.__labelTriggerMicro.configure(bg="#ffffff")
                self.__labelMicroRequette.configure(bg="#ffffff")
                self.__themeNB = 0 
                self.__darkModeEnable = False
        self.__labelTextDuringSpeak.configure(bg="#2b3ceb",fg="white")
        #Recuperation des image
        bgAcceuil = PhotoImage(file=cheminImage+fileImage[0],master=self.__canvasAcceuil)

        bgBoot0 = PhotoImage(file=cheminImage+fileImage[10],master=self.__canvasBoot0)
        bgBoot1 = PhotoImage(file=cheminImage+fileImage[11],master=self.__canvasBoot1)
        bgBoot2 = PhotoImage(file=cheminImage+fileImage[12],master=self.__canvasBoot2)
        bgBoot3 = PhotoImage(file=cheminImage+fileImage[13],master=self.__canvasBoot3)

        bgParole1 = PhotoImage(file=cheminImage+fileImage[7],master=self.__canvasParole1) 
        bgParole2  = PhotoImage(file=cheminImage+fileImage[8],master=self.__canvasParole2)
        bgParole3  = PhotoImage(file=cheminImage+fileImage[9],master=self.__canvasParole3)

        bgNoConnect = PhotoImage(file=cheminImage+fileImage[6],master=self.__canvasNoConnect)

        bgContent = PhotoImage(file=cheminImage+fileImage[15],master=self.__canvasContent)
        bgColere = PhotoImage(file=cheminImage+fileImage[14],master=self.__canvasColere)
        bgSurprit = PhotoImage(file=cheminImage+fileImage[3],master=self.__canvasSurprit)

        bgTriste1 = PhotoImage(file=cheminImage+fileImage[1],master=self.__canvasTriste1)
        bgTriste2 = PhotoImage(file=cheminImage+fileImage[2],master=self.__canvasTriste2)

        bgMicroEnable = PhotoImage(file=cheminImage+fileImage[17],master=self.__labelTriggerMicro)
        bgParaOpen = PhotoImage(file=cheminImage+fileImage[19],master=self.__canvasParaOpen)

        bgActu = PhotoImage(file=cheminImage+fileImage[16],master=self.__canvasActu)

        bgMute = [PhotoImage(file=cheminImage+fileImage[4],master=self.__canvasMute[0]),
                  PhotoImage(file=cheminImage+fileImage[5],master=self.__canvasMute[1])]
        
        bgMicroRequette = PhotoImage(file=cheminImage+fileImage[18],master=self.__labelMicroRequette)
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
        self.__canvasParaOpen.image_names = bgParaOpen
        self.__labelTriggerMicro.image_names =  bgMicroEnable
        self.__canvasActu.image_names = bgActu
        self.__canvasMute[0].image_names =  bgMute[0]
        self.__canvasMute[1].image_names =  bgMute[1]
        self.__labelTriggerMicro.image_names = bgMicroEnable
        self.__labelMicroRequette.image_names = bgMicroRequette
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
        self.__canvasParaOpen.create_image( 0, 0, image =bgParaOpen , anchor = "nw")
        self.__canvasActu.create_image( 0, 0, image =bgActu , anchor = "nw")
        self.__canvasMute[0].create_image( 0, 0, image =bgMute[0] , anchor = "nw")
        self.__canvasMute[1].create_image( 0, 0, image =bgMute[1] , anchor = "nw")
        self.__labelTriggerMicro.configure(image=bgMicroEnable)
        self.__labelTriggerMicro.configure(image=bgMicroEnable)
        self.__labelMicroRequette.configure(image=bgMicroRequette)
    

    def active(self):
        theardSequenceBoot = th.Thread(target=self.__sequenceBoot)
        theardSequenceBoot.start()
        self.__screen.mainloop()
    
    def __Apropop(self):
        if self.__themeNB == 0 :
            background = "white"
            textColor = "black"
        else :
            if self.__themeNB == 1 :
                background = "black"
                textColor = "white"
            else :
                background = "white"
                textColor = "black"
        #Variable
        copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        tailleIMG = (100,100)
        #Creation de la fenetre
        about = Tk()
        #about.configure(bg="white")
        about.title("A propos :"+self.__nameSoft)
        about.maxsize(400,300)
        about.minsize(400,300)
        about.configure(bg=background)
        #Traitement Image
        imageOrigine = Image.open(self.__emplacementIcon)    
        imageRedim = imageOrigine.resize(tailleIMG)
        icon = ImageTk.PhotoImage(imageRedim)
        #Label
        labelIcon = Label(about,bg=background)
        icon = ImageTk.PhotoImage(imageRedim,master=labelIcon)
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+self.__nameSoft+"\n",font=("arial","12"),bg=background,fg=textColor)
        labelVersion = Label(about,text=VERSION+"\n",font=("arial","11"),bg=background,fg=textColor)
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg=background,fg=textColor)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()
        about.mainloop()
    
    def __onClose(self):
        if (askyesno("Atention","Voulez-vous vraiment fermer Six")):
            self.__quit()
    
    def __quit(self):
        os.kill(os.getpid(), signal.SIGINT)
    
    def __sequenceBoot(self):
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
        self.__canvasAcceuil.place(x=0,y=0)
        if (self.__etatConnexion==False):
            self.__canvasAcceuil.place_forget()
            self.__screen.protocol("WM_DELETE_WINDOW",self.__quit)
            self.__canvasNoConnect.place(x=0,y=0)
            self.__screen.update()
        else :
            self.__entryUser.pack(side="bottom")
            self.__sequenceParole(self.__six.boot())
            self.__startingTriggerWord()
    
    def __clearView(self):
        self.__labelTriggerMicro.place_forget()
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
        self.__canvasParaOpen.place_forget()
    
    def __sequenceParole(self,texte:str):
        thSpeak = th.Thread(target=paroleSix,args=(texte,))
        self.__clearView()
        self.__canvasParole1.place_forget()
        self.__canvasParole2.place(x=0,y=0)
        self.__labelTextDuringSpeak.configure(text=texte,wraplength=440,justify="left")
        self.__screen.update()
        thSpeak.start()
        thSpeak.join()
        self.__canvasParole2.place_forget()
        self.__canvasParole3.place(x=0,y=0)
        self.__labelTextAfterSpeak.configure(text=texte,wraplength=475,justify="left")
        del thSpeak
        
        
    def __sequenceArret(self):
        texte = self.__six.shutdown()
        self.__clearView()
        self.__labelTextDuringSpeak.configure(text=texte,wraplength=320)
        self.__canvasParole2.place(x=0,y=0)
        self.__screen.update()
        paroleSix(texte)
        self.__canvasParole2.place_forget()
        self.__canvasBoot3.place(x=0,y=0)
        self.__screen.update()
        time.sleep(0.2)
        self.__canvasBoot3.place_forget()
        self.__canvasBoot2.place(x=0,y=0)
        self.__screen.update()
        time.sleep(0.2)
        self.__canvasBoot2.place_forget()
        self.__canvasBoot3.place(x=0,y=0)
        self.__screen.update()
        time.sleep(0.2)
        self.__canvasBoot3.place_forget()
        self.__canvasBoot0.place(x=0,y=0)
        self.__screen.update()
        time.sleep(0.2)
        self.__canvasBoot0.place_forget()
        self.__screen.update()

    def __detectionTouche(self,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        self.__screen.bind("<Key>", anychar)  
    
    def __envoie(self): 
        texte = self.__entryUser.get()
        if ("parametre" in texte ) :
            self.__activeParametre()
        else :
            if ("mute" in texte):
                self.__viewMute()
            else :
                self.__six.neuron(texte)
                self.__clearView()
                self.__canvasParole1.place(x=0,y=0)
                self.__screen.update()
                nbSortie = self.__six.getNbSortie()
                if (nbSortie==15):
                    self.__sequenceArret()
                    self.__quit()
                else :
                    if (nbSortie==11):
                        self.__sequenceParoleReponseNeuron("Désoler, il a un probleme qui m'empeche de vous donner votre résumer")
                    else :
                        listSortie  = self.__six.getListSortie()
                        if (nbSortie==12):
                            self.__sequenceParoleReponseNeuron("Okay voici votre résumer des actualités du jour. J'éspere qui vous sera utile")
                            self.__viewActu(listSortie)
                        else :
                            self.__sequenceParoleReponseNeuron(listSortie[0])
        self.__entryUser.delete(0,END)
    
    def __sequenceParoleReponseNeuron(self,text:str):
        self.__canvasParole1.place_forget()
        self.__canvasParole2.place(x=0,y=0)
        self.__labelTextDuringSpeak.configure(text=text,wraplength=440,justify="left")
        self.__screen.update()
        paroleSix(text)
        self.__canvasParole2.place_forget()
        self.__canvasParole3.place(x=0,y=0)
        self.__labelTextAfterSpeak.configure(text=text,wraplength=475,justify="left")

    def __reloadTheme(self):
        self.__setTheme()
        self.__screen.update()
    
    def __activeParametre(self):
        self.__stopingTriggerWord()
        self.__screen.title(self.__nameSoft+" : Parametre")
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.update()
        self.__clearView()
        self.__entryUser.pack_forget()
        self.__gazelleUI.active(self.__darkModeEnable)
    
    def __quitParametre(self):
        self.__screen.maxsize(500,400)
        self.__screen.minsize(500,400)
        self.__screen.title(self.__nameSoft)
        self.__screen.update()
        self.__sequenceParole("Les parametre on etais mit a jour")
        self.__startingTriggerWord()
        self.__entryUser.pack(side="bottom")
        self.__reloadTheme()
    
    def __sixTrigerWord(self):
        sortieTriger = int 
        sortieMicro = str
        while not self.__TriggerWorkStop.is_set():
            self.__microTriggerEnable()
            sortieTriger = self.__objTriger.detectWord()
            self.__microTriggerDisable()
            if (sortieTriger == 1 ):
                self.__microRequetteEnable()
                sortieMicro = self.__objSRCSix.micro()
                self.__entryUser.delete(0,END)
                if (sortieMicro!="nothing"):
                    self.__entryUser.insert(0,sortieMicro)
                self.__microRequetteDisable()
                time.sleep(0.2)
                self.__envoie()
    
    def __viewActu(self,listSortie:list):
        self.__clearView()
        self.__entryUser.pack_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.update()
        self.__canvasActu.place(x=0,y=0)
        self.__labelActu.configure(text=listSortie[0]+
                                   "\n"+listSortie[1]+
                                   "\n"+listSortie[2]+
                                   "\n"+listSortie[3]+
                                   "\n"+listSortie[4]+
                                   "\n"+listSortie[5],
                                   justify="left",
                                   wraplength=400)
        self.__btnReadActu.configure(command=lambda:self.__readActu(listSortie[0]+
                                   "."+listSortie[1]+
                                   "."+listSortie[2]+
                                   "."+listSortie[3]+
                                   "."+listSortie[4]+
                                   "."+listSortie[5]))
        self.__stopingTriggerWord()
        self.__thMinuteurActu.start()
    
    def __quitActu(self):
        self.__clearView()
        self.__canvasActu.place_forget()
        self.__screen.maxsize(500,400)
        self.__screen.minsize(500,400)
        self.__screen.update()
        self.__entryUser.pack(side="bottom")
        self.__screen.update()
        self.__sequenceParole("J'éspere que sa vous a étais utile")
        self.__startingTriggerWord()
        del self.__thMinuteurActu
        self.__thMinuteurActu = th.Thread(target=self.__minuteurActu)
    
    def __readActu(self,texte:str):
        thSpeak = th.Thread(target=paroleSix,args=(texte,))
        thSpeak.start()
        thSpeak.join()
        del thSpeak
    
    def __minuteurActu(self):
        time.sleep(60)
        self.__quitActu()
    
    def __viewMute(self):
        self.__sequenceParole("Okay je vous laisse tranquille")
        self.__clearView()
        self.__stopingTriggerWord()
        self.__entryUser.pack_forget()
        self.__screen.maxsize(500,350)
        self.__screen.minsize(500,350)
        self.__screen.update()
        nb = random.randint(0,1)
        self.__canvasMute[nb].place(x=0,y=0)
    
    def __quitMute(self):        
        self.__clearView()
        self.__screen.maxsize(500,400)
        self.__screen.minsize(500,400)
        self.__screen.update()
        self.__canvasMute[0].place_forget()
        self.__canvasMute[1].place_forget()
        self.__entryUser.pack(side="bottom")
        self.__screen.update()
        self.__sequenceParole("Content d'etre de retour")
        self.__startingTriggerWord()
    
    def __microTriggerEnable(self):
        self.__labelTriggerMicro.place(relx=1.0, rely=0.0, anchor='ne')
        self.__screen.update()
    
    def __microTriggerDisable(self):
        self.__labelTriggerMicro.place_forget()
        self.__screen.update()
    
    def __microRequetteEnable(self):
        self.__labelMicroRequette.place(relx=1.0, rely=0.0, anchor='ne')
        self.__screen.update()
    
    def __microRequetteDisable(self):
        self.__labelMicroRequette.place_forget()
        self.__screen.update()
    
    def __startingTriggerWord(self):
        # Création du thread Trigger word
        self.__thTrigger = th.Thread(target=self.__sixTrigerWord)
        self.__TriggerWorkStop.clear()
        self.__thTrigger.start()

    def __stopingTriggerWord(self):
        self.__TriggerWorkStop.set()