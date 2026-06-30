import signal
import requests
from setting_gui.arrera_gazelle import arrera_gazelle
from lynx_gui.arrera_lynx import arrera_lynx
import time
from tkinter.messagebox import *
from src.languageSIX import *
from librairy.arrera_tk import *
import threading as th
from brain.brain import confNeuron,ABrain
from src.six_voice import SixVoice
import random
from src.six_chat_widget import back_widget,six_information_widget,frame_conf,label_assistant,label_user

class six_gui_chat(aTk):
    def __init__(self, iconFolder: str, iconName: str,
                 conf : confNeuron,
                 theme_file: str,
                 version: str):

        self.__nameSoft = "Arrera Six"

        self.__state_conf = True
        self.__mute_enable = False

        # Objet
        self.__assistant_six = ABrain(conf)
        self.__gestionnaire = self.__assistant_six.getGestionnaire()
        self.__objOS = self.__gestionnaire.getOSObjet()
        self.__avoice = self.__gestionnaire.getArrVoice()
        self.__gest_user = self.__gestionnaire.getUserConf()

        self.__version = version

        self.__dir_GUI_dark = "asset/IMGinterface/dark/"
        self.__dir_GUIl_light = "asset/IMGinterface/white/"

        # Theard
        self.__th_thinking_assistant = th.Thread()

        super().__init__(title=self.__nameSoft, theme_file=theme_file,
                         fg_color=("#ffffff", "#000000"))

        self.__key_gest = keyboad_manager(self)

        self.__language = language_six(resource_path("language/six/phraseSix.json"),
                                       resource_path("language/six/firstBootSix.json"))

        # Parametre et firt boot
        self.__gazelleUI = arrera_gazelle(self, self.__gestionnaire,
                                          resource_path("json_conf/conf-setting.json"))
        self.__gazelleUI.passFNCQuit(self.__quit_setting)
        self.__gazelleUI.passFNCBTNIcon(lambda: self.__about())

        self.__lynx = arrera_lynx(self,self.__gestionnaire,
                                  resource_path("json_conf/configLynx.json"),
                                  lambda : self.__end_lynx())

        # Voix

        self.__voice = SixVoice(self.__objOS)

        self.__voice.load_voice_model()

        self.__th_voice = th.Thread(target=self.__check_voice_model)

        self.__th_speak = th.Thread()

        self.__th_firt_boot = th.Thread()

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
                                         send_fnc=lambda: print("send"))

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
                                                    fnc_projet=lambda: print("projet"),
                                                    fnc_sound=lambda : self.__action_mute(),
                                                    micro_fnc=lambda : print("micro"))

        self.__assistant_out = aScrollableFrame(self.__assistant_frame)

        self.__conf_frame = frame_conf(self.__assistant_frame,
                                       dir_gui_light=self.__dir_GUIl_light,
                                       dir_gui_dark=self.__dir_GUI_dark,
                                       list_voice=self.__voice.get_list_voice_model(),
                                       fnc_setting=self.__open_setting,
                                       fnc_change_voice=self.__change_voice,
                                       fnc_get_voice_model=lambda : self.__voice.get_current_model())

        self.__mute_frame = self.__frame_mute()



    def __view_frame_conf(self):
        if not self.__mute_enable:
            self.__assistant_frame.grid_columnconfigure(0, weight=1)
            self.__assistant_frame.grid_columnconfigure(1, weight=5)

            self.__btn_six.configure(command=self.__unview_frame_conf)

            self.__conf_frame.grid(row=0, column=0, sticky="nsew",padx=5,pady=5)
            self.__assistant_out.grid(row=0, column=1, sticky="nsew",padx=5,pady=5)


    def __unview_frame_conf(self):
        if not self.__mute_enable:
            self.__assistant_frame.grid_columnconfigure(0, weight=1)
            self.__assistant_frame.grid_columnconfigure(1, weight=0)

            self.__btn_six.configure(command=self.__view_frame_conf)

            self.__conf_frame.grid_forget()
            self.__assistant_out.grid(row=0, column=0, sticky="nsew",padx=5,pady=5)

    def __action_mute(self):
        if not self.__mute_enable:
            self.__mute_enable = True

            self.__information_widget.unview()

            self.__information_widget.active_mute()

            text = self.__language.getPhActiveMute()

            label_assistant(self.__assistant_out,text ).view()

            self.__th_voice = th.Thread(target=self.__voice.speak, args=(text,))

            self.__th_voice.start()

            self.after(100, self.__update_mute)


        else :
            self.__mute_enable = False

            self.__information_widget.unview()

            self.__information_widget.active_mute()

            self.__mute_frame.grid_forget()
            self.__assistant_out.grid(row=0, column=0, sticky="nsew",padx=5,pady=5)

            text = self.__language.getPhQuitMute()

            label_assistant(self.__assistant_out,text).view()

            self.__th_voice = th.Thread(target=self.__voice.speak, args=(text,))

            self.__th_voice.start()

            self.after(100, self.__update_mute)


    def __update_mute(self):
        if self.__th_voice.is_alive():
            self.after(100, self.__update_mute)
        else :
            if self.__mute_enable:
                nb = random.randint(0, 1)

                self.__assistant_out.grid_forget()
                self.__conf_frame.grid_forget()

                self.__icon_mute.configure(image=self.__mute_icon[nb])

                self.__mute_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

                self.__back_widget.grid_forget()

                self.__information_widget.view()
            elif not self.__mute_enable:
                self.__back_widget.grid(row=2, column=0, sticky="", pady=5)
                self.__information_widget.view()


    def __frame_mute(self):
        f = aFrame(self.__assistant_frame)
        f.grid_columnconfigure(0, weight=1)
        f.grid_rowconfigure(0, weight=2)
        f.grid_rowconfigure(1, weight=1)

        self.__mute_icon = [aImage(width=256, height=256,
            path_light="asset/IMGinterface/chat/mute1.png"),
             aImage(width=256, height=256,
                    path_light="asset/IMGinterface/chat/mute2.png")]

        self.__icon_mute = aLabel(f, image=self.__mute_icon[0])
        text_label = aLabel(f, text="Mode Mute Activer", police_size=30)

        self.__icon_mute.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        text_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        return f

    def active(self,update_available:bool):
        firstBoot = self.__gestionnaire.getUserConf().getFirstRun()
        if firstBoot:
            self.resizable(False, False)
            self.geometry(self.__lynx.get_geometry())
            self.update()
            self.__lynx.active()
        else :
            self.__boot()

        self.mainloop()

    def __view_gui(self):
        # Placement des widget
        self.__btn_six.grid(row=0, column=0, padx=10, pady=10)
        self.__information_widget.view()
        # Placement des Frame
        self.__main_frame.grid(row=0, column=0, sticky="nsew")
        self.__top_frame.grid(row=0, column=0, sticky="ew")
        self.__assistant_frame.grid(row=1, column=0, sticky="nsew")
        self.__assistant_out.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def __boot(self):
        self.resizable(True, True)
        self.geometry("550x700+5+30")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
        text_boot = self.__assistant_six.boot()

        label_assistant(self.__assistant_out, text_boot).view()

        self.__view_gui()

        self.__th_voice = th.Thread(target=self.__voice.speak, args=(text_boot,))

        self.__th_voice.start()

        self.after(1000, self.__updating_during_check_voice_model)

    def __end_lynx(self):
        self.__lynx.place_forget()
        del self.__lynx
        self.resizable(True, True)
        self.geometry("550x700+5+30")
        self.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.__view_gui()
        self.update()

        # Placement des Frame

        name = self.__gest_user.getLastnameUser()
        genre = self.__gest_user.getGenre()

        self.__th_firt_boot = th.Thread(target=self.__sequence_firt_boot,
                                        args=(self.__language.getPhraseFirstBoot(genre,name,1),
                                              self.__language.getPhraseFirstBoot(genre,name,2),))

        self.__th_firt_boot.start()
        self.__update_during_firt_boot()


    def __sequence_firt_boot(self,text1:str,text2:str):
        self.__voice.check_voice_model()
        self.__voice.load_voice_model()

        label_assistant(self.__assistant_out, text1).view()

        self.__voice.speak(text1)

        label_assistant(self.__assistant_out, text2).view()
        self.__voice.speak(text2)


    def __update_during_firt_boot(self):
        if self.__th_firt_boot.is_alive():
            self.after(500, self.__update_during_firt_boot)
        else :
            self.__th_firt_boot = th.Thread()
            self.__back_widget.grid(row=2, column=0, sticky="", pady=5)


    def __check_voice_model(self):
        if not self.__voice.check_voice_model():
            showerror("Error","Le model de voix ne sont pas disponible")

    def __updating_during_check_voice_model(self):
        if self.__th_voice.is_alive():
            self.after(1000,self.__updating_during_check_voice_model)
        else :
            self.__voice.load_voice_model()
            self.__back_widget.grid(row=2, column=0, sticky="", pady=5)

    def __send_assistant(self):
        text = self.__back_widget.get_text_entry()
        if text != "":
            label_user(self.__assistant_out,text).view()
            text_lower = text.lower()
            if "parametre" in text_lower or "settings" in text_lower:
                self.__open_setting()
                return
            elif "mute" in text_lower :
                self.__action_mute()
                return
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
            nb_sortie = self.__assistant_six.getValeurSortie()

            self.__treatment_out_assistant(nb_sortie,text)

        # STOP ASSISTANT
    def __on_close(self):
        if not self.__mute_enable :
            if askyesno("Atention", "Voulez-vous vraiment fermer Six"):
                self.title(self.__nameSoft)
                self.__gazelleUI.clearAllFrame()
                self.update()

                self.__beginning_sequence_stop()
        else :
            self.__action_mute()
            self.update()
            self.__on_close()

    def __stop_assistant(self):
        self.__six_speaking = True
        self.__on_close()

    def __beginning_sequence_stop(self):
        self.__six_speaking = True
        texte = self.__assistant_six.shutdown()

        label_assistant(self.__assistant_out,texte).view()

        self.__th_speak_stop = th.Thread(target=self.__voice.speak, args=(texte,))

        self.__th_speak_stop.start()

        self.__update_durring_stopping_speak()

    def __update_durring_stopping_speak(self):
        if self.__th_speak_stop.is_alive():
            self.update()
            self.after(100,self.__update_durring_stopping_speak)
        else :

            if self.__objOS.osWindows():
                os.kill(os.getpid(), signal.SIGINT)
            elif self.__objOS.osLinux() or self.__objOS.osMac():
                os.kill(os.getpid(), signal.SIGKILL)


    def __treatment_out_assistant(self,var:int,text:str):
        if var == 15:
            self.__stop_assistant()
        else :
            label_assistant(self.__assistant_out, text).view()
            self.__back_widget.grid(row=2, column=0, sticky="", pady=5)
            self.__th_speak = th.Thread(target=self.__voice.speak, args=(text,))
            self.__th_speak.start()
            self.__update_during_speak()

        self.__information_widget.update_state(tableur=self.__assistant_six.getTableur(),
                                               doc=self.__assistant_six.getWord(),
                                               projet=self.__assistant_six.getProject())

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

    def __change_voice(self):
        voice_model = self.__conf_frame.get_value_voice_menu()
        if self.__voice.set_voice_model(voice_model):
            if self.__voice.load_voice_model():
                showinfo("Info","Le model de voix a été changé avec succès")
            else :
                showerror("Error","Le model de voix ne sont pas disponible")
        else :
            showerror("Error","Le model ne sont pas disponible")

    def __quit_setting(self):
        self.__gazelleUI.clearAllFrame()
        self.__main_frame.grid(row=0, column=0, sticky="nsew")
        self.update_idletasks()
        self.update()
        text = self.__language.getPhQuitSetting()
        label_assistant(self.__assistant_out, text).view()
        self.__th_speak = th.Thread(target=self.__voice.speak, args=(text,))
        self.__th_speak.start()
        self.__update_during_speak()

    def __about(self):
        windows_about(nameSoft=self.__nameSoft,
                      iconFile=self.__emplacementIcon,
                      version=self.__version,
                      copyright="Copyright Arrera Software by Baptiste P 2023-2026",
                      linkSource="https://github.com/Arrera-Software/Six",
                      linkWeb="https://arrera-software.fr/")