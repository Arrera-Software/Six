from lynx.arreraLynx import*
from src.SixGUI import*

json = jsonWork("FileJSON/configUser.json")
sortieLynx = False

name = json.lectureJSON("user")
genre = json.lectureJSON("genre")
del json

if ( (name == "") and (genre == "")):
    showwarning("Arrera Six","Configurer votre assistant")
    windows = Tk()
    lynx = ArreraLynx(windows,
                    jsonWork("FileJSON/configLynx.json"),
                    jsonWork("FileJSON/configUser.json"),
                    jsonWork("FileJSON/configNeuron.json"))
    
    lynx.active()
    windows.mainloop()
    sortieLynx = lynx.confiCreate()
else :
    sortieLynx = True


if (sortieLynx==False):
    showerror("Six","L'assistant n'est pas configurer")
else :
    assistant = SixGUI("asset/icon/",
                       "icon",
                       "FileJSON/sixConfig.json",
                       "FileJSON/configUser.json",
                       "FileJSON/configNeuron.json",
                       "FileJSON/configSetting.json")

    assistant.active()