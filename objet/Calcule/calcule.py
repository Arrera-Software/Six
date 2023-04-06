from tkinter import*
from objet.Calcule.calculeBase import*
from objet.Calcule.calculeNombreComplex import*
from objet.Calcule.TheoremePythagore import*

class Calcule:
    def __init__(self,mainColor,mainTextColor,titre):
        self.mainColor = mainColor
        self.mainTextColor = mainTextColor
        self.screen = Tk()
        self.calculatriceMenu = Menu(self.screen,bg=mainTextColor,fg="black",font=("arial","25"))
        self.imgPlus = PhotoImage(file="image/btnPlus.png")
        self.imgMoin = PhotoImage(file="image/btnMoin.png")
        self.imgDivise = PhotoImage(file="image/btnDivisee.png")
        self.imgFois = PhotoImage(file="image/btnMultiplier.png")
        self.screen.title(titre)
        self.screen.config(bg=mainColor)
        self.screen.maxsize(600,500)
        self.screen.minsize(600,500)
        self.main = Frame(self.screen,bg=mainColor,width=600,height=600)
        self.top = Frame(self.main,bg=mainColor,width=600,height=175)
        self.bottom = Frame(self.main,bg=mainColor,width=600,height=175)
        self.mainNbComplex = Frame(self.screen,bg=mainColor,width=700,height=700)
        self.topNbComplex = Frame(self.mainNbComplex,bg=mainColor,width=700,height=175)
        self.bottomNbComplex = Frame(self.mainNbComplex,bg=mainColor,width=700,height=175)
        self.widget(mainColor,mainTextColor)
        self.AffichageMain()
        self.calculatriceMenu = Menu(self.screen,bg=mainTextColor,fg="black",font=("arial","25"))    
        self.calculatriceMenu.add_command(label="Nombre Complexe",command= self.NbComplexe)
        self.calculatriceMenu.add_command(label="Theoreme",command=self.AutreCalcule)
        self.screen.config(menu=self.calculatriceMenu)
        #CalculeBase()
        self.screen.mainloop()
    
    def widget(self,mainColor,mainTextColor):
        #label
        self.labelBienvenu = Label(self.screen,text="Calculatrice",font=("arial","25"),bg=mainColor,fg=mainTextColor)
        self.affichage = Label(self.screen,text="Affichage résultat",font=("arial","15"),bg=mainColor,fg=mainTextColor)
        self.labeli1 = Label(self.topNbComplex,text="j",font=("arial","25"),bg=mainColor,fg=mainTextColor)
        self.labeli2 = Label(self.bottomNbComplex,text="j",font=("arial","25"),bg=mainColor,fg=mainTextColor)
        #btn
        self.btnPlus = Button(self.screen,image=self.imgPlus,command=self.plus)
        self.btnMoin = Button(self.screen,image=self.imgMoin,command=self.moin)
        self.btnFois = Button(self.screen,image=self.imgFois,command=self.fois)
        self.btnDiviser = Button(self.screen,image=self.imgDivise,command=self.diviser)
        self.btnExit = Button(self.screen,text="Exit",font=("arial","20"),bg="white",fg="black")
        #entry
        self.entryNombre1 = Entry(self.top,width=30,font=("arial","15"),relief=SOLID)
        self.entryNombre2 = Entry(self.bottom,width=30,font=("arial","15"),relief=SOLID)
        self.entryNombre1NbComplex1 = Entry(self.topNbComplex,width=15,font=("arial","15"),relief=SOLID)
        self.entryNombre1NbComplex2 = Entry(self.topNbComplex,width=15,font=("arial","15"),relief=SOLID)
        self.entryNombre2NbComplex1 = Entry(self.bottomNbComplex,width=15,font=("arial","15"),relief=SOLID)
        self.entryNombre2NbComplex2 = Entry(self.bottomNbComplex,width=15,font=("arial","15"),relief=SOLID)
    
    def ShowResultatTheoreme(self,resultat):
        self.affichage.config(text=resultat)
      
    def AutreCalcule(self):
        self.calc = Toplevel()
        self.calc.title("Six : Calculatrice")
        def tPytagore():
            self.calc.destroy()
            nb1,nb2 = self.RecuperationEntry()
            resultat= str(Pythagore.theoemePythagore(nb1,nb2))
            self.ShowResultatTheoreme(resultat)
        def rPytagore():
            self.calc.destroy()
            nb1,nb2 = self.RecuperationEntry()
            resultat= str(Pythagore.ReciproquePythagore(nb1,nb2))
            print(resultat)
            self.ShowResultatTheoreme(resultat)
        self.calc.maxsize(700,300)
        self.calc.minsize(700,300)
        self.calc.config(bg=self.mainColor)
        btnPythagore = Button(self.calc,text="Théorème de Pythagore",bg="white",fg="black",font=("arial","15"),command=tPytagore)
        btnRPythagore = Button(self.calc,text="Reciproque de Pythagore",bg="white",fg="black",font=("arial","15"),command=rPytagore)
        btnThales = Button(self.calc,text="Théorème de Thalès",bg="white",fg="black",font=("arial","15"))
        labelTheoreme = Label(self.calc,text="Théorème :",font=("arial","20"),bg=self.mainColor,fg=self.mainTextColor)
        labelAutreCal = Label(self.calc,text="Autre Calcule :",font=("arial","20"),bg=self.mainColor,fg=self.mainTextColor)
        labelTheoreme.place(x=0,y=0)
        btnPythagore.place(x=25,y=50)
        btnRPythagore.place(x=433,y=50)
        labelAutreCal.place(x=0,y=130)
    
    def AffichageFrameMain(self):
        self.labelBienvenu.pack()
        self.top.pack()
        self.bottom.pack()
        self.entryNombre1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.entryNombre2.place(relx=0.5, rely=0.5, anchor=CENTER)
        
    def AffichageBTNOperateur(self):
        self.affichage.place(x=10,y=400)
        self.btnPlus.place(x=30,y=320)
        self.btnMoin.place(x=90,y=320)
        self.btnDiviser.place(x=150,y=320)
        self.btnFois.place(x=210,y=320)
        
    def AffichageFrameMainNbComplex(self):
        self.topNbComplex.pack()
        self.bottomNbComplex.pack()
        self.entryNombre1NbComplex1.place(x=100,y=100)
        self.entryNombre1NbComplex2.place(x=400,y=100)
        self.entryNombre2NbComplex1.place(x=100,y=100)
        self.entryNombre2NbComplex2.place(x=400,y=100)
        self.labeli1.place(x=575,y=90)
        self.labeli2.place(x=575,y=90)
        self.btnExit.place(x=410,y=320)
    
    def AffichageMain(self):
        self.AffichageFrameMain()
        self.main.place(x=0,y=0)
        self.AffichageBTNOperateur()
    
    def RecuperationEntry(self):
        nb1 = int(self.entryNombre1.get())
        nb2 = int(self.entryNombre2.get())
        self.entryNombre1.delete(0,END)
        self.entryNombre2.delete(0,END)
        return nb1 , nb2
    
    def RecuperationEntryComplex(self):
        nb1_1 = int(self.entryNombre1NbComplex1.get())
        nb1_2 = int(self.entryNombre1NbComplex2.get())
        nb2_1 = int(self.entryNombre2NbComplex1.get())
        nb2_2 = int(self.entryNombre2NbComplex2.get())
        self.entryNombre1NbComplex1.delete(0,END)
        self.entryNombre1NbComplex2.delete(0,END)
        self.entryNombre2NbComplex1.delete(0,END)
        self.entryNombre2NbComplex2.delete(0,END)
        return nb1_1,nb1_2,nb2_1,nb2_2   
    
    def ShowResultat(self,nb1,nb2,resultat,calc):
        self.affichage.configure(text=str(nb1)+calc+str(nb2)+" = "+str(resultat))
    
    def plus(self):
        nb1,nb2 = self.RecuperationEntry()
        resultat = str(CalculeBase().adition(nb1,nb2))
        self.ShowResultat(nb1,nb2,resultat,"+")
    def moin(self):
        nb1,nb2 = self.RecuperationEntry()
        resultat = str(CalculeBase().soustration(nb1,nb2))
        self.ShowResultat(nb1,nb2,resultat,"-")
    def fois(self):
        nb1,nb2 = self.RecuperationEntry()
        resultat = str(CalculeBase().multiplication(nb1,nb2))
        self.ShowResultat(nb1,nb2,resultat,"*")
    def diviser(self):
        nb1,nb2 = self.RecuperationEntry()
        resultat = str(CalculeBase().division(nb1,nb2))
        self.ShowResultat(nb1,nb2,resultat,"/")
    
    def plusNbComplex(self):
        nb1_1,nb1_2,nb2_1,nb2_2 = self.RecuperationEntryComplex()
        nb1,nb2,resultat = CalculeNbComplexe.aditionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        self.ShowResultat(nb1,nb2,resultat,"+")
    def moinNbComplex(self):
        nb1_1,nb1_2,nb2_1,nb2_2 = self.RecuperationEntryComplex()
        nb1,nb2,resultat = CalculeNbComplexe.soustrationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        self.ShowResultat(nb1,nb2,resultat,"-")
    def foisNbComplex(self):
        nb1_1,nb1_2,nb2_1,nb2_2 = self.RecuperationEntryComplex()
        nb1,nb2,resultat = CalculeNbComplexe.multiplicationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        self.ShowResultat(nb1,nb2,resultat,"*")
    def diviserNbComplex(self):
        nb1_1,nb1_2,nb2_1,nb2_2 = self.RecuperationEntryComplex()
        nb1,nb2,resultat = CalculeNbComplexe.divisionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2)
        self.ShowResultat(nb1,nb2,resultat,"/")
    
    def exitComplex(self):
        self.mainNbComplex.place_forget()
        self.btnExit.place_forget()
        self.AffichageMain()
        self.affichage.config(text="Affichage résultat")
        self.btnPlus.config(command=self.plus)
        self.btnMoin.config(command=self.moin)
        self.btnFois.config(command=self.fois)
        self.btnDiviser.config(command=self.diviser)
      
    def NbComplexe(self):
        self.AffichageFrameMainNbComplex()
        self.main.place_forget()
        self.btnExit.config(command=self.exitComplex)
        self.btnPlus.config(command=self.plusNbComplex)
        self.btnMoin.config(command=self.moinNbComplex)
        self.btnFois.config(command=self.foisNbComplex)
        self.btnDiviser.config(command=self.diviserNbComplex)
        self.mainNbComplex.place(x=0,y=0)
        self.AffichageBTNOperateur()
    