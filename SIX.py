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
        self.objetGestion = SIXGestion(sixConfig)
        self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.sixTK = sixTk(self.objetGestion)
        self.mainTK = SixTKMain(self.objetGestion)
        self.compteurNothing = 0
        #mise en place du theme
        self.objetGestion.setTheme()
        #varriable
        self.etatInternet = self.objetGestion.getEtatInternet()
        self.arreter_boucle = False
        self.varSix = 0
        #source six 
        self.srcSIX = SIXsrc(sixConfig)
        #theard Assistant 
        
    
    def bootAssistant(self):
        self.mainTK.acticeWindows()
        textBoot = self.arreraAssistant.boot()
        self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(textBoot))
        self.srcSIX.speak(textBoot)
        self.theardBoucle = th.Thread(target=self._assistant)
        self.theardBoucle.start()
        self.mainTK.bootInterface()
    
    def quitAssistant(self):
        os.kill(os.getpid(), signal.SIGINT)
        

    def _assistant(self):
        while (self.mainTK.flagBoucle.is_set() ):
            statement = self.srcSIX.micro()
            if ("mute" in statement) or (self.compteurNothing>=MAXNOTING):
                if (self.compteurNothing==MAXNOTING):
                    texte = "Je me met en pause appeler moi si vous avez besoin de moi"
                    self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(texte))
                    self.srcSIX.speak(texte)
                else :
                    texte =  "Ok je vous laisse tranquille"
                    self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(texte))
                    self.srcSIX.speak(texte)
                self.varSix = self.sixTK.muteSix()
                if (self.varSix ==15):
                    texte = "Au revoir"
                    self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(texte))
                    self.srcSIX.speak(texte)
                else :
                    texte = "Je vous ecoute monsieur"
                    self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(texte))
                    self.srcSIX.speak(texte)
                self.compteurNothing = 0
            else :
                if (statement=="nothing"):
                    self.compteurNothing = self.compteurNothing + 1
                else :
                    self.varSix,texte = self.arreraAssistant.neuron(statement)
                    if (self.varSix==15):
                        self.mainTK.windows.after(0,lambda :self.mainTK.viewParoleGUI(texte))
                        self.srcSIX.speak(texte)
                        self.mainTK.flagBoucle.clear()  
                    else :                  
                        if self.varSix == 0 and "parametre" in statement :
                            texte = "Ok je vous ouvre les parametre"
                            self.sixTK.activePara()
                            self.mainTK.windows.after(0,lambda :self.mainTK.viewParole(texte))
                            self.srcSIX.speak(texte)
                            self.arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                            texte = "Les modification on bien été pris en compte"
                            self.mainTK.windows.after(0,lambda :self.mainTK.viewParole(texte))
                            self.srcSIX.speak(texte)
                            texte = "Ok je vous ouvre les parametre"
                            self.mainTK.windows.after(0,lambda :self.mainTK.viewParole(texte))
                            self.srcSIX.speak(texte)
                        else :
                            self.mainTK.viewParoleGUI(texte)
                            self.srcSIX.speak(texte)
                            self.compteurNothing = 0
        self.mainTK.windows.destroy()