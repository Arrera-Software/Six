from pytube import*
from tkinter import*
from tkinter.messagebox import showinfo
import os
import webbrowser

class ArreraVideoDownload :
    def __init__(self,color,colorbutton,textcolorbutton,textcolorlabel):
        self.screen = Tk()
        self.varChoix = StringVar(self.screen)
        self.listChoix = ["simple","playlist"]
        self.fileMusic = "musique"
        self.fileVideo = "video"
        self.screen.title("Six : Video Download")
        self.screen.config(bg=color)
        self.screen.iconphoto(False,PhotoImage(file="image/logo.png"))
        self.screen.maxsize(500,300)
        self.screen.minsize(500,300)
        #cadre
        self.cardeMain = Frame(self.screen,bg=color,width=450,height=250)
        self.cadreDownload = Frame(self.screen,bg=color,width=450,height=250)
        self.cadreWait = Frame(self.screen,bg=color,width=450,height=250)
        #entry
        self.entryURL = Entry(self.cadreDownload,width=30,border=2,font=("arial",15))
        #label
        self.labelBeinvenu = Label(self.cardeMain,text="Bienvenu sur Arrera Download",font=("arial",15),bg=color,fg=textcolorlabel)
        self.labelindiction = Label(self.cadreDownload,font=("arial",15),bg=color,fg=textcolorlabel)
        self.labelWait = Label(self.cadreWait,text="En court",font=("arial",25),bg=color,fg=textcolorlabel)
        #option menu
        self.menu = OptionMenu(self.cadreDownload,self.varChoix,*self.listChoix)
        #button
        self.boutonVideo = Button(self.cardeMain,text="Télécharger \ndes vidéos",bg=colorbutton,fg=textcolorbutton,font=("arial",15),command=self.downloadVideoView)
        self.boutonMusique = Button(self.cardeMain,text="Télécharger \ndes musiques",bg=colorbutton,fg=textcolorbutton,font=("arial",15),command=self.downloadPlaylistView)
        self.boutonRetour = Button(self.cadreDownload,text="retour",bg=colorbutton,fg=textcolorbutton,font=("arial",15),command=self.main)
        self.boutonDownload = Button(self.cadreDownload,text="Télécharger",bg=colorbutton,fg=textcolorbutton,font=("arial",15))
        self.boutonYoutube = Button(self.cadreDownload,text="Ouvrir Youtube",bg=colorbutton,fg=textcolorbutton,font=("arial",15),command= lambda : webbrowser.open("https://www.youtube.com/"))
        #affichage
        self.labelBeinvenu.place(relx=0.5, rely=0, anchor="n")
        self.boutonVideo.place(x=0,y=100)
        self.boutonMusique.place(x=313,y=100)
        
        self.labelindiction.place(x=100,y=0)
        self.menu.place(x=0,y=0)
        self.entryURL.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.boutonRetour.place(x=0,y=210)
        self.boutonDownload.place(x=330,y=210)
        self.boutonYoutube.place(relx=0.5, rely=1.0, anchor="s")
        
        self.labelWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        self.main()
        
        self.screen.mainloop()
    
    def downloadVideoSimple(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download(self.fileVideo)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideoPlaylist(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download(self.fileVideo)      
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiqueSimple(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download(self.fileMusic)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiquePlaylist(self):
        self.waitView()
        valURL = self.entryURL.get()
        self.entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download(self.fileMusic)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideo(self):
        var = self.varChoix.get()
        if var == "simple" :
            self.downloadVideoSimple()
        else :
            self.downloadVideoPlaylist()
    
    def downloadMusique(self):
        var = self.varChoix.get()
        if var == "simple" :
            self.downloadMusiqueSimple()
        else :
            self.downloadMusiquePlaylist()
    
    def main(self):
        self.cadreDownload.place_forget()
        self.cardeMain.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def downloadView(self):
        self.cardeMain.place_forget()
        self.cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.varChoix.set(self.listChoix[0])
        
    def waitView(self):
        self.cadreDownload.place_forget()
        self.cadreWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def waitNoView(self):
        self.cadreWait.place_forget()
        self.cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)

    
    def downloadVideoView(self):
        self.labelindiction.configure(text="Copier L'URL d'une video")
        self.downloadView()
        self.boutonDownload.config(command=self.downloadVideo)
        self.boutonRetour.config(command=self.main)
        
    def downloadPlaylistView(self):
        self.labelindiction.configure(text="Copier L'URL d'une musique")
        self.downloadView()
        self.boutonDownload.config(command=self.downloadMusique)
        self.boutonRetour.config(command=self.main)