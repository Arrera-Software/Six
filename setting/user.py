from tkinter import*
from function.JSON import*
from setting.view import*
listGenre = ["monsieur","madame","maitre"]
def User(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6,btn7):
    varGenre = StringVar(screen)
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def Actulisaton():
        labelUser1.config(text=lectureJSON("setting/config.json","userGenre1")+" "+lectureJSON("setting/config.json","user1"))
        labelUser2.config(text=lectureJSON("setting/config.json","userGenre2")+" "+lectureJSON("setting/config.json","user2"))
        labelUser3.config(text=lectureJSON("setting/config.json","userGenre3")+" "+lectureJSON("setting/config.json","user3"))
        labelUser4.config(text=lectureJSON("setting/config.json","userGenre4")+" "+lectureJSON("setting/config.json","user4"))
    def userView():
        labelUserGenre.place(x=20,y=125)
        labelUserName.place(x=20,y=225)
        entryName.place(x=100,y=230)
        menuGenre.place(x=100,y=130)
        btnUserValider.place(x=225,y=300)
    def userNoView():
        labelUserGenre.place_forget()
        labelUserName.place_forget()
        entryName.place_forget()
        menuGenre.place_forget()
        btnUserValider.place_forget()
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
    def exitModif():
        Afficher()
        userNoView()
        btnUser5.config(command=exit)
    def User1():
        btnUser5.config(command=exitModif)
        def Valider1():
            newName=entryName.get()
            newGenre = varGenre.get()
            EcritureJSON("setting/config.json","user1",newName)
            EcritureJSON("setting/config.json","userGenre1",newGenre)
            exitModif()
            Actulisaton()
        genre = lectureJSON("setting/config.json","userGenre1")
        if genre == "monsieur" :
            varGenre.set(listGenre[0])
        else :
            if genre == "madame" :
                varGenre.set(listGenre[1])
            else :
                varGenre.set(listGenre[2])
        btnUserValider.config(command=Valider1)  
        NoAfficher()
        userView()
    def User2():
        btnUser5.config(command=exitModif)
        def Valider1():
            newName=entryName.get()
            newGenre = varGenre.get()
            EcritureJSON("setting/config.json","user2",newName)
            EcritureJSON("setting/config.json","userGenre2",newGenre)
            exitModif()
            Actulisaton()
        genre = lectureJSON("setting/config.json","userGenre2")
        if genre == "monsieur" :
            varGenre.set(listGenre[0])
        else :
            if genre == "madame" :
                varGenre.set(listGenre[1])
            else :
                varGenre.set(listGenre[2])
        btnUserValider.config(command=Valider1)  
        NoAfficher()
        userView()
    def User3():
        btnUser5.config(command=exitModif)
        def Valider1():
            newName=entryName.get()
            newGenre = varGenre.get()
            EcritureJSON("setting/config.json","user3",newName)
            EcritureJSON("setting/config.json","userGenre3",newGenre)
            exitModif()
            Actulisaton()
        genre = lectureJSON("setting/config.json","userGenre3")
        if genre == "monsieur" :
            varGenre.set(listGenre[0])
        else :
            if genre == "madame" :
                varGenre.set(listGenre[1])
            else :
                varGenre.set(listGenre[2])
        btnUserValider.config(command=Valider1)  
        NoAfficher()
        userView()
    def User4():
        btnUser5.config(command=exitModif)
        def Valider1():
            newName=entryName.get()
            newGenre = varGenre.get()
            EcritureJSON("setting/config.json","user4",newName)
            EcritureJSON("setting/config.json","userGenre4",newGenre)
            exitModif()
            Actulisaton()
        genre = lectureJSON("setting/config.json","userGenre4")
        if genre == "monsieur" :
            varGenre.set(listGenre[0])
        else :
            if genre == "madame" :
                varGenre.set(listGenre[1])
            else :
                varGenre.set(listGenre[2])
        btnUserValider.config(command=Valider1)  
        NoAfficher()
        userView()
    #declaration widget
    #btn
    btnUser1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User1)
    btnUser2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User2)
    btnUser3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User3)
    btnUser4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=User4)
    btnUser5 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    btnUserValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
    #Label
    labelIndication =Label(section,text="Changer votre nom d'utilisateur",bg="#5e262c",font=("arial","15"),fg="white")
    labelUser1 = Label(section,text=lectureJSON("setting/config.json","userGenre1")+" "+lectureJSON("setting/config.json","user1"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser2 = Label(section,text=lectureJSON("setting/config.json","userGenre2")+" "+lectureJSON("setting/config.json","user2"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser3 = Label(section,text=lectureJSON("setting/config.json","userGenre3")+" "+lectureJSON("setting/config.json","user3"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser4 = Label(section,text=lectureJSON("setting/config.json","userGenre4")+" "+lectureJSON("setting/config.json","user4"),bg="#5e262c",font=("arial","15"),fg="white")
    
    labelUserGenre = Label(section,text="Genre : ",bg="#5e262c",font=("arial","15"),fg="white")
    labelUserName = Label(section,text="Nom : ",bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    #entry
    entryName = Entry(section,width=30,font=("arial","15"))
    #Menu deroulant 
    menuGenre = OptionMenu(section,varGenre,*listGenre)
    def Afficher():
        labelUser1.place(x=20,y=125)
        labelUser2.place(x=20,y=225)
        labelUser3.place(x=20,y=325)
        labelUser4.place(x=20,y=425)
    
        btnUser1.place(x=250,y=125)
        btnUser2.place(x=250,y=225)
        btnUser3.place(x=250,y=325)
        btnUser4.place(x=250,y=425)
        btnUser5.place(x=225,y=525)
    def NoAfficher():
        labelUser1.place_forget()
        labelUser2.place_forget()
        labelUser3.place_forget()
        labelUser4.place_forget()
    
        btnUser1.place_forget()
        btnUser2.place_forget()
        btnUser3.place_forget()
        btnUser4.place_forget()
    
    Afficher()
    