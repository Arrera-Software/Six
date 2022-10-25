import speech_recognition as sr

def takeCommand():#Fonction micro et reconaissance vocal
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            Requette=r.recognize_google(audio,language='fr')
            print(Requette)
        except Exception as e:
            return "None" 
        return Requette