import json

def lectureJSON(file,flag):
    with open(file, 'r') as openfile:
        dict = json.load(openfile)[flag]
    return str(dict)

def EcritureJSON(file,flag,valeur):
    openfile = open(file, 'r')
    dict = json.load(openfile)
    openfile.close()
    writeFile = open(file, 'w')
    dict[flag] = valeur
    json.dump(dict,writeFile,indent=2)