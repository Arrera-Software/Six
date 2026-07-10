import threading as th
from typing import Callable, TYPE_CHECKING
from librairy.arrera_tk import *
from librairy.arrera_voice import CArreraVoice

if TYPE_CHECKING:
    from src.six_chat_widget import back_widget


class six_micro(aButton):
    def __init__(self,master,arr_voice:CArreraVoice,back_widget:'back_widget',fnc_send:Callable,fg_color:str=None):
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

        self.__back_widget = back_widget
        self.__fnc_send = fnc_send

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
            text = self.__arr_voice.getTextMicro()
            if text != "":
                self.__back_widget.set_text_entry(text)
                self.__fnc_send()

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
