from src.voice import*
from src.speechRecognition import *
from src.varInterface import*

def neuronSIX(var,genre,user,name,root,UserCourt,GenreCourt):
    
    if "change de profil" in var or "change d'utilisateur" in var:
            speak("Quelle est votre numero de profile",root)
            r = takeCommand()
            if "le premier" in r or "1" in r :
                speak("Ok bienvenu " +PrincipalUserGenre+" "+PrincipalUser,root)
                UserCourt = PrincipalUser
                GenreCourt = PrincipalUserGenre
                speak("En quoi je peux vous étre utile",root)
                return 1
            else :
                if "le deuxième" in r or "2" in r:
                    speak("Ok bienvenu " +SecondairUserGenre+" "+SecondairUser,root)
                    UserCourt = SecondairUser
                    GenreCourt = SecondairUserGenre
                    speak("En quoi je peux vous étre utile",root)
                    return 1
                else :
                    if "le troisième" in r or "3" in r:
                        speak("Ok bienvenu " +TroisiemeUserGenre+" "+TroisiemeUser,root)
                        UserCourt = TroisiemeUser
                        GenreCourt = TroisiemeUserGenre
                        speak("En quoi je peux vous étre utile",root)
                        return 1
                    else :
                        speak("Ok bienvenu " +QuatriemeUserGenre+" "+QuatriemeUser,root)
                        UserCourt = QuatriemeUser
                        GenreCourt = QuatriemeUserGenre
                        speak("En quoi je peux vous étre utile",root)
                        return 1
    else :
        if  var =="salut"   or var =="bonjour" or var =="bonsoir":
            speak(var+" en quoi je peux vous servir ?",root)
            return 1
        else :
            if "bien" in var or "oui" in var:
                speak("Sa me réjouit de savoir que tout se passe bien pour vous "+genre+" .",root)
                speak("En quoi je peux donc vous servir ?",root)
                return 1
            else :
                if "toujours là"  in var  or "es-tu là" in var or name in var :
                    speak("Oui, je suis toujours la "+genre+user+".",root)
                    return 1
                else :
                    if var == "tu es qui" or var == "présente-toi" or "présentation" in var or "qui es tu" in var or "qui es-tu" in var:
                        speak("Je suis SIX un assistant personnel crée par Baptiste Pauchet. Pour l'assistait dans l'uttilisation de son ordinateur.",root)
                        return 1
                    else :
                        return 0