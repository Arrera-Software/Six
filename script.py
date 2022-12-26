from setting.setting import*
from software.YoutubeDownlaod import *
from function.calcule import *
from function.temps import*

rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n3.Calcule\n4.Minuteur\n5.Chrono\n0.Quitter\n$ "))

match rep :
    case 1 :
      Setting()
    case 2 :
      YoutubeDownload()
    case 3 :
      Calcule()
    case 4 :
      Minuteur()
    case 5 : 
      Chrono()
    case other:
        print("sa correspont pas")
