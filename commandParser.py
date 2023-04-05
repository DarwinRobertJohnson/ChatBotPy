from dbHandler import Happy,Sad


class commandParser:
    def __init__(self):
        self.command=""

    def parseCommand(self,command):
        words=(command).split()
        print(words)
        for i in words:
            i=i.capitalize()
            if i in Happy:
                return "happy"
            elif i in Sad:
                return "sad"
        
        return "unid"

cp=commandParser()
print(cp.parseCommand("I am feeling happy"))
