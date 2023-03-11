from random import randint

greetings=["Hello","Hi","Howdy","Vanakkam","Namaskaram","salaam-malaekum"]
fareWell=["bye","good bye","see ya","farewell"]


emotions={"Happy":'Glade to hear that mate!',
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

#print("happy" in emotions)
print(msg)
while True:
    msg=input(">")
    if msg in ["q","quit"] or msg in fareWell:
        print("Hope to see you again!")
        break
    else:
        msg=msg.capitalize()
        if msg in greetings:
            print(greetings[randint(0,len(greetings)-1)])
        else:
              myList=msg.split()
              print(myList)
              for i in myList:
                  i=i.capitalize()
                  if i in emotions:
                    print(processEmotion(i))