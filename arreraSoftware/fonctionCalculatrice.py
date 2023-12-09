from tkinter import *
from librairy.travailJSON import *
import math

class fncCalculatrice :
    def __init__(self,ConfigNeuron:jsonWork):
        self.__configNeuron = ConfigNeuron
        self.__name = self.__configNeuron.lectureJSON("name")
        self.__icon = self.__configNeuron.lectureJSON("iconAssistant")
        self.__color = self.__configNeuron.lectureJSON("interfaceColor")
        self.__textColor = self.__configNeuron.lectureJSON("interfaceTextColor")
        self.__emplacementTouche = self.__configNeuron.lectureJSON("toucheCalculatrice")+"/"
        self.__operateurChooseComplex = ""
        
        
    def calculatrice(self,mode):
        self.__screen = Toplevel()
        self.__imageTouche()
        self.__screen.title(self.__name+" : Calculatrice")
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        self.__screen.maxsize(1000,500)
        self.__screen.minsize(1000,500)
        #cadre
        self.__clavier = Frame(self.__screen,width=500,height=250,bg=self.__color)
        self.__historique = Frame(self.__screen,width=500,height=500,bg=self.__color)
        self.__nbComplex = Frame(self.__screen,width=500,height=500,bg=self.__color)
        self.__operateurComplex = Frame(self.__nbComplex)
        self.__complex1 = Frame(self.__nbComplex)
        self.__complex2 = Frame(self.__nbComplex)
        self.__pythagore = Frame(self.__screen,width=500,height=500,bg=self.__color)
        self.__chooseCal = Frame(self.__pythagore)
        self.__nbPythagore = Frame(self.__pythagore)
        #widget
        self.__zoneCalcule = Text(self.__screen,width=50, height=10,highlightthickness=2, highlightbackground="black",font=("arial","25"))
        self.__affichageComplexOut = Entry(self.__nbComplex,state="disabled",width=42,highlightthickness=2, highlightbackground="black",font=("arial","15"))
        self.__zoneComplex1A = Entry(self.__complex1,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.__zoneComplex1B = Entry(self.__complex1,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.__zoneComplex2A = Entry(self.__complex2,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.__zoneComplex2B = Entry(self.__complex2,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.__zonePythagore1 = Entry(self.__nbPythagore,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        self.__zonePythagore2 = Entry(self.__nbPythagore,highlightthickness=1, highlightbackground="black",font=("arial","15"))
        #touche clavier
        #chiffre
        self.__btnNb0 = Button(self.__clavier,image=self.imgNb0,command= lambda : self.__ecritureCarractere("0"))
        self.__btnNb1 = Button(self.__clavier,image=self.imgNb1,command= lambda : self.__ecritureCarractere("1"))
        self.__btnNb2 = Button(self.__clavier,image=self.imgNb2,command= lambda : self.__ecritureCarractere("2"))
        self.__btnNb3 = Button(self.__clavier,image=self.imgNb3,command= lambda : self.__ecritureCarractere("3"))
        self.__btnNb4 = Button(self.__clavier,image=self.imgNb4,command= lambda : self.__ecritureCarractere("4"))
        self.__btnNb5 = Button(self.__clavier,image=self.imgNb5,command= lambda : self.__ecritureCarractere("5"))
        self.__btnNb6 = Button(self.__clavier,image=self.imgNb6,command= lambda : self.__ecritureCarractere("6"))
        self.__btnNb7 = Button(self.__clavier,image=self.imgNb7,command= lambda : self.__ecritureCarractere("7"))
        self.__btnNb8 = Button(self.__clavier,image=self.imgNb8,command= lambda : self.__ecritureCarractere("8"))
        self.__btnNb9 = Button(self.__clavier,image=self.imgNb9,command= lambda : self.__ecritureCarractere("9"))
        self.__btnPI = Button(self.__clavier,image=self.imgPI,command= lambda : self.__ecritureCarractere("3.1415926535897932"))
        #operateur
        self.__btnVirgule = Button(self.__clavier,image=self.imgVirgule,command= lambda : self.__ecritureCarractere("."))
        self.__btnPuissanceDix = Button(self.__clavier,image=self.imgPuissanceDix,command= lambda : self.__ecritureCarractere("*10**"))
        self.__btnEgal = Button(self.__clavier,image=self.imgEgal,command=self.__calcule)
        self.__btnplus = Button(self.__clavier,image=self.imgPlus,command= lambda : self.__ecritureCarractere("+"))
        self.__btnMoin = Button(self.__clavier,image=self.imgMoin,command= lambda : self.__ecritureCarractere("-"))
        self.__btnFois = Button(self.__clavier,image=self.imgFois,command= lambda : self.__ecritureCarractere("*"))
        self.__btnDiviser = Button(self.__clavier,image=self.imgDiviser,command= lambda : self.__ecritureCarractere("/"))
        self.__btnParenthese1 = Button(self.__clavier,image=self.imgParenthese1,command= lambda : self.__ecritureCarractere("("))
        self.__btnParenthese2 = Button(self.__clavier,image=self.imgParenthese2,command= lambda : self.__ecritureCarractere(")"))
        self.__btnRacine = Button(self.__clavier,image=self.imgRacine,command= lambda : self.__ecritureCarractere("math.sqrt("))
        self.__btnExposant = Button(self.__clavier,image=self.imgExposant,command= lambda : self.__ecritureCarractere("**"))
        self.__btnExpodentiel = Button(self.__clavier,image=self.imgExpodentiel,command= lambda : self.__ecritureCarractere("math.exp("))
        self.__btnLN = Button(self.__clavier,image=self.imgLN,command= lambda : self.__ecritureCarractere("math.log(x,math.e)"))
        self.__btnLOG = Button(self.__clavier,image=self.imgLOG,command= lambda : self.__ecritureCarractere("math.log(x,10)"))
        #cercle trigo
        self.__btnSIN = Button(self.__clavier,image=self.imgSIN,command=lambda : self.__ecritureCarractere("math.sin("))
        self.__btnCOS = Button(self.__clavier,image=self.imgCOS,command=lambda : self.__ecritureCarractere("math.cos("))
        self.__btnTAN = Button(self.__clavier,image=self.imgTAN,command=lambda :self.__ecritureCarractere("math.tan("))
        self.__btnARCSIN = Button(self.__clavier,image=self.imgARCSIN,command=lambda : self.__ecritureCarractere("math.asin("))
        self.__btnARCCOS = Button(self.__clavier,image=self.imgARCCOS,command=lambda : self.__ecritureCarractere("math.acos("))
        self.__btnARCTAN = Button(self.__clavier,image=self.imgARCTAN,command=lambda : self.__ecritureCarractere("math.cos("))
        #autre
        self.__btnClear = Button(self.__clavier,image=self.imgClear,command=self.__clearAll)
        self.__btnSuppr = Button(self.__clavier,image=self.imgSuppr,command=self.__suppr)
        #btn fonction special
        self.__btnAngle = Button(self.__clavier,text="Randian en degres",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__convertiseurDegRad)
        self.__btnPythagore = Button(self.__clavier,text="Theoreme de pythagore",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__modePythagore)
        self.__btnNbComplex = Button(self.__clavier,text="Nombre Complex",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__modeComplex)
        #btn nb complex
        self.__btnEgalComplex = Button(self.__nbComplex,image=self.imgEgal,command= lambda : self.__calculeComplex())
        self.__btnplusComplex = Button(self.__operateurComplex,image=self.imgPlus,command= lambda : self.__setOperateurComplex("+"))
        self.__btnMoinComplex = Button(self.__operateurComplex,image=self.imgMoin,command= lambda : self.__setOperateurComplex("-"))
        self.__btnFoisComplex = Button(self.__operateurComplex,image=self.imgFois,command= lambda : self.__setOperateurComplex("*"))
        self.__btnDiviserComplex = Button(self.__operateurComplex,image=self.imgDiviser,command= lambda : self.__setOperateurComplex("/"))
        self.__btnCancelComplex = Button(self.__nbComplex,text="Annuler",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__cancelOperateurComplex)
        self.__btnRetourComplex = Button(self.__nbComplex,text="Retour",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__modeCalcule)
        #bouton pythagore
        self.__btnReciproque = Button(self.__chooseCal,text="Reciproque",bg=self.__color,fg=self.__textColor,command=lambda : self.__calculePythagore(2))
        self.__btnTheoreme = Button(self.__chooseCal,text="Theoreme",bg=self.__color,fg=self.__textColor,command=lambda : self.__calculePythagore(1))
        self.__btnRetourPythagore = Button(self.__pythagore,text="Retour",font=("arial","13"),bg=self.__color,fg=self.__textColor,command=self.__modeCalcule)
        #label
        self.__labelPlus = Label(self.__operateurComplex,image=self.imgPlus)
        self.__labelMois = Label(self.__operateurComplex,image=self.imgMoin)
        self.__labelDiviser = Label(self.__operateurComplex,image=self.imgDiviser)
        self.__labelFois = Label(self.__operateurComplex,image=self.imgFois)
        self.__affichageHistorique = Label(self.__historique,text="Historique :",width=30,bg=self.__color,fg=self.__textColor,font=("arial","20"), anchor="w")
        self.__affichageComplexOut = Label(self.__nbComplex,width=42,font=("arial","15"),bg="grey",fg="white")
        self.__complex1L = Label(self.__complex1,text="j",font=("arial","15"),bg=self.__color)
        self.__complex2L = Label(self.__complex2,text="j",font=("arial","15"),bg=self.__color)
        self.__affichagePythagoreOut =  Label(self.__pythagore,width=42,font=("arial","15"),bg="grey",fg="white")
        #affichage 
        self.__widgetnbComplex()
        self.__widgetPythagore()
        self.__affichageClavier()
        self.__historique.pack(side="left",fill="both", expand=True) 
        if mode == "0":
            self.__modeCalcule()
        else :
            if mode == "1":
                self.__modeComplex()
            else :
                if mode == "2":
                    self.__modePythagore()
        #affichage historique
        self.__affichageHistorique.place(x=0,y=0)
        #verrifaction de carratere taper
        self.__zoneCalcule.bind("<KeyPress-Return>",self.__enterPressed)
        self.__zoneCalcule.bind("<KeyPress>",self.__carractereInterdit)
    
    def __modeCalcule(self):
        self.__nbComplex.pack_forget()
        self.__pythagore.pack_forget()
        self.__updateCalculatrice() 
        self.__clavier.pack(side="bottom",anchor="sw")
        self.__zoneCalcule.pack(side="top",anchor="nw") 
        
        
    def __affichageClavier(self):
        self.__btnNb7.place(x=0,y=0)
        self.__btnNb8.place(x=35,y=0)
        self.__btnNb9.place(x=70,y=0)
        self.__btnParenthese1.place(x=105,y=0)
        self.__btnParenthese2.place(x=140,y=0)
        
        self.__btnNb4.place(x=0,y=35)
        self.__btnNb5.place(x=35,y=35)
        self.__btnNb6.place(x=70,y=35)
        self.__btnFois.place(x=105,y=35)
        self.__btnDiviser.place(x=140,y=35)
        
        self.__btnNb1.place(x=0,y=70)
        self.__btnNb2.place(x=35,y=70)
        self.__btnNb3.place(x=70,y=70)
        self.__btnplus.place(x=105,y=70)
        self.__btnMoin.place(x=140,y=70)
        
        self.__btnNb0.place(x=0,y=105)
        self.__btnVirgule.place(x=35,y=105)
        self.__btnPuissanceDix.place(x=70,y=105)
        self.__btnEgal.place(x=105,y=105)
        self.__btnSuppr.place(x=140,y=105)
        self.__btnClear.place(x=175,y=105)
        
        self.__btnSIN.place(x=0,y=140)
        self.__btnCOS.place(x=35,y=140)
        self.__btnTAN.place(x=70,y=140)
        self.__btnARCSIN.place(x=105,y=140)
        self.__btnARCCOS.place(x=140,y=140)
        self.__btnARCTAN.place(x=175,y=140)
        
        self.__btnPI.place(x=0,y=175)
        self.__btnRacine.place(x=35,y=175)
        self.__btnExposant.place(x=70,y=175)
        self.__btnExpodentiel.place(x=105,y=175)
        self.__btnLN.place(x=140,y=175)
        self.__btnLOG.place(x=175,y=175)
        
        self.__btnAngle.place(x=250,y=35)
        self.__btnPythagore.place(x=250,y=105)
        self.__btnNbComplex.place(x=250,y=175)
        
    def __updateCalculatrice(self):
        self.__btnNb7.update() 
        self.__btnNb8.update() 
        self.__btnNb9.update() 
        self.__btnParenthese1.update() 
        self.__btnParenthese2.update() 
        
        self.__btnNb4.update() 
        self.__btnNb5.update() 
        self.__btnNb6.update() 
        self.__btnFois.update() 
        self.__btnDiviser.update() 
        
        self.__btnNb1.update() 
        self.__btnNb2.update() 
        self.__btnNb3.update() 
        self.__btnplus.update() 
        self.__btnMoin.update() 
        
        self.__btnNb0.update()
        self.__btnVirgule.update()
        self.__btnPuissanceDix.update()
        self.__btnEgal.update()
        self.__btnSuppr.update()
        self.__btnClear.update()
        
        self.__btnSIN.update()
        self.__btnCOS.update()
        self.__btnTAN.update()
        self.__btnARCSIN.update()
        self.__btnARCCOS.update()
        self.__btnARCTAN.update()
        
        self.__btnPI.update() 
        self.__btnRacine.update() 
        self.__btnExposant.update() 
        self.__btnExpodentiel.update() 
        self.__btnLN.update() 
        self.__btnLOG.update() 
        
        self.__btnAngle.update() 
        self.__btnPythagore.update() 
        self.__btnNbComplex.update() 
        
        self.__zoneCalcule.update() 
       
    def __imageTouche(self):
        self.imgNb0 = PhotoImage(file=self.__emplacementTouche+"tchNB0.png")
        self.imgNb1 = PhotoImage(file=self.__emplacementTouche+"tchNB1.png")
        self.imgNb2 = PhotoImage(file=self.__emplacementTouche+"tchNB2.png")
        self.imgNb3 = PhotoImage(file=self.__emplacementTouche+"tchNB3.png")
        self.imgNb4 = PhotoImage(file=self.__emplacementTouche+"tchNB4.png")
        self.imgNb5 = PhotoImage(file=self.__emplacementTouche+"tchNB5.png")
        self.imgNb6 = PhotoImage(file=self.__emplacementTouche+"tchNB6.png")
        self.imgNb7 = PhotoImage(file=self.__emplacementTouche+"tchNB7.png")
        self.imgNb8 = PhotoImage(file=self.__emplacementTouche+"tchNB8.png")
        self.imgNb9 = PhotoImage(file=self.__emplacementTouche+"tchNB9.png")
        self.imgPI = PhotoImage(file=self.__emplacementTouche+"tchPI.png")
        
        self.imgVirgule = PhotoImage(file=self.__emplacementTouche+"tchVirgule.png")
        self.imgPuissanceDix = PhotoImage(file=self.__emplacementTouche+"tchDixPuissance.png")
        self.imgEgal = PhotoImage(file=self.__emplacementTouche+"tchEgal.png")
        self.imgPlus = PhotoImage(file=self.__emplacementTouche+"tchPlus.png")
        self.imgMoin = PhotoImage(file=self.__emplacementTouche+"tchMoin.png")
        self.imgFois = PhotoImage(file=self.__emplacementTouche+"tchFois.png")
        self.imgDiviser = PhotoImage(file=self.__emplacementTouche+"tchDiviser.png")
        self.imgParenthese1 = PhotoImage(file=self.__emplacementTouche+"tchParenthese1.png")
        self.imgParenthese2 = PhotoImage(file=self.__emplacementTouche+"tchParenthese2.png")
        self.imgRacine = PhotoImage(file=self.__emplacementTouche+"tchRacine.png")
        self.imgExposant = PhotoImage(file=self.__emplacementTouche+"tchExposant.png")
        self.imgExpodentiel = PhotoImage(file=self.__emplacementTouche+"tchExpodentiel.png")
        self.imgLN = PhotoImage(file=self.__emplacementTouche+"tchLN.png")
        self.imgLOG = PhotoImage(file=self.__emplacementTouche+"tchLOG.png")
        
        self.imgClear = PhotoImage(file=self.__emplacementTouche+"tchClear.png")
        self.imgSuppr = PhotoImage(file=self.__emplacementTouche+"tchSuppr.png")
        
        self.imgSIN = PhotoImage(file=self.__emplacementTouche+"tchSIN.png")
        self.imgCOS = PhotoImage(file=self.__emplacementTouche+"tchCOS.png")
        self.imgTAN = PhotoImage(file=self.__emplacementTouche+"tchTAN.png")
        self.imgARCSIN = PhotoImage(file=self.__emplacementTouche+"tchARCSIN.png")
        self.imgARCCOS = PhotoImage(file=self.__emplacementTouche+"tchARCCOS.png")
        self.imgARCTAN = PhotoImage(file=self.__emplacementTouche+"tchARCTAN.png")
    
    def __carractereInterdit(self,event):
        carractereSpeciaux = "'_,?;§!ùµ*£$¤¨@ç|~&²¹#`\°"
        carractereSpeciaux2 = '"'
        if event.char.isalpha():
            return "break"
        elif event.char in carractereSpeciaux:
            return "break"
        elif event.char in carractereSpeciaux2:
            return "break"
        
    def __enterPressed(self,event):
        self.__calcule()
        return "break"
        
    def __ecritureCarractere(self,crc:str):
        self.__zoneCalcule.insert("end",crc)
        
    def __clearAll(self):
        self.__zoneCalcule.delete("1.0",END)
        
    def __suppr(self):
        # Récupérer le contenu actuel du widget Text
        contenu = self.__zoneCalcule.get("1.0", "end-1c")

        if contenu:
            # Supprimer le dernier caractère
            contenu = contenu[:-1]

            # Mettre à jour le widget Text avec le nouveau contenu
            self.__zoneCalcule.delete("1.0", "end")
            self.__zoneCalcule.insert("1.0", contenu)
            
    def __calcule(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        contenu = contenu.replace(" ", "")
        try:
            resultat = eval(contenu)
            self.__affichageHistorique.configure(text="Historique :\n" + str(contenu) + " = " + str(resultat))
            self.__affichageHistorique.update()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(resultat))
        except Exception as e:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
            
    def __modeComplex(self):
        self.__clavier.pack_forget()
        self.__zoneCalcule.pack_forget()
        self.__nbComplex.pack(side="left")  
        self.__complex1.place(x=15,y=25)
        self.__operateurComplex.place(x=((self.__nbComplex.winfo_reqwidth()-self.__operateurComplex.winfo_reqwidth())//2),y=75)
        self.__complex2.place(x=15,y=125)
        self.__btnEgalComplex.place(x=((self.__nbComplex.winfo_reqwidth()-self.__btnEgalComplex.winfo_reqwidth())//2),y=175)
        self.__affichageComplexOut.place(x=15,y=225)
        self.__btnCancelComplex.place(x=(500-self.__btnCancelComplex.winfo_reqwidth()),y=(500-self.__btnCancelComplex.winfo_reqheight()))
        self.__btnRetourComplex.place(x=0,y=(500-self.__btnCancelComplex.winfo_reqheight()))
        self.__affichageComplexOut.configure(text="")
        self.__zoneComplex1A.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex1B.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex2A.bind("<KeyPress>", self.__carractereInterdit)
        self.__zoneComplex2B.bind("<KeyPress>", self.__carractereInterdit)             
    
    def __widgetnbComplex(self):
        self.__zoneComplex1A.pack(side="left")
        self.__complex1L.pack(side="right")
        self.__zoneComplex1B.pack(side="right")
        self.__zoneComplex2A.pack(side="left")
        self.__complex2L.pack(side="right")
        self.__zoneComplex2B.pack(side="right") 
        self.__btnplusComplex.pack(side="left")
        self.__btnMoinComplex.pack(side="left")
        self.__btnFoisComplex.pack(side="left")
        self.__btnDiviserComplex.pack(side="left")
    
    def __setOperateurComplex(self,operateur:str):
        self.__operateurChooseComplex = operateur
        self.__btnplusComplex.pack_forget()
        self.__btnMoinComplex.pack_forget()
        self.__btnFoisComplex.pack_forget()
        self.__btnDiviserComplex.pack_forget()
        self.__operateurComplex.place_forget()
        if self.__operateurChooseComplex == "+":
            self.__labelPlus.pack()
        else :
            if self.__operateurChooseComplex == "-":
                self.__labelMois.pack()
            else :
                if self.__operateurChooseComplex == "*":
                    self.__labelFois.pack()
                else :
                    if self.__operateurChooseComplex== "/":
                        self.__labelDiviser.pack()
        self.__operateurComplex.update()
        self.__operateurComplex.place(x=((self.__nbComplex.winfo_reqwidth()-self.__operateurComplex.winfo_reqwidth())//2),y=75)
        
    def __cancelOperateurComplex(self):
        if self.__operateurChooseComplex == "":
            self.__operateurChooseComplex = ""
        else :
            self.__operateurChooseComplex = ""
            self.__labelPlus.pack_forget()
            self.__labelMois.pack_forget()
            self.__labelFois.pack_forget()
            self.__labelDiviser.pack_forget()
            self.__operateurComplex.place_forget()
            self.__btnplusComplex.pack(side="left")
            self.__btnMoinComplex.pack(side="left")
            self.__btnFoisComplex.pack(side="left")
            self.__btnDiviserComplex.pack(side="left")
            self.__operateurComplex.update()
            self.__operateurComplex.place(x=((self.__nbComplex.winfo_reqwidth()-self.__operateurComplex.winfo_reqwidth())//2),y=75)
        
        
    def __calculeComplex(self):
        nb1A = self.__zoneComplex1A.get()
        nb1B = self.__zoneComplex1B.get()
        nb2A = self.__zoneComplex2A.get()
        nb2B = self.__zoneComplex2B.get()
        if self.__operateurChooseComplex == "" or nb1A.strip() == "" or nb1B.strip() == "" or nb2A.strip() == "" or nb2B.strip() == "" :
            self.__affichageComplexOut.configure(text="Erreur")
        else :
            calcule = CalculeNbComplexe(int(nb1A),int(nb1B),int(nb2A),int(nb2B))
            if self.__operateurChooseComplex == "+":
                nb1 = calcule.recuperationNb1()
                nb2 = calcule.recuperationNb2()
                resultat = calcule.aditionNbComplex()
                self.__affichageHistorique.configure(text="Historique :\n" + nb1+"+"+nb2 + " = " + str(resultat))
            else :
                if self.__operateurChooseComplex == "-":
                    nb1 = calcule.recuperationNb1()
                    nb2 = calcule.recuperationNb2()
                    resultat = calcule.soustrationNbComplex()
                    self.__affichageHistorique.configure(text="Historique :\n" + nb1+"-"+nb2 + " = " + str(resultat))
                else :
                    if self.__operateurChooseComplex == "*":
                        nb1 = calcule.recuperationNb1()
                        nb2 = calcule.recuperationNb2()
                        resultat = calcule.multiplicationNbComplex()
                        self.__affichageHistorique.configure(text="Historique :\n" + nb1+"*"+nb2 + " = " + str(resultat))
                    else :
                        if self.__operateurChooseComplex == "/":
                            nb1 = calcule.recuperationNb1()
                            nb2 = calcule.recuperationNb2()
                            resultat = calcule.divisionNbComplex()
                            self.__affichageHistorique.configure(text="Historique :\n" + nb1+"/"+nb2 + " = " + str(resultat))
            self.__operateurChooseComplex = ""
            self.__affichageComplexOut.configure(text=str(resultat))
    
    def __widgetPythagore(self):
        self.__btnReciproque.pack(side="left")
        self.__btnTheoreme.pack(side="left")
        self.__zonePythagore1.pack(side="left")
        self.__zonePythagore2.pack(side="left")
    
    def __modePythagore(self):
        self.__clavier.pack_forget()
        self.__zoneCalcule.pack_forget()
        self.__pythagore.pack(side="right")  
        self.__nbPythagore.place(x=15,y=25)
        self.__chooseCal.place(x=(self.__pythagore.winfo_reqwidth() - self.__chooseCal.winfo_reqwidth()) // 2,y=125)
        self.__affichagePythagoreOut.place(x=15,y=225) 
        self.__btnRetourPythagore.place(x=0,y=(500-self.__btnRetourPythagore.winfo_reqheight()))
        self.__affichagePythagoreOut.configure(text="")
        
    def __calculePythagore(self,mode):
        nb1 = self.__zonePythagore1.get()
        nb2 = self.__zonePythagore2.get()
        if nb1.strip() == "" or nb2.strip() == "":
            self.__affichagePythagoreOut.configure(text="Erreur")
        else :
            calcule = Pythagore(int(nb1),int(nb2))
            if mode == 1:
                resultat = str(calcule.theoreme())
                sortieCalcule = calcule.recuperationCalcule()
                self.__affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
            else :
                if mode == 2:
                    if int(nb1) <= int(nb2) :
                        self.__affichagePythagoreOut.configure(text="Erreur")
                    else :
                        resultat = str(calcule.reciproque())
                        sortieCalcule = calcule.recuperationCalcule()
                        self.__affichagePythagoreOut.configure(text=sortieCalcule+"="+resultat)
    
    def __convertiseurDegRad(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        if contenu ==  "":
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        else :
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(math.degrees(int(contenu))))
                

class CalculeNbComplexe :
    def __init__(self,nb1_1:int,nb1_2:int,nb2_1:int,nb2_2:int):
        self.nb1= complex(nb1_1,nb1_2)
        self.nb2 = complex(nb2_1,nb2_2)
        
    def recuperationNb1(self):
        return str(self.nb1)
    
    def recuperationNb2(self):
        return str(self.nb2)
         
    def aditionNbComplex(self):
        resultat = self.nb1 + self.nb2
        return resultat
    
    def soustrationNbComplex(self):
        resultat = self.nb1 - self.nb2
        return resultat
    
    def multiplicationNbComplex(self):
        resultat = self.nb1 * self.nb2
        return resultat
    
    def divisionNbComplex(self):
        resultat = self.nb1 / self.nb2
        return resultat    
    

class Pythagore :
    def __init__(self,nb1:int,nb2:int):
        self.nb1 = nb1
        self.nb2 = nb2
        self.etatReciproque = bool
       
    def theoreme(self):
        resultat = math.sqrt(self.nb1**2+self.nb2**2)
        self.etatReciproque = False
        return resultat
    
    def reciproque(self):
        resultat = math.sqrt(self.nb1**2-self.nb2**2)
        self.etatReciproque = True
        return resultat 
    
    def recuperationCalcule(self):
        if self.reciproque == False :
            return str("math.sqrt("+str(self.nb1)+"**2"+"+"+str(self.nb2)+"**2"+")") 
        else :
            return str("math.sqrt("+str(self.nb1)+"**2"+"-"+str(self.nb2)+"**2"+")") 