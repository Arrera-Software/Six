from librairy.travailJSON import*
from librairy.dectectionOS import*
from librairy.gestionSoftWindows import*

class CArreraGazelle :
    def __init__(self,emplacementJsonUser:str,emplacementJsonNeuronNetwork:str,emplacementJsonAssistant:str):
        # Fichier json
        self.__fileJsonUser = jsonWork(emplacementJsonUser)
        self.__fileJsonNeuronNetwork = jsonWork(emplacementJsonNeuronNetwork)
        self.__fileJsonAssistant = jsonWork(emplacementJsonAssistant)
        # Objet 
        self.__objOS = OS()
        if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
            self.__softWin = gestionSoftWindows(self.__fileJsonNeuronNetwork.lectureJSON("emplacementSoftWindows"))
    
    def changeUserName(self,newName:str):
        self.__fileJsonUser.EcritureJSON("user",newName)
    
    def changeUserGenre(self,newGenre:str):
        self.__fileJsonUser.EcritureJSON("genre",newGenre)
    
    def ajoutVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if (mode == 1 ):
            self.__fileJsonUser.EcritureJSON("lieuDomicile",ville)
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.EcritureJSON("lieuTravail",ville)
                return True
            else :
                if (mode==3):
                    self.__fileJsonUser.EcritureJSONList("listVille",ville)
                    return True
                else :
                    return False
    
    def supprVilleMeteo(self,mode:int,ville:str):
        """
        1 : domicile
        2 : Travail 
        3 : Autre
        """
        if (mode == 1 ):
            self.__fileJsonUser.suppressionJson("lieuDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("lieuTravail")
                return True
            else :
                if ((mode==3)and(ville != "")):
                    self.__fileJsonUser.suppressionJsonList("listVille",ville)
                    return True
                else :
                    return False
    
    def getMeteoSave(self):
        listeMeteo = []
        if (self.__fileJsonUser.lectureJSON("lieuDomicile") != ""):
            listeMeteo.append("Lieu d'habitation enregister")

        if (self.__fileJsonUser.lectureJSON("lieuTravail") != ""):
            listeMeteo.append("Lieu de travail enregister")
        
        listeMeteo = listeMeteo+self.__fileJsonUser.lectureJSONList("listVille")

        return listeMeteo

    def ajoutGPSAdresse(self,mode:int,adresse:str):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.EcritureJSON("adresseDomicile",adresse)
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.EcritureJSON("adresseTravail",adresse)
                return True
            else :
                return False
    
    def supprGPSAdresse(self,mode:int):
        """
        1 : Adresse domicile
        2 : Adresse lieu de travail
        """
        if (mode==1):
            self.__fileJsonUser.suppressionJson("adresseDomicile")
            return True
        else :
            if (mode==2):
                self.__fileJsonUser.suppressionJson("adresseTravail")
                return True
            else :
                return False
    
    def addSoft(self,mode:int,name:str,command:str):
        """
        1 : Normal 
        2 : Traitement de texte
        3 : Tableur
        4 : Presentation
        5 : Navigateur
        6 : Musique
        7 : note
        """
        if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)and(self.__fileJsonNeuronNetwork.lectureJSON("emplacementSoftWindows")=="")):
            self.__fileJsonNeuronNetwork.EcritureJSON("emplacementSoftWindows",self.__softWin.setEmplacementSoft())
        
        if ((self.__objOS.osLinux()==True)and(self.__objOS.osWindows()==False)):
            if (command==""):
                return False
            else :
                match mode :
                    case 1 : # Normal 
                        if (name!=""):
                            self.__fileJsonUser.EcritureJSONDictionnaire("dictSoftLinux",name,command)
                            self.__fileJsonUser.EcritureJSON("nbSoft",str(int(self.__fileJsonUser.lectureJSON("nbSoft"))+1))
                            return True
                    case 2 : # Traitement de texte
                        self.__fileJsonUser.EcritureJSON("wordLinux",command)
                        return True
                    case 3 : # Tableur
                        self.__fileJsonUser.EcritureJSON("exelLinux",command)
                        return True
                    case 4 : # Presentation
                        self.__fileJsonUser.EcritureJSON("diapoLinux",command)
                        return True
                    case 5 : # Navigateur
                        self.__fileJsonUser.EcritureJSON("browserLinux",command)
                        return True
                    case 6 : # Musique
                        self.__fileJsonUser.EcritureJSON("musicLinux",command)
                        return True
                    case 7 : # note
                        self.__fileJsonUser.EcritureJSON("noteLinux",command)
                        return True
        else :
                
            if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                match mode :
                    case 1 : # Normal 
                        if (name!=""):
                            self.__softWin.setName(name)
                            sortie = self.__softWin.saveSoftware()
                            if (sortie == True) :
                                self.__fileJsonUser.EcritureJSONDictionnaire("dictSoftWindows",name,self.__softWin.getName())
                                self.__fileJsonUser.EcritureJSON("nbSoft",str(int(self.__fileJsonUser.lectureJSON("nbSoft"))+1))
                                return True
                            else :
                                return False
                        else :
                            return False
                    case 2 : # Traitement de texte
                        self.__softWin.setName("ttexte")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("wordWindows",self.__softWin.getName())
                            return True
                        else :
                            return False 
                    case 3 :  # Tableur
                        self.__softWin.setName("tableur")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("exelWindows",self.__softWin.getName())
                            return True
                        else :
                            return False 
                    case 4 : # Presentation
                        self.__softWin.setName("presentation")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("diapoWindows",self.__softWin.getName())
                            return True
                        else :
                            return False
                    case 5 : # Navigateur
                        self.__softWin.setName("browser")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("browserWindows",self.__softWin.getName())
                            return True
                        else :
                            return False 
                    case 6 : # Musique
                        self.__softWin.setName("musique")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("musicWindows",self.__softWin.getName())
                            return True
                        else :
                            return False
                    case 7 :  # note
                        self.__softWin.setName("note")
                        sortie = self.__softWin.saveSoftware()
                        if (sortie == True) :
                            self.__fileJsonUser.EcritureJSON("noteWindows",self.__softWin.getName())
                            return True
                        else :
                            return False
                        
    def supprSoft(self,mode:int,name:str):
        """
        1 : Normal 
        2 : Traitement de texte
        3 : Tableur
        4 : Presentation
        5 : Navigateur
        6 : Musique
        7 : note
        """
        # Creation listFlag 
        if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
            listFlag = ["dictSoftWindows","wordWindows","exelWindows","diapoWindows","browserWindows","noteWindows","musicWindows"]
        else : 
            if ((self.__objOS.osLinux()==True)and(self.__objOS.osWindows()==False)):
                listFlag = ["dictSoftLinux","wordLinux","exelLinux","diapoLinux","browserLinux","noteLinux","musicLinux"]
            else :
                return False
        match mode : 
            case 1 : # Normal 
                self.__fileJsonUser.supprJSONList(listFlag[0],name)
                self.__fileJsonUser.EcritureJSON("nbSoft",str(int(self.__fileJsonUser.lectureJSON("nbSoft"))-1))
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft(name)
                return True
            case 2 : # Traitement de texte
                self.__fileJsonUser.suppressionJson(listFlag[1])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("ttexte")
                return True
            case 3 : # Tableur
                self.__fileJsonUser.suppressionJson(listFlag[2])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("tableur")
                return True
            case 4 : # Presentation 
                self.__fileJsonUser.suppressionJson(listFlag[3])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("presentation")
                return True
            case 5 : # Navigateur 
                self.__fileJsonUser.suppressionJson(listFlag[4])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("browser")
                return True
            case 6 : # Musique 
                self.__fileJsonUser.suppressionJson(listFlag[6])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("note")
                return True
            case 7 : # Musique 
                self.__fileJsonUser.suppressionJson(listFlag[5])
                if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
                    self.__softWin.supprSoft("musique")
                return True
        
    def getListSoft(self):
        listSortie = []
        # Creation listFlag 
        if ((self.__objOS.osLinux()==False)and(self.__objOS.osWindows()==True)):
            listFlag = ["dictSoftWindows","wordWindows","exelWindows","diapoWindows","browserWindows","noteWindows","musicWindows"]
        else : 
            if ((self.__objOS.osLinux()==True)and(self.__objOS.osWindows()==False)):
                listFlag = ["dictSoftLinux","wordLinux","exelLinux","diapoLinux","browserLinux","noteLinux","musicLinux"]
            else :
                return ["error","error"]
        if(self.__fileJsonUser.lectureJSON(listFlag[1])!=""):
            listSortie.append("Traitement de texte")
    
        if(self.__fileJsonUser.lectureJSON(listFlag[2])!=""):
            listSortie.append("Tableur")
        
        if(self.__fileJsonUser.lectureJSON(listFlag[3])!=""):
            listSortie.append("Presentation")
        
        if(self.__fileJsonUser.lectureJSON(listFlag[4])!=""):
            listSortie.append("Navigateur internet")
        
        if(self.__fileJsonUser.lectureJSON(listFlag[5])!=""):
            listSortie.append("Note")
        
        if(self.__fileJsonUser.lectureJSON(listFlag[6])!=""):
            listSortie.append("Musique")
        
        # Recuperation du dictionnaire
        dictSoft = self.__fileJsonUser.lectureJSONDict(listFlag[0])

        if (len(dictSoft)!=0) :
            listSortie = listSortie+(list(dictSoft.keys()))

        return listSortie

    def addSite(self,mode:int,name:str,link:str):
        """
        1 : normal
        2 : lien cloud
        """
        if (link == "") :
            return False

        match mode :
            case 1 :
                if (name==""):
                    return False 
                self.__fileJsonUser.EcritureJSONDictionnaire("dictSite",name,link)
                self.__fileJsonUser.EcritureJSON("nbSite",str(int(self.__fileJsonUser.lectureJSON("nbSite"))+1))
                return True
            case 2 : 
                self.__fileJsonUser.EcritureJSON("lienCloud",link)
                return True
    
    def supprSite(self,mode:int,name:str):
        """
        1 : normal
        2 : lien cloud
        """
        match mode :
            case 1 :
                if (name==""):
                    return False 
                self.__fileJsonUser.supprJSONList("dictSite",name)
                self.__fileJsonUser.EcritureJSON("nbSite",str(int(self.__fileJsonUser.lectureJSON("nbSite"))-1))
                return True
            case 2 : 
                self.__fileJsonUser.suppressionJson("lienCloud")
                return True
    
    def getListSite(self):
        listSortie = []
        if (self.__fileJsonUser.lectureJSON("lienCloud")!=""):
            listSortie.append("Cloud")
        dictSite = self.__fileJsonUser.lectureJSONDict("dictSite")
        if (len(dictSite)==0):
            return listSortie
        else :
            return listSortie + list(dictSite.keys())

    def changeMoteur(self,moteur:str):
        self.__fileJsonUser.EcritureJSON("moteurRecherche",moteur)
        return True
    
    def changeTheme(self,theme:str):
        self.__fileJsonAssistant.EcritureJSON("theme",theme)
        return True
    
    def changeSoundMicro(self,enable:bool):
        if(enable==False):
            self.__fileJsonAssistant.EcritureJSON("soundMicro","0")
            return True
        else :
            if(enable==True):
                self.__fileJsonAssistant.EcritureJSON("soundMicro","1")
                return True
            else :
                return False
    
    def getSoundMicroAsEnable(self):
        sortie = self.__fileJsonAssistant.lectureJSON("soundMicro")
        if (sortie=="1"):
            return True
        else :
            return False
    
    def getOS(self):
        linux = self.__objOS.osLinux()
        windows = self.__objOS.osWindows()
        if ((linux==True)and (windows==False)):
            return "linux"
        else :
            if ((linux==False)and (windows==True)):
                return "windows"
            else :
                return "other"