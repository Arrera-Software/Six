from lib.arrera_tk import aLabel

class six_speak(aLabel):
    def __init__(self,master):
        super().__init__(master,text="", wraplength=440,justify="left",police_size=20,corner_radius=0)

    def set_text(self,texte:str):
        self.configure(text=texte)

    def view_during_speak(self):
        self.configure(fg_color="#2b3ceb", text_color="white")
        self.place(x=30, y=110)
        self.master.update()

    def view_after_speak(self):
        self.configure(fg_color=("#ffffff","#000000"),text_color=("#000000","#ffffff"))
        self.place(x=10, y=80)
        self.master.update()

    def unview(self):
        self.place_forget()
        self.master.update()