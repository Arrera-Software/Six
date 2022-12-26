import time as t
from tkinter import *
import winsound

frequency = 2000
duration = 1000

class MINUTEUR:
    def __init__(self, master, duration):
        self.master = master
        self.duration = duration
        self.label = Label(master, text=self.FormatTemps(self.duration), font=("arial", 20),bg="#3c0f14",fg="white")
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        #self.start_button = Button(master, text="Start", command=self.start,font=("arial", 15),bg="white",fg="#3c0f14")
        #self.start_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop,font=("arial", 15),bg="white",fg="black")
        self.stop_button.place(x=30,y=40)

        self.reset_button = Button(master, text="Reset", command=self.reset,font=("arial", 15),bg="white",fg="black")
        self.reset_button.place(x=400,y=40)

        self.is_running = False
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0

        self.start()
        
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
                self.stop_button.place_forget()
                self.reset_button.place_forget()
            self.label.configure(text=self.FormatTemps(remaining_time))
            self.master.after(10, self.UpdateHorloge)

    def FormatTemps(self, time):
        minutes, seconds = divmod(time, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"
 