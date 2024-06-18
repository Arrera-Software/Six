from ArreraNeuron.ObjetsNetwork.arreraNeuron import*

class CArreraSix :
    def __init__(self,userFile:str,neuronConfig:str,listFete:str):
        # Atribut sortie 
        self.__nbSortie = int 
        self.__listSortie = []
        # Mise de parametre dans des atribut 
        self.__userFile = userFile
        self.__fileNeuronConfig = neuronConfig
        self.__fileListeFete = listFete
        # Declaration de l'objet Arrera Neuron Network
        self.__neuronArrera = ArreraNetwork(self.__userFile,
                                            self.__fileNeuronConfig,
                                            self.__fileListeFete)
    
    def boot(self):
        return self.__neuronArrera.boot()

    def neuron(self,texte:str):
        self.__nbSortie,self.__listSortie = self.__neuronArrera.neuron(texte)
    
    def getNbSortie(self):
        return self.__nbSortie
    
    def getListSortie(self):
        return self.__listSortie