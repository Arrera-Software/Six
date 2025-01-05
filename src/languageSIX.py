from librairy.travailJSON import *

class CLanguageSIX :
    def __init__(self, fileLanguage:str, fileHelp:str):
        self.__language = jsonWork(fileLanguage)
        self.__help = jsonWork(fileHelp)

    def getPhQuitSetting(self):
        return self.__language.lectureJSON("phQuitSetting")

    def getPhQuitActu(self):
        return self.__language.lectureJSON("phQuitActu")

    def getPhActiveMute(self):
        return self.__language.lectureJSON("phActiveMute")

    def getPhQuitMute(self):
        return self.__language.lectureJSON("phQuitMute")

    def getphErreurResumer(self):
        return self.__language.lectureJSON("phErreurResumer")

    def getPhOpenResumerActu(self):
        return self.__language.lectureJSON("phOpenResumerActu")

    def getPhOpenActu(self):
        return self.__language.lectureJSON("phOpenActu")

    def getPhErreurActu(self):
        return self.__language.lectureJSON("phErreurActu")

    def getPhReadDocument(self):
        return self.__language.lectureJSON("phReadDocument")

    def getPhReadTableur(self):
        return self.__language.lectureJSON("phReadTableur")

    def getPhOpenResumerAgendaTache(self):
        return self.__language.lectureJSON("phOpenResumerAgendaTache")

    def getPhOpenResumerAll(self):
        return self.__language.lectureJSON("phOpenResumerAll")

    def getPhErreurResumerAll(self):
        return self.__language.lectureJSON("phErreurResumerAll")

    def getPhOpenAideTableur(self):
        return self.__language.lectureJSON("phOpenAideTableur")

    def getPhOpenAideWord(self):
        return self.__language.lectureJSON("phOpenAideWord")

    def getPhOpenAideFichier(self):
        return self.__language.lectureJSON("phOpenAideFichier")

    def getPhOpenAideRadio(self):
        return self.__language.lectureJSON("phOpenAideRadio")

    def getPhOpenAideProjet(self):
        return self.__language.lectureJSON("phOpenAideProjet")

    def getPhOpenAideWork(self):
        return self.__language.lectureJSON("phOpenAideWork")

    def getHelpTableur(self):
        return self.__help.lectureJSON("tableur")

    def getHelpWord(self):
        return self.__help.lectureJSON("word")

    def getHelpProjet(self):
        return self.__help.lectureJSON("projet")