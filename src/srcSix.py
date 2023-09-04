import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
from src.SIXGestion import*
import threading


class SIXsrc :
    def __init__(self,objetGestionSix:SIXGestion):
        self.rootWidht = 600
        self.rootHeight = 200
        #objet
        self.objetGestionSix = objetGestionSix
        #mise en place du theme
        self.objetGestionSix.setTheme()
        #Creation de la fenetre
        self.rootWindows = Tk()
        self.rootWindows.maxsize(self.rootWidht,self.rootHeight)
        self.rootWindows.minsize(self.rootWidht,self.rootHeight)
        #recuperation des fond
        self.mainFond = self.objetGestionSix.getGUIMain()
        self.listFondParole = [self.objetGestionSix.getGUIparole1(),self.objetGestionSix.getGUIparole2(),self.objetGestionSix.getGUIparole3()]
        self.colorText = self.objetGestionSix.getGUItextColor()
        
    def speak(self,texte):
        tts = gTTS(texte, lang="fr")
        text1,text2 = self.division(texte,8)
        self.rootWindows.update()
        nbMots2 = self.compteur(text2)
        if (nbMots2 > 8):
            text2,text3 = self.division(text2,8)
        else :
            text3 = " "
        tts.save("voc.mp3")
        playsound("voc.mp3")
        os.remove("voc.mp3")
        
    """
    def speakOtherLang(self,langue,texte):
        self.fenetre.blit(self.listFondParole[1].convert(),(0,0))
        pygame.display.update()
        tts = gTTS(texte, lang=str(langue))
        text1,text2 = self.division(texte,8)
        nbMots2 = self.compteur(text2)
        if (nbMots2 > 8):
            text2,text3 = self.division(text2,8)
        else :
            text3 = " "
        tts.save("voc.mp3")
        self.fenetre.blit(self.listFondParole[0].convert(),(0,0))
        pygame.display.update()
        time.sleep(0.5)
        labelAssistant1 = self.formatSpeak.render(text1,1,(self.colorText))
        labelAssistant2 = self.formatSpeak.render(text2,1,(self.colorText))
        labelAssistant3 = self.formatSpeak.render(text3,1,(self.colorText))
        textRect1 = labelAssistant1.get_rect(center=(600/2 ,55))
        textRect2 = labelAssistant2.get_rect(center=(600/2 ,75))
        textRect3 = labelAssistant3.get_rect(center=(600/2 ,95))
        self.fenetre.blit(self.listFondParole[2].convert(),(0,0))
        self.fenetre.blit(labelAssistant1,textRect1)
        self.fenetre.blit(labelAssistant2,textRect2)
        self.fenetre.blit(labelAssistant3,textRect3)
        pygame.display.update()
        playsound("voc.mp3")
        os.remove("voc.mp3")
        self.fenetre.blit(self.mainFond.convert(),(0,0))
        pygame.display.update()
    """
    
    def division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def compteur(self,s):
        mots = s.split()
        return int(len(mots))
    
    def Micro(self):
        r= sr.Recognizer()
        self.rootWindows.update()
        with sr.Microphone() as source:
            audio=r.listen(source)
            self.rootWindows.update()
            try:
                requette=r.recognize_google(audio,language='fr')
                self.rootWindows.update()
            except Exception as e:
                return "None"
            self.rootWindows.update() 
            return requette
    
    