from librairy.travailJSON import *

class CLanguageSIX :
    def __init__(self,fileLanguage:str):
        self.language = jsonWork(fileLanguage)

    def getPhQuitSetting(self):
        return self.language.lectureJSON("phQuitSetting")

    def getPhQuitActu(self):
        return self.language.lectureJSON("phQuitActu")

    def getPhActiveMute(self):
        return self.language.lectureJSON("phActiveMute")

    def getPhQuitMute(self):
        return self.language.lectureJSON("phQuitMute")

    def getphErreurResumer(self):
        return self.language.lectureJSON("phErreurResumer")

    def getPhOpenResumerActu(self):
        return self.language.lectureJSON("phOpenResumerActu")

    def getPhOpenActu(self):
        return self.language.lectureJSON("phOpenActu")

    def getPhErreurActu(self):
        return self.language.lectureJSON("phErreurActu")

    def getPhReadDocument(self):
        return self.language.lectureJSON("phReadDocument")

    def getPhReadTableur(self):
        return self.language.lectureJSON("phReadTableur")

    def getPhOpenResumerAgendaTache(self):
        return self.language.lectureJSON("phOpenResumerAgendaTache")

    def getPhOpenResumerAll(self):
        return self.language.lectureJSON("phOpenResumerAll")

    def getPhErreurResumerAll(self):
        return self.language.lectureJSON("phErreurResumerAll")