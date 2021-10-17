#fichier de l'assistant
from gtts import gTTS
from io import BytesIO
from tkinter import*
import os
#importation variable pour lancer la voix
mp3_fp = BytesIO()
#fontion pour les requette de l'uttilisateur
def reponse():
    requette=input.get()
    if(requette == "bonjour",requette == "Bonjour"):
      open("voix/voix1.mp3")       
#creation fenetre
screen=Tk()
#declaration de la zone de texte pour prendre les requette 
input= Entry(screen,width=100)
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
valider = Button(screen,height=1,width=100,text="Envoyer",bg="green",command=reponse).pack(side = BOTTOM)
input.pack(side = BOTTOM)

screen.mainloop()