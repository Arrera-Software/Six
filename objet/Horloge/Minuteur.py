import time as t
from tkinter import *
import winsound

frequency = 2000
duration = 1000

class MINUTEUR:
    def __init__(self, master,mainColor,textColor,duration):
        self.master = master
        self.mainColor = mainColor
        self.textColor =  textColor
        self.duration = duration
        self.label = Label(master, text=self.FormatTemps(self.duration), font=("arial", 40),bg=mainColor,fg=textColor)
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.start_button = Button(master, text="Start", command=self.start,font=("arial", 15),bg=mainColor,fg=textColor)
        self.start_button.place(x=15,y=315)

        self.stop_button = Button(master, text="Stop", command=self.stop,font=("arial", 15),bg=mainColor,fg=textColor)
        self.stop_button.place(x=425,y=315)

        self.reset_button = Button(master, text="Reset", command=self.reset,font=("arial", 15),bg=mainColor,fg=textColor)
        self.reset_button.place(x=215,y=315)

        self.is_running = False
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0

        
    def start(self):
        if not self.is_running:
            self.start_time = t.time()
            self.is_running = True
            self.UpdateHorloge()

    def stop(self):
        self.label.place_forget()
        self.stop_button.place_forget()
        self.reset_button.place_forget()
        if self.is_running:
            self.is_running = False

    def reset(self):
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0
        self.label.configure(text=self.FormatTemps(self.duration))

    def UpdateHorloge(self):
        if self.is_running:
            self.current_time = t.time()
            self.elapsed_time = self.current_time - self.start_time
            remaining_time = self.duration - self.elapsed_time
            if remaining_time <= 0:
                winsound.Beep(frequency, duration)
                t.sleep(0.5)
                winsound.Beep(frequency, duration)
                t.sleep(0.5)
                winsound.Beep(frequency, duration)
                self.stop()
                self.label.place_forget()
                self.start_button.place_forget()
                self.stop_button.place_forget()
                self.reset_button.place_forget()
                AppMinuteur(self.master,self.mainColor,self.textColor)
            self.label.configure(text=self.FormatTemps(remaining_time))
            self.master.after(10, self.UpdateHorloge)

    def FormatTemps(self, time):
        minutes, seconds = divmod(time, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"


class AppMinuteur :
    def __init__(self,master,mainColor,textColor):
        self.master = master
        self.mainColor = mainColor
        self.textColor = textColor
        self.zoneEntrer = Frame(master,bg=mainColor)
        self.entryMin = Entry(self.zoneEntrer,width=5,font=("arial","15"))
        self.entrySec = Entry(self.zoneEntrer,width=5,font=("arial","15"))
        self.labelMin = Label(self.zoneEntrer,text="min",font=("arial","15"),bg=mainColor,fg=textColor)
        self.labelSec = Label(self.zoneEntrer,text="s",font=("arial","15"),bg=mainColor,fg=textColor)
        self.btnBoot = Button(master,text="Demarrer",bg=mainColor,fg=textColor,font=("arial","15"),command=self.boot)
        self.btnPrereglage1 = Button(master,text="15 minutes",bg=mainColor,fg=textColor,command=self.prereglage1,font=("arial","15"))
        self.btnPrereglage2 = Button(master,text="30 minutes",bg=mainColor,fg=textColor,command=self.prereglage2,font=("arial","15"))
        
        self.zoneEntrer.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.entryMin.pack(side="left")
        self.labelMin.pack(side="left")
        self.entrySec.pack(side="left")
        self.labelSec.pack(side="left")
        self.btnBoot.place(x=205,y=315)
        self.btnPrereglage1.place(x=15,y=315)
        self.btnPrereglage2.place(x=370,y=315)
    
    def noAffichage(self):
        self.zoneEntrer.place_forget()
        self.btnBoot.place_forget()
        self.btnPrereglage1.place_forget()
        self.btnPrereglage2.place_forget()
    
    def prereglage1(self):
        self.noAffichage()
        MINUTEUR(self.master,self.mainColor,self.textColor,900)
    
    def prereglage2(self):
        self.noAffichage()
        MINUTEUR(self.master,self.mainColor,self.textColor,1800)
    
    def boot(self):
        self.noAffichage()
        min = int(self.entryMin.get())*60
        sec = int(self.entrySec.get())       
        temps = min + sec
        MINUTEUR(self.master,self.mainColor,self.textColor,temps)