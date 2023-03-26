import json

def lectureJSON(file,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction
    with open(file, 'r' , encoding='utf-8') as openfile:
        dict = json.load(openfile)[flag]
    return str(dict)

def lectureJSONDict(file,flag): # Permet de lire la valeur du flag defini a l'appel de la fonction et de le retourner sous forme de dictionnaire
    with open(file, 'r', encoding='utf-8') as openfile:
        dict = json.load(openfile)[flag]
    return dict

def lectureSimpleJSON(file):#Permet de juste recuperer le contenu d'un fichier JSON
    with open(file, 'r', encoding='utf-8') as openfile:
        dict = json.load(openfile)
    return dict

def EcritureJSON(file,flag,valeur):#Permet d'ecrire une nouvelle valeur a flag definie
    openfile = open(file, 'r', encoding='utf-8')
    dict = json.load(openfile)
    openfile.close()
    writeFile = open(file, 'w', encoding="utf-8")
    dict[flag] = valeur
    json.dump(dict,writeFile,indent=2, ensure_ascii=False)

def EcritureSansEcrasement(file,vardict,newDictName):#Permet d'ecrire un nouveau dictionnaire dans le fichier
    with open(file, 'r', encoding='utf-8') as openfile:
        dict1 = json.load(openfile)
    with open(file,"w") as file :
        newdict = {newDictName : vardict} 
        alldict = dict(dict1,**newdict)
        json.dump(alldict,file,indent=2)
        
def EcritureEcrasement(file,dictionnaire):#Permet d'ecrire dans un json en efacent son contenue
    with open(file, "w") as f:
        json.dump(dictionnaire, f,indent=2)

def compteurJSON(file):#Permet de compter le nombre de valeur dans un dictionnaire
    with open(file, 'r', encoding='utf-8') as openfile:
        dict1 = json.load(openfile)
        return len(dict1)
    
def searchKey(valeur, dict):
    for cle, val in dict.items():
        if val == valeur:
            return cle
    return None