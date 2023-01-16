from setting.setting import*
from software.YoutubeDownlaod import *
from objet.Calcule.calcule import *
from objet.Horloge.AppHorloge import*
from src.varInterface import*

rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n3.Calcule\n4.Application Horloge\n0.Quitter\n$ "))

match rep :
    case 1 :
      Setting()
    case 2 :
      YoutubeDownload()
    case 3 :
      Calcule("#3c0f14","white","Six : Calcule")
    case 4 :
      AppHorloge("white","black","Horloge","Acceuil")
    case other:
        print("sa correspont pas")
