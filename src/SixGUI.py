import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
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
        self.__mute_is_enable = False

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
        self.protocol("WM_DELETE_WINDOW", self.__on_close)

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

        self.__th_reflect = th.Thread()

        # Teste de la connextion internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False

        # Instantation de l'objet language
        self.__language = language_six(resource_path("FileJSON/phraseSix.json"),
                                       resource_path("FileJSON/aideSix.json"),
                                       resource_path("FileJSON/firstBootSix.json"))

        # Declaration de l'objet Arrera Gazelle
        self.__gazelleUI = arrera_gazelle(self,self.__gestionnaire,
                                          "json_conf/conf-setting.json")
        self.__gazelleUI.passFNCQuit(self.__quitParametre)
        self.__gazelleUI.passFNCBTNIcon(lambda : self.__about())
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
        self.__c_no_connect = self.__canvas_no_connect()
        # Canvas Emotion
        self.__c_happy = self.__canvas_happy()

        self.__c_not_happy = self.__canvas_not_happy()

        self.__c_surprised = self.__canvas_surprised()
        # Canvas Triste
        self.__c_sad_one = self.__canvas_sad_one()
        self.__c_sad_two = self.__canvas_sad_two()
        # Canvas Parametre
        self.__c_setting_open = self.__canvas_setting()
        # Canvas Actu
        self.__c_actualites = self.__canvas_actu()
        # Canvas Mute
        self.__L_c_mute = self.__canvas_mute()

        self.__widget_main_windows()

        # Mise a place de la touche entree
        if self.__objOS.osWindows() :
            self.__detectionTouche(self.__send_assistant,13)
        elif self.__objOS.osLinux() :
            self.__detectionTouche(self.__send_assistant,36)
        elif self.__objOS.osMac() :
            self.__detectionTouche(self.__send_assistant,603979789)

        # Declaration de la variable pour contenir les theard
        self.__thSpeak = th.Thread()
        self.__thSpeakNeuron = th.Thread()
        self.__thSpeakActu = th.Thread()
        self.__thMinuteurActu = th.Thread()
        self.__thBoot = th.Thread()


    def active(self,firstBoot:bool):
        if firstBoot:
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

        # Image

        imageTableurOpen = aImage(path_light=self.__dir_GUIl_light + self.__file_img_gui[23],
                                  path_dark=self.__dir_GUI_dark + self.__file_img_gui[23],
                                  width=30, height=30)

        imageProjetOpen = aImage(path_light=self.__dir_GUIl_light + self.__file_img_gui[22],
                                 path_dark=self.__dir_GUI_dark + self.__file_img_gui[22],
                                width=30, height=30)
        imageWordOpen = aImage(path_light=self.__dir_GUIl_light + self.__file_img_gui[24],
                               path_dark=self.__dir_GUI_dark + self.__file_img_gui[24],
                                width=30, height=30)

        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[9],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[9],
                             width=500,height=350,fg_color=("#ffffff","#000000"))

        self.__l_text_after_speak = aLabel(c, police_size=20,
                                           light_color="#ffffff", dark_color="#000000",
                                           dark_text_color="#ffffff", light_text_color="#000000")

        self.__btn_tableur_is_open = aButton(c, width=30, height=30, text="", image=imageTableurOpen,
                                             dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                             command=lambda : self.__set_requette_with_btn("aide tableur"))
        self.__btn_word_is_open = aButton(c, width=30, height=30, text="", image=imageWordOpen,
                                          dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                          command = lambda : self.__set_requette_with_btn("aide word"))
        self.__btn_project_is_open = aButton(c, width=30, height=30, text="", image=imageProjetOpen,
                                             dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                             command=lambda: self.__set_requette_with_btn("aide projet"))

        self.__l_text_after_speak.place(x=10, y=80)

        return c

    def __canvas_no_connect(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[6],
                    background_dark=self.__dir_GUI_dark+self.__file_img_gui[6],
                    width=500,height=350)

        return c

    def __canvas_happy(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[15],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[15],
                             width=500,height=350)

        return c

    def __canvas_not_happy(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[14],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[14],
                             width=500,height=350)

        return c

    def __canvas_surprised(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[3],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[3],
                             width=500,height=350)

        return c

    def __canvas_sad_one(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[1],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[1],
                             width=500,height=350)

        return c

    def __canvas_sad_two(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[2],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[2],
                             width=500,height=350)

        return c

    def __canvas_setting(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[19],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[19],
                             width=500,height=350)

        return c

    def __canvas_actu(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[16],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[16],
                             width=500,height=350)

        self.__l_actu = aLabel(c, dark_text_color="#ffffff", light_text_color="#000000", dark_color="#000000", light_color="#ffffff", police_size=15)
        self.__btn_quit_actu = aButton(c, text="Quitter", size=15, command=self.__quitActu)
        self.__btnReadActu =  aButton(c, text="Lire a voix haute",size=15)

        self.__l_actu.place(x=70, y=0)
        self.__btnReadActu.place(relx=0, rely=1, anchor='sw')
        self.__btn_quit_actu.place(relx=1, rely=1, anchor='se')

        return c

    def __canvas_mute(self):
        c1 = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[4],
                             background_dark=self.__dir_GUI_dark+self.__file_img_gui[4],
                             width=500,height=400,fg_color=("#ffffff","#000000"))

        c2 = aBackgroundImage(self,background_light=self.__dir_GUIl_light+self.__file_img_gui[5],
                              background_dark=self.__dir_GUI_dark+self.__file_img_gui[5],
                              width=500,height=400,fg_color=("#ffffff","#000000"))

        self.__btn_stop_mute = [aButton(c1, text="Demute", dark_color="#1f1f1f", light_color="#e0e0e0",
                                        hover_color=("#949494","#505050"), size=20,
                                        light_text_color="#000000", dark_text_color="#ffffff",
                                        command=self.__stopping_mode_mute),
                                aButton(c2, text="Demute", dark_color="#1f1f1f", light_color="#e0e0e0",
                                        hover_color=("#949494","#505050"), size=20,
                                        light_text_color="#000000", dark_text_color="#ffffff",
                                        command=self.__stopping_mode_mute)]
        self.__btn_quit_mute = [aButton(c1, text="Quitter", dark_color="#1f1f1f", light_color="#e0e0e0",
                                        hover_color=("#949494","#505050"), size=20,
                                        light_text_color="#000000", dark_text_color="#ffffff",
                                        command=self.__stop_assistant),
                                aButton(c2, text="Quitter", dark_color="#1f1f1f", light_color="#e0e0e0",
                                        light_text_color="#000000", dark_text_color="#ffffff",
                                        hover_color=("#949494","#505050"), size=20, command=self.__stop_assistant)]

        for i in self.__btn_stop_mute:
            i.place(relx=0, rely=1, anchor='sw')

        for i in self.__btn_quit_mute:
            i.place(relx=1, rely=1, anchor='se')

        return [c1,c2]

    def __widget_main_windows(self):

        self.__entryUser = aEntry(self,police_size=20,width=360)

        imageMicroTriger= aImage(path_light=self.__dir_GUIl_light+self.__file_img_gui[17],
                                 path_dark=self.__dir_GUI_dark+self.__file_img_gui[17],
                                 width=50,height=50)
        imageMicroRequette=aImage(path_light=self.__dir_GUIl_light+self.__file_img_gui[18],
                                  path_dark=self.__dir_GUI_dark+self.__file_img_gui[18],
                                  width=50,height=50)
        imageMicroSimple = aImage(path_light=self.__dir_GUIl_light+self.__file_img_gui[20],
                                  path_dark=self.__dir_GUI_dark+self.__file_img_gui[20],
                                  width=30,height=30)
        imageParametre = aImage(path_light=self.__dir_GUIl_light+self.__file_img_gui[21],
                                path_dark=self.__dir_GUI_dark+self.__file_img_gui[21],
                                width=30,height=30)

        self.__labelTriggerMicro = aLabel(self,text="",width=50,height=50,image=imageMicroTriger)
        self.__labelMicroRequette = aLabel(self,text="",width=50,height=50,image=imageMicroRequette)

        # Bouton pour activer le micro quand le trigger word est pas activer
        self.__btn_microphone = aButton(self, width=30, height=30,text="",
                                        dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                        image=imageMicroSimple, command=lambda  : self.__sixMicroEnable())
        # Bouton pour activer les parametre
        self.__btnParametre = aButton(self,width=30, height=30,text="",
                                      dark_color="#1f1f1f", light_color="#e0e0e0",
                                      hover_color=("#949494","#505050"),
                                      image=imageParametre,command=self.__activeParametre)

    # About

    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile=self.__emplacementIcon,
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Six",
                      linkWeb="https://arrera-software.fr/")
    
    def __on_close(self):
        if askyesno("Atention", "Voulez-vous vraiment fermer Six"):
            self.title(self.__nameSoft)
            self.__gazelleUI.clearAllFrame()
            self.update()
            self.__entryUser.placeBottomCenter()
            self.__btnParametre.placeBottomLeft()
            self.__stop_assistant()
    
    def __stop_assistant(self):
        if self.__mute_is_enable :
            self.__stopping_mode_mute()
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
            self.protocol("WM_DELETE_WINDOW", self.__stop_assistant)
            self.__c_no_connect.place(x=0, y=0)
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
            self.__entryUser.placeBottomCenter()
            self.__btnParametre.placeBottomLeft()
            self.__startingTriggerWord()
            self.__manage_btn_open_fnc()
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
        if not self.__etatConnexion:
            self.__c_welcome.place_forget()
            self.protocol("WM_DELETE_WINDOW", self.__stop_assistant)
            self.__c_no_connect.place(x=0, y=0)
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
            self.__entryUser.placeBottomCenter()
            self.__btnParametre.placeBottomLeft()
            self.__startingTriggerWord()
            self.__manage_btn_open_fnc()
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
        self.__c_no_connect.place_forget()
        self.__c_happy.place_forget()
        self.__c_not_happy.place_forget()
        self.__c_surprised.place_forget()
        self.__c_sad_one.place_forget()
        self.__c_sad_two.place_forget()
        self.__c_setting_open.place_forget()
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

    def __set_requette_with_btn(self,requette:str):
        self.__entryUser.delete(0,END)
        self.__entryUser.insert(0,requette)
        self.__send_assistant()

    def __send_assistant(self):
        content = self.__entryUser.get().lower()
        self.__entryUser.delete(0, END)
        if content :
            if "parametre" in content or "settings" in content:
                self.__activeParametre()
                return
            elif "mute" in content or "silence" in content:
                self.__active_mode_mute()
                return
            else :
                self.__th_reflect = th.Thread(target=self.__assistant_six.neuron, args=(content,))
                self.__th_reflect.start()
                self.after(100, self.__update_during_assistant_reflect,True)

    def __update_during_assistant_reflect(self,firstCall:bool=False):
        if self.__th_reflect.is_alive():
            if firstCall:
                self.__clearView()
                self.__c_speak_one.place(x=0, y=0)
            self.update()
            self.after(100, self.__update_during_assistant_reflect)
        else:
            nbSortie = self.__assistant_six.getValeurSortie()
            listSortie = self.__assistant_six.getListSortie()
            if nbSortie == 15:
                self.__stop_assistant()
            elif nbSortie == 17:
                self.__windows_help_assistant(listSortie[0])
            else :
                self.__sequenceParoleReponseNeuron(listSortie[0])

            self.__manage_btn_open_fnc()

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
            self.__entryUser.placeBottomCenter()
            if not self.__gazelleUI.gettigerWordSet():
                self.__btn_microphone.placeBottomRight()
            self.__btnParametre.placeBottomLeft()
            self.__c_speak_three.place(x=0, y=0)
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
        self.__entryUser.placeBottomCenter()
        self.__btnParametre.placeBottomLeft()
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
                self.__send_assistant()

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
                self.__send_assistant()

    def __duringSixListen(self):
        if self.__thSixListen.is_alive():
            self.update()
            self.after(100,self.__duringSixListen)

    
    def __quitActu(self):
        self.__clearView()
        self.__c_actualites.place_forget()
        self.maxsize(500,400)
        self.minsize(500,400)
        self.update()
        self.__entryUser.placeBottomCenter()
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
    
    def __active_mode_mute(self):
        self.__sequenceParole(self.__language.getPhActiveMute())
        self.__clearView()
        self.__stopingTriggerWord()
        self.__entryUser.place_forget()
        self.update()
        nb = random.randint(0,1)
        self.__L_c_mute[nb].place(x=0, y=0)
        self.__mute_is_enable = True
    
    def __stopping_mode_mute(self):
        self.__clearView()
        self.update()
        self.__L_c_mute[0].place_forget()
        self.__L_c_mute[1].place_forget()
        self.update()
        self.__sequenceParole(self.__language.getPhQuitMute())
        self.__entryUser.placeBottomCenter()
        self.__btnParametre.placeBottomLeft()
        self.__startingTriggerWord()
        self.__mute_is_enable = False
    
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
            self.__btn_microphone.placeBottomRight()

    def __stopingTriggerWord(self):
        self.__TriggerWorkStop.set()

    def __checkTrigerWord(self):
        self.__startingTriggerWord()

    def __manage_btn_open_fnc(self):
        if self.__assistant_six.getTableur() :
            self.__btn_tableur_is_open.placeBottomRight()
        else :
            self.__btn_tableur_is_open.place_forget()

        if self.__assistant_six.getWord():
            self.__btn_word_is_open.placeBottomLeft()
        else :
            self.__btn_word_is_open.place_forget()

        if self.__assistant_six.getProject():
            self.__btn_project_is_open.placeBottomCenter()
        else :
            self.__btn_project_is_open.place_forget()

    def __windows_help_assistant(self,texte:str):
        winHelp = aTopLevel(width=500, height=600,title="Arrera Six : Aide Assistant",
                            icon=self.__emplacementIcon)
        labelTitleHelp = aLabel(winHelp, police_size=25,text="Six - Aide")
        aideView = aText(winHelp, width=475, height=500,wrap="word",police_size=20)

        self.__sequenceParoleReponseNeuron("Open INTERFACE") # TODO : Texte a revoir

        aideView.insert_text(texte)
        labelTitleHelp.placeTopCenter()
        aideView.placeCenter()