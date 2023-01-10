import numpy as np

class Pythagore :
    def theoemePythagore(self,nb1,nb2):
        resultat = np.sqrt((np.square(nb1)+np.square(nb2)))
        return str(format(resultat,".6f"))
    def ReciproquePythagore(self,nb1,nb2):
        resultat = int(np.sqrt((np.square(nb1)-np.square(nb2))))
        return str(format(resultat,".6f"))