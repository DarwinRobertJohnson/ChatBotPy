
class speakerIdentifier:

    def __init__(self,command):
        self.command=command

    def idSpeaker(self):
        sent=(self.command).split()
        for i in sent:
            i=i.capitalize()
            if i in ['I','Me']:
                return "first-person"

si=speakerIdentifier("Feeling like shit he  have been lately")
print(si.idSpeaker())
