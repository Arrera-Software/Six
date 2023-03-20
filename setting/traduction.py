from tkinter import *
from function.JSON import*
from setting.view import*

listLang = list(lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json").values())
def Trad(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8):
    varLang = StringVar(screen)
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
    
    def Valider():
            nameLang = varLang.get()
            newLang = searchKey(nameLang,lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json"))
            EcritureJSON("setting/config.json","langTradDefault",newLang)
            exit()
            
    def tradView():
        labelTrad1.place(x=20,y=125)
        menuLangue.place(x=100,y=230)
        btnTradValider.place(x=225,y=300)
        listLang = list(lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json").values())
        langSortieDefault = lectureJSON("setting/config.json","langTradDefault")
        dictTrad = lectureSimpleJSON("objet/traduction/dictLangueTraducteur.json")
        
        i=0
        while i < len(listLang):
            if (dictTrad[langSortieDefault]==listLang[i]):
                varLang.set(listLang[i])
                i=len(listLang)
            else :
                i = i + 1
        
    #declaration widget
    #btn
    btnTrad1 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    btnTradValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white",command=Valider)
    #Label
    labelIndication =Label(section,text="Modifier la langue de l'outil \nde traduction de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    labelTrad1 = Label(section,text="Langue :",bg="#5e262c",font=("arial","15"),fg="white")
    #Menu deroulant 
    menuLangue = OptionMenu(section,varLang,*listLang)
    
    labelIndication.place(x=125,y=0)
    
    tradView()
    
    btnTrad1.place(x=225,y=650)