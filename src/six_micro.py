import threading as th
from librairy.arrera_tk import *
from librairy.arrera_voice import CArreraVoice

class six_micro(aButton):
    def __init__(self,master,arr_voice:CArreraVoice,fg_color:str=None):
        self.__img_micro = aImage(path_light="asset/icon/microphone/microphone_dark.png",
                                  path_dark="asset/icon/microphone/microphone_white.png",
                                  height=32,width=32)
        self.__img_listen = aImage(path_light="asset/icon/microphone/listen.png"
                                   ,height=32,width=32)
        self.__img_disable = aImage(path_light="asset/icon/microphone/disable_dark.png",
                                    path_dark="asset/icon/microphone/disable_white.png",
                                    height=32,width=32)
        self.__img_trigger = aImage(path_light="asset/icon/microphone/trigger.png"
                                    ,height=32,width=32)

        self.__arr_voice = arr_voice

        self.__th_listen = th.Thread()

        if fg_color is not None:
            super().__init__(master,text="",image=self.__img_micro,fg_color=fg_color,width=32, height=32)
        else :
            super().__init__(master, text="", image=self.__img_micro,width=32, height=32)

        self.configure(command=self.__action_btn_micro)

    # Methode du micro

    def __action_btn_micro(self):
        if not self.__th_listen.is_alive():
            self.__enable_micro_no_trigger()
        else :
            self.__arr_voice.stop_listen()

    def __update_microphone_no_trigger(self):
        if self.__th_listen.is_alive():
            self.update()
            self.after(100, self.__update_microphone_no_trigger)
        else :
            self.configure(image=self.__img_micro,text="")


    # Getteur

    def get_state_microphone(self):
        return self.__th_listen.is_alive()

    def get_texte_microphone(self):
        return self.__arr_voice.getTextMicro()

    # Sans trigger

    def __enable_micro_no_trigger(self):
        self.__th_listen = th.Thread(target=self.__arr_voice.listen)
        self.configure(image=self.__img_listen,text="")
        self.__th_listen.start()
        self.__update_microphone_no_trigger()
