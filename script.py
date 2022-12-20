from setting.setting import*
from software.YoutubeDownlaod import *

rep = int(input("Outil debugage:\n1.Parametre\n2.Youtube download\n0.Quitter\n$"))

match rep :
    case 1 :
      Setting()
    case 2 :
      YoutubeDownload()
    case other:
        print("sa correspont pas")
