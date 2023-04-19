import pygame
import os
from src.varInterface import*
import time
def debugPygame():     
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