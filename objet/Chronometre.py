import time as t
from tkinter import *

class CHRONOMETRE:
    def __init__(self, master):
        self.master = master
        self.label = Label(master, text="00:00", font=("arial", 20),bg="#3c0f14",fg="white")
        self.label.pack()

        self.start_button = Button(master, text="Start", command=self.start ,font=("arial", 15),bg="white",fg="black")
        self.start_button.place(x=30,y=105)

        self.stop_button = Button(master, text="Stop", command=self.stop ,font=("arial", 15),bg="white",fg="black")
        self.stop_button.place(x=400,y=105)

        self.reset_button = Button(master, text="Reset", command=self.reset ,font=("arial", 15),bg="white",fg="black")
        self.reset_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.is_running = False
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0

    def start(self):
        if not self.is_running:
            self.start_time = t.time()
            self.is_running = True
            self.UpdateTemps()

    def stop(self):
        if self.is_running:
            self.is_running = False

    def reset(self):
        self.current_time = 0
        self.start_time = 0
        self.elapsed_time = 0
        self.label.configure(text="00:00")

    def UpdateTemps(self):
        if self.is_running:
            self.current_time = t.time()
            self.elapsed_time = self.current_time - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            self.label.configure(text=f"{int(minutes):02d}:{int(seconds):02d}")
            self.master.after(10, self.UpdateTemps)
