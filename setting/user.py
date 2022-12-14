from tkinter import *
from function.JSON import*
from setting.view import*
listGenre = ["monsieur","madame","maitre"]
def User(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6)
   #declaration widget
    #btn
    btnUser1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnUser2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnUser3 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnUser4 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white")
    btnUser5 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    #Label
    labelIndication =Label(section,text="Changer votre nom d'utilisateur",bg="#5e262c",font=("arial","15"),fg="white")
    labelUser1 = Label(section,text=lectureJSON("setting/config.json","userGenre1")+" "+lectureJSON("setting/config.json","user1"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser2 = Label(section,text=lectureJSON("setting/config.json","userGenre2")+" "+lectureJSON("setting/config.json","user2"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser3 = Label(section,text=lectureJSON("setting/config.json","userGenre3")+" "+lectureJSON("setting/config.json","user3"),bg="#5e262c",font=("arial","15"),fg="white")
    labelUser4 = Label(section,text=lectureJSON("setting/config.json","userGenre4")+" "+lectureJSON("setting/config.json","user4"),bg="#5e262c",font=("arial","15"),fg="white")
    
    labelIndication.place(x=125,y=0)
    
    labelUser1.place(x=20,y=125)
    labelUser2.place(x=20,y=225)
    labelUser3.place(x=20,y=325)
    labelUser4.place(x=20,y=425)
    
    btnUser1.place(x=250,y=125)
    btnUser2.place(x=250,y=225)
    btnUser3.place(x=250,y=325)
    btnUser4.place(x=250,y=425)
    btnUser5.place(x=225,y=525)
    