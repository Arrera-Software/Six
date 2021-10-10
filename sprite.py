from gtts import gTTS
from io import BytesIO
from tkinter import*
def reponse():
    print("cc")
#creation fenetre + mise en place de parametre de la fenetre
screen=Tk()
screen.maxsize("500","500")
screen.minsize("500","500")
screen.title("SIX")
#importation d'une icon
screen.iconphoto(False,PhotoImage(file='icon.png'))
#definition de color de la fenetre et importation du logo
screen.config(bg="black")
logo = PhotoImage(file='logo.png')
label_image=Label(screen,image=logo,bg="black").pack()
#Zone de text et bouton valider
input= Text(screen, height= 1,width=100).pack(side = BOTTOM)
valider = Button(screen,height=1,width=100,text="Envoyer",bg="green").pack(side = BOTTOM)

screen.mainloop()