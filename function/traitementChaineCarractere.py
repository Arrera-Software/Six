def passageLigne(text, nbMots):#passe le text passer a la fonction au bout du nombre de mots que est definie a l'appel de la fonction
        mots = text.split()
        newText = ""
        ligne = ""
        for i, mot in enumerate(mots):
            ligne += mot + " "
            if (i + 1) % nbMots == 0:
                newText += ligne + "\n"
                ligne = ""
            elif i == len(mots) - 1:
                newText += ligne
        return newText