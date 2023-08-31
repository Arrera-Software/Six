from setting.setting import*
from software.YoutubeDownload import *
from objet.Calcule.calcule import *
from objet.Horloge.AppHorloge import*
from src.varInterface import*
from function.api import*
from function.calendar import*
from function.traduction import*
from function.reading import*
from function.openSofware import ouvertureAide
from debugage.fenetrePygame import *
from main import *

rep = int(input("Outil debugage:\n 1 . Demarer SIX \n 2. Debugage fonction individuelle\n$"))

match rep :
  case 1 :
    Six()
  case 2 : 
    rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n3.Calcule\n4.Application Horloge\n5.Actualités description\n6.Calendrier\n7.Fenetre Pygame\n8.Traduction\n9.Lecture\n10.Ouverture fichier\n0.Quitter\n$ "))
    match rep :
      case 1 :
        Setting()
      case 2 :
        ArreraVideoDownload("#3c0b10","white","#3c0b10","white")
      case 3 :
        Calcule("#3c0f14","white","Six : Calcule")
      case 4 :
        AppHorloge("#3c0f14","white","Six : Horloge","Acceuil")
      case 5 :
        DescriptionActu()
      case 6 :
        SixCalendar()
      case 7 :
        debugPygame()
      case 8 :
        Trad()
      case 9 :
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
        pygame.init()
        pygame.display.set_icon(pygame.image.load("image/logo.png"))
        pygame.display.set_caption("Assistant SIX")
        root  = pygame.display.set_mode((rootWidht,rootHeight))
        police = pygame.font.SysFont("arial", 25)
        var = True 
        root.blit(fond, (0, 0))
        pygame.display.update()
        Reading(root,police)
      case 10 :
        ouvertureAide()
      case other:
          print("sa correspont pas")
  case other :
    print("Ereur")      
    