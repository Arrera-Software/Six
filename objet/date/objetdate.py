import datetime

class TriageDate :
    def heure(var):
        return str(var.time().hour)
    
    def minute(var):
        return str(var.time().minute)
    
    def second(var):
        return str(var.time().second)
    
    def jour(var):
        return str(var.day)

    def nomMois(var):
        var = int(var.month)
        match(var):
            case 1 :
                return "Janvier" 
            case 2 :
                return "Fevrier"
            case 3 :
                return "Mars"
            case 4 :
                return "Avril"
            case 5 :
                return "Mai"
            case 6 : 
                return "Juin"
            case 7 :
                return "Juillet"
            case 8 :
                return  "Aout"
            case 9 :
                return "Septembre"
            case 10 :
                return "Octobre"
            case 11 :
                return "Novembre"
            case 12 :
                return "Décembre"
    def numMois(var):
        return str(var.month)
    
    def annes(var):
        return str(var.year) 

class dateToday :
    def __init__(self):
        self.date= datetime.datetime.now()
        
    def heure(self):
        return TriageDate.heure(self.date)

    def minute(self):
        return TriageDate.minute(self.date)
    
    def second(self):
        return TriageDate.second(self.date)
    
    def jour(self):
        return TriageDate.jour(self.date)
    
    def moisSTR(self):
        return TriageDate.nomMois(self.date)
    
    def moisINT(self):
        return TriageDate.numMois(self.date)
    
    def annes(self):
        return TriageDate.annes(self.date) 
    
class dateTommorow :
    def __init__(self):
        self.date= datetime.datetime.now()- datetime.timedelta(days=1)
        
    def heure(self):
        return TriageDate.heure(self.date)

    def minute(self):
        return TriageDate.minute(self.date)
    
    def second(self):
        return TriageDate.second(self.date)
    
    def jour(self):
        return TriageDate.jour(self.date)
    
    def moisSTR(self):
        return TriageDate.nomMois(self.date)
    
    def moisINT(self):
        return TriageDate.numMois(self.date)
    
    def annes(self):
        return TriageDate.annes(self.date) 
    
    
class dateYesterday :
    def __init__(self):
        self.date= datetime.datetime.now() + datetime.timedelta(days=1)
        
    def heure(self):
        return TriageDate.heure(self.date)

    def minute(self):
        return TriageDate.minute(self.date)
    
    def second(self):
        return TriageDate.second(self.date)
    
    def jour(self):
        return TriageDate.jour(self.date)
    
    def moisSTR(self):
        return TriageDate.nomMois(self.date)
    
    def moisINT(self):
        return TriageDate.numMois(self.date)
    
    def annes(self):
        return TriageDate.annes(self.date) 