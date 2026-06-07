from librairy.arrera_tk import *

class back_widget(aFrame):
    def __init__(self,master,dir_gui_light:str,dir_gui_dark:str,
                 send_fnc:Callable):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.__entry = aEntry(self,police_size=25,width=360)

        image_send = aImage(path_light=dir_gui_light + "sendsimple.png",
                                  path_dark=dir_gui_dark + "sendsimple.png",
                                  width=30, height=30)


        self.__btn_send = aButton(self, width=30, height=30, text="",
                                  image=image_send,
                                  command=send_fnc)

        self.__entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.__btn_send.grid(row=0, column=1, padx=5, pady=5)


    def get_text_entry(self):
        text = self.__entry.get()
        self.__entry.delete(0, END)
        return text

    def set_text_entry(self,text:str):
        self.__entry.delete(0,END)
        self.__entry.insert(0,text)