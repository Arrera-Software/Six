from tkinter.messagebox import *
from tkinter import*
from pytube import YouTube , Playlist
import os

Color = "#3c0f14"
TextColor = "white"

def YoutubeDownload():
    screen = Tk()
    screen.title("Youtube Downloader")
    screen.config(bg=Color)
    screen.maxsize(500,600)
    screen.minsize(500,600)
    LabelVideo = Label(screen,text= "Video",bg=Color,fg="white",font=("arial","25"))
    CadreVideo = Frame(screen,bg=Color,width=400,height=100)
    LabelVideo2 = Label(screen,text= "Playlist Video",bg=Color,fg="white",font=("arial","25"))
    CadreVideo2 = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic = Label(screen,text= "Musique",bg=Color,fg="white",font=("arial","25"))
    CadreMusic = Frame(screen,bg=Color,width=400,height=100)
    LabelMusic2 = Label(screen,text= "Playlist Musique",bg=Color,fg="white",font=("arial","25"))
    CadreMusic2 = Frame(screen,bg=Color,width=400,height=100)
    #Label
    LabelURL1 = Label(CadreVideo,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL2 = Label(CadreVideo2,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL3 = Label(CadreMusic,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    LabelURL4 = Label(CadreMusic2,text="Taper l'URL",fg="white",bg=Color,font=("arial","15"))
    #Entry
    EntryURL1 = Entry(CadreVideo,width=75)
    EntryURL2 = Entry(CadreVideo2,width=75)
    EntryURL3 = Entry(CadreMusic,width=75)
    EntryURL4 = Entry(CadreMusic2,width=75)
    #Fonction
    def AffichageCadre():
        LabelVideo.pack()
        CadreVideo.pack()
        LabelVideo2.pack()
        CadreVideo2.pack()
        LabelMusic.pack()
        CadreMusic.pack()
        LabelMusic2.pack()
        CadreMusic2.pack()
    
    def Download1():
        URL = str(EntryURL1.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download("video")
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        
    def Download2():
        URL = str(EntryURL2.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download("video")
        showinfo(title="Youtube Downloader",message="Videos Télécharger")
        
    def Download3():
        URL = str(EntryURL3.get())
        Media = YouTube(URL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download("musique")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Musique Télécharger")
        
    def Download4():
        URL = str(EntryURL4.get())
        playlist = Playlist(URL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download("musique")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Musiques Télécharger")
        
    #Bouton
    BoutonDownload1 = Button(CadreVideo,text="Télécharger",bg=Color,fg="white",command=Download1)
    BoutonDownload2 = Button(CadreVideo2,text="Télécharger",bg=Color,fg="white",command=Download2)
    BoutonDownload3 = Button(CadreMusic,text="Télécharger",bg=Color,fg="white",command=Download3)
    BoutonDownload4 = Button(CadreMusic2,text="Télécharger",bg=Color,fg="white",command=Download4)
    #Affichage
    AffichageCadre()
    LabelURL1.place(x="150",y="0")
    LabelURL2.place(x="150",y="0")
    LabelURL3.place(x="150",y="0")
    LabelURL4.place(x="150",y="0")
    EntryURL1.place(x="10",y="30")
    EntryURL2.place(x="10",y="30")
    EntryURL3.place(x="10",y="30")
    EntryURL4.place(x="10",y="30")
    BoutonDownload1.place(x="150",y="60")
    BoutonDownload2.place(x="150",y="60")
    BoutonDownload3.place(x="150",y="60")
    BoutonDownload4.place(x="150",y="60")
    screen.mainloop()