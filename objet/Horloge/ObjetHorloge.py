from tkinter import*
import time

class Clock() :
    def __init__(self,master,mainColor,textColor):
        self.master = master
        self.clock = Label(master, font = ("arial", 60, "bold"),bg=mainColor,fg=textColor)
        self.clock.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.time()

    def time(self): 
        self.running = True
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        self.master.after(10,self.time)
