from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from function.JSON import*
from setting.view import*
from function.openSofware import*


def Application(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
    
    def Affichage():
        labelAppWeb1.place(x=20,y=125)
        labelAppWeb2.place(x=20,y=185)
        labelAppWeb3.place(x=20,y=245)
        labelAppWeb4.place(x=20,y=305)
        labelAppWeb5.place(x=20,y=365)
        labelAppWeb6.place(x=20,y=425)
    
        btnAppWeb1.place(x=265,y=125)
        btnAppWeb2.place(x=265,y=185)
        btnAppWeb3.place(x=265,y=245)
        btnAppWeb4.place(x=265,y=305)
        btnAppWeb5.place(x=265,y=365)
        btnAppWeb6.place(x=265,y=425)
    
    def NoAffichage():
        labelAppWeb1.place_forget()
        labelAppWeb2.place_forget()
        labelAppWeb3.place_forget()
        labelAppWeb4.place_forget()
        labelAppWeb5.place_forget()
        labelAppWeb6.place_forget()
    
        btnAppWeb1.place_forget()
        btnAppWeb2.place_forget()
        btnAppWeb3.place_forget()
        btnAppWeb4.place_forget()
        btnAppWeb5.place_forget()
        btnAppWeb6.place_forget()
    
    def note():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","appNote",str(var))
        exit()
    
    def navigateurInternet():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","navigateurInternet",str(var))
        exit()
        
    def editeurtext():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","editeurtexte",str(var))
        exit()
    
    def presentation():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","editeurpresentation",str(var))
        exit()
        
    def tableur():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","tableur",str(var))
        exit()
        
    def musique():
        messagebox.showinfo(title="Information", message="Veiller selectionner un racourcie sans espace")
        var = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk"),("All Files", "*.*")])
        EcritureJSON("setting/config.json","appMusique",str(var))
        exit()
        
    #btn
    btnAppWeb1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=note)
    btnAppWeb2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=navigateurInternet)
    btnAppWeb3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=editeurtext)
    btnAppWeb4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=presentation)
    btnAppWeb5 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=tableur)
    btnAppWeb6 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=musique)
    btnAppWeb7 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Selectionner les racourcie qui correspont au\napplication suivante:",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb1 = Label(section,text="Application note",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb2 = Label(section,text="Navigateur internet",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb3 = Label(section,text="Editeur de texte",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb4 = Label(section,text="Editeur de presentation",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb5 = Label(section,text="Tableur",bg="#5e262c",font=("arial","15"),fg="white")
    labelAppWeb6  = Label(section,text="Musique",bg="#5e262c",font=("arial","15"),fg="white") 
    labelAppWeb7  = Label(section,text="Lien : ",bg="#5e262c",font=("arial","15"),fg="white") 
    
    
    labelIndication.place(x=95,y=0)
    
    Affichage()
    
    btnAppWeb7.place(x=225,y=650)
    
    
    #askopenfilename(defaultextension=".docCode", filetypes=[("Documentation", ".docCode"),("All Files", "*.*")])