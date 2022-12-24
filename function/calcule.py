from src.voice import*
from src.speechRecognition import*
from tkinter import*
import numpy as np

Color = "#3c0f14"
TextColor = "white"
#theoreme pythagore
def theoemePythagore(nb1,nb2):
    resultat = np.sqrt((np.square(nb1)+np.square(nb2)))
    return resultat
def ReciproquePythagore(nb1,nb2):
    resultat = np.sqrt((np.square(nb1)-np.square(nb2)))
    return resultat

def adtion(nb1,nb2):
    return nb1+nb2
def soustration(nb1,nb2):
    return nb1-nb2
def multiplication(nb1,nb2):
    return nb1*nb2
def division(nb1,nb2):
    return nb1/nb2
def Calcule():
    screen = Tk()
    #calculatriceMenu = Menu(screen,bg=TextColor,fg="black",font=("arial","25"))
    imgPlus = PhotoImage(file="image/btnPlus.png")
    imgMoin = PhotoImage(file="image/btnMoin.png")
    imgDivise = PhotoImage(file="image/btnDivisee.png")
    imgFois = PhotoImage(file="image/btnMultiplier.png")
    screen.title("Six : Calculatrice")
    screen.config(bg=Color)
    screen.maxsize(700,700)
    screen.minsize(700,700)
    top = Frame(screen,bg=Color,width=700,height=175)
    acceuil = Frame(screen,bg=Color,width=700,height=300)
    bottom = Frame(screen,bg=Color,width=700,height=175)
    def ShowResultat(nb1,nb2,resultat,calc):
        affichage.config(text=str(nb1)+calc+str(nb2)+" = "+str(resultat))
    def ShowResultatTheoreme(resultat):
        affichage.config(resultat)
    def plus():
        nb1,nb2 = RecupérationEntry()
        resultat = str(adtion(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"+")
    def moin():
        nb1,nb2 = RecupérationEntry()
        resultat = str(soustration(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"-")
    def fois():
        nb1,nb2 = RecupérationEntry()
        resultat = str(multiplication(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"*")
    def diviser():
        nb1,nb2 = RecupérationEntry()
        resultat = str(division(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"/")
    
    def AutreCalcule():
        calc = Toplevel()
        calc.title("Six : Calculatrice")
        def tPytagore():
            calc.destroy()
            nb1,nb2 = RecupérationEntry()
            resultat= str(theoemePythagore(nb1,nb2))
            ShowResultatTheoreme(resultat)
        def rPytagore():
            calc.destroy()
            nb1,nb2 = RecupérationEntry()
            resultat= str(ReciproquePythagore(nb1,nb2))
            ShowResultatTheoreme(resultat)
        calc.maxsize(700,300)
        calc.minsize(700,300)
        calc.config(bg=Color)
        btnPythagore = Button(calc,text="Théorème de Pythagore",bg="white",fg="black",font=("arial","15"),command=tPytagore)
        btnRPythagore = Button(calc,text="Reciproque de Pythagore",bg="white",fg="black",font=("arial","15"),command=rPytagore)
        btnThales = Button(calc,text="Théorème de Thalès",bg="white",fg="black",font=("arial","15"))
        btnIntegrale = Button(calc,text="intégrales",bg="white",fg="black",font=("arial","15"))
        btnEquationDiférenciel = Button(calc,text="Equation différentielles",bg="white",fg="black",font=("arial","15"))
        btnNombreComplexe = Button(calc,text="Nombre Complexe",bg="white",fg="black",font=("arial","15"))
        labelTheoreme = Label(calc,text="Théorème :",font=("arial","20"),bg=Color,fg=TextColor)
        labelAutreCal = Label(calc,text="Autre Calcule :",font=("arial","20"),bg=Color,fg=TextColor)
        
        labelTheoreme.place(x=0,y=0)
        btnPythagore.place(x=25,y=70)
        btnRPythagore.place(x=475,y=70)
        #labelAutreCal.place(x=0,y=130)
        #btnIntegrale.place(x=25,y=200)
        #btnNombreComplexe.place(x=485,y=200)
        #btnEquationDiférenciel.place(x=200,y=200)
    #widget
    #label
    affichage = Label(screen,text="Affichage résultat",font=("arial","25"),bg=Color,fg=TextColor)
    #btn
    btnPlus = Button(acceuil,image=imgPlus,command=plus)
    btnMoin = Button(acceuil,image=imgMoin,command=moin)
    btnFois = Button(acceuil,image=imgFois,command=fois)
    btnDiviser = Button(acceuil,image=imgDivise,command=diviser)
    #entry
    entryNombre1 = Entry(top,width=40,font=("arial","15"))
    entryNombre2 = Entry(bottom,width=40,font=("arial","15"))
    #affichage
    top.pack(side="top")
    acceuil.place(relx=0.5, rely=0.5, anchor=CENTER)
    bottom.pack(side="bottom")
    entryNombre1.place(relx=0.5, rely=0.5, anchor=CENTER)
    entryNombre2.place(relx=0.5, rely=0.5, anchor=CENTER)
    affichage.place(relx=0.5, rely=0.5, anchor=CENTER)
    btnPlus.place(x=50,y=120)
    btnMoin.place(x=600,y=120)
    btnDiviser.place(x=500,y=120)
    btnFois.place(x=150,y=120)
    #calculatriceMenu.add_command(label="Autre calcule",command=AutreCalcule)
    #fonction
    def RecupérationEntry():
        nb1 = int(entryNombre1.get())
        nb2 = int(entryNombre2.get())
        entryNombre1.delete(0,END)
        entryNombre2.delete(0,END)
        return nb1 , nb2
    #screen.config(menu=calculatriceMenu)
    screen.mainloop()
        