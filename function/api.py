from tkinter import*
from src.srcSix import* 
from objet.actualiter.apiActualiter import*
from objet.meteo.apiMeteo import*
from function.JSON import*
from objet.date.objetdate import*
from objet.GPS.apiGPS import*
from function.traitementChaineCarractere import*
import webbrowser

def Resumer(root,police):#Fonction de resumer des actaulités et de la meteo
    varGPSDomicile = ville(lectureJSON("setting/config.json","ville1"))
    listActu = Actualiter().recuperationTitre()
    varMeteoDomicile = meteo(varGPSDomicile.lat(),varGPSDomicile.long())
    dateJour = date().jour() + " " + date().mois() + " "+date().annes()
    heureActuel = date().heure()+" Heure "+date().minute()
    six = SIXsrc(root,police)
    
    six.speak("On est le "+dateJour+" a "+heureActuel+" ")
    time.sleep(1)
    six.speak("La météo a "+lectureJSON("setting/config.json","ville1")+" est "+varMeteoDomicile.description()+" avec une température de "+varMeteoDomicile.temperature()+"°C")
    time.sleep(1)
    six.speak("Les actualités du jour sont :")
    time.sleep(1)
    six.speak(listActu[0])
    time.sleep(1)
    six.speak(listActu[1])
    time.sleep(1)
    six.speak(listActu[2])
    time.sleep(1)
    six.speak(listActu[3])
    time.sleep(1)
    six.speak(listActu[4])
    

def DescriptionActu():
    
    listActuTitre = Actualiter().recuperationTitre()
    listActuURL = Actualiter().recuperationURL()
    listActuDescription = Actualiter().recuperationDescription()
    
    varGPSDomicile = ville(lectureJSON("setting/config.json","ville1"))
    varMeteoDomicile = meteo(varGPSDomicile.lat(),varGPSDomicile.long())
    temperature = varMeteoDomicile.temperature()
    humiditer = varMeteoDomicile.humiditer()
    description = varMeteoDomicile.description()
    codeImage = varMeteoDomicile.icon()
    
    screen = Tk()
    
    def Actu1():
        webbrowser.open(listActuURL[0])
        screen.destroy()
        
    def Actu2():
        webbrowser.open(listActuURL[1])
        screen.destroy()
        
    def Actu3():
        webbrowser.open(listActuURL[2])
        screen.destroy()
        
    def Actu4():
        webbrowser.open(listActuURL[3])
        screen.destroy()
        
    def Actu5():
        webbrowser.open(listActuURL[4])
        screen.destroy()
    
    imageMeteo = PhotoImage(file="image/meteo/"+codeImage+".png")
    screen.title("Six : Actualités")
    screen.maxsize(600,700) 
    screen.minsize(600,700)
    screen.config(bg="#3c0b10")
    screen.iconphoto(False,PhotoImage(file="image/logo.png"))
    
    cadreMeteo = Frame(screen,bg="#3c0b10",width=575,height=250)
    
    canvasActu = Canvas(screen,bg="#3c0b10",highlightthickness=0)
    scrollbarActu = Scrollbar(canvasActu, orient="vertical", command=canvasActu.yview)
    canvasActu.config(yscrollcommand=scrollbarActu.set)
    
    cadreActuMain = Frame(canvasActu,bg="#3c0b10")
    canvasActu.create_window((0,0),window=cadreActuMain,anchor="nw")
    
    cadreActu1 = Frame(cadreActuMain,bg="#3c0b10",width=525,height=275)
    cadreActu2 = Frame(cadreActuMain,bg="#3c0b10",width=525,height=275)
    cadreActu3 = Frame(cadreActuMain,bg="#3c0b10",width=525,height=275)
    cadreActu4 = Frame(cadreActuMain,bg="#3c0b10",width=525,height=275)
    cadreActu5 = Frame(cadreActuMain,bg="#3c0b10",width=525,height=275)
    
    labelTitre1 = Label(cadreActu1,text=passageLigne(listActuTitre[0],8)+"\n",font=("arial",15, "bold"),fg="white",bg="#3c0b10",justify="left")
    labelTitre2 = Label(cadreActu2,text=passageLigne(listActuTitre[1],8)+"\n",font=("arial",15, "bold"),fg="white",bg="#3c0b10",justify="left")
    labelTitre3 = Label(cadreActu3,text=passageLigne(listActuTitre[2],8)+"\n",font=("arial",15, "bold"),fg="white",bg="#3c0b10",justify="left")
    labelTitre4 = Label(cadreActu4,text=passageLigne(listActuTitre[3],8)+"\n",font=("arial",15, "bold"),fg="white",bg="#3c0b10",justify="left")
    labelTitre5 = Label(cadreActu5,text=passageLigne(listActuTitre[4],8)+"\n",font=("arial",15, "bold"),fg="white",bg="#3c0b10",justify="left")
    
    labelDescription1 = Label(cadreActu1,text=passageLigne(listActuDescription[0],8)+"\n\n",font=("arial",12),fg="white",bg="#3c0b10",justify="left")
    labelDescription2 = Label(cadreActu2,text=passageLigne(listActuDescription[1],8)+"\n\n",font=("arial",12),fg="white",bg="#3c0b10",justify="left")
    labelDescription3 = Label(cadreActu3,text=passageLigne(listActuDescription[2],8)+"\n\n",font=("arial",12),fg="white",bg="#3c0b10",justify="left")
    labelDescription4 = Label(cadreActu4,text=passageLigne(listActuDescription[3],8)+"\n\n",font=("arial",12),fg="white",bg="#3c0b10",justify="left")
    labelDescription5 = Label(cadreActu5,text=passageLigne(listActuDescription[4],8)+"\n\n",font=("arial",12),fg="white",bg="#3c0b10",justify="left")
    
    buttonActu1 = Button(cadreActu1,text="Consulter",font=("arial",15),fg="#3c0b10",bg="white",command= Actu1)
    buttonActu2 = Button(cadreActu2,text="Consulter",font=("arial",15),fg="#3c0b10",bg="white",command= Actu2)
    buttonActu3 = Button(cadreActu3,text="Consulter",font=("arial",15),fg="#3c0b10",bg="white",command= Actu3)
    buttonActu4 = Button(cadreActu4,text="Consulter",font=("arial",15),fg="#3c0b10",bg="white",command= Actu4)
    buttonActu5 = Button(cadreActu5,text="Consulter",font=("arial",15),fg="#3c0b10",bg="white",command= Actu5)
    
    
    
    labelIconMeteo = Label(cadreMeteo,bg="#3c0b10",image=imageMeteo)
    labelLocalisation = Label(cadreMeteo,fg="white",bg="#3c0b10",font=("arial",22),text=lectureJSON("setting/config.json","ville1"))
    labelTemperature = Label(cadreMeteo,text=temperature+"°C",font=("arial",32),fg="white",bg="#3c0b10")
    labelHumiditer = Label(cadreMeteo,text=humiditer+"%",font=("arial",32),fg="white",bg="#3c0b10")
    labelDescriptionMeteo = Label(cadreMeteo,text=description,font=("arial",32),fg="white",bg="#3c0b10")
    
    
    cadreActu1.pack()
    cadreActu2.pack()
    cadreActu3.pack()
    cadreActu4.pack()
    cadreActu5.pack()
    
    labelTitre1.place(x=0,y=0)
    labelDescription1.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttonActu1.place(relx=0.5, rely=1.0, anchor="s")
    
    labelTitre2.place(x=0,y=0)
    labelDescription2.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttonActu2.place(relx=0.5, rely=1.0, anchor="s")
    
    labelTitre3.place(x=0,y=0)
    labelDescription3.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttonActu3.place(relx=0.5, rely=1.0, anchor="s")
    
    labelTitre4.place(x=0,y=0)
    labelDescription4.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttonActu4.place(relx=0.5, rely=1.0, anchor="s")
    
    labelTitre5.place(x=0,y=0)
    labelDescription5.place(relx=0.5, rely=0.5, anchor=CENTER)
    buttonActu5.place(relx=0.5, rely=1.0, anchor="s")

    labelLocalisation.place(x=300,y=0)
    labelTemperature.place(x=0,y=150)
    labelHumiditer.place(x=450,y=150)
    labelDescriptionMeteo.place(relx=0.5, rely=0.5, anchor=CENTER)
    labelIconMeteo.place(x=0,y=0)
    cadreMeteo.pack(side="top")
    canvasActu.pack(side="left", fill="both", expand=True)
    scrollbarActu.pack(side="right", fill="y")
    
    cadreActuMain.update_idletasks()
    canvasActu.config(scrollregion=canvasActu.bbox("all"))
    
    screen.mainloop()