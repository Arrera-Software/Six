import threading as th
from librairy.arrera_tk import *
from librairy.arrera_voice import CArreraVoice

class six_micro(aButton):
    def __init__(self,master,arr_voice:CArreraVoice,fg_color:str=None):
        self.__img_micro = aImage(path_light="asset/icon/microphone/microphone_white.png",
                                  path_dark="asset/icon/microphone/microphone_dark.png",height=30,width=30)
        self.__img_listen = aImage(path_light="asset/icon/microphone/listen.png"
                                   ,height=30,width=30)
        self.__img_disable = aImage(path_light="asset/icon/microphone/disable_white.png",
                                    path_dark="asset/icon/microphone/disable_dark.png",height=30,width=30)
        self.__img_trigger = aImage(path_light="asset/icon/microphone/trigger.png"
                                    ,height=30,width=30)

        self.__arr_voice = arr_voice

        self.__th_listen = th.Thread()

        if fg_color is not None:
            super().__init__(master,text="",image=self.__img_micro,fg_color=fg_color)
        else :
            super().__init__(master, text="", image=self.__img_micro)

    # Methode du micro

    def update_microphone_no_trigger(self):
        if self.__th_listen.is_alive():
            self.update()
            self.after(100, self.update_microphone_no_trigger)
        else :
            self.configure(image=self.__img_listen,text="")


    # Sans trigger

    def __enable_micro_no_trigger(self):
        self.__th_listen = th.Thread(target=self.__arr_voice.listen)
        self.configure(image=self.__img_listen,text="")
        self.__th_listen.start()
        self.update_microphone_no_trigger()
