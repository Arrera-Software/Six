import subprocess

def openSoftware(name):
    name = str(name)
    subprocess.Popen(["cmd", "/c", "start", name])
    
def ouvertureAide():
    openSoftware("raccourci/index.html.lnk")