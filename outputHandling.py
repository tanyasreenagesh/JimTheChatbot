import json
import random
import requests
import time

with open('outputCategories.json') as f:
    outputCategories = json.load(f)


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

def JimSay(category, name=''):
    if category[0] == "howTo":
        with open('howToSteps.json') as f:
            howTo = json.load(f)
        print("JIM: This is how you do the " + category[1] + " exercise: " + howTo[category[1]])
    elif category[0] == "quote":
        with open('quotes.json') as f:
            quotes = json.load(f)
        print("JIM:", random.choice(outputCategories["tell quote"]) + random.choice(quotes["quotes"]))
    elif category[0] == "anecdote":
        with open('anecdotes.json') as f:
            anecdotes = json.load(f)
        print("JIM:", random.choice(outputCategories["tell anecdote"]) + ", " + name + "! " + random.choice(anecdotes["anecdotes"]))
    elif category[0] == "filler":
        print("JIM:", random.choice(outputCategories["filler"]) + ", " + name + "!") 
    elif category[0] == "bye":
        print("JIM:", random.choice(outputCategories["bye"])) 
    

def createWorkout(level, duration):
    return "INSERT HERE: Awesome plan for " + duration + " mins long, " + level + " level workout."

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