from librairy.travailJSON import *
from pathlib import Path
from librairy.dectectionOS import *

BASECONF = {"theme": "white",
            "soundMicro": "1",
            "fileMicro": "asset/Sound/bootMicro.mp3",
            "listWord": []}

class SixConf:
    def __init__(self):
        self.__osDect = OS()
        self.__firstRun = False
        # Mise en place du chemin du fichier de configuration utilisateur
        if self.__osDect.osLinux() or self.__osDect.osMac():
            home = Path.home()
            self.__sixSettingPath = str(home) + "/.config/assistant/six/six-config.json"
        elif self.__osDect.osWindows():
            home = Path.home() / "AppData" / "Roaming"
            self.__sixSettingPath = str(home) + "/assistant/six/six-config.json"
        else :
            self.__sixSettingPath = None


        if not Path(self.__sixSettingPath).is_file():
            path = Path(self.__sixSettingPath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as f:
                json.dump(BASECONF, f, ensure_ascii=False, indent=2)

    def getSixSettingPath(self):
        return self.__sixSettingPath