#import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
import time
from tkinter.messagebox import *
from src.languageSIX import *
from librairy.arrera_tk import *
import threading as th
from brain.brain import ABrain
from src.six_voice import SixVoice
import random
from src.six_chat_widget import back_widget,six_information_widget,frame_conf,label_assistant,label_user

class six_gui_chat(aTk):
    def __init__(self, iconFolder: str, iconName: str,
                 brain: ABrain, theme_file: str,
                 version: str):

        self.__nameSoft = "Arrera Six"

        # Objet
        self.__assistant_six = brain
        self.__gestionnaire = self.__assistant_six.getGestionnaire()
        self.__objOS = self.__gestionnaire.getOSObjet()
        self.__avoice = self.__gestionnaire.getArrVoice()
        self.__gest_user = self.__gestionnaire.getUserConf()

        self.__version = version

        self.__dir_GUI_dark = "asset/IMGinterface/dark/"
        self.__dir_GUIl_light = "asset/IMGinterface/white/"

        # Theard
        self.__th_thinking_assistant = th.Thread()

        super().__init__(title=self.__nameSoft,resizable=True, theme_file=theme_file,
                         fg_color=("#ffffff", "#000000"))

        self.geometry("550x700+5+30")

        self.__key_gest = keyboad_manager(self)

        # Parametre
        self.__gazelleUI = arrera_gazelle(self, self.__gestionnaire,
                                          resource_path("json_conf/conf-setting.json"))
        self.__gazelleUI.passFNCQuit(self.__quit_setting)
        self.__gazelleUI.passFNCBTNIcon(lambda: self.__about())

        # Voix

        self.__voice = SixVoice(self.__objOS)

        self.__voice.load_voice_model()

        self.__th_voice = th.Thread(target=self.__check_voice_model)

        self.__th_speak = th.Thread()

        # Partie Icone

        if self.__objOS.osWindows():
            self.__emplacementIcon = iconFolder + "win/" + iconName + ".ico"
            self.iconbitmap(self.__emplacementIcon)
            self.__key_gest.add_key(13, self.__send_assistant)
            self.__key_gest.add_key(27, lambda: self.focus())
        elif self.__objOS.osLinux():
            self.__emplacementIcon = iconFolder + "linux/" + iconName + ".png"
            self.iconphoto(False, PhotoImage(file=self.__emplacementIcon))
            self.__key_gest.add_key(36, self.__send_assistant)
            self.__key_gest.add_key(9, lambda: self.focus())
        elif self.__objOS.osMac():
            self.__emplacementIcon = resource_path(iconFolder + "macos/" + iconName + ".png")
            self.iconphoto(False, PhotoImage(file=self.__emplacementIcon))
            self.__key_gest.add_key(603979789, self.__send_assistant)
            self.__key_gest.add_key(889192475, lambda: self.focus())

        # Configuration de la fenêtre principale
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Widgets
        self.__main_frame = aFrame(self)
        self.__main_frame.grid_rowconfigure(0, weight=0)  # top_frame
        self.__main_frame.grid_rowconfigure(1, weight=2)  # assistant_frame
        self.__main_frame.grid_rowconfigure(2, weight=0)  # back_widget
        self.__main_frame.grid_columnconfigure(0, weight=1)

        # Image
        img_six = aImage(width=50,height=50,
                         path_light="asset/icon/linux/icon.png",
                         path_dark="asset/icon/linux/icon.png")
        # Frame
        self.__top_frame = aFrame(self.__main_frame,height=75)
        self.__assistant_frame = aFrame(self.__main_frame)
        self.__back_widget = back_widget(self.__main_frame, dir_gui_light=self.__dir_GUIl_light,
                                         dir_gui_dark=self.__dir_GUI_dark,
                                         send_fnc=lambda: print("send"),
                                         micro_fnc=lambda: print("micro"))

        # Config Frame

        self.__top_frame.grid_columnconfigure(0, weight=0)
        self.__top_frame.grid_columnconfigure(1, weight=1)
        self.__top_frame.grid_columnconfigure(2, weight=0)

        self.__assistant_frame.grid_columnconfigure(0, weight=1)
        self.__assistant_frame.grid_rowconfigure(0, weight=1)
        self.__assistant_frame.grid_columnconfigure(1, weight=0)

        # Widget
        self.__btn_six = aButton(self.__top_frame,text="",image=img_six,fg_color="transparent",
                          corner_radius=25,width=15,height=15,command=self.__view_frame_conf)

        self.__information_widget = six_information_widget(self.__top_frame,
                                                    dir_gui_light=self.__dir_GUIl_light,
                                                    dir_gui_dark=self.__dir_GUI_dark,
                                                    fnc_doc=lambda: print("doc"),
                                                    fnc_tableur=lambda: print("tableur"),
                                                    fnc_projet=lambda: print("projet"))
        self.__assistant_out = aScrollableFrame(self.__assistant_frame)
        self.__conf_frame = frame_conf(self.__assistant_frame,
                                       dir_gui_light=self.__dir_GUIl_light,
                                       dir_gui_dark=self.__dir_GUI_dark,
                                       list_voice=self.__voice.get_list_voice_model(),
                                       fnc_setting=self.__open_setting)



    def __view_frame_conf(self):
        self.__assistant_frame.grid_columnconfigure(0, weight=1)
        self.__assistant_frame.grid_columnconfigure(1, weight=5)

        self.__btn_six.configure(command=self.__unview_frame_conf)

        self.__conf_frame.grid(row=0, column=0, sticky="nsew",padx=5,pady=5)
        self.__assistant_out.grid(row=0, column=1, sticky="nsew",padx=5,pady=5)

    def __unview_frame_conf(self):
        self.__assistant_frame.grid_columnconfigure(0, weight=1)
        self.__assistant_frame.grid_columnconfigure(1, weight=0)

        self.__btn_six.configure(command=self.__view_frame_conf)

        self.__conf_frame.grid_forget()
        self.__assistant_out.grid(row=0, column=0, sticky="nsew",padx=5,pady=5)

    def active(self,firstBoot:bool,update_available:bool):
        text_boot = self.__assistant_six.boot()

        label_assistant(self.__assistant_out,text_boot).view()

        self.__th_voice.start()

        self.after(1000, self.__updating_during_check_voice_model)

        self.mainloop()

    def __check_voice_model(self):
        if not self.__voice.check_voice_model():
            showerror("Error","Le model de voix ne sont pas disponible")

    def __updating_during_check_voice_model(self):
        if self.__th_voice.is_alive():
            self.after(1000,self.__updating_during_check_voice_model)
        else :
            # Placement des widget
            self.__btn_six.grid(row=0, column=0, padx=10, pady=10)
            self.__information_widget.grid(row=0, column=2, padx=10, pady=10)
            # Placement des Frame
            self.__main_frame.grid(row=0, column=0, sticky="nsew")
            self.__top_frame.grid(row=0, column=0, sticky="ew")
            self.__assistant_frame.grid(row=1, column=0, sticky="nsew")
            self.__back_widget.grid(row=2, column=0, sticky="", pady=5)

            self.__assistant_out.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def __send_assistant(self):
        text = self.__back_widget.get_text_entry()
        if text != "":
            label_user(self.__assistant_out,text).view()
            self.__th_thinking_assistant = th.Thread(target=self.__thinking_assistant,args=(text,))
            self.__th_thinking_assistant.start()
            self.__update_during_thinking()

    def __thinking_assistant(self,text:str):
        self.__back_widget.grid_forget()
        self.__assistant_six.neuron(text)

    def __update_during_thinking(self):
        if self.__th_thinking_assistant.is_alive():
            self.after(100, self.__update_during_thinking)
        else:
            self.__th_thinking_assistant = th.Thread()
            text = self.__assistant_six.getListSortie()[0]
            label_assistant(self.__assistant_out,text).view()
            self.__back_widget.grid(row=2, column=0, sticky="", pady=5)
            self.__th_speak = th.Thread(target=self.__voice.speak,args=(text,))
            self.__th_speak.start()
            self.__update_during_speak()

    def __update_during_speak(self):
        if self.__th_speak.is_alive():
            self.after(100, self.__update_during_speak)
            self.update()
        else :
            del self.__th_speak
            self.__th_speak = th.Thread()

    def __open_setting(self):
        self.__unview_frame_conf()
        self.__main_frame.grid_forget()
        self.__gazelleUI.active()
        self.update_idletasks()
        self.update()


    def __quit_setting(self):
        self.__gazelleUI.clearAllFrame()
        self.__main_frame.grid(row=0, column=0, sticky="nsew")
        self.update_idletasks()
        self.update()

    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile=self.__emplacementIcon,
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Six",
                      linkWeb="https://arrera-software.fr/")