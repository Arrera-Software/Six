from src.varInterface import*


def neuroneUser(var):
    if "passe à l'utilisateur 1" in var or "l'utilisateur 1"in var or "utilisateur 1" in var or "utilisateur numéro 1" in var:
        return 1,0
    else :
        if "passe à l'utilisateur 2" in var or "l'utilisateur 2"in var or "utilisateur 2" in var or "utilisateur numéro 2" in var:
            return 2,0
        else :
            if "passe à l'utilisateur 3" in var or "l'utilisateur 3"in var or "utilisateur 3" in var or "utilisateur numéro 3" in var:
                return 3,0
            else :
                if "passe à l'utilisateur 4" in var or "l'utilisateur 4"in var or "utilisateur 4" in var or "utilisateur numéro 4" in var:
                    return 4,0
                else :
                    return 0,0