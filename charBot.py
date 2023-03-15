from random import randint
from emoDBCon import happy,sad

def printRS(rs):
    for i in rs:
        print(i[1])




print(happy)

greetings=["Hello","Hi","Howdy","Vanakkam","Namaskaram","salaam-malaekum"]
fareWell=["bye","good bye","see ya","farewell"]


emotions={"Happy":"Glad to hear that mate!why dont't you burst out some move!",
          "Sad":"That's awfull tell me,how can I help you?",
          "Restless":"Slowdown my friend rushing to your grave isn't gonna help you"
            }

def processEmotion(emoState):
    if emoState in emotions:
        return(emotions[emoState])
    else:
        return("Ain't gotta clue what to say mate.")

msg='''
            Welcome to EmoBot v1.0.0b 
    A Safe place to reveal your emotional state
                    and
    get some good adivise along the way
'''


def processEmotion(msg):
     msg=msg.capitalize()
     if msg in greetings:
        print(greetings[randint(0,len(greetings)-1)],"\nHow are you feeling today?")
     else:
        myList=msg.split()
        print(myList)
        for i in myList:
            i=i.capitalize()
            if i in happy:
                print(emotions["Happy"])
            elif i in sad:
                print(emotions["Sad"])


print(msg)
while True:
    msg=input(">")
    if msg in ["q","quit"] or msg in fareWell:
        print("Hope to see you again!")
        break
    else:
       processEmotion(msg)
