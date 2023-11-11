from setting.arreraAssistantSetting import *
from PIL import Image, ImageTk
from src.SIXGestion import*
import re

class sixTk :
    def __init__(self,gestionnaire:SIXGestion):
        self.para = ArreraSettingAssistant("setting/configSetting.json","configNeuron.json","sixConfig.json","FileUser/configUser.json") 
        self.gestionnaire = gestionnaire    
    
    def activePara(self):
        self.screenPara = Tk()
        self.screenPara.iconphoto(False,PhotoImage(file="asset/logo.png"))
        self.para.windows(self.screenPara)
        self.para.passageFonctionQuitter(self.fncQuit)
        self.para.mainView()
        self.screenPara.mainloop()

    def muteSix(self)->int:
        self.varOut = 0
        screenMute = Tk()
        image = Image.open(self.gestionnaire.getGUIMute())
        photo = ImageTk.PhotoImage(image)
        screenMute.title("Assistant Mute")
        screenMute.iconphoto(False,PhotoImage(file="asset/logo.png"))
        screenMute.maxsize(500,500)
        screenMute.minsize(500,500)
        fond = Canvas(screenMute,width=500,height=500)
        fond.create_image(0, 0, anchor=NW, image=photo)
        btnQuitter = Button(fond,text="Quitter",font=("arial","15"),command=lambda:self.quitMute(screenMute))
        btnUmute = Button(fond,text="Demuter",font=("arial","15"),command=lambda:self.uMute(screenMute))
        btnUmute.place(x=((fond.winfo_reqwidth()-btnUmute.winfo_reqwidth())-20),y=((fond.winfo_reqheight()-btnUmute.winfo_reqheight())-20))
        btnQuitter.place(x=20,y=((fond.winfo_reqheight()-btnQuitter.winfo_reqheight())-20))
        fond.pack()
        screenMute.mainloop()
        return self.varOut
    
    def uMute(self,screen:Tk):
        self.varOut = 0 
        screen.destroy()
    
    def quitMute(self,screen:Tk):
        self.varOut = 15
        screen.destroy()
    
    def fncQuit(self):
        self.screenPara.destroy()

    def _division(self,text, nombre):
        mots = text.split()
        premierPartie = mots[:nombre]
        deuxiemePartie = mots[nombre:]
        return ' '.join(premierPartie), ' '.join(deuxiemePartie)
    
    def _compteur(self,s:str):
        mots = s.split()
        return int(len(mots))   

    def _sautLigne(texte:str, nbMots:int):
        mots = re.findall(r'\S+\s*', texte)
        lignes = []  
        ligne_actuelle = [] 
        for mot in mots:
            ligne_actuelle.append(mot)
            if len(ligne_actuelle) >= nbMots:
                lignes.append(" ".join(ligne_actuelle))
                ligne_actuelle = []
        if ligne_actuelle:
            lignes.append(" ".join(ligne_actuelle))

        return "\n".join(lignes)