from objet.calendrier.calendrier import*
from objet.date.objetdate import*
from tkcalendar import Calendar
from tkinter.messagebox import showinfo
from tkinter import*

    
def SixCalendar():
    screen = Tk()
    selected_date = StringVar()
    varSupprEvent = StringVar(screen)
    screen.title("Six : agenda du jour")
    screen.iconphoto(False,PhotoImage(file="image/logo.png"))
    screen.maxsize(500,300)
    screen.minsize(500,300)
    screen.config(bg="white")
    listeEvent = []
    #fonction
    def SupprEvent():
        if len(lectureSimpleJSON("objet/calendrier/agenda.json")) == 0 :
           showinfo(title="Six : agenda du jour",message="Il n'a pas d'événement enregister")  
        else :
            cadreToday.place_forget()
            cadreSuppr.place(relx=0.5,rely=0.5,anchor=CENTER)
            dictEvent = Agenda("objet/calendrier/agenda.json").ListEventName()
            compteur = compteurJSON("objet/calendrier/agenda.json")
            i = 1 
            while i<= compteur :
                listeEvent.append(dictEvent[str(i)])
                i = i + 1 
            menuOptionSuppr = OptionMenu(cadreSuppr,varSupprEvent,*listeEvent)
            menuOptionSuppr.place(relx=0.5,rely=0.5,anchor=CENTER)
            def valider():
                var = varSupprEvent.get()
                i = 1 
                while i<= compteur :
                    valeur = dictEvent.get(str(i))
                    if valeur == var :
                        Agenda("objet/calendrier/agenda.json").SupprEnvent(i)
                        i = compteur + 1
                    else :
                        i = i + 1 
                cadreSuppr.place_forget()
                listeEvent.clear()
                menuOptionSuppr.destroy()
                cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
            boutonnVadiderSuppr.config(command=valider)
    def createEvent():
        cadreToday.place_forget()
        cadreEvent.place(relx=0.5,rely=0.5,anchor=CENTER)
    def ValiderAddEvent():
        name = entryName.get()
        def SortieDate():
            date =  str(calendrier.selection_get().strftime('%Y-{0}-%d'.format(calendrier.selection_get().strftime('%m').lstrip('0'))))
            labelAffichageDate.configure(text=date)
            Agenda("objet/calendrier/agenda.json").addEvent(name,date)
            cadreEvent.place_forget()
            cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
            top.destroy()
        if name == "":
            showinfo(title="Six : agenda du jour",message="Veuiller donner un nom a l'evenement")      
        else :
            top = Toplevel()
            calendrier = Calendar(top, selectmode="day")
            calendrier.pack()
            Button(top, text="Valider", command=SortieDate).pack()
        
    #carde
    cadreToday = Frame(screen,width=500,height=233,bg="white")
    cadreEvent = Frame(screen,width=500,height=233,bg="white")
    cadreSuppr = Frame(screen,width=500,height=233,bg="white")
    #menu
    menuBar  =  Menu(screen,bg="white",fg="black")
    menuBar.add_command(label="Créer un événement",command=createEvent)
    menuBar.add_command(label="Supprimmer un événement",command=SupprEvent)
    #label
    labelToday = Label(cadreToday,bg="white",fg="#3c0b10",font=("arial","20"),text="Aujourd'hui : "+dateToday().jour()+" "+dateToday().moisSTR()+" "+dateToday().annes())
    labelFeteToday = Label(cadreToday,font=("arial","15"),bg="white",fg="#3c0b10")
    labelIndicationName = Label(cadreEvent,text="Name :",bg="white",fg="#3c0b10",font=("arial","13"))
    labelAffichageDate = Label(cadreEvent,bg="white",fg="#3c0b10",font=("arial","15"))
    #Entry
    entryName = Entry(cadreEvent,width=20,font=("arial",15),relief=SOLID)
    #Bouton 
    BoutonValiderEvent  = Button(cadreEvent,command=ValiderAddEvent,text="Valider",bg="white",fg="#3c0b10",font=("arial","15")) 
    boutonnVadiderSuppr = Button(cadreSuppr,text="Valider",bg="white",fg="#3c0b10",font=("arial","15"))
    #option menu
    compteurEvent = compteurJSON("objet/calendrier/agenda.json")
    if compteurEvent == 0 :
        labelFeteToday.configure(text="Fête du jour : "+CalendrierToday().SaintDujour())
    else :
        valDateToday = dateToday().annes()+"-"+dateToday().moisINT()+"-"+dateToday().jour()
        listEvent = Agenda("objet/calendrier/agenda.json").ListEventDate()
        labelFeteToday.configure(text="Fête du jour : "+CalendrierToday().SaintDujour()+"\nProgramme du jour :")
        i = 1 
        while i <= compteurEvent :
            dateEvent = listEvent[str(i)]
            if valDateToday == dateEvent :
                listEventName = Agenda("objet/calendrier/agenda.json").ListEventName()[str(i)]
                labelFeteToday.configure(text=labelFeteToday.cget("text")+"\n"+listEventName)
                i = i+1
            else :
                i = i+1
 
    cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    labelToday.place(x=0,y=0)
    labelIndicationName.place(x=0,y=50)
    labelFeteToday.place(relx=0.5,rely=0.5,anchor=CENTER)
    
    BoutonValiderEvent.place(relx=0.5, rely=1.0, anchor='s')
    boutonnVadiderSuppr.place(relx=0.5, rely=1.0, anchor='s')
    
    entryName.place(x=70,y=50)
    
   
    
    screen.config(menu=menuBar)
    
    screen.mainloop()
    
    
def SortieEvenementTexte():
    varAngenda = Agenda("objet/calendrier/agenda.json")
    compteurEvent = compteurJSON("objet/calendrier/agenda.json")
    if compteurEvent == 0 :
        texte =  "Vous avez rien de prevu aujourd'hui"
    else :
        valDateToday = dateToday().annes()+"-"+dateToday().moisINT()+"-"+dateToday().jour()
        listEventDate = varAngenda.ListEventDate()
        listeEnvetName = varAngenda.ListEventName()
       
        if compteurEvent > 1 : 
            texte = "Vous avez quelque chose de prévue ajourd'hui qui sont "
        else :
            texte = "Vous avez quelque chose de prévue ajourd'hui qui est "
        i = 1 
        while i <= compteurEvent :
            dateEvent = listEventDate[str(i)]
            nameEvent = listeEnvetName[str(i)]
            if valDateToday == dateEvent :
                texte = texte + " "+nameEvent
                i = i + 1
            else :
                i = i+1
    return texte