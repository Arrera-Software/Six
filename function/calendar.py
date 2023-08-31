from objet.calendrier.calendrier import*
from objet.date.objetdate import*
from tkcalendar import Calendar
from tkinter.messagebox import showinfo
from tkinter import*

    
class SixCalendar():
    def __init__(self):
        self.screen = Tk()
        self.selected_date = StringVar()
        self.varSupprEvent = StringVar(self.screen)
        self.screen.title("Six : agenda du jour")
        self.screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        self.screen.maxsize(500,300)
        self.screen.minsize(500,300)
        self.screen.config(bg="#3c0b10")
        self.listeEvent = []
        #carde
        self.cadreToday = Frame(self.screen,width=500,height=233,bg="#3c0b10")
        self.cadreEvent = Frame(self.screen,width=500,height=233,bg="#3c0b10")
        self.cadreSuppr = Frame(self.screen,width=500,height=233,bg="#3c0b10")
        #menu
        self.menuBar  =  Menu(self.screen,bg="#3c0b10",fg="white")
        self.menuBar.add_command(label="Créer un événement",command=self.createEvent)
        self.menuBar.add_command(label="Supprimmer un événement",command=self.SupprEvent)
        #label
        self.labelToday = Label(self.cadreToday,bg="#3c0b10",fg="white",font=("arial","20"),text="Aujourd'hui : "+dateToday().jour()+" "+dateToday().moisSTR()+" "+dateToday().annes())
        self.labelFeteToday = Label(self.cadreToday,font=("arial","15"),bg="#3c0b10",fg="white")
        self.labelIndicationName = Label(self.cadreEvent,text="Name :",bg="#3c0b10",fg="white",font=("arial","13"))
        self.labelAffichageDate = Label(self.cadreEvent,bg="#3c0b10",fg="#3c0b10",font=("arial","15"))
        #Entry
        self.entryName = Entry(self.cadreEvent,width=20,font=("arial",15),relief=SOLID)
        #Bouton 
        self.BoutonValiderEvent  = Button(self.cadreEvent,command=self.ValiderAddEvent,text="Valider",bg="#3c0b10",fg="white",font=("arial","15")) 
        self.boutonVadiderSuppr = Button(self.cadreSuppr,text="Valider",bg="#3c0b10",fg="white",font=("arial","15"))
        #option menu
        self.compteurEvent = compteurJSON("objet/calendrier/agenda.json")
        if self.compteurEvent == 0 :
            self.labelFeteToday.configure(text="Fête du jour : "+CalendrierToday().SaintDujour())
        else :
            valDateToday = dateToday().annes()+"-"+dateToday().moisINT()+"-"+dateToday().jour()
            listEvent = Agenda("objet/calendrier/agenda.json").ListEventDate()
            self.labelFeteToday.configure(text="Fête du jour : "+CalendrierToday().SaintDujour()+"\nProgramme du jour :")
            i = 1 
            while i <= self.compteurEvent :
                dateEvent = listEvent[str(i)]
                if valDateToday == dateEvent :
                    listEventName = Agenda("objet/calendrier/agenda.json").ListEventName()[str(i)]
                    self.labelFeteToday.configure(text=self.labelFeteToday.cget("text")+"\n"+listEventName)
                    i = i+1
                else :
                    i = i+1
    
        self.cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        self.labelToday.place(x=0,y=0)
        self.labelIndicationName.place(x=0,y=50)
        self.labelFeteToday.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        self.BoutonValiderEvent.place(relx=0.5, rely=1.0, anchor='s')
        self.boutonVadiderSuppr.place(relx=0.5, rely=1.0, anchor='s')
        
        self.entryName.place(x=70,y=50)
        
    
        
        self.screen.config(menu=self.menuBar)
        
        self.screen.mainloop()
    
    def SupprEvent(self):
        if len(lectureSimpleJSON("objet/calendrier/agenda.json")) == 0 :
           showinfo(title="Six : agenda du jour",message="Il n'a pas d'événement enregister")  
        else :
            self.cadreToday.place_forget()
            self.cadreSuppr.place(relx=0.5,rely=0.5,anchor=CENTER)
            dictEvent = Agenda("objet/calendrier/agenda.json").ListEventName()
            compteur = compteurJSON("objet/calendrier/agenda.json")
            i = 1 
            while i<= compteur :
                self.listeEvent.append(dictEvent[str(i)])
                i = i + 1 
            menuOptionSuppr = OptionMenu(self.cadreSuppr,self.varSupprEvent,*self.listeEvent)
            menuOptionSuppr.place(relx=0.5,rely=0.5,anchor=CENTER)
            def valider():
                var = self.varSupprEvent.get()
                i = 1 
                while i<= compteur :
                    valeur = dictEvent.get(str(i))
                    if valeur == var :
                        Agenda("objet/calendrier/agenda.json").SupprEnvent(i)
                        i = compteur + 1
                    else :
                        i = i + 1 
                self.cadreSuppr.place_forget()
                self.listeEvent.clear()
                menuOptionSuppr.destroy()
                self.cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
            self.boutonVadiderSuppr.config(command=valider)
    
    def createEvent(self):
        self.cadreToday.place_forget()
        self.cadreEvent.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def ValiderAddEvent(self):
        name = self.entryName.get()
        def SortieDate():
            date =  str(calendrier.selection_get().strftime('%Y-{0}-%d'.format(calendrier.selection_get().strftime('%m').lstrip('0'))))
            self.labelAffichageDate.configure(text=date)
            Agenda("objet/calendrier/agenda.json").addEvent(name,date)
            self.cadreEvent.place_forget()
            self.cadreToday.place(relx=0.5,rely=0.5,anchor=CENTER)
            top.destroy()
        if name == "":
            showinfo(title="Six : agenda du jour",message="Veuiller donner un nom a l'evenement")      
        else :
            top = Toplevel()
            calendrier = Calendar(top, selectmode="day")
            calendrier.pack()
            Button(top, text="Valider", command=SortieDate).pack()
            

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