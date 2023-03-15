from src.srcSix import *
from function.reading import*
from function.openSofware import ouvertureAide 

import random

def Main(var,genre,user,name,root,UserCourt,GenreCourt,police):
        if "raconter une blague" in var or "raconte-moi une blague" in var :
            nb = random.randint(1,10)
            blague = ["Que dit une noisette quand elle tombe dans l’eau ?"
                          ,"Comment est-ce que les abeilles communiquent entre elles ?"
                          ,"Quel est l’arbre préféré du chômeur ?","Qu’est-ce qu’une frite enceinte ?"
                          ,"Que dit une mère à son fils geek quand le dîner est servi ?"
                          ,"Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?"
                          ,"Pourquoi les Ch’tis aiment les fins de vacances au camping ?"
                          ,"Quelle est la partie de la voiture la plus dangereuse ?"
                          ,"Pourquoi dit-on que les poissons travaillent illégalement ?"
                          ,"Mettre du sirop dans son gel douche"
                          ]
            reponseBlague=["Je me noix."
                               ,"Par-miel."
                               ,"Le bouleau."
                               ,"Une patate sautée."
                               ,"Alt Tab !"
                               ,"Marcher"
                               ,"Parce que c’est le moment où ils peuvent démonter leur tente."
                               ,"La conductrice."
                               ,"Parce qu'ils n'ont pas de FISH de paie"
                               ,"En fait, dans tous les gels douches. Qu’une fois dans la salle de bain il n’y ait aucune issue possible."
                               ]
            SIXsrc(root,police).speak(blague[nb])
            time.sleep(1.5)
            SIXsrc(root,police).speak(reponseBlague[nb])
            return 1
        else :
            if "peux-tu me lire un truc" in var :
                SIXsrc(root,police).speak("Copier ce que vous voulez  que je vous lise "+genre+".")
                Reading(root,police)
                return 1
            else :
                if  var =="salut"   or var =="bonjour" or var =="bonsoir":
                    SIXsrc(root,police).speak(var+" en quoi je peux vous servir ?")
                    return 1
                else :
                    if "bien" in var or "oui" in var:
                        SIXsrc(root,police).speak("Sa me réjouit de savoir que tout se passe bien pour vous "+genre+" .")
                        SIXsrc(root,police).speak("En quoi je peux donc vous servir ?")
                        return 1
                    else :
                        if "toujours là"  in var  or "es-tu là" in var or name in var :
                            SIXsrc(root,police).speak("Oui, je suis toujours la "+genre+user+".")
                            return 1
                        else :
                            if "tu es qui" in var or "présente-toi" in var or "présentation" in var or "qui es tu" in var or "qui es-tu" in var:
                                SIXsrc(root,police).speak("Je suis SIX un assistant personelle. Comment je peux vous aidez ?")
                                return 1
                            else :
                                if "ouvre-moi la page d'aide" in var :
                                    SIXsrc(root,police).speak("Ok je vous ouvre la page d'aide")
                                    ouvertureAide()
                                    return 1
                                else :
                                    return 0