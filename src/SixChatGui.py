import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
import time
from tkinter.messagebox import *
from src.languageSIX import *
from librairy.arrera_tk import *
import threading as th
from brain.brain import ABrain
import random
from src.six_widget import six_speak,back_widget

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

        self.__dir_GUI_dark = "asset/IMGinterface/dark/"
        self.__dir_GUIl_light = "asset/IMGinterface/white/"

        super().__init__(title=self.__nameSoft,resizable=True, theme_file=theme_file,
                         fg_color=("#ffffff", "#000000"))

        self.geometry("500x700+5+30")

        self.__key_gest = keyboad_manager(self)

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

        self.__back_widget = back_widget(self, dir_gui_light=self.__dir_GUIl_light,
                                         dir_gui_dark=self.__dir_GUI_dark,
                                         micro_fnc=lambda: print("micro"),
                                         parametre_fnc=lambda: print("parametre"))

        self.__back_widget.placeBottomCenter()

    def active(self,firstBoot:bool,update_available:bool):
        self.mainloop()

    def __send_assistant(self):
        print("send")