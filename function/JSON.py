import json

def lectureJSON(file,flag):
    with open(file, 'r') as openfile:
        dict = json.load(openfile)[flag]
    return dict