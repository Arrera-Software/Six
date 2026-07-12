from brain.brain import ABrain,confNeuron
from lynx_gui.arrera_lynx import arrera_lynx
from src.SixChatGui import six_gui_chat
from config.tiger_demon import tiger_demon
from librairy.arrera_tk import *


THEME_FILE = "asset/theme/theme_blanc_gris.json"

VERSION = "dev"

class six_chat:
    def __init__(self):
        # Init de la conf
        self.__assistant_conf = confNeuron(
            name="Arrera SIX",
            lang="fr",
            asset="asset/",
            icon="asset/icon/linux/icon.png",
            assistant_color="#0b31f4",
            assistant_texte_color="black",
            bute="Assistant personnel dédié à la productivité, la recherche et l'automatisation des tâches.",
            createur="Baptiste P",
            listFonction=["Ouvrir une application",
                          "Aider aux recherches sur Internet",
                          "Donner la météo",
                          "Faire un résumé des actualités",
                          "Aider à organiser son travail",
                          "Donner l'heure",
                          "Créer des projets",
                          "Éditer des fichiers Word",
                          "Éditer des tableurs"],
            moteurderecherche="google",
            etatService=1,
            etatTime=1,
            etatOpen=1,
            etatSearch=1,
            etatChatbot=1,
            etatApi=1,
            etatCodehelp=0,
            etatWork=1,
            etatSocket=1,
            lienDoc="https://arrera-software.fr/docSix",
            fichierLangue="language/",  # Path to language files
            fichierKeyword="keyword/",  # Path to keyword files
            voiceAssistant=True
        )

        # Demon de MAJ
        self.__demon = tiger_demon("six", VERSION)

    def active(self):
        assistant = six_gui_chat(iconFolder="asset/icon/",
                                 iconName="icon",
                                 conf=self.__assistant_conf,
                                 theme_file=THEME_FILE,
                                 version=self.__demon.get_local_version())
        assistant.active(self.__demon.checkUpdate())

