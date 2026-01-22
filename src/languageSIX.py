from librairy.travailJSON import *

class language_six :
    def __init__(self, fileLanguage:str, fileHelp:str,fileFirstBoot:str):
        self.__language = jsonWork(fileLanguage)
        self.__help = jsonWork(fileHelp)
        self.__firstBoot = jsonWork(fileFirstBoot)

    def getPhQuitSetting(self):
        return self.__language.getContentJsonFlag("phQuitSetting")

    def getPhQuitActu(self):
        return self.__language.getContentJsonFlag("phQuitActu")

    def getPhActiveMute(self):
        return self.__language.getContentJsonFlag("phActiveMute")

    def getPhQuitMute(self):
        return self.__language.getContentJsonFlag("phQuitMute")

    def getphErreurResumer(self):
        return self.__language.getContentJsonFlag("phErreurResumer")

    def getPhOpenResumerActu(self):
        return self.__language.getContentJsonFlag("phOpenResumerActu")

    def getPhOpenActu(self):
        return self.__language.getContentJsonFlag("phOpenActu")

    def getPhErreurActu(self):
        return self.__language.getContentJsonFlag("phErreurActu")

    def getPhReadDocument(self):
        return self.__language.getContentJsonFlag("phReadDocument")

    def getPhReadTableur(self):
        return self.__language.getContentJsonFlag("phReadTableur")

    def getPhOpenResumerAgendaTache(self):
        return self.__language.getContentJsonFlag("phOpenResumerAgendaTache")

    def getPhOpenResumerAll(self):
        return self.__language.getContentJsonFlag("phOpenResumerAll")

    def getPhErreurResumerAll(self):
        return self.__language.getContentJsonFlag("phErreurResumerAll")

    def getPhOpenAideTableur(self):
        return self.__language.getContentJsonFlag("phOpenAideTableur")

    def getPhOpenAideWord(self):
        return self.__language.getContentJsonFlag("phOpenAideWord")

    def getPhOpenAideFichier(self):
        return self.__language.getContentJsonFlag("phOpenAideFichier")

    def getPhOpenAideRadio(self):
        return self.__language.getContentJsonFlag("phOpenAideRadio")

    def getPhOpenAideProjet(self):
        return self.__language.getContentJsonFlag("phOpenAideProjet")

    def getPhOpenAideWork(self):
        return self.__language.getContentJsonFlag("phOpenAideWork")

    def getHelpTableur(self):
        return self.__help.getContentJsonFlagList("tableur")

    def getHelpWord(self):
        return self.__help.getContentJsonFlagList("word")

    def getHelpProjet(self):
        return self.__help.getContentJsonFlagList("projet")

    def getPhraseFirstBoot(self, genre:str, name:str, nb:int):
        return self.__firstBoot.getContentJsonFlag(str(nb)).format(genre=genre, lastname=name)
