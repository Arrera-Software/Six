from tkinter import*

class Acceuil : 
    def __init__(self,master,mainColor,textColor,img):
        self.master = master
        self.label = Label(master,image=img,bg=mainColor)
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)