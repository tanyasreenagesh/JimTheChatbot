# Chatbot

from inputHandling import *
from outputHandling import *

# 0: intro/get name of user
# 1: ask to tell joke 
# 2: ask difficulty level
# 3: ask duration of workout
# 4: create workout
#flow = [False, False, False, False, False]
flow = [True, True, True, True, True]
name = ''
diffLevel = ''
unknownCount = 0

def chat():
    global flow, name, diffLevel, unknownCount

    while True:
        if not flow[0]:
            JimAsk("greetings+intro")
            reply = input("YOU: ")
            name = getName(reply)
            flow[0] = True

        elif not flow[1]:
            JimAsk("ask to tell a joke", name)
            reply = input("YOU: ")
            saidJoke = tellJoke(reply)
            flow[1] = True
        
        elif not flow[2]:
            JimAsk("ask for level", saidJoke)
            reply = input("YOU: ")
            diffLevel = getLevel(reply)
            if diffLevel == -1:
                JimAsk("try again")
            else:
                JimAsk("response for " + diffLevel, name)
                flow[2] = True
        
        elif not flow[3]:
            JimAsk("ask for duration")
            reply = input("YOU: ")
            duration = getDuration(reply)
            if duration == -1:
                JimAsk("try again")
            else:
                flow[3] = True
            
        elif not flow[4]:
            JimAsk("reveal plan", name)
            print("JIM:", createWorkout(diffLevel, duration))

            # Check if workout needs to be changed
            JimAsk("change workout")
            reply = input("YOU: ")
            while "no" not in reply.lower():
                print("JIM:", createWorkout(diffLevel, duration))
                JimAsk("change workout")
                reply = input("YOU: ")
                
            print("JIM: Awesome, happy to help, " + name + "!")      # continue conversation instead
            print("JIM: Now, I can try answering any questions you may have or... we can just chat about life!")
            flow[4] = True
                
        # Casual conversation
        else:
            reply = input("YOU: ")
            outputCategory = parseInput(reply)
            if outputCategory != None:
                JimSay(outputCategory)
            else:
                unknownCount += 1
                if unknownCount % 3 == 0:
                    JimAsk("try again")
                elif unknownCount % 5 == 0:
                    JimAsk("filler")
                elif unknownCount % 2 == 0:
                    JimSay(["quote"])
                else:
                    JimSay(["anecdote"], name)


chat()