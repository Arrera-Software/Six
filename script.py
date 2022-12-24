from setting.setting import*
from software.YoutubeDownlaod import *
from function.calcule import *

rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n3.Calcule\n0.Quitter\n$ "))

match rep :
    case 1 :
      Setting()
    case 2 :
      YoutubeDownload()
    case 3 :
      Calcule()
    case other:
        print("sa correspont pas")
