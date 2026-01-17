from brain.brain import ABrain,confNeuron
from lynx_gui.arrera_lynx import arrera_lynx
from src.SixGUI import*

THEME_FILE = "asset/theme/theme_gris.json"

class SixBoot :
    def __init__(self):
        # Init de la conf
        self.__assistant_conf = confNeuron(
            name="Arrera SIX",
            lang="fr",
            asset="asset/",
            icon="asset/linux/icon.png",
            assistant_color="white",
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

        # Demarage du reseau de neuron
        self.__assistant = ABrain(self.__assistant_conf)
        self.__gestionnaire = self.__assistant.getGestionnaire()

        # Var
        self.__firt_boot = self.__gestionnaire.getUserConf().getFirstRun()

    def active(self):
        if self.__firt_boot:
            arrera_lynx(self.__gestionnaire,
                        "json_conf/configLynx.json",
                        THEME_FILE)
        self.__boot()


    def __boot(self):
        arrTk = CArreraTK()
        self.__checkUpdate(arrTk)
        if not self.__sortieLynx:
            screen = arrTk.aTK(title="Arrera Six",resizable=False,width=500,height=350)
            imgCavas = arrTk.createArreraBackgroudImage(screen,
                                                        imageDark="asset/IMGinterface/dark/NoConfig.png",
                                                        imageLight="asset/IMGinterface/white/NoConfig.png",
                                                        width=500,height=350)
            labeltext = arrTk.createLabel(screen,
                                          text="Désoler mais vous avez pas configuer l'assistant correctement",
                                          ppolice="Arial",ptaille=20,
                                          pstyle="bold",bg="#2b3ceb",
                                          fg="white",pwraplength=300,
                                          justify="left")
            btnConf = arrTk.createButton(screen,text="Configurer",ppolice="Arial",ptaille=20,
                                          pstyle="bold",command=lambda:self.__restartConf(screen))
            imgCavas.pack()
            labeltext.place(x=190,y=40)
            arrTk.placeBottomCenter(btnConf)
            arrTk.view()
        else :
            assistant = SixGUI("asset/icon/",
                               "icon",
                               self.__sixConf.getSixSettingPath(),
                               resource_path("FileJSON/configNeuron.json"),
                               resource_path("FileJSON/configSetting.json"),
                               self.__demonTiger.getVersionSoft())
            assistant.active(self.__firstStart)

    def __restartConf(self,windows:ctk.CTk):
        windows.destroy()
        self.active()

    def __checkUpdate(self,arrTk:CArreraTK):
        if self.__demonTiger.checkUpdate():
            screen = arrTk.aTK(title="Arrera Six",resizable=False,width=500,height=350)
            imgCavas = arrTk.createArreraBackgroudImage(screen,
                                                        imageDark="asset/IMGinterface/dark/MAJ.png",
                                                        imageLight="asset/IMGinterface/white/MAJ.png",
                                                        width=500,height=350)
            labeltext = arrTk.createLabel(screen,
                                          text="Une mise à jour d'ARRERA SIX est disponible. Installez-la pour bénéficier des dernières fonctionnalités.",
                                          ppolice="Arial",ptaille=20,
                                          pstyle="bold",bg="#2b3ceb",
                                          fg="white",pwraplength=250,
                                          justify="left")

            btnUpdate = arrTk.createButton(screen,text="Mettre a jour",ppolice="Arial",ptaille=20,
                                         pstyle="bold",
                                         command=lambda :
                                         wb.open("https://www.github.com/Arrera-Software/Six/releases"))

            btnContinuer = arrTk.createButton(screen,text="Me rappeler plus tart",ppolice="Arial",ptaille=20,
                                         pstyle="bold",
                                         command=lambda : screen.destroy())

            imgCavas.pack()
            labeltext.place(x=190,y=40)
            arrTk.placeBottomLeft(btnUpdate)
            arrTk.placeBottomRight(btnContinuer)
            arrTk.view()