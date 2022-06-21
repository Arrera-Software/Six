import speech_recognition as sr

def Micro():
    Micro = sr.Recognizer()
    with sr.Microphone() as sources:
        audio = Micro.listen(sources)
    try :
        textsearch = Micro.recognize_google(audio ,language="fr-FR")
        return textsearch
    except sr.UnknownValueError: 
        return "Error"