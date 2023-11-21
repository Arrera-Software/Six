from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from src.SIXGestion import*
from src.SixTK import *
import threading as th
import os
import signal
MAXNOTING = 5 
class AssistantSIX :
    def __init__(self):
        #objet
        sixConfig = jsonWork("sixConfig.json")
        self.__objetGestion = SIXGestion(sixConfig)
        self.__arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.__sixTK = sixTk(self.__objetGestion)
        self.__mainTK = SixTKMain(self.__objetGestion)
        self.__compteurNothing = 0
        #mise en place du theme
        self.__objetGestion.setTheme()
        #varriable
        self.__etatInternet = self.__objetGestion.getEtatInternet()
        self.__varSix = 0
        #source six 
        self.__srcSIX = SIXsrc(sixConfig)
        #theard Assistant 
        
    
    def bootAssistant(self):
        if self.__etatInternet == True :
            self.__mainTK.acticeWindows()
            textBoot = self.__arreraAssistant.boot()
            self.__mainTK.windows.after(0,lambda :self.__mainTK.viewBigParole(textBoot))
            self.__srcSIX.speak(textBoot)
            self.theardBoucle = th.Thread(target=self._assistant)
            self.theardBoucle.start()
            self.__mainTK.bootInterface()
    
    def quitAssistant(self):
        os.kill(os.getpid(), signal.SIGINT)
        

    def _assistant(self):
        while (self.__mainTK.flagBoucle.is_set() ):
            statement = self.__srcSIX.micro()
            self.__mainTK.setTextMicro(statement)
            if ("mute" in statement) or (self.__compteurNothing>=MAXNOTING):
                if (self.__compteurNothing==MAXNOTING):
                    texte = "Je me met en pause appeler moi si vous avez besoin de moi"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                    self.__srcSIX.speak(texte)
                else :
                    texte =  "Ok je vous laisse tranquille"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                    self.__srcSIX.speak(texte)
                self.__varSix = self.__sixTK.muteSix()
                if (self.__varSix ==15):
                    texte = "Au revoir"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                    self.__srcSIX.speak(texte)
                    self.__mainTK.flagBoucle.clear() 
                else :
                    texte = "Je vous ecoute monsieur"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                    self.__srcSIX.speak(texte)
                self.__compteurNothing = 0
            else :
                if (statement=="nothing"):
                    self.__compteurNothing = self.__compteurNothing + 1
                else :
                    self.__varSix,texte = self.__arreraAssistant.neuron(statement)
                    if (self.__varSix==15):
                        self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                        self.__srcSIX.speak(texte)
                        self.__mainTK.flagBoucle.clear() 
                    else :                  
                        if (self.__varSix == 0) and ("parametre" in statement) :
                            texte = "Ok je vous ouvre les parametre"
                            self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                            self.__srcSIX.speak(texte)
                            self.__sixTK.activePara()
                            self.__arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                            texte = "Les modification on bien été pris en compte"
                            self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(texte))
                            self.__srcSIX.speak(texte)
                            self.__arreraAssistant.setOld("parametre","parametre")
                        else :
                            self.__mainTK.viewParoleGUI(texte)
                            self.__srcSIX.speak(texte)
                            self.__compteurNothing = 0
        self.__mainTK.destroyWindows()