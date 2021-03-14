# chatbot.py - Framework of the chatbot that combines input and output handling.

# 0: intro/get name of user
# 1: ask to tell joke 
# 2: ask difficulty level
# 3: ask duration of workout
# 4: create workout

from inputHandling import *
from outputHandling import *

flow = [False, False, False, False, False]
name = ''
diffLevel = ''
unknownCount = 0

def chat():
    global flow, name, diffLevel, unknownCount

    while True:
        # Greets the user and stores their name
        if not flow[0]:
            JimAsk("greetings+intro")
            reply = input("YOU: ")
            name = getName(reply)
            flow[0] = True

        # Asks to tell a joke
        elif not flow[1]:
            JimAsk("ask to tell a joke", name)
            reply = input("YOU: ")
            saidJoke = tellJoke(reply)
            flow[1] = True
        
        # Gets and parses the input for workout difficulty level
        elif not flow[2]:
            JimAsk("ask for level", saidJoke)
            reply = input("YOU: ")
            diffLevel = getLevel(reply)
            if diffLevel == -1:
                JimAsk("try again")
            else:
                JimAsk("response for " + diffLevel, name)
                flow[2] = True
        
        # Gets and parses the input for workout duration
        elif not flow[3]:
            JimAsk("ask for duration")
            reply = input("YOU: ")
            duration = getDuration(reply)
            if duration == -1 or not duration.isnumeric():
                JimAsk("try again")
            else:
                flow[3] = True
        
        # Creates and displays the personalized workout
        elif not flow[4]:
            JimAsk("reveal plan", name)
            createWorkout(diffLevel, int(duration))

            # Check if workout needs to be changed
            JimAsk("change workout")
            reply = input("YOU: ")
            while "no" not in reply.lower():
                createWorkout(diffLevel, int(duration))
                JimAsk("change workout")
                reply = input("YOU: ")
            
            # Gateway to casual conversation
            print("JIM: Awesome, happy to help, " + name + "!")      
            print("JIM: Now, I can try answering any questions you may have or... we can just chat about life!")
            flow[4] = True
                
        # Casual (free) conversation
        else:
            reply = input("YOU: ")
            outputCategory = parseInput(reply)

            # Output the category for parsed input
            if outputCategory != None:
                JimSay(outputCategory, name)
                if outputCategory[0] == "bye":
                    break
            
            # Unknown (un-parseable) user input
            else:
                unknownCount += 1
                if unknownCount % 3 == 0:
                    JimAsk("try again")
                outputTypes = ["filler", "tell a joke", "quote", "anecdote"]
                temp = random.choice(outputTypes)
                print("Temp: ", temp)
                JimSay([temp])


chat()