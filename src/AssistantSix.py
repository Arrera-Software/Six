from ObjetsNetwork.arreraNeuron import*

class CArreraSix :
    def __init__(self,neuronConfig:str):
        # Atribut sortie 
        self.__nbSortie = int 
        self.__listSortie = []
        # Mise de parametre dans des atribut
        # Declaration de l'objet Arrera Neuron Network
        self.__neuronArrera = ArreraNetwork(neuronConfig)
    
    def boot(self):
        return self.__neuronArrera.boot(2)

    def shutdown(self):
        return self.__neuronArrera.shutdown()

    def neuron(self,texte:str):
        self.__neuronArrera.neuron(texte)
    
    def getNbSortie(self):
        return self.__neuronArrera.getValeurSortie()
    
    def getListSortie(self):
        return self.__neuronArrera.getListSortie()