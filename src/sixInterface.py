import os 
import pygame 
import time as t
from src.SIXGestion import*
import re

class SIXInterface:
    def __init__(self,objetGestion:SIXGestion):
        self.rootWidht = 600
        self.rootHeight = 500
        self.objetGestion = objetGestion 
        self.oldRequette = str
        self.nbInterfaceAttent = 0

    def setGUI(self):
        self.mainGUI = self.objetGestion.getGUIMain()
        self.AcceuilGUI = self.objetGestion.getGUIAcceuil()
        self.paroleGUI = [self.objetGestion.getGUIparoleBigSmall(),
                               self.objetGestion.getGUIparoleSmallSmall()] 
        self.attendGUI = self.objetGestion.getGUIAttent()
        self.colorText = self.objetGestion.getGUItextColor()
            
    def initialisationFenetre(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
        pygame.init()
        pygame.display.set_icon(pygame.image.load("asset/logo.png"))
        pygame.display.set_caption("Assistant SIX")
        self.root  = pygame.display.set_mode((self.rootWidht,self.rootHeight),pygame.NOFRAME)
        self.policeTitre = pygame.font.SysFont("arial", 30)
        self.police = pygame.font.SysFont("arial", 25)
        self.root.blit(self.mainGUI.convert(),(0,0))
        self.formatSpeak = pygame.font.SysFont("arial", 20)
        pygame.display.update()

    def quitWindows(self):
        pygame.display.quit()
    
    def interfaceMain(self):
        self.root.blit(self.mainGUI.convert(),(0,0))
        pygame.display.update()
    
    def interfaceBoot(self,text:str):
        texte = text
        self.root.blit(self.AcceuilGUI.convert(),(0,0))
        if self._compteur(texte) >= 4 :
            text1,text2 = self._division(texte,4)
            if self._compteur(text2) >= 4 :
                text2,text3 = self._division(text2,4)
                labelText1 = self.policeTitre.render(text1,1,(self.colorText))
                labelText2 = self.policeTitre.render(text2,1,(self.colorText))
                labelText3 = self.policeTitre.render(text3,1,(self.colorText))
                textRect1 = labelText1.get_rect(center=(600/2 ,240))
                textRect2 = labelText2.get_rect(center=(600/2 ,270))
                textRect3 = labelText3.get_rect(center=(600/2 ,300))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
                self.root.blit(labelText3,textRect3)
            else :
                labelText1 = self.policeTitre.render(text1,1,(self.colorText))
                labelText2 = self.policeTitre.render(text2,1,(self.colorText))
                textRect1 = labelText1.get_rect(center=(600/2 ,240))
                textRect2 = labelText2.get_rect(center=(600/2 ,270))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
        else :
            labelText = self.policeTitre.render(texte,1,(self.colorText))
            textRect = labelText.get_rect(center=(600/2 ,240))
            self.root.blit(labelText,textRect)
        self.speakBig = True
        self.oldSpeak = texte
        pygame.display.update()
        
    def interfaceSpeak(self,texte:str):
        nbMots = self._compteur(texte)
        if nbMots > 6 :
            text1,text2 = self._division(texte,6)
            nbMots = self._compteur(text2)
            if nbMots > 6 :
                guiParole = self.paroleGUI[0] #Big
                self.root.blit(guiParole.convert(),(0,0))
                text2,text3 = self._division(text2,6)
                labelText1 =  self.police.render(text1,1,(self.colorText))
                labelText2 =  self.police.render(text2,1,(self.colorText))
                labelText3 =  self.police.render(text3,1,(self.colorText))
                textRect1 = labelText1.get_rect(topleft=(125,40))
                textRect2 = labelText2.get_rect(topleft=(125,60))
                textRect3 = labelText3.get_rect(topleft=(125,80))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
                self.root.blit(labelText3,textRect3)        
                self._affichageEntre(True)
            else : 
                guiParole = self.paroleGUI[1] #Small
                self.root.blit(guiParole.convert(),(0,0))
                labelText1 =  self.police.render(text1,1,(self.colorText))
                labelText2 =  self.police.render(text2,1,(self.colorText))
                textRect1 = labelText1.get_rect(topleft=(130,90))
                textRect2 = labelText2.get_rect(topleft=(130,110))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
                self._affichageEntre(False)
        else :
            guiParole = self.paroleGUI[1] #Small
            self.root.blit(guiParole.convert(),(0,0))
            labelText =  self.police.render(texte,1,(self.colorText))
            textRect = labelText.get_rect(topleft=(130,90))
            self.root.blit(labelText,textRect)
            self._affichageEntre(False)
        pygame.display.update()

    def interfaceCloseOpenParametre(self,texte:str):
        texte = texte
        self.root.blit(self.AcceuilGUI.convert(),(0,0))
        if self._compteur(texte) >= 4 :
            text1,text2 = self._division(texte,4)
            if self._compteur(text2) >= 4 :
                text2,text3 = self._division(text2,4)
                labelText1 = self.policeTitre.render(text1,1,(self.colorText))
                labelText2 = self.policeTitre.render(text2,1,(self.colorText))
                labelText3 = self.policeTitre.render(text3,1,(self.colorText))
                textRect1 = labelText1.get_rect(center=(600/2 ,240))
                textRect2 = labelText2.get_rect(center=(600/2 ,270))
                textRect3 = labelText3.get_rect(center=(600/2 ,300))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
                self.root.blit(labelText3,textRect3)
            else :
                labelText1 = self.policeTitre.render(text1,1,(self.colorText))
                labelText2 = self.policeTitre.render(text2,1,(self.colorText))
                textRect1 = labelText1.get_rect(center=(600/2 ,240))
                textRect2 = labelText2.get_rect(center=(600/2 ,270))
                self.root.blit(labelText1,textRect1)
                self.root.blit(labelText2,textRect2)
        else :
            labelText = self.policeTitre.render(texte,1,(self.colorText))
            textRect = labelText.get_rect(center=(600/2 ,240))
            self.root.blit(labelText,textRect)
        self.speakBig = True
        self.oldSpeak = texte
        pygame.display.update()
        
    def interfaceAttente(self):
        if self.nbInterfaceAttent == 0 :
            self.root.blit(self.attendGUI[0].convert(),(0,0))
            self.nbInterfaceAttent =+ 1
        else :
            if self.nbInterfaceAttent == 1 :
                self.root.blit(self.attendGUI[1].convert(),(0,0))
                self.nbInterfaceAttent =+ 1
            else :
                if self.nbInterfaceAttent == 2 :
                    self.root.blit(self.attendGUI[2].convert(),(0,0))
                    self.nbInterfaceAttent = 0
                else :
                    self.root.blit(self.attendGUI[0].convert(),(0,0))
                    self.nbInterfaceAttent = 1
        pygame.display.update()

    def interfaceParametre(self):
        self.root.blit(self.parametreGUI.convert(),(0,0))
        pygame.display.update()
      
    def _affichageEntre(self,big:bool):
        texte = self.oldRequette
        if self._compteur(texte) > 6 :
            texte1,texte2 = self._division(texte,6)
            labelRequette1 = self.police.render(texte1,1,(self.colorText))
            labelRequette2 = self.police.render(texte2,1,(self.colorText))
            if big == True :
               requetteRect1 = labelRequette1.get_rect(topleft=(130,360)) 
               requetteRect2 = labelRequette2.get_rect(topleft=(130,380))
               
            else :
                requetteRect1 = labelRequette1.get_rect(topleft=(130,350)) 
                requetteRect2 = labelRequette2.get_rect(topleft=(130,370))
            self.root.blit(labelRequette1,requetteRect1)
            self.root.blit(labelRequette2,requetteRect2)   
        else :
            labelRequette = self.police.render(texte,1,(self.colorText))
            if big == True :
               requetteRect = labelRequette.get_rect(topleft=(130,370))
            else :
                requetteRect = labelRequette.get_rect(topleft=(130,350))
            self.root.blit(labelRequette,requetteRect)
      
    def saveValMicro(self,requette:str):
        self.oldRequette = requette
        
    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))   

    def _sautLigne(texte:str, nbMots:int):
        # Utilise une expression régulière pour diviser le texte en mots
        mots = re.findall(r'\S+\s*', texte)

        lignes = []  # Liste pour stocker les lignes de texte
        ligne_actuelle = []  # Liste pour stocker les mots de la ligne actuelle

        for mot in mots:
            ligne_actuelle.append(mot)
            # Si la ligne actuelle contient plus de mots_par_ligne, commencez une nouvelle ligne
            if len(ligne_actuelle) >= nbMots:
                lignes.append(" ".join(ligne_actuelle))
                ligne_actuelle = []

        # Ajoutez la ligne finale si elle n'est pas vide
        if ligne_actuelle:
            lignes.append(" ".join(ligne_actuelle))

        return "\n".join(lignes)