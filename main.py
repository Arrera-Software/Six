#fichier de l'assistant
from sys import displayhook
from gtts import gTTS
from io import BytesIO
from tkinter import*
from playsound import playsound
from requette import*
from navigateur import*
from application import*
#creation fenetre
screen=Tk()
#declaration de la zone de texte pour prendre les requette 
input= Entry(screen,width=100)
#fontion pour traiter les requette de l'uttilisateur
def var():
  requette=input.get()
  if (requette == "bonjour"):
    phrase1()
  if (requette == "salut"):
    phrase1Bis()
  if (requette == "ouvre opera"):
    phrase3()
    ouvertureDUCKDUCKGO()
  if (requette == "ouvre notion"):
    phrase4()
    ouvertureNOTION()
  if (requette == "ouvre youtube music"):
    phrase4bis()
    ouvertureYM()
  if (requette == "ouvre youtube"):
    phrase4bisbis()
    ouvertureY()
  if (requette == "ouvre l'explorateur de fichier"):
    phrase5()
    explorateurFichier()
  if (requette == "ouvre libreoffice"):
    phrase6()
    libreOffcie()
  if (requette == "ouvre visual studio code"):
    phrase7()
    code()
  if (requette == "ouvre discord"):
    phrase8()
    discord()
#mise en place de parametre de la fenetre
screen.maxsize("500","500")
screen.minsize("500","500")
screen.title("SIX")
#importation d'une icon
screen.iconphoto(False,PhotoImage(file='icon.png'))
#definition de color de la fenetre et importation du logo
screen.config(bg="black")
logo = PhotoImage(file='logo.png')
label_image=Label(screen,image=logo,bg="black").pack()
#afichage zone de text et bouton valider
valider = Button(screen,height=1,width=100,text="Envoyer",bg="green",command=var).pack(side = BOTTOM)
input.pack(side = BOTTOM)
screen.mainloop()