import random
from librairy.travailJSON import *

class language_six :
    def __init__(self, fileLanguage:str,fileFirstBoot:str):
        self.__language = jsonWork(fileLanguage)
        self.__firstBoot = jsonWork(fileFirstBoot)

    def getPhQuitSetting(self):
        return self.__language.getContentJsonFlag("phQuitSetting")

    def getPhActiveMute(self):
        return self.__language.getContentJsonFlag("phActiveMute")

    def getPhQuitMute(self):
        return self.__language.getContentJsonFlag("phQuitMute")

    def phOpenInterface(self, genre:str, name:str):
        l = self.__language.getFlagListJson("phOpenInterface")
        v = random.randint(0,len(l)-1)
        return l[v].format(genre=genre, lastname=name)

    def getPhraseFirstBoot(self, genre:str, name:str, nb:int):
        return self.__firstBoot.getContentJsonFlag(str(nb)).format(genre=genre, lastname=name)
