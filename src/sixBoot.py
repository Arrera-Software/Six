from lynx.arreraLynx import*
from librairy.dectectionOS import*
from src.SixGUI import*
import os
import shutil

class SixBoot :
    def __init__(self):
        # Ouverture JSON
        json = jsonWork("FileJSON/configUser.json")

        # Declaration des var
        self.__sortieLynx = False
        self.__firstStart = False
        self.__os = OS()

        if (self.__os.osWindows() == True):
            # Verification de la configuration de l'assistant
            if ((json.lectureJSON("user") == "") and
                    (json.lectureJSON("genre") == "")):
                self.__firstStart = True
            else :
                self.__firstStart = False
            del json
        elif (self.__os.osLinux() == True):
            self.__destUser = os.path.expanduser("~/.config/six/configUser.json")
            if not os.path.exists(self.__destUser):
                os.makedirs(os.path.dirname(self.__destUser), exist_ok=True)
                shutil.copyfile("FileJSON/configUser.json",
                                self.__destUser)
                self.__firstStart = True
            else :
                self.__firstStart = False


    def active(self):
        if (self.__firstStart):
            lynx = ArreraLynx("FileJSON/configLynx.json",
                              "FileJSON/configUser.json",
                              "FileJSON/configNeuron.json")
            lynx.active()
            self.__sortieLynx = lynx.confiCreate()
        else :
            self.__sortieLynx = True

        self.__boot()


    def __boot(self):
        if (self.__sortieLynx == False):
            arrTk = CArreraTK()
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
        elif (self.__os.osWindows() == True):
            assistant = SixGUI("asset/icon/",
                               "icon",
                               "FileJSON/sixConfig.json",
                               "FileJSON/configUser.json",
                               "FileJSON/configNeuron.json",
                               "FileJSON/configSetting.json")

            assistant.active(self.__firstStart)
        elif (self.__os.osLinux() == True):
            assistant = SixGUI("asset/icon/",
                               "icon",
                               "FileJSON/sixConfig.json",
                               "~/.config/six/configUser.json",
                               "FileJSON/configNeuron.json",
                               "FileJSON/configSetting.json")

            assistant.active(self.__firstStart)

    def __restartConf(self,windows:ctk.CTk):
        windows.destroy()
        self.active()