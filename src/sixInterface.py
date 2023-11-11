import os 
import pygame 
import time as t
from src.SIXGestion import*
import re

class SIXInterface:
        
    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))   

    def _sautLigne(texte:str, nbMots:int):
        mots = re.findall(r'\S+\s*', texte)
        lignes = []  
        ligne_actuelle = [] 
        for mot in mots:
            ligne_actuelle.append(mot)
            if len(ligne_actuelle) >= nbMots:
                lignes.append(" ".join(ligne_actuelle))
                ligne_actuelle = []
        if ligne_actuelle:
            lignes.append(" ".join(ligne_actuelle))

        return "\n".join(lignes)