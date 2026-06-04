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

        super().__init__(title=self.__nameSoft,resizable=True, theme_file=theme_file,
                         fg_color=("#ffffff", "#000000"))

        self.geometry("500x700+5+30")

    def active(self,firstBoot:bool,update_available:bool):
        self.mainloop()