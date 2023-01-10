class CalculeNbComplexe :
    def aditionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
        nb1 = complex(nb1_1,nb1_2)
        nb2 = complex(nb2_1,nb2_2)
        resultat = nb1 + nb2
        return nb1,nb2,resultat
    def soustrationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
        nb1 = complex(nb1_1,nb1_2)
        nb2 = complex(nb2_1,nb2_2)
        resultat = nb1 - nb2
        return nb1,nb2,resultat
    def multiplicationNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
        nb1 = complex(nb1_1,nb1_2)
        nb2 = complex(nb2_1,nb2_2)
        resultat = nb1 * nb2
        return nb1,nb2,resultat
    def divisionNbComplex(nb1_1,nb1_2,nb2_1,nb2_2):
        nb1 = complex(nb1_1,nb1_2)
        nb2 = complex(nb2_1,nb2_2)
        resultat = nb1 / nb2
        return nb1,nb2,resultat