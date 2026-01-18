import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
from librairy.arrera_tk import *
import time
from tkinter.messagebox import *
from src.languageSIX import *
from lib.arrera_tk import *
import threading as th
from brain.brain import ABrain
import random

class six_gui(aTk) :
    def __init__(self,iconFolder:str,iconName:str,
                 brain:ABrain,theme_file:str,
                 version:str):

        # var
        self.__nameSoft = "Arrera Six"
        self.__sixSpeaking = bool
        self.__version = version

        # Objet
        self.__assistant_six = brain
        self.__gestionnaire = self.__assistant_six.getGestionnaire()
        self.__objOS = self.__gestionnaire.getOSObjet()
        self.__avoice = self.__gestionnaire.getArrVoice()
        self.__gest_user = self.__gestionnaire.getUserConf()

        super().__init__(title=self.__nameSoft,resizable=False,theme_file=theme_file,
                         fg_color=("#ffffff","#000000"))
        # initilisation fenetre
        self.geometry("500x400+5+30")
        self.protocol("WM_DELETE_WINDOW",self.__onClose)

        # Partie Icone

        if self.__objOS.osWindows():
            self.__emplacementIcon = iconFolder + "win/" + iconName + ".ico"
            self.iconbitmap(self.__emplacementIcon)
        elif self.__objOS.osLinux():
            self.__emplacementIcon = iconFolder + "linux/" + iconName + ".png"
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))
        elif self.__objOS.osMac() :
            self.__emplacementIcon = resource_path(iconFolder+ "macos/" + iconName+".png")
            self.iconphoto(False,PhotoImage(file=self.__emplacementIcon))

        # Variable des theard
        self.__thSixListen = th.Thread()
        self.__thTrigger = th.Thread()
        self.__TriggerWorkStop = th.Event()
        # Teste de la connextion internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False
        # Demarage d'Arrera TK
        self.__arrTK = CArreraTK()

        # Instantation de l'objet language
        self.__language = CLanguageSIX(resource_path("FileJSON/phraseSix.json"),
                                       resource_path("FileJSON/aideSix.json"),
                                       resource_path("FileJSON/firstBootSix.json"))

        # Declaration de l'objet Arrera Gazelle
        self.__gazelleUI = arrera_gazelle(self,self.__gestionnaire,
                                          "json_conf/conf-setting.json")
        self.__gazelleUI.passFNCQuit(self.__quitParametre)
        self.__gazelleUI.passFNCBTNIcon(lambda : self.__apropos())
        # widget et canvas
        # canvas

        # Image de fond
        self.__file_img_gui = ["acceuil.png",#0
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
        self.__dir_GUI_dark = "asset/IMGinterface/dark/"
        self.__dir_GUIl_light = "asset/IMGinterface/white/"

        # Canvas Acceuil
        self.__c_welcome = self.__canvas_welcome()
        # Canvas Boot
        self.__c_boot_one = self.__canvas_boot_one()

        self.__c_boot_two = self.__canvas_boot_two()

        self.__c_boot_three = self.__canvas_boot_three()

        self.__c_boot_four = self.__canvas_boot_four()
        # Canvas Parole
        self.__c_speak_one = self.__canvas_speak_one()

        self.__c_speak_two = self.__canvas_speak_two()

        self.__c_speak_three = self.__canvas_speak_three()

        # Canvas NoConnect
        self.__canvasNoConnect = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[6],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[6],
                                                                       width=500,height=350)
        # Canvas Emotion
        self.__canvasContent = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[15],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[15],
                                                                       width=500,height=350)
        self.__canvasColere = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[14],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[14],
                                                                       width=500,height=350)
        self.__canvasSurprit = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[3],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[3],
                                                                       width=500,height=350)
        # Canvas Triste
        self.__canvasTriste1 = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[1],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[1],
                                                                       width=500,height=350)
        self.__canvasTriste2 = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[2],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[2],
                                                                       width=500,height=350)
        # Canvas Parametre
        self.__canvasParaOpen = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[19],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[19],
                                                                       width=500,height=350)
        # Canvas Actu
        self.__canvasActu = self.__arrTK.createArreraBackgroudImage(self,
                                                                       imageLight=self.__dir_GUIl_light+self.__file_img_gui[16],
                                                                       imageDark=self.__dir_GUI_dark+self.__file_img_gui[16],
                                                                       width=500,height=600)
        # Canvas Mute
        self.__canvasMute = [self.__arrTK.createArreraBackgroudImage(self,
                                                                     imageLight=self.__dir_GUIl_light+self.__file_img_gui[4],
                                                                     imageDark=self.__dir_GUI_dark+self.__file_img_gui[4],
                                                                     width=500,height=350),
                             self.__arrTK.createArreraBackgroudImage(self,
                                                                     imageLight=self.__dir_GUIl_light+self.__file_img_gui[5],
                                                                     imageDark=self.__dir_GUI_dark+self.__file_img_gui[5],
                                                                     width=500,height=350)]
        # widget
        self.__entryUser = aEntry(self,police_size=20,width=360)

        # Label Micro
        imageMicroTriger=self.__arrTK.createImage(pathLight=self.__dir_GUIl_light+self.__file_img_gui[17],
                                                  pathDark=self.__dir_GUI_dark+self.__file_img_gui[17],
                                                  tailleX=50,tailleY=50)
        imageMicroRequette=self.__arrTK.createImage(pathLight=self.__dir_GUIl_light+self.__file_img_gui[18],
                                                  pathDark=self.__dir_GUI_dark+self.__file_img_gui[18],
                                                    tailleX=50,tailleY=50)
        imageMicroSimple = self.__arrTK.createImage(pathLight=self.__dir_GUIl_light + self.__file_img_gui[20],
                                                    pathDark=self.__dir_GUI_dark + self.__file_img_gui[20],
                                                    tailleX=30, tailleY=30)
        imageParametre = self.__arrTK.createImage(pathLight=self.__dir_GUIl_light + self.__file_img_gui[21],
                                                  pathDark=self.__dir_GUI_dark + self.__file_img_gui[21],
                                                  tailleX=30, tailleY=30)
        imageTableurOpen = self.__arrTK.createImage(pathLight=self.__dir_GUIl_light + self.__file_img_gui[23],
                                                  pathDark=self.__dir_GUI_dark + self.__file_img_gui[23],
                                                  tailleX=35, tailleY=35)
        imageProjetOpen = self.__arrTK.createImage(pathLight=self.__dir_GUIl_light + self.__file_img_gui[22],
                                                    pathDark=self.__dir_GUI_dark + self.__file_img_gui[22],
                                                    tailleX=35, tailleY=35)
        imageWordOpen = self.__arrTK.createImage(pathLight=self.__dir_GUIl_light + self.__file_img_gui[24],
                                                    pathDark=self.__dir_GUI_dark + self.__file_img_gui[24],
                                                    tailleX=35, tailleY=35)

        self.__labelTriggerMicro = self.__arrTK.createLabel(self,width=50,height=50,image=imageMicroTriger)
        self.__labelMicroRequette = self.__arrTK.createLabel(self,width=50,height=50,image=imageMicroRequette)

        # Bouton pour montrer qu'un projet/Tableur/Word est ouvert
        self.__btnTableurOpen = self.__arrTK.createButton(self.__c_speak_three, width=35, height=35,
                                                          image=imageTableurOpen,
                                                          command=lambda : self.__winHelpFileAndProjet(1))
        self.__btnWordOpen = self.__arrTK.createButton(self.__c_speak_three, width=35, height=35,
                                                       image=imageWordOpen,
                                                       command = lambda : self.__winHelpFileAndProjet(2))
        self.__btnProjetOpen = self.__arrTK.createButton(self.__c_speak_three, width=35, height=35,
                                                         image=imageProjetOpen,
                                                         command=lambda: self.__winHelpFileAndProjet(3))

        # Bouton pour activer le micro quand le trigger word est pas activer
        self.__btn_microphone = aButton(self, width=30, height=30,text="",
                                        dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                        image=imageMicroSimple, command=lambda  : self.__sixMicroEnable())
        # Bouton pour activer les parametre
        self.__btnParametre = aButton(self,width=30, height=30,text="",
                                      dark_color="#1f1f1f", light_color="#e0e0e0",
                                      hover_color=("#949494","#505050"),
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
        # self.__setTheme()
        #Affichage label parole


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
        self.__thBoot = th.Thread()
    
    def __setTheme(self):
        self.__avoice.loadConfig()
        theme = self.__arrTK.getTheme().lower()
        if theme == "light" :
            self.__arrTK.boutonChangeColor(self.__btn_microphone, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnWordOpen, bg="#e0e0e0", hoverbg="#949494")
            self.configure(fg_color="#ffffff")
            self.__arrTK.labelChangeColor(self.__l_text_after_speak, bg="#ffffff", fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelActu,bg="#ffffff",fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelTriggerMicro,bg="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelMicroRequette,bg="#ffffff")
        elif theme == "dark" :
            self.configure(fg_color="#000000")
            self.__arrTK.boutonChangeColor(self.__btn_microphone, bg="#1f1f1f", hoverbg="#505050")
            self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#1f1f1f", hoverbg="#505050")
            self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#1f1f1f", hoverbg="#505050")
            self.__arrTK.boutonChangeColor(self.__btnWordOpen, bg="#1f1f1f", hoverbg="#505050")
            self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#1f1f1f", hoverbg="#505050")
            self.__arrTK.labelChangeColor(self.__l_text_after_speak, bg="#000000", fg="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelActu, bg="#000000",fg="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelTriggerMicro, bg="#000000")
            self.__arrTK.labelChangeColor(self.__labelMicroRequette, bg="#000000")
        else :
            self.configure(fg_color="#ffffff")
            self.__arrTK.boutonChangeColor(self.__btn_microphone, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnTableurOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnProjetOpen, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btnParametre, bg="#e0e0e0", hoverbg="#949494")
            self.__arrTK.boutonChangeColor(self.__btn_microphone, bg="#ffffff", hoverbg="#949494")
            self.__arrTK.labelChangeColor(self.__l_text_after_speak, bg="#ffffff", fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelActu, bg="#ffffff", fg="#000000")
            self.__arrTK.labelChangeColor(self.__labelTriggerMicro, bg="#ffffff")
            self.__arrTK.labelChangeColor(self.__labelMicroRequette, bg="#ffffff")

        self.__arrTK.labelChangeColor(self.__l_during_assistant_speak, bg="#2b3ceb", fg="white")
        self.__l_during_assistant_speak.configure(corner_radius=0)

        # self.after(1000,self.__setTheme)


    def active(self,firstBoot:bool):
        if (firstBoot == True):
            self.__sequenceFistBoot()
        else :
            self.__sequenceBoot()
        self.mainloop()

    # Declaration des diferente page de l'inteface

    def __canvas_welcome(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[0],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[0],
                             width=500,height=350)
        return c

    def __canvas_boot_one(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[10],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[10],
                             width=500,height=350)
        return c

    def __canvas_boot_two(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[11],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[11],
                             width=500,height=350)
        return c

    def __canvas_boot_three(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[12],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[12],
                             width=500,height=350)
        return c

    def __canvas_boot_four(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[13],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[13],
                             width=500,height=350)
        return c

    def __canvas_speak_one(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[7],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[7],
                             width=500,height=350)
        return c

    def __canvas_speak_two(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[8],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[8],
                             width=500,height=350)
        self.__l_during_assistant_speak = aLabel(c, police_size=20, fg_color="#2b3ceb", text_color="white")

        self.__l_during_assistant_speak.place(x=30, y=110)
        return c

    def __canvas_speak_three(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[9],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[9],
                             width=500,height=350)

        self.__l_text_after_speak = aLabel(c, police_size=20,
                                           light_color="#ffffff", dark_color="#000000",
                                           dark_text_color="#ffffff", light_text_color="#000000")

        self.__l_text_after_speak.place(x=10, y=80)

        return c

    # About

    def __apropos(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile=self.__emplacementIcon,
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Six",
                      linkWeb="https://arrera-software.fr/")
    
    def __onClose(self):
        if (askyesno("Atention","Voulez-vous vraiment fermer Six")):
            self.title(self.__nameSoft)
            self.__gazelleUI.clearAllFrame()
            self.update()
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
        self.__c_boot_one.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_one.place_forget()
        self.__c_boot_two.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_two.place_forget()
        self.__c_boot_three.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_three.place_forget()
        self.__c_boot_four.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_welcome.place(x=0, y=0)
        if not self.__etatConnexion:
            self.__c_welcome.place_forget()
            self.protocol("WM_DELETE_WINDOW",self.__quit)
            self.__canvasNoConnect.place(x=0,y=0)
            self.update()
        else :
            self.__speakBoot()


    def __speakBoot(self):
        texte = self.__assistant_six.boot()
        self.__thBoot = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__thBoot.start()
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.__l_text_after_speak.configure(text=texte, wraplength=475, justify="left")
        self.after(100,self.__duringSpeakBoot)

    def __duringSpeakBoot(self):
        if self.__thBoot.is_alive():
            self.update()
            self.after(100,self.__duringSpeakBoot)
        else :
            self.__arrTK.placeBottomCenter(self.__entryUser)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__startingTriggerWord()
            self.setButtonOpen()
            self.__c_speak_two.place_forget()
            self.__c_speak_three.place(x=0, y=0)
            self.__sixSpeaking = False
            self.update()

    def __sequenceFistBoot(self):
        self.__c_boot_one.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_one.place_forget()
        self.__c_boot_two.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_two.place_forget()
        self.__c_boot_three.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_boot_three.place_forget()
        self.__c_boot_four.place(x=0, y=0)
        time.sleep(0.2)
        self.__c_welcome.place(x=0, y=0)
        if (self.__etatConnexion==False):
            self.__c_welcome.place_forget()
            self.protocol("WM_DELETE_WINDOW",self.__quit)
            self.__canvasNoConnect.place(x=0,y=0)
            self.update()
        else :
            self.__thBoot = th.Thread(target=self.__firstBootSpeak)
            self.__thBoot.start()
            self.after(100, self.__duringFirstBootSpeak)

    def __firstBootSpeak(self):
        name = self.__gest_user.getFirstnameUser()
        genre = self.__gest_user.getGenre()
        texte = self.__language.getPhraseFirstBoot(genre,name,1)
        self.__avoice.say(texte)
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.update()
        time.sleep(3)
        texte = (self.__language.getPhraseFirstBoot(genre,name, 2))
        self.__avoice.say(texte)
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.update()
        time.sleep(3)
        texte = (self.__language.getPhraseFirstBoot(genre,name, 3))
        self.__avoice.say(texte)
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.update()
        time.sleep(3)
        texte = (self.__language.getPhraseFirstBoot(genre,name, 4))
        self.__avoice.say(texte)
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.update()

    def __duringFirstBootSpeak(self):
        if self.__thBoot.is_alive():
            self.update()
            self.after(100,self.__duringFirstBootSpeak)
        else :
            userData = self.__assistant_six.getUserData()
            self.__arrTK.placeBottomCenter(self.__entryUser)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__startingTriggerWord()
            self.setButtonOpen()
            self.__c_speak_two.place_forget()
            self.__c_speak_three.place(x=0, y=0)
            self.__sixSpeaking = False
            self.__l_text_after_speak.configure(text=self.__language.getPhraseFirstBoot(userData[1], userData[0], 4)
                                                , wraplength=440, justify="left")
            self.update()
    
    def __clearView(self):
        self.__labelTriggerMicro.place_forget()
        self.__c_welcome.place_forget()
        self.__c_boot_one.place_forget()
        self.__c_boot_two.place_forget()
        self.__c_boot_three.place_forget()
        self.__c_boot_four.place_forget()
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place_forget()
        self.__c_speak_three.place_forget()
        self.__canvasNoConnect.place_forget()
        self.__canvasContent.place_forget()
        self.__canvasColere.place_forget()
        self.__canvasSurprit.place_forget()
        self.__canvasTriste1.place_forget()
        self.__canvasTriste2.place_forget()
        self.__canvasParaOpen.place_forget()
        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()
    
    def __sequenceParole(self,texte:str):
        self.__sixSpeaking = True 
        self.__thSpeak = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__clearView()
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=texte, wraplength=440, justify="left")
        self.__l_text_after_speak.configure(text=texte, wraplength=475, justify="left")
        self.update()
        self.__duringSpeak()

    def __duringSpeak(self):
        if self.__thSpeak.is_alive():
            self.update()
            self.after(100,self.__duringSpeak)
        else :
            self.__c_speak_two.place_forget()
            self.__c_speak_three.place(x=0, y=0)
            self.__sixSpeaking = False
            self.update()
        
    def __sequenceArret(self):
        texte = self.__assistant_six.shutdown()
        self.__clearView()
        thSpeak = th.Thread(target=self.__avoice.say, args=(texte,))
        thSpeak.start()
        self.__l_during_assistant_speak.configure(text=texte, wraplength=320)
        self.__c_speak_two.place(x=0, y=0)
        self.update()
        thSpeak.join()
        self.__c_speak_two.place_forget()
        self.__c_boot_four.place(x=0, y=0)
        self.update()
        time.sleep(0.2)
        self.__c_boot_four.place_forget()
        self.__c_boot_three.place(x=0, y=0)
        self.update()
        time.sleep(0.2)
        self.__c_boot_three.place_forget()
        self.__c_boot_four.place(x=0, y=0)
        self.update()
        time.sleep(0.2)
        self.__c_boot_four.place_forget()
        self.__c_boot_one.place(x=0, y=0)
        self.update()
        time.sleep(0.2)
        self.__c_boot_one.place_forget()
        self.update()
        del thSpeak

    def __detectionTouche(self,fonc,touche):
        def anychar(event):
            if event.keycode == touche:
                fonc()               
        self.bind("<Key>", anychar)
    
    def __envoie(self): 
        if not self.__sixSpeaking:
            texte = self.__entryUser.get().lower()
            self.__entryUser.delete(0, END)
            if "parametre" in texte :
                self.__activeParametre()
            elif "mute" in texte or "silence" in texte or "ta gueule" in texte:
                    self.__viewMute()
            else :
                self.__assistant_six.neuron(texte)
                self.__clearView()
                self.__c_speak_one.place(x=0, y=0)
                self.update()
                nbSortie = self.__assistant_six.getValeurSortie()
                listSortie = self.__assistant_six.getListSortie()
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
        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()
        self.__c_speak_one.place_forget()
        self.__c_speak_two.place(x=0, y=0)
        self.__l_during_assistant_speak.configure(text=text, wraplength=440, justify="left")
        self.__l_text_after_speak.configure(text=text, wraplength=475, justify="left")
        self.update()
        self.__thSpeakNeuron = th.Thread(target=self.__avoice.say,args=(text,))
        self.__thSpeakNeuron.start()
        self.after(100,self.__duringSpeakReponseNeuron)
        self.update()

    def __duringSpeakReponseNeuron(self):
        if self.__thSpeakNeuron.is_alive():
            self.update()
            self.after(100,self.__duringSpeakReponseNeuron)
        else :
            self.__c_speak_two.place_forget()
            self.__arrTK.placeBottomCenter(self.__entryUser)
            if not self.__gazelleUI.gettigerWordSet():
                self.__arrTK.placeBottomRight(self.__btn_microphone)
            self.__arrTK.placeBottomLeft(self.__btnParametre)
            self.__c_speak_three.place(x=0, y=0)
            self.update()

    def __loadSetting(self):
        self.__setTheme()
        self.update()
    
    def __activeParametre(self):
        self.__stopingTriggerWord()
        self.title(self.__nameSoft+" : Parametre")
        self.update()
        self.__clearView()
        self.__entryUser.place_forget()
        self.__gazelleUI.active()
        self.update()
    
    def __quitParametre(self):
        self.title(self.__nameSoft)
        self.__gazelleUI.clearAllFrame()
        self.update()
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
        self.__thSixListen = th.Thread(target=self.__sixLinstenTheard)
        self.__thSixListen.start()
        self.__duringSixListen()

    def __duringTigerWord(self):
        if self.__thTrigger.is_alive():
            self.update()
            self.after(100,self.__duringSixListen)
        else :
            self.__microTriggerDisable()


    def __sixLinstenTheard(self):
        self.__microRequetteEnable()
        microOK = self.__avoice.listen()
        self.__microRequetteDisable()
        if (microOK == 0):
            sortieMicro = self.__avoice.getTextMicro()
            self.__entryUser.delete(0, END)
            if (sortieMicro != "nothing"):
                self.__entryUser.insert(0, sortieMicro)
                time.sleep(0.5)
                self.__envoie()

    def __duringSixListen(self):
        if self.__thSixListen.is_alive():
            self.update()
            self.after(100,self.__duringSixListen)

    
    def __viewResumer(self, listSortie:list, mode:int):
        """
        1 : Resumer actualités
        2 : actuliés
        3 : Resumer agenda
        4 : Resumer totale
        """
        self.__clearView()
        self.__entryUser.place_forget()
        self.maxsize(500,600)
        self.minsize(500,600)
        self.update()
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
        self.after(10,self.__duringMinuteurActu)
    
    def __quitActu(self):
        self.__clearView()
        self.__canvasActu.place_forget()
        self.maxsize(500,400)
        self.minsize(500,400)
        self.update()
        self.__arrTK.placeBottomCenter(self.__entryUser)
        self.update()
        self.__sequenceParole(self.__language.getPhQuitActu())
        self.__startingTriggerWord()
        self.__thMinuteurActu = th.Thread(target=self.__minuteurActu)

    
    def __readActu(self,texte:str):
        self.__thSpeakActu = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__thSpeakActu.start()
        self.after(100,self.__duringSpeakActu)

    def __duringSpeakActu(self):
        if self.__thSpeakActu.is_alive():
            self.update()
            self.after(100,self.__duringSpeakActu)
    
    def __minuteurActu(self):
        time.sleep(60)

    def __duringMinuteurActu(self):
        if self.__thMinuteurActu.is_alive():
            self.update()
            self.after(100,self.__duringMinuteurActu)
        else :
            self.__quitActu()
    
    def __viewMute(self):
        self.__sequenceParole(self.__language.getPhActiveMute())
        self.__clearView()
        self.__stopingTriggerWord()
        self.__entryUser.place_forget()
        self.maxsize(500,350)
        self.minsize(500,350)
        self.update()
        nb = random.randint(0,1)
        self.__canvasMute[nb].place(x=0,y=0)
    
    def __quitMute(self):        
        self.__clearView()
        self.maxsize(500,400)
        self.minsize(500,400)
        self.update()
        self.__canvasMute[0].place_forget()
        self.__canvasMute[1].place_forget()
        self.__arrTK.placeBottomCenter(self.__entryUser)
        self.update()
        self.__sequenceParole(self.__language.getPhQuitMute())
        self.__startingTriggerWord()
    
    def __microTriggerEnable(self):
        self.__labelTriggerMicro.place(relx=1.0, rely=0.0, anchor='ne')
        self.update()
    
    def __microTriggerDisable(self):
        self.__labelTriggerMicro.place_forget()
        self.update()
    
    def __microRequetteEnable(self):
        self.__labelMicroRequette.place(relx=1.0, rely=0.0, anchor='ne')
        self.update()
    
    def __microRequetteDisable(self):
        self.__labelMicroRequette.place_forget()
        self.update()
    
    def __startingTriggerWord(self):
        # Création du thread Trigger word
        self.__btn_microphone.place_forget()
        if self.__gazelleUI.gettigerWordSet():
            self.__thTrigger = th.Thread(target=self.__sixTrigerWord)
            self.__TriggerWorkStop.clear()
            self.__thTrigger.start()
            self.after(100, self.__duringTigerWord)
        else :
            self.__arrTK.placeRightBottom(self.__btn_microphone)

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
        if self.__assistant_six.getTableur() :
            self.__arrTK.placeBottomRight(self.__btnTableurOpen)
        else :
            self.__btnTableurOpen.place_forget()

        if self.__assistant_six.getWord():
            self.__arrTK.placeBottomLeft(self.__btnWordOpen)
        else :
            self.__btnWordOpen.place_forget()

        if self.__assistant_six.getProject():
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