from commandParser import cp



#the class that gets a response to be displayed
class emotion_handler:
    def __init__(self):
        self.emotions={
                "happy":"thats great to hear",
                "sad":"thats awful tell me everything",
                "bored":"that is not good why dont you do one of your hobbies",
                "unid":"not parsable command"
                }

    def getEmotionResponse(self,command):
        if command in self.emotions:
            return self.emotions[command]



#the class that gets the user's input
class user_interface:

    def __init__(self,command=" "):
        self.command=command
        self.emo_handler=emotion_handler()

    def process(self,command):
         response=cp.parseCommand(self.command)                  #function call to get emotion state
         print((self.emo_handler).getEmotionResponse(response))  #printing the adequate response


    def getUserCommand(self):
        while self.command not in ["q","quit"]:
            self.command=input(">")
            if self.command in ["q","quit"]:
                break
            self.process(self.command)

    def showUserCommand(self):
        print(self.command)

#object creation and function call to ui
ui=user_interface()
ui.getUserCommand()

