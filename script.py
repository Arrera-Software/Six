from setting.setting import*
from software.YoutubeDownload import *
from objet.Calcule.calcule import *
from objet.Horloge.AppHorloge import*
from src.varInterface import*
from function.api import*
from src.varInterface import*
from function.calendar import*
import pygame

rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n3.Calcule\n4.Application Horloge\n5.Actualités description\n6.Calendrier\n7.Fenetre Pygame\n0.Quitter\n$ "))

match rep :
    case 1 :
      Setting()
    case 2 :
      ArreraVideoDownload("#3c0b10","white","#3c0b10","white")
    case 3 :
      Calcule("#3c0f14","white","Six : Calcule")
    case 4 :
      AppHorloge("white","black","Horloge","Acceuil")
    case 5 :
      DescriptionActu()
    case 6 :
      SixCalendar()
    case 7 :
      os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,35)
      pygame.init()
      pygame.display.set_icon(pygame.image.load("image/logo.png"))
      pygame.display.set_caption("Assistant SIX")
      root  = pygame.display.set_mode((rootWidht,rootHeight))
      police = pygame.font.SysFont("arial", 25)
      var = True 
      root.blit(fond, (0, 0))
      pygame.display.update()
      while var:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                var = False
              else :
                if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_a:
                    root.blit(fondParole1, (0, 0))
                    pygame.display.update()
                    time.sleep(5)
                  else :
                    if event.key == pygame.K_z :
                      root.blit(fondFenetre, (0, 0))
                      pygame.display.update()
                      time.sleep(5)
                    else :
                      if event.key == pygame.K_e:
                        root.blit(fondMute, (0, 0))
                        pygame.display.update()
                        time.sleep(5)
                      else :
                        root.blit(fond, (0, 0))
                        pygame.display.update()
                else :
                  root.blit(fond, (0, 0))
                  pygame.display.update()
      
                    
                  
    
      pygame.quit()
    
    case other:
        print("sa correspont pas")