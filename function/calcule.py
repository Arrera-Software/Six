from src.voice import*
from src.speechRecognition import*
from tkinter import*
import numpy as np

Color = "#3c0f14"
TextColor = "white"
#theoreme pythagore
def theoemePythagore(nb1,nb2):
    resultat = np.sqrt((np.square(nb1)+np.square(nb2)))
    return str(format(resultat,".6f"))
def ReciproquePythagore(nb1,nb2):
    resultat = int(np.sqrt((np.square(nb1)-np.square(nb2))))
    return str(format(resultat,".6f"))
#nombre complexe 
def adition(nb1,nb2):
    return nb1+nb2
def soustration(nb1,nb2):
    return nb1-nb2
def multiplication(nb1,nb2):
    return nb1*nb2
def division(nb1,nb2):
    return nb1/nb2
#nombre complex
def aditionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
    nb1 = complex(nb1_1,nb1_2)
    nb2 = complex(nb2_1,nb2_2)
    resultat = nb1 + nb2
    return nb1,nb2,resultat
def soustrationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
    nb1 = complex(nb1_1,nb1_2)
    nb2 = complex(nb2_1,nb2_2)
    resultat = nb1 - nb2
    return nb1,nb2,resultat
def multiplicationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
    nb1 = complex(nb1_1,nb1_2)
    nb2 = complex(nb2_1,nb2_2)
    resultat = nb1 * nb2
    return nb1,nb2,resultat
def divisionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
    nb1 = complex(nb1_1,nb1_2)
    nb2 = complex(nb2_1,nb2_2)
    resultat = nb1 / nb2
    return nb1,nb2,resultat

def Calcule():
    screen = Tk()
    calculatriceMenu = Menu(screen,bg=TextColor,fg="black",font=("arial","25"))
    imgPlus = PhotoImage(file="image/btnPlus.png")
    imgMoin = PhotoImage(file="image/btnMoin.png")
    imgDivise = PhotoImage(file="image/btnDivisee.png")
    imgFois = PhotoImage(file="image/btnMultiplier.png")
    screen.title("Six : Calculatrice")
    screen.config(bg=Color)
    screen.maxsize(700,700)
    screen.minsize(700,700)
    def ShowResultat(nb1,nb2,resultat,calc):
        affichage.config(text=str(nb1)+calc+str(nb2)+" = "+str(resultat))
    def ShowResultatTheoreme(resultat):
        affichage.config(text=resultat)
    def plus():
        nb1,nb2 = RecuperationEntry()
        resultat = str(adition(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"+")
    def moin():
        nb1,nb2 = RecuperationEntry()
        resultat = str(soustration(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"-")
    def fois():
        nb1,nb2 = RecuperationEntry()
        resultat = str(multiplication(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"*")
    def diviser():
        nb1,nb2 = RecuperationEntry()
        resultat = str(division(nb1,nb2))
        ShowResultat(nb1,nb2,resultat,"/")
    def AutreCalcule():
        calc = Toplevel()
        calc.title("Six : Calculatrice")
        def tPytagore():
            calc.destroy()
            nb1,nb2 = RecuperationEntry()
            resultat= str(theoemePythagore(nb1,nb2))
            ShowResultatTheoreme(resultat)
        def rPytagore():
            calc.destroy()
            nb1,nb2 = RecuperationEntry()
            resultat= str(ReciproquePythagore(nb1,nb2))
            print(resultat)
            ShowResultatTheoreme(resultat)
        calc.maxsize(700,300)
        calc.minsize(700,300)
        calc.config(bg=Color)
        btnPythagore = Button(calc,text="Théorème de Pythagore",bg="white",fg="black",font=("arial","15"),command=tPytagore)
        btnRPythagore = Button(calc,text="Reciproque de Pythagore",bg="white",fg="black",font=("arial","15"),command=rPytagore)
        btnThales = Button(calc,text="Théorème de Thalès",bg="white",fg="black",font=("arial","15"))
        labelTheoreme = Label(calc,text="Théorème :",font=("arial","20"),bg=Color,fg=TextColor)
        labelAutreCal = Label(calc,text="Autre Calcule :",font=("arial","20"),bg=Color,fg=TextColor)
        labelTheoreme.place(x=0,y=0)
        btnPythagore.place(x=25,y=50)
        btnRPythagore.place(x=433,y=50)
        labelAutreCal.place(x=0,y=130)

    #nombre complex
    def plusNbComplex():
        nb1_1,nb1_2,nb2_1,nb2_2 = RecuperationEntryComplex()
        nb1,nb2,resultat = aditionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        ShowResultat(nb1,nb2,resultat,"+")
    def moinNbComplex():
        nb1_1,nb1_2,nb2_1,nb2_2 = RecuperationEntryComplex()
        nb1,nb2,resultat = soustrationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        ShowResultat(nb1,nb2,resultat,"-")
    def foisNbComplex():
        nb1_1,nb1_2,nb2_1,nb2_2 = RecuperationEntryComplex()
        nb1,nb2,resultat = multiplicationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        ShowResultat(nb1,nb2,resultat,"*")
    def diviserNbComplex():
        nb1_1,nb1_2,nb2_1,nb2_2 = RecuperationEntryComplex()
        nb1,nb2,resultat = divisionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        ShowResultat(nb1,nb2,resultat,"/")
    #widget
    #frame
    main = Frame(screen,bg=Color,width=700,height=700)
    top = Frame(main,bg=Color,width=700,height=175)
    bottom = Frame(main,bg=Color,width=700,height=175)
    mainNbComplex = Frame(screen,bg=Color,width=700,height=700)
    topNbComplex = Frame(mainNbComplex,bg=Color,width=700,height=175)
    bottomNbComplex = Frame(mainNbComplex,bg=Color,width=700,height=175)
    #label
    affichage = Label(screen,text="Affichage résultat",font=("arial","25"),bg=Color,fg=TextColor)
    labeli1 = Label(topNbComplex,text="j",font=("arial","25"),bg=Color,fg=TextColor)
    labeli2 = Label(bottomNbComplex,text="j",font=("arial","25"),bg=Color,fg=TextColor)
    #btn
    btnPlus = Button(screen,image=imgPlus,command=plus)
    btnMoin = Button(screen,image=imgMoin,command=moin)
    btnFois = Button(screen,image=imgFois,command=fois)
    btnDiviser = Button(screen,image=imgDivise,command=diviser)
    btnExit = Button(mainNbComplex,text="Exit",font=("arial","15"),bg="white",fg="black")
    #entry
    entryNombre1 = Entry(top,width=40,font=("arial","15"))
    entryNombre2 = Entry(bottom,width=40,font=("arial","15"))
    entryNombre1NbComplex1 = Entry(topNbComplex,width=15,font=("arial","15"))
    entryNombre1NbComplex2 = Entry(topNbComplex,width=15,font=("arial","15"))
    entryNombre2NbComplex1 = Entry(bottomNbComplex,width=15,font=("arial","15"))
    entryNombre2NbComplex2 = Entry(bottomNbComplex,width=15,font=("arial","15"))
    #affichage
    def exitComplex():
        mainNbComplex.place_forget()
        AffichageMain()
        affichage.config(text="Affichage résultat",font=("arial","25"))
        btnPlus.config(command=plus)
        btnMoin.config(command=moin)
        btnFois.config(command=fois)
        btnDiviser.config(command=diviser)
    def NbComplexe():
        AffichageFrameMainNbComplex()
        main.place_forget()
        affichage.config(text="Cacule\nNombre Complex",font=("arial","15"))
        btnExit.config(command=exitComplex)
        btnPlus.config(command=plusNbComplex)
        btnMoin.config(command=moinNbComplex)
        btnFois.config(command=foisNbComplex)
        btnDiviser.config(command=diviserNbComplex)
        mainNbComplex.place(x=0,y=0)
        AffichageBTNOperateur()
    def AffichageFrameMainNbComplex():
        topNbComplex.place(x=0,y=0)
        bottomNbComplex.place(x=0,y=475)
        entryNombre1NbComplex1.place(x=100,y=100)
        entryNombre1NbComplex2.place(x=400,y=100)
        entryNombre2NbComplex1.place(x=100,y=100)
        entryNombre2NbComplex2.place(x=400,y=100)
        labeli1.place(x=575,y=90)
        labeli2.place(x=575,y=90)
        #entryNombre2NbComplex.place(relx=0.5, rely=0.5, anchor=CENTER)
        btnExit.place(x=600,y=625)
    def AffichageFrameMain():
        top.place(x=0,y=0)
        bottom.place(x=0,y=475)
        entryNombre1.place(relx=0.5, rely=0.5, anchor=CENTER)
        entryNombre2.place(relx=0.5, rely=0.5, anchor=CENTER)
    def AffichageBTNOperateur():
        affichage.place(relx=0.5, rely=0.5, anchor=CENTER)
        btnPlus.place(x=50,y=320)
        btnMoin.place(x=600,y=320)
        btnDiviser.place(x=500,y=320)
        btnFois.place(x=150,y=320)
    def AffichageMain():
        AffichageFrameMain()
        main.place(x=0,y=0)
        AffichageBTNOperateur()
    
    AffichageMain()
    calculatriceMenu.add_command(label="Nombre Complexe",command=NbComplexe)
    calculatriceMenu.add_command(label="Theoreme",command=AutreCalcule)
    #fonction
    def RecuperationEntry():
        nb1 = int(entryNombre1.get())
        nb2 = int(entryNombre2.get())
        entryNombre1.delete(0,END)
        entryNombre2.delete(0,END)
        return nb1 , nb2
    def RecuperationEntryComplex():
        nb1_1 = int(entryNombre1NbComplex1.get())
        nb1_2 = int(entryNombre1NbComplex2.get())
        nb2_1 = int(entryNombre2NbComplex1.get())
        nb2_2 = int(entryNombre2NbComplex2.get())
        entryNombre1NbComplex1.delete(0,END)
        entryNombre1NbComplex2.delete(0,END)
        entryNombre2NbComplex1.delete(0,END)
        entryNombre2NbComplex2.delete(0,END)
        return nb1_1,nb1_2,nb2_1,nb2_2
    screen.config(menu=calculatriceMenu)
    screen.mainloop()
        