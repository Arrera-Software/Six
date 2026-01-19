from brain.brain import ABrain,confNeuron
from lynx_gui.arrera_lynx import arrera_lynx
from src.SixGUI import six_gui
from src.version_demon import demon,soft_config
from lib.arrera_tk import *


THEME_FILE = "asset/theme/theme_bleu.json"

SOFT_CONF = soft_config(
    name_soft="six",
    version="I2026-0.00"
)

class six_assistant :
    def __init__(self):
        # Init de la conf
        self.__assistant_conf = confNeuron(
            name="Arrera SIX",
            lang="fr",
            asset="asset/",
            icon="asset/icon/linux/icon.png",
            assistant_color="#e0e0e0",
            assistant_texte_color="black",
            bute="",
            createur="Baptiste P",
            listFonction=[],
            moteurderecherche="google",
            etatService=1,
            etatTime=1,
            etatOpen=1,
            etatSearch=1,
            etatChatbot=1,
            etatApi=1,
            etatCodehelp=0,
            etatWork=1,
            etatSocket=0,
            lienDoc="www.google.com", # TODO : A changer plus tart
            fichierLangue="language/", # Path to language files
            fichierKeyword="keyword/",            # Path to keyword files
            voiceAssistant=True
        )

        # Demon de MAJ
        self.__demon = demon(SOFT_CONF, "https://arrera-software.fr/depots.json")

        # Demarage du reseau de neuron
        self.__assistant = ABrain(self.__assistant_conf)
        self.__gestionnaire = self.__assistant.getGestionnaire()

        # Var
        self.__firt_boot = self.__gestionnaire.getUserConf().getFirstRun()
        self.__state_conf = False

    def active(self):
        if self.__firt_boot:
            l = arrera_lynx(self.__gestionnaire,
                        "json_conf/configLynx.json",
                        THEME_FILE)
            self.__state_conf = l.return_state_lynx()
        else :
            self.__state_conf = True
        self.__boot()


    def __boot(self):
        self.__checkUpdate()
        if not self.__state_conf:
            w = aTk(title="Arrera Six",resizable=False,width=500,height=350,
                         theme_file=THEME_FILE)
            img_cavas = aBackgroundImage(w,
                                        background_dark="asset/IMGinterface/dark/NoConfig.png",
                                        background_light="asset/IMGinterface/white/NoConfig.png",
                                        width=500,height=350)
            label_text = aLabel(w,text="Désoler mais vous avez pas configuer l'assistant correctement",
                               police_size=20,fg_color="#2b3ceb",
                               text_color="white",wraplength=300,justify="left")
            btn_conf = aButton(w,text="Configurer",
                              size=20,command=lambda:self.__restartConf(w))
            img_cavas.pack()
            label_text.place(x=190,y=40)
            btn_conf.placeBottomCenter()
            w.mainloop()
        else :
            assistant = six_gui("asset/icon/",
                                "icon",
                                self.__assistant,
                                THEME_FILE,
                                self.__demon.getVersionSoft())
            assistant.active(self.__firt_boot)

    def __restartConf(self,windows:aTk):
        windows.destroy()
        self.active()

    def __checkUpdate(self):
        if self.__demon.checkUpdate():
            w = aTk(title="Arrera Six",resizable=False,width=500,
                         height=350,theme_file=THEME_FILE)
            img_canvas = aBackgroundImage(w,
                                        background_dark="asset/IMGinterface/dark/MAJ.png",
                                        background_light="asset/IMGinterface/white/MAJ.png",
                                        width=500,height=350)

            label_text = aLabel(w,text="Une mise à jour d'ARRERA SIX est disponible. Installez-la pour bénéficier des dernières fonctionnalités.",
                               police_size=20,fg_color="#2b3ceb",
                               text_color="white",wraplength=250,justify="left")

            btn_update = aButton(w,text="Mettre a jour",size=20,
                                command=lambda :wb.open("https://www.github.com/Arrera-Software/Six/releases"))

            btn_continuer = aButton(w,text="Me rappeler plus tart",size=20,command=lambda : w.destroy())

            img_canvas.pack()
            label_text.place(x=190,y=40)
            btn_update.placeBottomLeft()
            btn_continuer.placeBottomRight()
            w.mainloop()