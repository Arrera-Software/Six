from abc import abstractmethod
from librairy.arrera_tk import *

class six_information_widget(aFrame):
    def __init__(self,master,dir_gui_light:str,dir_gui_dark:str,
                 fnc_tableur:Callable,fnc_doc:Callable,fnc_projet:Callable):
        super().__init__(master)

        self.__img_tableur = [
            aImage(path_light=dir_gui_light+"tableur_noopen.png",
                   path_dark=dir_gui_dark+"tableur_noopen.png",
                   width=32,height=32),
            aImage(path_light=dir_gui_light+"tableur.png"
                   ,path_dark=dir_gui_dark+"tableur.png",
                   width=32, height=32),
        ]

        self.__img_doc = [
            aImage(path_light=dir_gui_light+"word_noopen.png",
                   path_dark=dir_gui_dark+"word_noopen.png",
                   width=32,height=32),
            aImage(path_light=dir_gui_light+"word.png",
                   path_dark=dir_gui_dark+"word.png",
                   width=32, height=32),
        ]

        self.__img_projet = [
            aImage(path_light=dir_gui_light+"projet_noopen.png",
                   path_dark=dir_gui_dark+"projet_noopen.png",
                   width=32,height=32),
            aImage(path_light=dir_gui_light+"projet.png",
                   path_dark=dir_gui_dark+"projet.png",
                   width=32, height=32),
        ]

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__b_tableur = aButton(self, image=self.__img_tableur[0], text="",
                                   width=32, height=32, fg_color="transparent",
                                   command=fnc_tableur)
        self.__b_doc = aButton(self, image=self.__img_doc[0], text="",
                               width=32, height=32, fg_color="transparent",
                               command=fnc_doc)
        self.__b_projet = aButton(self, image=self.__img_projet[0], text="",
                                  width=32, height=32, fg_color="transparent",
                                  command=fnc_projet)

        self.__b_tableur.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.__b_doc.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.__b_projet.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    def update_state(self,tableur:bool,doc:bool,projet:bool):
        if tableur:
            self.__b_tableur.configure(image=self.__img_tableur[1], text="")
        else :
            self.__b_tableur.configure(image=self.__img_tableur[0], text="")
        
        if doc:
            self.__b_doc.configure(image=self.__img_doc[1], text="")
        else :
            self.__b_doc.configure(image=self.__img_doc[0], text="")
        
        if projet:
            self.__b_projet.configure(image=self.__img_projet[1], text="")
        else :
            self.__b_projet.configure(image=self.__img_projet[0], text="")

class back_widget(aFrame):
    def __init__(self,master,dir_gui_light:str,dir_gui_dark:str,
                 send_fnc:Callable,micro_fnc:Callable):
        super().__init__(master)

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        self.__entry = aEntry(self,police_size=25,width=400)

        image_send = aImage(path_light=dir_gui_light + "sendsimple.png",
                                  path_dark=dir_gui_dark + "sendsimple.png",
                                  width=30, height=30)

        image_micro = aImage(path_light=dir_gui_light + "microsimple.png",
                             path_dark=dir_gui_dark + "microsimple.png",
                             width=30, height=30)


        self.__btn_send = aButton(self, width=30, height=30, text="",
                                  image=image_send,
                                  command=send_fnc)

        self.__btn_micro = aButton(self, width=30,
                                   height=30, text="",
                                   image=image_micro,
                                   command=micro_fnc)

        self.__entry.bind("<FocusIn>", self.__on_focus)
        self.__entry.bind("<FocusOut>", self.__on_unfocus)

        self.__btn_micro.grid(row=0, column=0, padx=5, pady=5)
        self.__entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.__btn_send.grid(row=0, column=2, padx=5, pady=5)

    def __on_focus(self, event):
        self.__entry.configure(width=500)

        self.__btn_micro.grid_forget()
        self.__btn_send.grid_forget()

    def __on_unfocus(self, event):
        self.__entry.configure(width=400)

        self.__btn_micro.grid(row=0, column=0, padx=5, pady=5)
        self.__btn_send.grid(row=0, column=2, padx=5, pady=5)


    def get_text_entry(self):
        text = self.__entry.get()
        self.__entry.delete(0, END)
        return text

    def set_text_entry(self,text:str):
        self.__entry.delete(0,END)
        self.__entry.insert(0,text)

class frame_conf(aFrame):
    def __init__(self,master,dir_gui_light:str,dir_gui_dark:str,list_voice:list,
                 fnc_setting:Callable,fnc_change_voice:Callable,fnc_get_voice_model):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=5)
        self.grid_rowconfigure(4, weight=1)

        img_setting = aImage(path_light=dir_gui_light + "settings.png",
                             path_dark=dir_gui_dark + "settings.png",
                             height=30,width=30)

        self.grid_columnconfigure(0, weight=1)

        l = aLabel(self,text="Arrera Six",police_size=25)

        btn_voice_validate = aButton(self, text="Valider",
                                     command=fnc_change_voice)

        self.__m_voice = aOptionMenu(self,value=list_voice,
                                     fg_color=btn_voice_validate.cget("fg_color"),
                                     text_color=btn_voice_validate.cget("text_color"))

        self.__m_voice.set_text(fnc_get_voice_model())

        setting_btn = aButton(self,text="",image=img_setting,command=fnc_setting)

        l.grid(row=0, column=0, sticky="n", pady=10)
        self.__m_voice.grid(row=1, column=0, sticky="n", pady=5)
        btn_voice_validate.grid(row=2, column=0, sticky="n", pady=5)
        setting_btn.grid(row=4, column=0, sticky="s", pady=10)

    def get_value_voice_menu(self):
        return self.__m_voice.getValue()

class label_parole(aLabel):
    def __init__(self,master,fg_color:str,text_color:str,justify:str,text:str):
        super().__init__(master,wraplength=250,police_size=16,text=text,
                         justify=justify,fg_color=fg_color,text_color=text_color,corner_radius=15)

    @abstractmethod
    def view(self):
        pass


class label_assistant(label_parole):
    def __init__(self,master,text:str):
        super().__init__(master,fg_color="#0024f3",text_color="#ffffff",text=text,justify="left")

    def view(self):
        self.pack(anchor="w",pady=6)

class label_user(label_parole):
    def __init__(self, master, text: str):
        super().__init__(master, fg_color="#4c6fff", text_color="#ffffff", text=text,justify="right")

    def view(self):
        self.pack(anchor="e",pady=6)