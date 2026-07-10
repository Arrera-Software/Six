from librairy.arrera_tk import *
from src.six_micro import six_micro
from librairy.arrera_voice import CArreraVoice

class six_speak(aLabel):
    def __init__(self,master):
        super().__init__(master,text="", wraplength=440,justify="left",police_size=20,corner_radius=0)

    def set_text(self,texte:str):
        self.configure(text=texte)

    def view_during_speak(self):
        self.configure(fg_color="#2b3ceb", text_color="white")
        self.place(x=30, y=110)
        self.master.update()

    def view_after_speak(self):
        self.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.place(x=10, y=80)
        self.master.update()

    def unview(self):
        self.place_forget()
        self.master.update()


class back_widget(aFrame):
    def __init__(self,master,dir_gui_light:str,dir_gui_dark:str,
                 parametre_fnc:Callable,arr_voice:CArreraVoice,
                 fnc_send:Callable,use_trigger:bool=False):
        super().__init__(master,width=500,height=50)
        self.__btn_micro_is_enable = True

        self.__entry = aEntry(self,police_size=20,width=360)

        imageParametre = aImage(path_light=dir_gui_light + "settings.png",
                                path_dark=dir_gui_dark + "settings.png",
                                width=30, height=30)

        self.__btn_microphone = six_micro(self,arr_voice=arr_voice,
                                          back_widget=self,
                                          fnc_send=fnc_send,
                                          use_trigger=use_trigger)

        self.__btnParametre = aButton(self, width=30, height=30, text="",
                                      image=imageParametre, command=parametre_fnc)

        self.__entry.bind("<FocusIn>", self.__on_focus)
        self.__entry.bind("<FocusOut>", self.__on_unfocus)

        self.__btn_microphone.placeCenterRight()
        self.__entry.placeCenter()
        self.__btnParametre.placeCenterLeft()

    def __on_focus(self, event):
        self.__entry.configure(width=450)

        self.__btn_microphone.place_forget()
        self.__btnParametre.place_forget()

    def __on_unfocus(self, event):
        self.__entry.configure(width=360)

        if self.__btn_micro_is_enable:
            self.__btn_microphone.placeCenterRight()
        self.__btnParametre.placeCenterLeft()


    def get_text_entry(self):
        text = self.__entry.get()
        self.__entry.delete(0, END)
        return text

    def set_text_entry(self,text:str):
        self.__entry.delete(0,END)
        self.__entry.insert(0,text)

    def set_use_trigger(self, use_trigger: bool):
        self.__btn_microphone.set_use_trigger(use_trigger)