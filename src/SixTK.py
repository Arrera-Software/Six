from setting.arreraAssistantSetting import *

class sixTk :
    def __init__(self):
        self.para = ArreraSettingAssistant("setting/configSetting.json","configNeuron.json","sixConfig.json","FileUser/configUser.json") 
        
    def activePara(self):
        self.screenPara = Tk()
        self.para.windows(self.screenPara)
        self.para.passageFonctionQuitter(self.fncQuit)
        self.para.mainView()
        self.screenPara.mainloop()
    
    def fncQuit(self):
        self.screenPara.destroy()