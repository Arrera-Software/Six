from lynx.arreraLynx import*
from src.SixGUI import*
from src.CTigerDemon import *

class SixBoot :
    def __init__(self):
        # Ouverture JSON
        json = jsonWork("FileJSON/configUser.json")

        # Declaration des var
        self.__sortieLynx = False

        # Verification de la configuration de l'assistant
        if ((json.lectureJSON("user") == "") and
                (json.lectureJSON("genre") == "")):
            self.__firstStart = True
        else :
            self.__firstStart = False
        del json
        self.__demonTiger = CTigerDemon("six","https://arrera-software.fr/depots.json")


    def active(self):
        if self.__firstStart:
            lynx = ArreraLynx("FileJSON/configLynx.json",
                              "FileJSON/configUser.json",
                              "FileJSON/configNeuron.json")
            lynx.active()
            self.__sortieLynx = lynx.confiCreate()
        else :
            self.__sortieLynx = True

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
                               "FileJSON/sixConfig.json",
                               "FileJSON/configUser.json",
                               "FileJSON/configNeuron.json",
                               "FileJSON/configSetting.json",self.__demonTiger.getVersionSoft())
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