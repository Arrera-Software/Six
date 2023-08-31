import pygame
from  pygame.locals import *
from function.JSON import *
lienMain = ["image/interface/interfaceDefault.png","image/interface/interfaceLIght.png","image/interface/interfaceDark.png"]
lienMute = ["image/interface/interfaceDefaultMute.png","image/interface/interfaceLIghtMute.png","image/interface/interfaceDarkMute.png"]
lienParole1 = ["image/interface/interfaceDefaultVoice1.png","image/interface/interfaceLIghtVoice1.png","image/interface/interfaceDarkVoice1.png"]
lienParole2 = ["image/interface/interfaceDefaultVoice2.png","image/interface/interfaceLIghtVoice2.png","image/interface/interfaceDarkVoice2.png"]
lienParole3 = ["image/interface/interfaceDefaultVoice3.png","image/interface/interfaceLIghtVoice3.png","image/interface/interfaceDarkVoice3.png"]
lienFenetre = ["image/interface/interfaceDefaultFenetre.png","image/interface/interfaceLIghtFenetre.png","image/interface/interfaceDarkFenetre.png"]

principalUser =  lectureJSON("setting/config.json","user1")
secondairUser =  lectureJSON("setting/config.json","user2")
troisiemeUser =  lectureJSON("setting/config.json","user3")
quatriemeUser =  lectureJSON("setting/config.json","user4")
principalUserGenre = lectureJSON("setting/config.json","userGenre1")
secondairUserGenre =  lectureJSON("setting/config.json","userGenre2")
troisiemeUserGenre =  lectureJSON("setting/config.json","userGenre3")
quatriemeUserGenre =  lectureJSON("setting/config.json","userGenre4") 

def GUIMain():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienMain[0])
    else :
        if var == "white" :
            return pygame.image.load(lienMain[1])
        else :
            return pygame.image.load(lienMain[2])
def GUIMute():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienMute[0])
    else :
        if var == "white" :
            return pygame.image.load(lienMute[1])
        else :
            return pygame.image.load(lienMute[2])
def GUIparole1():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienParole1[0])
    else :
        if var == "white" :
            return pygame.image.load(lienParole1[1])
        else :
            return pygame.image.load(lienParole1[2])   

def GUIparole2():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienParole2[0])
    else :
        if var == "white" :
            return pygame.image.load(lienParole2[1])
        else :
            return pygame.image.load(lienParole2[2])  

def GUIparole3():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienParole3[0])
    else :
        if var == "white" :
            return pygame.image.load(lienParole3[1])
        else :
            return pygame.image.load(lienParole3[2])    

def GUItextColor():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return (255,255,255)
    else :
        if var == "white" :
            return (0,0,0)
        else :
            return (255,255,255) 

def GUIOpenFentreTkinter():
    var = lectureJSON("setting/config.json","theme")
    if var == "default" :
        return pygame.image.load(lienFenetre[0])
    else :
        if var == "white":
            return pygame.image.load(lienFenetre[1])
        else :
            return pygame.image.load(lienFenetre[2])

rootWidht = 600
rootHeight = 200
fondMute = GUIMute()
fond = GUIMain()
fondFenetre = GUIOpenFentreTkinter()
fondParole1 = GUIparole1()
fondParole2 = GUIparole2()
fondParole3 = GUIparole3()
ColorText = GUItextColor()