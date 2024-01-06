from pygame.locals import *
from ObjetsNetwork.arreraNeuron import*
from src.srcSix import *
from src.SIXGestion import*
from src.SixTK import *
from arreraLynx.arreraLynx import*
import threading as th
import os
import signal
MAXNOTING = 5 
class AssistantSIX :
    def __init__(self):
        #objet
        sixConfig = jsonWork("sixConfig.json")
        self.__objetGestion = SIXGestion(sixConfig)
        self.__sixTK = sixTk(self.__objetGestion)
        self.__compteurNothing = 0
        #mise en place du theme
        self.__objetGestion.setTheme()
        #varriable
        self.__etatInternet = self.__objetGestion.getEtatInternet()
        self.__varSix = 0
        #source six 
        self.__srcSIX = SIXsrc(sixConfig)

    def __onClose(self):
        if (messagebox.askyesno("Atention","Voulez-vous vraiment fermer Six")):
            self.__mainTK.flagBoucle.clear() 
            self.quit()
    
    def __bootAssistant(self):
        self.__mainTK = SixTKMain(self.__objetGestion)
        self.__arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")  
        self.__mainTK.acticeWindows()
        if self.__etatInternet == True :
            self.theardBoucle = th.Thread(target=self.__assistant)
            self.theardBoucle.start()
            self.__mainTK.windows.protocol("WM_DELETE_WINDOW",self.__onClose) 
            self.__mainTK.bootInterface()
        else :
            self.__mainTK.noConnectionInterface()
            self.__mainTK.bootInterface()

        
    def boot(self):
        fileUser = jsonWork("fileUser/configUser.json")
        if not fileUser.lectureJSON("user") and not fileUser.lectureJSON("genre") :
            screen = Tk()
            arreraLynx = ArreraLynx(screen,jsonWork("arreraLynx/configLynx.json"),jsonWork("FileUser/configUser.json"),jsonWork("configNeuron.json"))
            arreraLynx.active()
            screen.mainloop()
            sortieLynx = arreraLynx.confiCreate()
            if sortieLynx == False :
                messagebox.showwarning("La configuration mauvaise","Vous avez pas entre votre nom et genre dans l'outil de configuration")
            else :
                self.__bootAssistant()
        else :
            self.__bootAssistant()
    
    def quit(self):
        os.kill(os.getpid(), signal.SIGINT)
        

    def __assistant(self):
        self.__mainTK.sequenceBoot(self.__srcSIX,self.__arreraAssistant.boot())
        while (self.__mainTK.flagBoucle.is_set() ):
            self.__mainTK.guiNoParole()
            statement = self.__mainTK.guiMicro(self.__srcSIX)
            if ("mute" in statement)or("silence" in statement) or (self.__compteurNothing>=MAXNOTING):
                if (self.__compteurNothing==MAXNOTING):
                    texte = "Je me met en pause appeler moi si vous avez besoin de moi"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(1,texte))
                    self.__srcSIX.speak(texte)
                else :
                    texte =  "Ok je vous laisse tranquille"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(1,texte))
                    self.__srcSIX.speak(texte)
                self.__mainTK.activeMute()
                self.__varSix = self.__sixTK.muteSix()
                if (self.__varSix ==15):
                    self.__mainTK.sequenceArret(self.__srcSIX,"Au revoir")
                    self.__mainTK.flagBoucle.clear() 
                else :
                    texte = "Je vous ecoute monsieur"
                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(0,texte))
                    self.__srcSIX.speak(texte)
                self.__compteurNothing = 0
            else :
                if (statement=="nothing"):
                    self.__compteurNothing = self.__compteurNothing + 1
                else :
                    self.__varSix,listOut = self.__arreraAssistant.neuron(statement)
                    if self.__varSix == 12 or self.__varSix ==  11 :
                        self.__mainTK.vueActu(listOut,self.__varSix)
                    else :
                        if self.__varSix ==  3 :
                            self.__mainTK.vueActu(listOut,self.__varSix)
                        else :
                            if (self.__varSix==15):
                                self.__mainTK.sequenceArret(self.__srcSIX,self.__arreraAssistant.transformeListSTR(listOut))
                                self.__mainTK.flagBoucle.clear() 
                                self.__compteurNothing = 0
                            else : 
                                if (self.__varSix == 0) :             
                                    if ("parametre" in statement) :
                                        texte = "Ok je vous ouvre les parametre"
                                        self.__mainTK.viewParoleGUI(1,texte)
                                        self.__srcSIX.speak(texte)
                                        self.__mainTK.paraOpen()
                                        self.__sixTK.activePara()
                                        self.__arreraAssistant = ArreraNetwork("fileUser/configUser.json","configNeuron.json","listFete.json")
                                        self.__arreraAssistant.setOld("parametre","open parametre")
                                        self.__mainTK.setTheme()
                                        texte = "Les modification on bien été pris en compte"
                                        self.__mainTK.viewParoleGUI(1,texte)
                                        self.__srcSIX.speak(texte)
                                        self.__arreraAssistant.setOld("parametre","parametre")
                                        self.__compteurNothing = 0
                                    else :
                                        if ("codehelp"in statement ):
                                            text ="Je suis desoler, je n'est pas la fonctioanilites CodeHelp."
                                            self.__mainTK.viewParoleGUI(1,texte)
                                            self.__srcSIX.speak(text)
                                            self.__compteurNothing = 0
                                        else :
                                            if ("aide" in statement ) or ("tu peux faire quoi" in statement ) or ("ouvre wiki" in statement):
                                                texte = "Ok je vous ouvre le wiki, je me mute pour vous laisser tanquille" 
                                                self.__mainTK.viewParoleGUI(1,texte)
                                                self.__srcSIX.speak(texte)
                                                webbrowser.open("https://github.com/Arrera-Software/Six/wiki")
                                                self.__mainTK.activeMute()
                                                self.__varSix = self.__sixTK.muteSix()
                                                if (self.__varSix ==15):
                                                    self.__mainTK.sequenceArret(self.__srcSIX,"Au revoir")
                                                    self.__mainTK.flagBoucle.clear() 
                                                else :
                                                    texte = "J'espere que le wiki vous aiderra"
                                                    self.__mainTK.windows.after(0,lambda : self.__mainTK.viewParoleGUI(0,texte))
                                                    self.__srcSIX.speak(texte)

                                            texte = self.__arreraAssistant.transformeListSTR(listOut)
                                            self.__mainTK.viewParoleGUI(1,texte)
                                            self.__srcSIX.speak(texte)
                                            self.__compteurNothing = 0
                                else :
                                    texte = self.__arreraAssistant.transformeListSTR(listOut)
                                    self.__mainTK.viewParoleGUI(1,texte)
                                    self.__srcSIX.speak(texte)
                                    self.__compteurNothing = 0
        self.__mainTK.destroyWindows()