import random
from ObjetsNetwork.gestion import*
class formule : 
    def __init__(self,gestionnaireNeuron:gestionNetwork):
        self.vous = bool(gestionnaireNeuron.getVous())
        self.genre = str(gestionnaireNeuron.getGenre())
        self.user  = str(gestionnaireNeuron.getUser())
    
    def nocomprehension(self):
        if self.vous == True:
            text = "Je ne comprend ce que vous m'avez dit ou je ne peux pas vous répondre a votre demande"
        else : 
            text = "Je ne comprend ce que tu m'as dit ou ce que tu demande m'est imposible a repondre"   
        return text
        
    def salutation(self, hour):
        if hour >= 0 and hour < 3:
            if self.vous:
                formule = "Bonjour,"
                cmp = self.genre + " " + self.user
                phrase = ["Que faites-vous si tôt ?", "J'espère que vous avez un peu dormi."]
            else:
                formule = "Zzzz"
                cmp = self.user
                phrase = ["Il faudrait peut-être dormir, non ?", "Comment peux-tu travailler si tard ?"]
        else:
            if hour >= 3 and hour <= 6:
                if self.vous:
                    formule = "Bonjour,"
                    cmp = self.genre + " " + self.user
                    phrase = ["Êtes-vous prêt à travailler ?", ""]
                else:
                    formule = "Zzzz"
                    cmp = self.user
                    phrase = ["Il faudrait peut-être dormir, non ?", "Comment peux-tu travailler si tard ?"]
            else:
                if hour >= 6 and hour <= 10:
                    if self.vous:
                        formule = "Bonjour, "
                        cmp = self.genre + " " + self.user
                        phrase = ["J'espère que vous avez passé une bonne nuit.", "J'espère que vous avez bien dormi."]
                    else:
                        formule = "Hey,"
                        cmp = self.user
                        phrase = ["As-tu bien dormi ?", "As-tu passé une bonne nuit ?"]
                else:
                    if hour >= 10 and hour <= 12:
                        if self.vous:
                            formule = "Bonjour, "
                            cmp = self.genre + " " + self.user
                            phrase = ["J'espère que vous passez une bonne matinée.", "J'espère que vous passez un bon début de journée."]
                        else:
                            formule = "Salut,"
                            cmp = self.user
                            phrase = ["Comment se passe ta matinée ?", "Que fais-tu de beau ce matin ?"]
                    else:
                        if hour >= 13 and hour <= 14:
                            if self.vous:
                                formule = "Bonjour,"
                                cmp = self.genre + " " + self.user
                                phrase = ["J'espère que vous passez une bonne après-midi ?", ""]
                            else:
                                formule = "Alors"
                                cmp = self.user
                                phrase = ["Prêt à travailler ?", "Es-tu prêt à travailler cet après-midi ?"]
                        else:
                            if hour >= 15 and hour <= 18:
                                if self.vous:
                                    formule = "Bonjour,"
                                    cmp = self.genre + " " + self.user
                                    phrase = ["Sur quoi puis-je vous aider cet après-midi ?", "Comment puis-je vous aider ?"]
                                else:
                                    formule = "Salut,"
                                    cmp = self.user
                                    phrase = ["Sur quoi travailles-tu ?", "En quoi puis-je t'aider ?"]
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.vous:
                                        formule = "Bonsoir,"
                                        cmp = self.genre + " " + self.user
                                        phrase = ["Comment se passe votre début de soirée ?", "J'espère que votre début de soirée se passe bien."]
                                    else:
                                        formule = "Alors"
                                        cmp = self.user
                                        phrase = ["Que veux-tu faire ce soir ?", "Veux-tu travailler ou te divertir ce soir ?"]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.vous:
                                            formule = "Bonsoir,"
                                            cmp = self.genre + " " + self.user
                                            phrase = ["Comment se passe votre soirée ?", "J'espère que votre soirée s'est bien passée."]
                                        else:
                                            formule = "*bâille*"
                                            cmp = self.user
                                            phrase = ["Que fais-tu si tard ?", "Pourquoi me réveilles-tu si tard ?"]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.vous:
                                                formule = "Bonjour,"
                                                cmp = self.genre + " " + self.user
                                                phrase = ["Que faites-vous si tôt ?", "J'espère que vous avez un peu dormi."]
                                            else:
                                                formule = "Zzzz"
                                                cmp = self.user
                                                phrase = ["Il faudrait peut-être dormir, non ?", "Comment peux-tu travailler si tard ?"]
                                        else:
                                            if self.vous:
                                                formule = "Bonjour,"
                                                cmp = self.genre + " " + self.user
                                                phrase = ["Que voulez-vous qu'on fasse ?", ""]
                                            else:
                                                formule = "Salut,"
                                                cmp = self.user
                                                phrase = ["Que veux-tu que je t'aide à faire ?", ""]

            
            nbrand = random.randrange(0,1)
            return str(formule+" "+cmp+" "+phrase[nbrand]) 
        
    def aurevoir(self, hour):
        if hour >= 0 and hour < 3:
            if self.vous:
                formule = "Bonne nuit,"
                cmp = self.genre + " " + self.user
                phrase = ["Reposez-vous bien.", "Passez une bonne nuit."]
            else:
                formule = "Au revoir,"
                cmp = self.user
                phrase = ["Bonne nuit.", "Bonne nuit, repose-toi bien."]
        else:
            if hour >= 3 and hour <= 6:
                if self.vous:
                    formule = "Bonne nuit,"
                    cmp = self.genre + " " + self.user
                    phrase = ["Essayez de vous reposer.", "Reposez-vous bien."]
                else:
                    formule = "Bonne nuit,"
                    cmp = self.user
                    phrase = ["Essaie de te reposer un peu.", "Repose-toi un peu."]
            else:
                if hour >= 6 and hour <= 10:
                    if self.vous:
                        formule = "Bonne journée,"
                        cmp = self.genre + " " + self.user
                        phrase = ["Passez une bonne journée.", "Profitez bien de votre journée."]
                    else:
                        formule = "Au revoir,"
                        cmp = self.user
                        phrase = ["Passe une bonne journée.", "Profite bien de ta journée."]
                else:
                    if hour >= 10 and hour <= 12:
                        if self.vous:
                            formule = "Au revoir,"
                            cmp = self.genre + " " + self.user
                            phrase = ["Passez une bonne fin de matinée.", "Profitez bien de votre fin de matinée."]
                        else:
                            formule = "Au revoir,"
                            cmp = self.user
                            phrase = ["Passe une bonne fin de matinée.", "Profite bien de ta fin de matinée."]
                    else:
                        if hour >= 13 and hour <= 14:
                            if self.vous:
                                formule = "Bonne après-midi,"
                                cmp = self.genre + " " + self.user
                                phrase = ["Profitez bien.", ""]
                            else:
                                formule = "Bonne après-midi,"
                                cmp = self.user
                                phrase = ["", "Profite bien."]
                        else:
                            if hour >= 15 and hour <= 18:
                                if self.vous:
                                    formule = "Au revoir,"
                                    cmp = self.genre + " " + self.user
                                    phrase = ["Passez une bonne fin d'après-midi.", "Profitez bien de votre fin de soirée."]
                                else:
                                    formule = "Au revoir,"
                                    cmp = self.user
                                    phrase = ["Profite bien de ta fin d'après-midi.", ""]
                            else:
                                if hour >= 18 and hour <= 20:
                                    if self.vous:
                                        formule = "Bonne soirée,"
                                        cmp = self.genre + " " + self.user
                                        phrase = ["Profitez bien ", "Reposez-vous bien ce soir."]
                                    else:
                                        formule = "Au revoir,"
                                        cmp = self.user
                                        phrase = ["Profite bien de ta soirée.", "Repose-toi bien ce soir."]
                                else:
                                    if hour >= 20 and hour <= 23:
                                        if self.vous:
                                            formule = "Bonne nuit,"
                                            cmp = self.genre + " " + self.user
                                            phrase = ["Dormez bien.", "Reposez-vous bien."]
                                        else:
                                            formule = "Bonne nuit,"
                                            cmp = self.user
                                            phrase = ["Dors bien.", "Repose-toi bien."]
                                    else:
                                        if hour >= 0 and hour < 3:
                                            if self.vous:
                                                formule = "Bonne nuit,"
                                                cmp = self.genre + " " + self.user
                                                phrase = ["Dormez bien, soyez en forme pour demain.",
                                                        "Reposez-vous bien pour demain."]
                                            else:
                                                formule = "Bonne nuit,"
                                                cmp = self.user
                                                phrase = ["Dors bien, sois en forme pour demain.",
                                                        "Repose-toi bien pour demain."]
                                        else:
                                            if self.vous:
                                                formule = "Au revoir,"
                                                cmp = self.genre + " " + self.user
                                                phrase = ["J'espère vous revoir bientôt.", ""]
                                            else:
                                                formule = "Au revoir,"
                                                cmp = self.user
                                                phrase = ["J'espère te revoir bientôt.", ""]
    
            
            nbrand = random.randrange(0,1)
            return str(formule+" "+cmp+" "+phrase[nbrand])