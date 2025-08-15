import signal
from setting.ArreraGazelleUISix import*
from librairy.arrera_tk import *
from librairy.arrera_voice import *
from ObjetsNetwork.arreraNeuron import*
from src.languageSIX import *
from librairy.asset_manage import resource_path

class SixGUI :
    def __init__(self,iconFolder:str,iconName:str,
                 jsonConfAssistant:str,jsonUser:str,
                 jsonNeuronNetwork:str,jsonConfSetting:str,
                 version:str):
        # var
        self.__nameSoft = "Arrera Six"
        self.__sixSpeaking = bool
        self.__version = version
        # Teste de la connextion internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        # Demarage d'Arrera TK
        self.__arrTK = CArreraTK()
        # Instantation de l'objet Six
        self.__assistantSix = ArreraNetwork(jsonNeuronNetwork)
        # Instantation de l'objet language
        self.__language = CLanguageSIX("FileJSON/phraseSix.json",
                                       "FileJSON/aideSix.json",
                                       "FileJSON/firstBootSix.json")
        # Instantation de l'objet arrera voice
        self.__avoice = CArreraVoice(jsonWork(jsonConfAssistant))
        # Objet
        self.__objOS = OS()
        # Creation du theard Trigger word
        self.__TriggerWorkStop = th.Event()
        # Recuperation de l'emplacement de l'icon
        if self.__objOS.osWindows():
            self.__emplacementIcon = iconFolder + "/win/" + iconName + ".ico"
        elif self.__objOS.osLinux():
                self.__emplacementIcon = iconFolder + "/linux/" + iconName + ".png"
        elif self.__objOS.osMac() :
            self.__emplacementIcon = resource_path(iconFolder+ "macos/" + iconName+".png")
        # initilisation fenetre
        self.__screen = self.__arrTK.aTK(title="Arrera Six",
                                         icon=self.__emplacementIcon)
        self.__screen.title(self.__nameSoft)
        self.__screen.geometry("500x400+5+30")
        self.__arrTK.setResizable(False)
        self.__screen.protocol("WM_DELETE_WINDOW",self.__onClose)
        # Declaration de l'objet Arrera Gazelle 
        self.__gazelleUI = CArreraGazelleUISix(self.__arrTK,
                                               self.__screen,
                                               jsonUser,
                                               jsonNeuronNetwork,
                                               jsonConfAssistant,
                                               jsonConfSetting,
                                               "asset/Sound/ecoute.mp3")
        self.__gazelleUI.passFNCQuit(self.__quitParametre)
        self.__gazelleUI.passFNCBTNIcon(lambda : self.__apropos())
        # widget et canvas
        # canvas

        # Image de fond
        fileImage = ["acceuil.png",#0
                     "triste1.png",#1
                     "triste2.png",#2
                     "sureprit.png",#3
                     "mute1.png",#4
                     "mute2.png",#5
                     "noConnect.png",#6
                     "parole1.png",#7
                     "parole2.png",#8
                     "parole3.png",#9
                     "boot0.png",#10
                     "boot1.png",#11
                     "boot2.png",#12
                     "boot3.png",#13
                     "colere.png",#14
                     "content.png",#15
                     "actu.png",#16
                     "micro.png",#17
                     "microIcon.png",#18
                     "parametreOpen.png",#19
                     "microsimple.png",#20
                     "settings.png",#21
                     "projet.png",#22
                     "tableur.png",#23
                     "word.png",#24
                     ]
        emplacementGUIDark = "asset/IMGinterface/dark/"
        emplacementGUILight = "asset/IMGinterface/white/"

        # Canvas Acceuil
        self.__canvasAcceuil = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[0],
                                                                       imageDark=emplacementGUIDark+fileImage[0],
                                                                       width=500,height=350)
        # Canvas Boot
        self.__canvasBoot0 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[10],
                                                                       imageDark=emplacementGUIDark+fileImage[10],
                                                                       width=500,height=350)
        self.__canvasBoot1 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[11],
                                                                       imageDark=emplacementGUIDark+fileImage[11],
                                                                       width=500,height=350)
        self.__canvasBoot2 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[12],
                                                                       imageDark=emplacementGUIDark+fileImage[12],
                                                                       width=500,height=350)
        self.__canvasBoot3 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[13],
                                                                       imageDark=emplacementGUIDark+fileImage[13],
                                                                       width=500,height=350)
        # Canvas Parole
        self.__canvasParole1 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[7],
                                                                       imageDark=emplacementGUIDark+fileImage[7],
                                                                       width=500,height=350)
        self.__canvasParole2 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[8],
                                                                       imageDark=emplacementGUIDark+fileImage[8],
                                                                       width=500,height=350)
        self.__canvasParole3 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[9],
                                                                       imageDark=emplacementGUIDark+fileImage[9],
                                                                       width=500,height=350)
        # Canvas NoConnect
        self.__canvasNoConnect = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[6],
                                                                       imageDark=emplacementGUIDark+fileImage[6],
                                                                       width=500,height=350)
        # Canvas Emotion
        self.__canvasContent = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[15],
                                                                       imageDark=emplacementGUIDark+fileImage[15],
                                                                       width=500,height=350)
        self.__canvasColere = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[14],
                                                                       imageDark=emplacementGUIDark+fileImage[14],
                                                                       width=500,height=350)
        self.__canvasSurprit = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[3],
                                                                       imageDark=emplacementGUIDark+fileImage[3],
                                                                       width=500,height=350)
        # Canvas Triste
        self.__canvasTriste1 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[1],
                                                                       imageDark=emplacementGUIDark+fileImage[1],
                                                                       width=500,height=350)
        self.__canvasTriste2 = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[2],
                                                                       imageDark=emplacementGUIDark+fileImage[2],
                                                                       width=500,height=350)
        # Canvas Parametre
        self.__canvasParaOpen = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[19],
                                                                       imageDark=emplacementGUIDark+fileImage[19],
                                                                       width=500,height=350)
        # Canvas Actu
        self.__canvasActu = self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                       imageLight=emplacementGUILight+fileImage[16],
                                                                       imageDark=emplacementGUIDark+fileImage[16],
                                                                       width=500,height=600)
        # Canvas Mute
        self.__canvasMute = [self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                     imageLight=emplacementGUILight+fileImage[4],
                                                                     imageDark=emplacementGUIDark+fileImage[4],
                                                                     width=500,height=350),
                             self.__arrTK.createArreraBackgroudImage(self.__screen,
                                                                     imageLight=emplacementGUILight+fileImage[5],
                                                                     imageDark=emplacementGUIDark+fileImage[5],
                                                                     width=500,height=350)]
        # widget 
        self.__entryUser = self.__arrTK.createEntry(self.__screen, ppolice="Arial", ptaille=25, width=400)
        self.__labelTextDuringSpeak = self.__arrTK.createLabel(self.__canvasParole2,ppolice="Arial",ptaille=20,pstyle="bold")
        self.__labelTextAfterSpeak = self.__arrTK.createLabel(self.__canvasParole3,ppolice="Arial",ptaille=20,pstyle="bold")
        # Label Micro
        imageMicroTriger=self.__arrTK.createImage(pathLight=emplacementGUILight+fileImage[17],
                                                  pathDark=emplacementGUIDark+fileImage[17],
                                                  tailleX=50,tailleY=50)
        imageMicroRequette=self.__arrTK.createImage(pathLight=emplacementGUILight+fileImage[18],
                                                  pathDark=emplacementGUIDark+fileImage[18],
                                                    tailleX=50,tailleY=50)
        imageMicroSimple = self.__arrTK.createImage(pathLight=emplacementGUILight + fileImage[20],
                                                    pathDark=emplacementGUIDark + fileImage[20],
                                                    tailleX=35, tailleY=35)
        imageParametre = self.__arrTK.createImage(pathLight=emplacementGUILight + fileImage[21],
                                                  pathDark=emplacementGUIDark + fileImage[21],
                                                  tailleX=35, tailleY=35)
        imageTableurOpen = self.__arrTK.createImage(pathLight=emplacementGUILight + fileImage[23],
                                                  pathDark=emplacementGUIDark + fileImage[23],
                                                  tailleX=35, tailleY=35)
        imageProjetOpen = self.__arrTK.createImage(pathLight=emplacementGUILight + fileImage[22],
                                                    pathDark=emplacementGUIDark + fileImage[22],
                                                    tailleX=35, tailleY=35)
        imageWordOpen = self.__arrTK.createImage(pathLight=emplacementGUILight + fileImage[24],
                                                    pathDark=emplacementGUIDark + fileImage[24],
                                                    tailleX=35, tailleY=35)

        self.__labelTriggerMicro = self.__arrTK.createLabel(self.__screen,width=50,height=50,image=imageMicroTriger)
        self.__labelMicroRequette = self.__arrTK.createLabel(self.__screen,width=50,height=50,image=imageMicroRequette)

        # Bouton pour montrer qu'un projet/Tableur/Word est ouvert
        self.__btnTableurOpen = self.__arrTK.createButton(self.__canvasParole3,width=35,height=35,
                                                          image=imageTableurOpen,
                                                          command=lambda : self.__winHelpFileAndProjet(1))
        self.__btnWordOpen = self.__arrTK.createButton(self.__canvasParole3, width=35, height=35,
                                                       image=imageWordOpen,
                                                       command = lambda : self.__winHelpFileAndProjet(2))
        self.__btnProjetOpen = self.__arrTK.createButton(self.__canvasParole3, width=35, height=35,
                                                         image=imageProjetOpen,
                                                         command=lambda: self.__winHelpFileAndProjet(3))

        # Bouton pour activer le micro quand le trigger word est pas activer
        self.__btnMicro = self.__arrTK.createButton(self.__screen,width=35,height=35,
                                                    image=imageMicroSimple,command=lambda  : self.__sixMicroEnable())
        # Bouton pour activer les parametre
        self.__btnParametre = self.__arrTK.createButton(self.__screen,width=35,height=35,
                                                        image=imageParametre,command=self.__activeParametre)
        # Canvas Actu
        self.__labelActu = self.__arrTK.createLabel(self.__canvasActu,ppolice="arial",ptaille=15,bg="red",)
        self.__btnQuitActu = self.__arrTK.createButton(self.__canvasActu,text="Quitter",ppolice="arial",ptaille=15,command=self.__quitActu)
        self.__btnReadActu =  self.__arrTK.createButton(self.__canvasActu,text="Lire a voix haute",ppolice="arial",ptaille=15)
        self.__btnStopMute = [self.__arrTK.createButton(self.__canvasMute[0],text="Demute",ppolice="arial",ptaille=15,command=self.__quitMute),
                             self.__arrTK.createButton(self.__canvasMute[1],text="Demute",ppolice="arial",ptaille=15,command=self.__quitMute)]
        self.__btnQuitMute = [self.__arrTK.createButton(self.__canvasMute[0],text="Quitter",ppolice="arial",ptaille=15,command=self.__quit),
                             self.__arrTK.createButton(self.__canvasMute[1],text="Quitter",ppolice="arial",ptaille=15,command=self.__quit)]
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
        if self.__objOS.osWindows() :
            self.__detectionTouche(self.__envoie,13)
        elif self.__objOS.osLinux() :
            self.__detectionTouche(self.__envoie,36)
        elif self.__objOS.osMac() :
            self.__detectionTouche(self.__envoie,603979789)

        # Declaration de la variable pour contenir les theard
        self.__thSpeak = th.Thread()
        self.__thSpeakNeuron = th.Thread()
        self.__thSpeakActu = th.Thread()
        self.__thMinuteurActu = th.Thread()
    
    def __setTheme(self):
        self.__avoice.loadConfig()
        theme = self.__arrTK.getTheme().lower()
        if theme == "light" :
            self.__arrTK.boutonChangeColor(self.__btnMicro,bg="#e0e0e0",hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnWordOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__screen.configure(fg_color="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelTextAfterSpeak,bg="#ffffff",fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelActu,bg="#ffffff",fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelTriggerMicro,bg="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelMicroRequette,bg="#ffffff")
        else :
            if theme == "dark" :
                self.__screen.configure(fg_color="#000000")
                self.__arrTK.boutonChangeColor(self.__btnMicro, bg="#1f1f1f", hoverbg="#505050")
                self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#1f1f1f", hoverbg="#505050")
                self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#1f1f1f", hoverbg="#505050")
                self.__arrTK.boutonChangeColor(self.__btnWordOpen, bg="#1f1f1f", hoverbg="#505050")
                self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#1f1f1f", hoverbg="#505050")
                self.__arrTK.labelChangeColor(self.__labelTextAfterSpeak, bg="#000000",fg="#ffffff")
                self.__arrTK.labelChangeColor(self.__labelActu, bg="#000000",fg="#ffffff")
                self.__arrTK.labelChangeColor(self.__labelTriggerMicro, bg="#000000")
                self.__arrTK.labelChangeColor(self.__labelMicroRequette, bg="#000000")
            else :
                self.__screen.configure(fg_color="#ffffff")
                self.__arrTK.boutonChangeColor(self.__btnMicro, bg="#e0e0e0", hoverbg="#949494")
                self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
                self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#e0e0e0", hoverbg="#949494")
                self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#e0e0e0", hoverbg="#949494")
                self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
                self.__arrTK.boutonChangeColor(self.__btnMicro, bg="#ffffff", hoverbg="#949494")
                self.__arrTK.labelChangeColor(self.__labelTextAfterSpeak, bg="#ffffff", fg="#000000")
                self.__arrTK.labelChangeColor(self.__labelActu, bg="#ffffff", fg="#000000")
                self.__arrTK.labelChangeColor(self.__labelTriggerMicro, bg="#ffffff")
                self.__arrTK.labelChangeColor(self.__labelMicroRequette, bg="#ffffff")
        self.__arrTK.labelChangeColor(self.__labelTextDuringSpeak,bg="#2b3ceb",fg="white")
        self.__labelTextDuringSpeak.configure(corner_radius=0)

        self.__screen.after(1000,self.__setTheme)


    def active(self,firstBoot:bool):
        if (firstBoot == True):
            theardSequenceBoot = th.Thread(target=self.__sequenceFistBoot)
        else :
            theardSequenceBoot = th.Thread(target=self.__sequenceBoot)

        theardSequenceBoot.start()
        self.__screen.mainloop()

    def __apropos(self):
        self.__arrTK.aproposWindows(
            nameSoft=self.__nameSoft,
            iconFile=self.__emplacementIcon,
            version=self.__version,
            copyright="Copyright Arrera Software by Baptiste P 2023-2025",
            linkSource="https://github.com/Arrera-Software/Six",
            linkWeb="https://arrera-software.fr/")
    
    def __onClose(self):
        if (askyesno("Atention","Voulez-vous vraiment fermer Six")):
            self.__screen.title(self.__nameSoft)
            self.__gazelleUI.clearAllFrame()
            self.__screen.update()
            self.__arrTK.placeBottomCenter(self.__entryUser)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__quit()
    
    def __quit(self):
        self.__sequenceArret()
        if self.__objOS.osWindows() :
            os.kill(os.getpid(), signal.SIGINT)
        elif self.__objOS.osLinux() or self.__objOS.osMac() :
            os.kill(os.getpid(), signal.SIGKILL)
    
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
            self.__sequenceParole(self.__assistantSix.boot(2))
            self.__arrTK.placeBottomCenter(self.__entryUser)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__startingTriggerWord()
            self.setButtonOpen()

    def __sequenceFistBoot(self):
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
            userData = self.__assistantSix.getUserData()
            self.__sequenceParole(self.__language.getPhraseFirstBoot(userData[1],userData[0],1))
            time.sleep(3)
            self.__sequenceParole(self.__language.getPhraseFirstBoot(userData[1],userData[0],2))
            time.sleep(3)
            self.__sequenceParole(self.__language.getPhraseFirstBoot(userData[1],userData[0],3))
            time.sleep(3)
            self.__sequenceParole(self.__language.getPhraseFirstBoot(userData[1],userData[0],4))
            self.__arrTK.placeBottomCenter(self.__entryUser)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__startingTriggerWord()
            self.setButtonOpen()
    
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
        self.__btnMicro.place_forget()
        self.__btnParametre.place_forget()
    
    def __sequenceParole(self,texte:str):
        self.__sixSpeaking = True 
        self.__thSpeak = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__clearView()
        self.__canvasParole1.place_forget()
        self.__canvasParole2.place(x=0,y=0)
        self.__labelTextDuringSpeak.configure(text=texte,wraplength=440,justify="left")
        self.__labelTextAfterSpeak.configure(text=texte, wraplength=475, justify="left")
        self.__screen.update()
        self.__duringSpeak()

    def __duringSpeak(self):
        if self.__thSpeak.is_alive():
            self.__screen.update()
            self.__screen.after(100,self.__duringSpeak)
        else :
            self.__canvasParole2.place_forget()
            self.__canvasParole3.place(x=0, y=0)
            self.__sixSpeaking = False
            self.__screen.update()
        
    def __sequenceArret(self):
        texte = self.__assistantSix.shutdown()
        self.__clearView()
        thSpeak = th.Thread(target=self.__avoice.say, args=(texte,))
        thSpeak.start()
        self.__labelTextDuringSpeak.configure(text=texte,wraplength=320)
        self.__canvasParole2.place(x=0,y=0)
        self.__screen.update()
        thSpeak.join()
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
        del thSpeak

    def __detectionTouche(self,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        self.__screen.bind("<Key>", anychar)  
    
    def __envoie(self): 
        if not self.__sixSpeaking:
            texte = self.__entryUser.get().lower()
            self.__entryUser.delete(0, END)
            if "parametre" in texte :
                self.__activeParametre()
            elif "mute" in texte or "silence" in texte or "ta gueule" in texte:
                    self.__viewMute()
            else :
                self.__assistantSix.neuron(texte)
                self.__clearView()
                self.__canvasParole1.place(x=0,y=0)
                self.__screen.update()
                nbSortie = self.__assistantSix.getValeurSortie()
                listSortie = self.__assistantSix.getListSortie()
                match nbSortie:
                    case 0 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                    case 1 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                    case 2 :
                        pass
                    case 3 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhOpenActu())
                        self.__viewResumer(listSortie, 2)
                    case 4 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                    case 5 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                    case 6 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhErreurActu())
                    case 7 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                        self.setButtonOpen()
                    case 8 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                        self.setButtonOpen()
                    case 9 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhReadDocument())
                        self.__windowsReadFile(listSortie,2)
                    case 10 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                        self.setButtonOpen()
                    case 11 :
                        self.__sequenceParoleReponseNeuron(self.__language.getphErreurResumer())
                    case 12 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhOpenResumerActu())
                        self.__viewResumer(listSortie, 1)
                    case 13 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhReadTableur())
                        self.__windowsReadFile(listSortie,1)
                    case 14 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                        self.setButtonOpen()
                    case 15 :
                        self.__quit()
                    case 16 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                    case 17 :
                        self.__windowsHelp(listSortie)
                    case 18 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhOpenResumerAgendaTache())
                        self.__viewResumer(listSortie,3)
                    case 19 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhOpenResumerAll())
                        self.__viewResumer(listSortie,4)
                    case 20 :
                        self.__sequenceParoleReponseNeuron(self.__language.getPhErreurResumerAll())
                    case 21 :
                        self.__sequenceParoleReponseNeuron(listSortie[0])
                        self.setButtonOpen()
                    case other :
                        pass


    def __sequenceParoleReponseNeuron(self,text:str):
        self.__entryUser.place_forget()
        self.__btnMicro.place_forget()
        self.__btnParametre.place_forget()
        self.__canvasParole1.place_forget()
        self.__canvasParole2.place(x=0,y=0)
        self.__labelTextDuringSpeak.configure(text=text,wraplength=440,justify="left")
        self.__labelTextAfterSpeak.configure(text=text, wraplength=475, justify="left")
        self.__screen.update()
        self.__thSpeakNeuron = th.Thread(target=self.__avoice.say,args=(text,))
        self.__thSpeakNeuron.start()
        self.__screen.after(100,self.__duringSpeakReponseNeuron)
        self.__screen.update()

    def __duringSpeakReponseNeuron(self):
        if self.__thSpeakNeuron.is_alive():
            self.__screen.update()
            self.__screen.after(100,self.__duringSpeakReponseNeuron)
        else :
            self.__canvasParole2.place_forget()
            self.__arrTK.placeBottomCenter(self.__entryUser)
            if not self.__gazelleUI.gettigerWordSet():
                self.__arrTK.placeBottomRight(self.__btnMicro)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__canvasParole3.place(x=0, y=0)
            self.__screen.update()

    def __loadSetting(self):
        self.__setTheme()
        self.__screen.update()
    
    def __activeParametre(self):
        self.__stopingTriggerWord()
        self.__screen.title(self.__nameSoft+" : Parametre")
        self.__screen.update()
        self.__clearView()
        self.__entryUser.place_forget()
        self.__gazelleUI.active()
        self.__screen.update()
    
    def __quitParametre(self):
        self.__screen.title(self.__nameSoft)
        self.__gazelleUI.clearAllFrame()
        self.__screen.update()
        self.__sequenceParole(self.__language.getPhQuitSetting())
        self.__arrTK.placeBottomCenter(self.__entryUser)
        self.__arrTK.placeBottomLeft(self.__btnParametre)
        self.__loadSetting()
        self.__startingTriggerWord()
    
    def __sixTrigerWord(self):
        while not self.__TriggerWorkStop.is_set():
            self.__microTriggerEnable()
            sortieTriger = self.__avoice.trigerWord()
            self.__microTriggerDisable()
            if sortieTriger == 1:
                self.__microRequetteEnable()
                microOK = self.__avoice.listen()
                if microOK == 0:
                    sortieMicro = self.__avoice.getTextMicro()
                    self.__entryUser.delete(0,END)
                    if sortieMicro!= "nothing":
                        self.__entryUser.insert(0,sortieMicro)
                self.__microRequetteDisable()
                time.sleep(0.2)
                self.__envoie()

    def __sixMicroEnable(self):
        self.__microRequetteEnable()
        microOK = self.__avoice.listen()
        if (microOK == 0):
            sortieMicro = self.__avoice.getTextMicro()
            self.__entryUser.delete(0, END)
            if (sortieMicro != "nothing"):
                self.__entryUser.insert(0, sortieMicro)
                self.__microRequetteDisable()
                time.sleep(0.5)
                self.__envoie()
            else :
                self.__microRequetteDisable()

    
    def __viewResumer(self, listSortie:list, mode:int):
        """
        1 : Resumer actualités
        2 : actuliés
        3 : Resumer agenda
        4 : Resumer totale
        """
        self.__clearView()
        self.__entryUser.place_forget()
        self.__screen.maxsize(500,600)
        self.__screen.minsize(500,600)
        self.__screen.update()
        self.__canvasActu.place(x=0,y=0)
        match mode :
            case 1 : 
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
            case 2 : 
                self.__labelActu.configure(text=listSortie[0]+
                                        "\n"+listSortie[1]+
                                        "\n"+listSortie[2],
                                        justify="left",
                                        wraplength=400)
                self.__btnReadActu.configure(command=lambda:self.__readActu(listSortie[0]+
                                        "."+listSortie[1]+
                                        "."+listSortie[2]))
            case 3 :
                self.__labelActu.configure(text=listSortie[0]+"\n"+listSortie[1],
                                        justify="left",
                                        wraplength=400)
                self.__btnReadActu.configure(command=lambda: self.__readActu(listSortie[0]
                                                                             +"."+listSortie[1] ))
            case 4 :
                self.__labelActu.configure(text=listSortie[0] + "\n" + listSortie[1]+"\n"
                                                +listSortie[2] + "\n" + listSortie[3]+"\n"
                                                +listSortie[4] + "\n" + listSortie[5]+"\n"
                                                +listSortie[7] + "\n" + listSortie[8],
                                           justify="left",
                                           wraplength=400)
                self.__btnReadActu.configure(command=lambda: self.__readActu(listSortie[0] + "."
                                                                             + listSortie[1]+"."
                                                                             +listSortie[2] + "."
                                                                             + listSortie[3]+"."
                                                                             +listSortie[4] + "."
                                                                             + listSortie[5]+"."
                                                                             +listSortie[7] + "."
                                                                             + listSortie[8]))
        self.__stopingTriggerWord()
        self.__thMinuteurActu.start()
        self.__screen.after(10,self.__duringMinuteurActu)
    
    def __quitActu(self):
        self.__clearView()
        self.__canvasActu.place_forget()
        self.__screen.maxsize(500,400)
        self.__screen.minsize(500,400)
        self.__screen.update()
        self.__arrTK.placeBottomCenter(self.__entryUser)
        self.__screen.update()
        self.__sequenceParole(self.__language.getPhQuitActu())
        self.__startingTriggerWord()
        self.__thMinuteurActu = th.Thread(target=self.__minuteurActu)

    
    def __readActu(self,texte:str):
        self.__thSpeakActu = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__thSpeakActu.start()
        self.__screen.after(100,self.__duringSpeakActu)

    def __duringSpeakActu(self):
        if self.__thSpeakActu.is_alive():
            self.__screen.update()
            self.__screen.after(100,self.__duringSpeakActu)
    
    def __minuteurActu(self):
        time.sleep(60)

    def __duringMinuteurActu(self):
        if self.__thMinuteurActu.is_alive():
            self.__screen.update()
            self.__screen.after(100,self.__duringMinuteurActu)
        else :
            self.__quitActu()
    
    def __viewMute(self):
        self.__sequenceParole(self.__language.getPhActiveMute())
        self.__clearView()
        self.__stopingTriggerWord()
        self.__entryUser.place_forget()
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
        self.__arrTK.placeBottomCenter(self.__entryUser)
        self.__screen.update()
        self.__sequenceParole(self.__language.getPhQuitMute())
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
        self.__btnMicro.place_forget()
        if self.__gazelleUI.gettigerWordSet():
            self.__thTrigger = th.Thread(target=self.__sixTrigerWord)
            self.__TriggerWorkStop.clear()
            self.__thTrigger.start()
        else :
            self.__arrTK.placeRightBottom(self.__btnMicro)

    def __stopingTriggerWord(self):
        self.__TriggerWorkStop.set()

    def __checkTrigerWord(self):
        self.__startingTriggerWord()

    def __windowsHelp(self, list: list):
        winHelp = self.__arrTK.aTopLevel(width=500, height=600,
                                         title="Arrera Six : Aide",
                                         resizable=False,
                                         icon=self.__emplacementIcon)
        labelTitleHelp = self.__arrTK.createLabel(winHelp, ppolice="Arial", ptaille=25, pstyle="bold")
        aideView = self.__arrTK.createTextBox(winHelp, width=450, height=500,
                                              wrap="word", ppolice="Arial",
                                              ptaille=20, pstyle="normal")
        self.__arrTK.insertTextOnTextBox(aideView, list[0])

        textSpeak = ""

        match list[1]:
            case "tableur":
                textSpeak = self.__language.getPhOpenAideTableur()
                labelTitleHelp.configure(text="Aide Tableur")
            case "word":
                textSpeak = self.__language.getPhOpenAideWord()
                labelTitleHelp.configure(text="Aide Traitement de texte")
            case "fichier":
                textSpeak = self.__language.getPhOpenAideFichier()
                labelTitleHelp.configure(text="Types créables par Arrera SIX")
            case "radio":
                textSpeak = self.__language.getPhOpenAideRadio()
                labelTitleHelp.configure(text="Radio disponible avec Arrera SIX")
            case "projet" :
                textSpeak = self.__language.getPhOpenAideProjet()
                labelTitleHelp.configure(text="Aide Arrera Projet")
            case "work" :
                textSpeak = self.__language.getPhOpenAideWork()
                labelTitleHelp.configure(text="Aide fonction Arrera Work")

        self.__arrTK.placeTopCenter(labelTitleHelp)
        self.__arrTK.placeCenter(aideView)
        self.__sequenceParoleReponseNeuron(textSpeak)

    def setButtonOpen(self):
        if self.__assistantSix.getTableur() :
            self.__arrTK.placeBottomRight(self.__btnTableurOpen)
        else :
            self.__btnTableurOpen.place_forget()

        if self.__assistantSix.getWord():
            self.__arrTK.placeBottomLeft(self.__btnWordOpen)
        else :
            self.__btnWordOpen.place_forget()

        if self.__assistantSix.getProject():
            self.__arrTK.placeBottomCenter(self.__btnProjetOpen)
        else :
            self.__btnProjetOpen.place_forget()

    def __winHelpFileAndProjet(self,mode:int):
        """
        :param mode:
            1. Tableur
            2. Word
            3. Projet
        :return:
        """
        winHelp = self.__arrTK.aTopLevel(width=500, height=600,
                                         resizable=False,
                                         icon=self.__emplacementIcon)

        labelTitleHelp = self.__arrTK.createLabel(winHelp, ppolice="Arial", ptaille=25, pstyle="bold")
        aideView = self.__arrTK.createTextBox(winHelp, width=475, height=500,
                                              wrap="word", ppolice="Arial",
                                              ptaille=20, pstyle="normal")

        match mode:
            case 1:
                winHelp.title("Arrera Six : Aide Tableur")
                labelTitleHelp.configure(text="Aide Tableur")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpTableur()))
            case 2:
                winHelp.title("Arrera Six : Aide Traitement de texte")
                labelTitleHelp.configure(text="Aide Traitement de texte")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpWord()))
            case 3:
                winHelp.title("Arrera Six : Aide Arrera Projet")
                labelTitleHelp.configure(text="Aide Arrera Projet")
                self.__arrTK.insertTextOnTextBox(aideView,
                                                 self.__traitementTextHelpFileAndProjet(
                                                     self.__language.getHelpProjet()))

        self.__arrTK.placeTopCenter(labelTitleHelp)
        self.__arrTK.placeCenter(aideView)

    def __traitementTextHelpFileAndProjet(self, liste:list):
        newText = ""
        for i in range(0, len(liste)):
            text = liste[i]
            if text[0] == "-" :
                text = text.replace("-", "").strip().lstrip()
                newText += "\n"+text+"\n"
            elif text[0]== "*":
                text = text.replace("*","").strip().lstrip()
                newText += "    "+text+"\n"

        return newText.strip()

    def __windowsReadFile(self, liste:list, mode:int):
        """
        :param mode:
        1. Tableur
        2. Word
        :return:
        """
        winRead = self.__arrTK.aTopLevel(width=500, height=600,
                                         resizable=False,
                                         icon=self.__emplacementIcon)

        labelTitleRead = self.__arrTK.createLabel(winRead, ppolice="Arial", ptaille=25, pstyle="bold")

        content = self.__arrTK.createTextBox(winRead, width=475, height=500,
                                             wrap="word", ppolice="Arial",
                                             ptaille=20, pstyle="normal")
        btnRead = self.__arrTK.createButton(winRead, text="Lire a voix haute", ppolice="Arial", ptaille=15)


        match mode :
            case 1 :
                winRead.title("Arrera Six : Lecture Tableur")
                labelTitleRead.configure(text="Lecture : Tableur")
                textContent = ""
                for i in range(0, len(liste)):
                    textContent = textContent+str(liste[i]) + "\n"
                self.__arrTK.insertTextOnTextBox(content, textContent)
                btnRead.configure(command=lambda : self.__readActu(textContent))

            case 2 :
                winRead.title("Arrera Six : Lecture Traitement de texte")
                labelTitleRead.configure(text="Lecture : Traitement de texte")
                self.__arrTK.insertTextOnTextBox(content, liste[0])
                btnRead.configure(command=lambda : self.__readActu(liste[0]))

        self.__arrTK.placeCenter(content)
        self.__arrTK.placeTopCenter(labelTitleRead)
        self.__arrTK.placeBottomCenter(btnRead)