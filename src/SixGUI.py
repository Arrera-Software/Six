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
from src.six_widget import six_speak

class six_gui(aTk) :
    def __init__(self,iconFolder:str,iconName:str,
                 brain:ABrain,theme_file:str,
                 version:str):
        # var
        self.__nameSoft = "Arrera Six"
        self.__six_speaking = False
        self.__version = version
        self.__mute_is_enable = False
        self.__setting_is_open = False
        self.__first_boot = False
        self.__assistant_load = False
        self.__index_load = 0

        self.__timer = 0

        self.__dir_GUI_dark = "asset/IMGinterface/dark/"
        self.__dir_GUIl_light = "asset/IMGinterface/white/"

        self.__L_img_gui_load = []
        self.__L_img_gui_boot = []
        self.__L_img_gui_speak = []

        self.__D_img_gui_emotion = {
            "not_emotion":(self.__dir_GUIl_light+"boot3.png", self.__dir_GUI_dark+"boot3.png"),
            "happy":(self.__dir_GUIl_light+"content.png",self.__dir_GUI_dark+"content.png"),
            "not_happy":(self.__dir_GUIl_light+"colere.png",self.__dir_GUI_dark+"colere.png"),
            "surprised":(self.__dir_GUIl_light+"sureprit.png",self.__dir_GUI_dark+"sureprit.png"),
            "sad_1":(self.__dir_GUIl_light+"triste1.png",self.__dir_GUI_dark+"triste1.png"),
            "sad_2":(self.__dir_GUIl_light+"triste2.png",self.__dir_GUI_dark+"triste2.png")
        }

        self.__L_aImage_gui_open = [aImage(path_light=self.__dir_GUIl_light + "tableur.png",
                                           path_dark=self.__dir_GUI_dark + "tableur.png",
                                           width=30, height=30),
                                    aImage(path_light=self.__dir_GUIl_light + "projet.png",
                                           path_dark=self.__dir_GUI_dark + "projet.png",
                                           width=30, height=30),
                                    aImage(path_light=self.__dir_GUIl_light + "word.png",
                                           path_dark=self.__dir_GUI_dark + "word.png",
                                           width=30, height=30)]

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

        # Initilisation du keymanager
        self.__key_gest = keyboad_manager(self)

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

        self.__th_speak_stop = th.Thread()

        # Teste de la connextion internet
        try:
            requests.get("https://duckduckgo.com",timeout=5)
            self.__etatConnexion = True
        except requests.ConnectionError :
            self.__etatConnexion = False

        # Instantation de l'objet language
        self.__language = language_six(resource_path("language/six/phraseSix.json"),
                                       resource_path("language/six/firstBootSix.json"))

        # Declaration de l'objet Arrera Gazelle
        self.__gazelleUI = arrera_gazelle(self,self.__gestionnaire,
                                          "json_conf/conf-setting.json")
        self.__gazelleUI.passFNCQuit(self.__quitParametre)
        self.__gazelleUI.passFNCBTNIcon(lambda : self.__about())
        # widget et canvas

        # Canvas Acceuil
        self.__c_welcome = self.__canvas_welcome()
        # Canvas Boot

        self.__c_boot = self.__canvas_boot()

        # Canvas Parole

        self.__c_speak = self.__canvas_speak()

        # Canvas NoConnect
        self.__c_no_connect = self.__canvas_no_connect()

        self.__c_maj = self.__canvas_maj()

        # Canvas emotion
        self.__c_emotion = self.__canvas_emotion()

        # Canvas Mute
        self.__L_c_mute = self.__canvas_mute()
        
        # Canvas Load
        self.__c_load = self.__canvas_load()


        self.__widget_main_windows()

        # Mise a place de la touche entree
        if self.__objOS.osWindows() :
            self.__key_gest.add_key(13,self.__send_assistant)
        elif self.__objOS.osLinux() :
            self.__key_gest.add_key(36,self.__send_assistant)
        elif self.__objOS.osMac() :
            self.__key_gest.add_key(603979789,self.__send_assistant)

        # Declaration de la variable pour contenir les theard
        self.__thSpeak = th.Thread()
        self.__th_speak = th.Thread()
        self.__thSpeakActu = th.Thread()
        self.__thMinuteurActu = th.Thread()
        self.__thBoot = th.Thread()


    def active(self,firstBoot:bool,update_available:bool):

        self.__first_boot = firstBoot

        if update_available:
            self.__c_maj.place(x=0,y=0)
        else :
            self.__boot()

        self.mainloop()

    def __boot(self):
        if self.__first_boot:
            self.__sequence_first_boot()
        else :
            self.__sequence_boot()

    # Declaration des diferente page de l'inteface

    def __canvas_welcome(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+"acceuil.png",
                             background_dark=self.__dir_GUI_dark+"acceuil.png",
                             width=500,height=350)
        return c

    def __canvas_boot(self):
        self.__L_img_gui_boot.append((self.__dir_GUIl_light+"boot0.png", self.__dir_GUI_dark+"boot0.png"))
        self.__L_img_gui_boot.append((self.__dir_GUIl_light+"boot1.png", self.__dir_GUI_dark+"boot1.png"))
        self.__L_img_gui_boot.append((self.__dir_GUIl_light+"boot2.png", self.__dir_GUI_dark+"boot2.png"))
        self.__L_img_gui_boot.append((self.__dir_GUIl_light+"boot3.png", self.__dir_GUI_dark+"boot3.png"))

        c = aBackgroundImage(self, background_light=self.__L_img_gui_boot[0][0],
                             background_dark=self.__L_img_gui_boot[0][1],
                             width=500, height=350)

        return c

    def __canvas_speak(self):
        # Image
        self.__L_img_gui_speak.append((self.__dir_GUIl_light+"parole0.png", self.__dir_GUI_dark+"parole0.png"))
        self.__L_img_gui_speak.append((self.__dir_GUIl_light+"parole1.png", self.__dir_GUI_dark+"parole1.png"))

        # Widget

        c = aBackgroundImage(self,background_light=self.__L_img_gui_speak[0][0],
                             background_dark=self.__L_img_gui_speak[0][1],
                             width=500,height=350)

        self.__btn_tableur_is_open_speak = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[0],
                                                   dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                                   command=lambda : self.__set_requette_with_btn("aide tableur"))
        self.__btn_word_is_open_speak = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[1],
                                                dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                                command = lambda : self.__set_requette_with_btn("aide word"))
        self.__btn_project_is_open_speak = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[2],
                                                   dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                                   command=lambda: self.__set_requette_with_btn("aide projet"))

        self.__label_six_speak = six_speak(c)

        return c

    def __canvas_no_connect(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+"noConnect.png",
                    background_dark=self.__dir_GUI_dark+"noConnect.png",
                    width=500,height=350)

        return c

    def __canvas_maj(self):
        c = aBackgroundImage(self,background_light=self.__dir_GUIl_light+"MAJ.png",
                             background_dark=self.__dir_GUI_dark+"MAJ.png",
                             width=500,height=350,fg_color=("#ffffff","#000000"))

        label_text = aLabel(c,text="Une mise à jour d'ARRERA SIX est disponible. Installez-la pour bénéficier des dernières fonctionnalités.",
                            police_size=20,fg_color="#2b3ceb",
                            text_color="white",wraplength=250,justify="left")

        btn_update = aButton(c,text="Mettre a jour",size=20,
                             command=lambda :wb.open("https://www.github.com/Arrera-Software/Six/releases"))

        btn_continuer = aButton(c,text="Me rappeler plus tart",size=20,command=self.__boot)

        label_text.place(x=190,y=40)
        btn_update.placeBottomLeft()
        btn_continuer.placeBottomRight()

        return c

    def __canvas_emotion(self):
        imgLight,imgDark = self.__D_img_gui_emotion["not_emotion"][0],self.__D_img_gui_emotion["not_emotion"][1]

        c = aBackgroundImage(self,background_light=imgLight,
                             background_dark=imgDark,
                             width=500,height=350)

        self.__btn_tableur_is_open_emotion = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[0],
                                             dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                             command=lambda : self.__set_requette_with_btn("aide tableur"))
        self.__btn_word_is_open_emotion = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[1],
                                          dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                          command = lambda : self.__set_requette_with_btn("aide word"))
        self.__btn_project_is_open_emotion = aButton(c, width=30, height=30, text="", image=self.__L_aImage_gui_open[2],
                                             dark_color="#1f1f1f", light_color="#e0e0e0", hover_color=("#949494","#505050"),
                                             command=lambda: self.__set_requette_with_btn("aide projet"))

        return c

    def __canvas_mute(self):
        c1 = aBackgroundImage(self,background_light=self.__dir_GUIl_light+"mute1.png",
                             background_dark=self.__dir_GUI_dark+"mute1.png",
                             width=500,height=400,fg_color=("#ffffff","#000000"))

        c2 = aBackgroundImage(self,background_light=self.__dir_GUIl_light+"mute2.png",
                              background_dark=self.__dir_GUI_dark+"mute2.png",
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

    def __canvas_load(self):
        self.__L_img_gui_load.append((self.__dir_GUIl_light+"load0.png", self.__dir_GUI_dark+"load0.png"))
        self.__L_img_gui_load.append((self.__dir_GUIl_light+"load1.png", self.__dir_GUI_dark+"load1.png"))
        self.__L_img_gui_load.append((self.__dir_GUIl_light+"load2.png", self.__dir_GUI_dark+"load2.png"))

        c = aBackgroundImage(self,background_light=self.__L_img_gui_load[0][0],
                         background_dark=self.__L_img_gui_load[0][1],
                         width=500,height=400,fg_color=("#ffffff","#000000"))
        return c

    def __widget_main_windows(self):

        self.__entryUser = aEntry(self,police_size=20,width=360)

        imageMicroTriger= aImage(path_light=self.__dir_GUIl_light+"micro.png",
                                 path_dark=self.__dir_GUI_dark+"micro.png",
                                 width=50,height=50)
        imageMicroRequette=aImage(path_light=self.__dir_GUIl_light+"microIcon.png",
                                  path_dark=self.__dir_GUI_dark+"microIcon.png",
                                  width=50,height=50)
        imageMicroSimple = aImage(path_light=self.__dir_GUIl_light+"microsimple.png",
                                  path_dark=self.__dir_GUI_dark+"microsimple.png",
                                  width=30,height=30)
        imageParametre = aImage(path_light=self.__dir_GUIl_light+"settings.png",
                                path_dark=self.__dir_GUI_dark+"settings.png",
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

    # Methode qui modifie les image des canvas

    def __change_img_canvas_boot(self,index:int):
       if not (0 <= index <= 3):
           index = 0

       light_path, dark_path = self.__L_img_gui_boot[index]

       self.__c_boot.change_background(background_light=light_path, background_dark=dark_path)

       self.update()

    def __change_img_canvas_speak(self,index:int):
        if not (0 <= index <= 1):
            index = 0

        light_path, dark_path = self.__L_img_gui_speak[index]

        self.__c_speak.change_background(background_light=light_path, background_dark=dark_path)

        self.update()

    def __change_img_canvas_emotion(self,emotion:str):
        if emotion not in self.__D_img_gui_emotion.keys():
            emotion = "not_emotion"

        light_path, dark_path = self.__D_img_gui_emotion[emotion]

        self.__c_emotion.change_background(background_light=light_path, background_dark=dark_path)

        self.update()

    # About

    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile=self.__emplacementIcon,
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Six",
                      linkWeb="https://arrera-software.fr/")

    # STOP ASSISTANT
    def __on_close(self):
        if askyesno("Atention", "Voulez-vous vraiment fermer Six"):
            self.title(self.__nameSoft)
            self.__gazelleUI.clearAllFrame()
            self.update()
            self.__entryUser.placeBottomCenter()
            self.__btnParametre.placeBottomLeft()
            self.__stop_assistant()
    
    def __stop_assistant(self):
        self.__six_speaking = True
        if self.__mute_is_enable :
            self.__stopping_mode_mute()
        self.__beginning_sequence_stop()

    # SEQUENCE

    def __sequence_emotion(self):
        if 10 >= self.__timer >=40:
            self.__change_img_canvas_emotion("not_emotion")
        elif 41 <= self.__timer >=80:
            if random.randint(1,2) == 1 :
                self.__change_img_canvas_emotion("happy")
            else :
                self.__change_img_canvas_emotion("surprised")
        elif 81 <= self.__timer >=180:
            var = random.randint(1,2)
            if var == 1 :
                self.__change_img_canvas_emotion("sad_1")
            else :
                self.__change_img_canvas_emotion("sad_2")
        elif self.__timer >= 181 and self.__timer != 0 :
            self.__change_img_canvas_emotion("not_happy")

    def __sequence_boot(self):
        self.__clear_view()
        self.__change_img_canvas_boot(0)
        self.__c_boot.place(x=0, y=0)
        time.sleep(0.2)
        self.__change_img_canvas_boot(1)
        time.sleep(0.2)
        self.__change_img_canvas_boot(2)
        time.sleep(0.2)
        self.__change_img_canvas_boot(3)
        time.sleep(0.2)
        self.__c_boot.place_forget()
        self.__c_welcome.place(x=0, y=0)
        if not self.__etatConnexion:
            self.__c_welcome.place_forget()
            self.protocol("WM_DELETE_WINDOW", self.__stop_assistant)
            self.__c_no_connect.place(x=0, y=0)
            self.update()
        else :
            self.__speak_boot()


    def __speak_boot(self):
        texte = self.__assistant_six.boot()
        self.__th_speak = th.Thread(target=self.__avoice.say,args=(texte,))
        self.__th_speak.start()
        self.__view_beggin_speak(texte)
        self.__update_speak(True)

    def __sequence_load(self):
        index = 0
        match self.__index_load:
            case 0 :
                index = 0
            case 1 :
                index = 1
            case 2 :
                index = 2
            case 3 :
                index = 1
            case _ :
                index = 0

        light_path, dark_path = self.__L_img_gui_load[index]
        self.__c_load.change_background(background_light=light_path, background_dark=dark_path)

    def __sequence_first_boot(self):
        self.__clear_view()
        self.__change_img_canvas_boot(0)
        self.__c_boot.place(x=0, y=0)
        time.sleep(0.2)
        self.__change_img_canvas_boot(1)
        self.update()
        time.sleep(0.2)
        self.__change_img_canvas_boot(2)
        self.update()
        time.sleep(0.2)
        self.__change_img_canvas_boot(3)
        self.update()
        time.sleep(0.2)
        self.__th_speak = th.Thread(target=self.__speak_first_boot)
        self.__th_speak.start()
        self.__update_speak(True)
        self.__c_boot.place_forget()
        
    def __speak_first_boot(self):
        name = self.__gest_user.getLastnameUser()
        genre = self.__gest_user.getGenre()
        texte = self.__language.getPhraseFirstBoot(genre,name,1)
        self.__view_beggin_speak(texte)
        self.update()
        self.__avoice.say(texte)
        self.__view_after_speak()
        time.sleep(3)
        texte = (self.__language.getPhraseFirstBoot(genre,name, 2))
        self.__view_beggin_speak(texte)
        self.update()
        self.__avoice.say(texte)
    
    def __clear_view(self):
        self.__labelTriggerMicro.place_forget()
        self.__c_welcome.place_forget()
        self.__c_boot.place_forget()
        self.__c_speak.place_forget()
        self.__c_no_connect.place_forget()
        self.__c_emotion.place_forget()
        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()
        self.__c_maj.place_forget()
        self.__c_load.place_forget()
        
    def __beginning_sequence_stop(self):
        self.__six_speaking = True
        texte = self.__assistant_six.shutdown()

        self.__th_speak_stop = th.Thread(target=self.__avoice.say, args=(texte,))

        self.__view_beggin_speak(texte)

        self.__th_speak_stop.start()

        self.__update_durring_stopping_speak()

    def __update_durring_stopping_speak(self):
        if self.__th_speak_stop.is_alive():
            self.update()
            self.after(100,self.__update_durring_stopping_speak)
        else :
            self.__clear_view()

            self.__change_img_canvas_boot(3)
            self.__c_boot.place(x=0, y=0)
            self.update()

            time.sleep(0.2)
            self.__change_img_canvas_boot(2)
            self.update()

            time.sleep(0.2)
            self.__change_img_canvas_boot(1)
            self.update()

            time.sleep(0.2)
            self.__change_img_canvas_boot(0)
            self.update()

            if self.__objOS.osWindows():
                os.kill(os.getpid(), signal.SIGINT)
            elif self.__objOS.osLinux() or self.__objOS.osMac():
                os.kill(os.getpid(), signal.SIGKILL)

    def __set_requette_with_btn(self,requette:str):
        self.__entryUser.delete(0,END)
        self.__entryUser.insert(0,requette)
        self.__send_assistant()

    def __send_assistant(self):
        content = self.__entryUser.get().lower()
        self.__entryUser.delete(0, END)
        if content :
            self.__entryUser.place_forget()
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
                self.__clear_view()
                self.__assistant_load  = True
                self.__c_load.place(x=0, y=0)

                self.__sequence_load()

                self.__c_load.place(x=0, y=0)

                self.__index_load += 1

            self.update()

            self.__sequence_load()
            self.__index_load += 1

            if self.__index_load == 3 :
                self.__index_load = 0

            self.after(100, self.__update_during_assistant_reflect)
        else:
            self.__assistant_load = False
            nbSortie = self.__assistant_six.getValeurSortie()
            listSortie = self.__assistant_six.getListSortie()

            self.__index_load = 0
            self.__clear_view()

            self.__treatment_out_assistant(nbSortie,listSortie)

    def __treatment_out_assistant(self,var:int,out:list):
        if var == 15:
            self.__stop_assistant()
        elif var == 17:
            self.__windows_help_assistant(out[0])
        else :
            self.__sequence_speak(out[0])

        self.__manage_btn_open_fnc()

    def __update__assistant(self):
        if not self.__setting_is_open and not self.__mute_is_enable and not self.__six_speaking and not self.__assistant_load:
            self.__timer += 1
            if self.__assistant_six.updateAssistant():
                varOut = self.__assistant_six.getValeurSortie()
                listOut = self.__assistant_six.getListSortie()
                self.__treatment_out_assistant(varOut,listOut)
            elif self.__timer >= 10:
                if self.__timer == 10:
                    self.__c_speak.place_forget()
                    self.__c_emotion.place(x=0, y=0)
                self.__sequence_emotion()

        self.after(1000,self.__update__assistant)

    def __view_beggin_speak(self,text:str):
        self.__change_img_canvas_speak(0)
        self.__label_six_speak.set_text(text)
        self.__label_six_speak.view_during_speak()
        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()
        self.__c_speak.place(x=0, y=0)
        self.update()

    def __view_after_speak(self):
        self.__change_img_canvas_speak(1)
        self.__label_six_speak.view_after_speak()
        self.update()


    def __sequence_speak(self, text:str):
        self.__six_speaking = True
        self.__timer = 0
        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()
        self.__entryUser.place_forget()

        self.__view_beggin_speak(text)

        self.update()
        self.__th_speak = th.Thread(target=self.__avoice.say, args=(text,))
        self.__th_speak.start()
        self.__update_speak()
        self.update()

    def __update_speak(self,boot:bool=False):
        if self.__th_speak.is_alive():
            self.update()
            if boot :
                self.after(100, self.__update_speak,True)
            else :
                self.after(100, self.__update_speak)
        else :
            self.__entryUser.placeBottomCenter()
            if not self.__gazelleUI.gettigerWordSet():
                self.__btn_microphone.placeBottomRight()
            self.__btnParametre.placeBottomLeft()
            self.__change_img_canvas_speak(1)
            self.__label_six_speak.view_after_speak()
            self.update()
            self.__six_speaking = False
            if boot:
                self.__update__assistant()
    
    def __activeParametre(self):
        self.__setting_is_open = True
        self.__timer = 0
        self.__stopingTriggerWord()
        self.title(self.__nameSoft+" : Parametre")
        self.update()
        self.__clear_view()
        self.__entryUser.place_forget()
        self.__gazelleUI.active()
        self.update()
    
    def __quitParametre(self):
        self.title(self.__nameSoft)
        self.__gazelleUI.clearAllFrame()
        self.update()
        texte = self.__language.getPhQuitSetting()
        self.__th_speak = th.Thread(target=self.__avoice.say, args=(texte,))
        self.__view_beggin_speak(texte)
        self.__th_speak.start()
        self.__update_speak()
        self.__setting_is_open = False
    
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
        if microOK == 0:
            sortieMicro = self.__avoice.getTextMicro()
            self.__entryUser.delete(0, END)
            if sortieMicro != "nothing":
                self.__entryUser.insert(0, sortieMicro)
                time.sleep(0.5)
                self.__send_assistant()

    def __duringSixListen(self):
        if self.__thSixListen.is_alive():
            self.update()
            self.after(100,self.__duringSixListen)
    
    def __active_mode_mute(self):
        self.__mute_is_enable = True
        texte = (self.__language.getPhActiveMute())
        self.__view_beggin_speak(texte)
        self.__th_speak = th.Thread(target=self.__avoice.say, args=(texte,))
        self.__th_speak.start()
        self.__update_active_mute()

    def __update_active_mute(self):
        if self.__th_speak.is_alive():
            self.update()
            self.after(100,self.__update_active_mute)
        else :
            self.__clear_view()
            self.__stopingTriggerWord()
            self.__entryUser.place_forget()
            self.update()
            nb = random.randint(0,1)
            self.__L_c_mute[nb].place(x=0, y=0)
            self.__mute_is_enable = True
            self.__timer = 0

    
    def __stopping_mode_mute(self):
        self.__clear_view()
        self.update()
        self.__L_c_mute[0].place_forget()
        self.__L_c_mute[1].place_forget()
        self.update()
        texte = self.__language.getPhQuitMute()
        self.__th_speak = th.Thread(target=self.__avoice.say, args=(texte,))
        self.__mute_is_enable = False
        self.__view_beggin_speak(texte)
        self.__th_speak.start()
        self.__startingTriggerWord()
        self.__update_speak()
    
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
            self.__btn_tableur_is_open_speak.placeBottomRight()
            self.__btn_tableur_is_open_emotion.placeBottomRight()
        else :
            self.__btn_tableur_is_open_speak.place_forget()

        if self.__assistant_six.getWord():
            self.__btn_word_is_open_speak.placeBottomLeft()
            self.__btn_word_is_open_emotion.placeBottomLeft()
        else :
            self.__btn_word_is_open_speak.place_forget()

        if self.__assistant_six.getProject():
            self.__btn_project_is_open_speak.placeBottomCenter()
            self.__btn_project_is_open_emotion.placeBottomCenter()
        else :
            self.__btn_project_is_open_speak.place_forget()

    def __windows_help_assistant(self,texte:str):
        winHelp = aTopLevel(width=500, height=600,title="Arrera Six : Aide Assistant",
                            icon=self.__emplacementIcon)
        labelTitleHelp = aLabel(winHelp, police_size=25,text="Six - Aide")
        aideView = aText(winHelp, width=475, height=500,wrap="word",police_size=20)

        self.__sequence_speak(self.__language.phOpenInterface(
            genre=self.__gest_user.getGenre(),
            name=self.__gest_user.getLastnameUser()))

        aideView.insert_text(texte)
        labelTitleHelp.placeTopCenter()
        aideView.placeCenter()