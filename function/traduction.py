from objet.traduction.trad import*
from function.JSON import*
from tkinter import*

Color = "#3c0f14"
TextColor = "white"

class Trad:#Fonction de Traduction
    def __init__(self):
        screen = Tk()
        self.varInt = StringVar(screen)
        self.varOut = StringVar(screen)
        self.dictTrad = lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json")
        listLang = list(lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json").values())
        langSortieDefault = lectureJSON("setting/config.json","langTradDefault")
        imgFleche = PhotoImage(file="image/fleche.png")
        screen.title("Six traduction")
        screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        screen.minsize(800,500)
        screen.maxsize(800,500)
        screen.config(bg="#3c0f14")
    
        menuInt = OptionMenu(screen,self.varInt,*listLang)
        menuOut = OptionMenu(screen,self.varOut,*listLang)
    
        i=0
        while i < len(listLang):
            if (self.dictTrad[langSortieDefault]==listLang[i]):
                self.varOut.set(listLang[i])
                i=len(listLang)
            else :
                i = i + 1
        self.varInt.set(listLang[28])
        
        self.ZoneTextint = Text(screen,width=40,height=20)
        self.ZoneTextOut =  Text(screen,width=40,height=20)
        self.ZoneTextOut.config(state="disable")
        
        boutonTrad = Button(screen,image=imgFleche,command=self.trad)
    
        self.ZoneTextint.pack(side="left")
        self.ZoneTextOut.pack(side="right")
        boutonTrad.place(relx=0.5,rely=0.5,anchor=CENTER)
        menuInt.place(x=0,y=40)
        menuOut.place(x=475,y=40)
        screen.mainloop()
        
    def trad(self):
        
        text = self.ZoneTextint.get("1.0", END)
        sortie = ArreraTrad(searchKey(self.varInt.get(),self.dictTrad),searchKey(self.varOut.get(),self.dictTrad)).Tradution(text)
        self.ZoneTextOut.config(state="normal")
        self.ZoneTextOut.delete("1.0", END)
        self.ZoneTextOut.insert(INSERT,sortie)
        self.ZoneTextOut.config(state="disable")
        