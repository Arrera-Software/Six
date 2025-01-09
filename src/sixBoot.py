from lynx.arreraLynx import*
from src.SixGUI import*

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


    def active(self):
        if (self.__firstStart):
            showwarning("Arrera Six","Configurer votre assistant")
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
            showerror("Six","L'assistant n'est pas configurer")
        else :
            assistant = SixGUI("asset/icon/",
                               "icon",
                               "FileJSON/sixConfig.json",
                               "FileJSON/configUser.json",
                               "FileJSON/configNeuron.json",
                               "FileJSON/configSetting.json")
            assistant.active()
