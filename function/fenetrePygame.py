from src.srcSix import *
from src.varInterface import *


class pygameFond :
    
    def __init__(self,root,police,genre):
        self.parole = SIXsrc(root,police) 
        self.fenetre = root
        self.genre = genre
    
    def OuvertureTK(self,texte):
        self.parole.speak(texte)
        time.sleep(0.5)
        self.parole.speak("Je serai indisponible tant que vous fermerez pas la fenetre "+self.genre)
        self.fenetre.blit(fondFenetre.convert(),(0,0))
        pygame.display.update()
    
    def FermetureTK(self):
        self.parole.speak("Ravi de votre retour "+self.genre+" j'espere que l'application vous a été utile")
        self.fenetre.blit(fond.convert(),(0,0))
        pygame.display.update()
    
    