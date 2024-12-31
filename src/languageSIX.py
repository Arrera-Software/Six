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

