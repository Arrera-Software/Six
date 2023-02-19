from tkinter import *
from function.JSON import*
from setting.view import*
import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound

def prononciationMicro():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            Requette=r.recognize_google(audio,language='fr')
        except Exception as e:
            return "None" 
        return Requette
def Assistant(cadre,screen,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8):
    cadre.pack_forget()
    section= Frame(screen,width=500,height=700,bg="#5e262c")
    section.pack(side="right")
    #fonction
    def exit():
        section.pack_forget()
        cadre.pack(side="right")
        ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
    def Actualisation():
        labelAssistant1.config(text="Nom :"+lectureJSON("setting/config.json","nomAssistant"))
    def Afficher():
        labelAssistant1.place(x=20,y=125)
        labelAssistant2.place(x=20,y=225)
        btnAssistant1.place(x=250,y=125)
        btnAssistant2.place(x=250,y=225)
    def NoAfficher():
        labelAssistant1.place_forget()
        labelAssistant2.place_forget()
        btnAssistant1.place_forget()
        btnAssistant2.place_forget()
    def ExitName():
        labelAssistant3.place_forget()
        entryName.place_forget()
        btnAssistantValider.place_forget()
        btnAssistant3.config(command=exit)
        Afficher()
    def ExitPrononciation():
        labelAssistant4.place_forget()
        btnAssistant4.place_forget()
        btnAssistant5.place_forget()
        btnAssistantValider.place_forget()
        btnAssistant3.config(command=exit)
        Afficher()
    def AssistantName():
        NoAfficher()
        def ValiderName():
            newName = entryName.get()
            EcritureJSON("setting/config.json","nomAssistant",newName)
            ExitName()
            Afficher()
            Actualisation()
            entryName.delete(0, "end")
        btnAssistant3.config(command=ExitName)
        btnAssistantValider.config(command=ValiderName)
        labelAssistant3.place(x=20,y=125)
        entryName.place(x=100,y=230)
        btnAssistantValider.place(x=225,y=300)
    def AssistantPronociation():
        NoAfficher()
        btnAssistant3.config(command=ExitPrononciation)
        def ValiderPronociation():
            ExitPrononciation()
        def Ecoute():
            tts = gTTS(lectureJSON("setting/config.json","pronociationAssistant"), lang="fr")
            tts.save("voc.mp3")
            playsound("voc.mp3")
            os.remove("voc.mp3")
        def micro():
            var = prononciationMicro()
            EcritureJSON("setting/config.json","pronociationAssistant",var)
        btnAssistantValider.config(command=ValiderPronociation)
        btnAssistant4.config(command=micro)
        btnAssistant5.config(command=Ecoute)
        labelAssistant4.place(x=20,y=125)
        btnAssistant4.place(x=50,y=230)
        btnAssistant5.place(x=50,y=330)
        btnAssistantValider.place(x=225,y=400)
    #declaration widget
    #btn
    btnAssistant1 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=AssistantName)
    btnAssistant2 = Button(section,text="Modifier",bg="#3c0b10",font=("arial","15"),fg="white",command=AssistantPronociation)
    btnAssistant3 = Button(section,text="Exit",bg="white",font=("arial","15"),fg="black",command=exit)
    btnAssistant4 = Button(section,text="Appuyer pour parler",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAssistant5 = Button(section,text="Ecouter",bg="#3c0b10",font=("arial","15"),fg="white")
    btnAssistantValider = Button(section,text="Valider",bg="#3c0b10",font=("arial","15"),fg="white")
    #Label
    labelIndication =Label(section,text="Changer le nom de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant1 = Label(section,text="Nom :"+lectureJSON("setting/config.json","nomAssistant"),bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant2 = Label(section,text="Pronociation",bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant3 = Label(section,text="Nouveau nom :",bg="#5e262c",font=("arial","15"),fg="white")
    labelAssistant4 = Label(section,text="Pronication du nom de l'assistant",bg="#5e262c",font=("arial","15"),fg="white")
    labelIndication.place(x=125,y=0)
    #entry
    entryName = Entry(section,width=30,font=("arial","15"))
    Afficher()
    
    btnAssistant3.place(x=225,y=525)