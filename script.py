from setting.setting import*

rep = int(input("Outil debugage:\n1.Parametre\n0.Quitter\n$"))

match rep :
    case 1 :
      Setting()
    case other:
        print("sa correspont pas")
