import json
import random
import requests
import time


# Loads required JSON data files
with open('data/outputCategories.json') as f:
    outputCategories = json.load(f)
with open('data/exercisesByLevel.json') as f:
    exercisesByLevel = json.load(f)
with open('data/howToSteps.json') as f:
    howTo = json.load(f)
with open('data/quotes.json') as f:
    quotes = json.load(f)
with open('data/anecdotes.json') as f:
    anecdotes = json.load(f)


# Asks the user various questions to get the required info
def JimAsk(category, name=''):
    if category == "ask for level" and name != '':
        print("JIM:", name + random.choice(outputCategories[category]))
    elif category == "ask to tell a joke" and name != '':
        print("JIM:", random.choice(outputCategories[category]) + ", " + name + "?") 
    elif "response for" in category and name != '':
        print("JIM:", random.choice(outputCategories[category]) + ", " + name + "!")
    elif category == "reveal plan" and name != '':
        print("JIM:", name + ", " + random.choice(outputCategories[category]))
    else:
        print("JIM:", random.choice(outputCategories[category]))


# Various outputs (formatted differently) depending on category input
def JimSay(category, name=''):
    if category[0] == "howTo":
        print("JIM: This is how you do the " + category[1] + " exercise: " + howTo[category[1]])
    elif category[0] == "quote":
        print("JIM:", random.choice(outputCategories["tell quote"]) + random.choice(quotes["quotes"]))
    elif category[0] == "anecdote":
        print("JIM:", random.choice(outputCategories["tell anecdote"]) + ", " + name + "! " + random.choice(anecdotes["anecdotes"]))
    elif category[0] == "filler":
        print("JIM:", random.choice(outputCategories["filler"]) + ", " + name + "!") 
    elif category[0] == "bye":
        print("JIM:", random.choice(outputCategories["say bye"])) 
    elif category[0] == "welcome":
        print("JIM:", random.choice(outputCategories["welcome"]) + ", " + name) 
    elif category[0] == "tell a joke":
        print("JIM:", random.choice(outputCategories["tell a joke"]))
        tellJoke("yes")
    else:
        print("JIM:", random.choice(outputCategories[category[0]]))
    

# Creates and outputs the personalized workout plan
def createWorkout(level, duration):
    exercises = random.sample(exercisesByLevel[level], 3)
    roundTime = duration//4
    warmAndCoolTime = roundTime//2
    breakTime = roundTime//4
    exerciseTime = (roundTime - breakTime)//3

    print("     Warm-up: " + str(warmAndCoolTime) + " minutes")
    print("     Do 3 rounds of:")
    for ex in exercises:
        print("        " + ex + ": " + str(exerciseTime) + " mins")
    print("        Short break: " + str(breakTime) + " mins")
    print("     Each round will be roughly " + str(roundTime) + " minutes long.")
    print("     Cool-down: " + str(warmAndCoolTime) + " minutes")


# Connects to API and tells a joke depending on user reply
def tellJoke(reply):
    if "no" in reply.lower():
        print("JIM: Okay, maybe next time!")
        return ''
    else:
        # Connect to Jokes API
        f = r"https://official-joke-api.appspot.com/random_joke"
        data = requests.get(f)
        tt = json.loads(data.text)
        #print(tt)

        print("JIM:",tt['setup'])         # setup
        time.sleep(3)
        print("JIM:",tt['punchline'])     # punchline
        time.sleep(2)
        return "Haha anyway... "