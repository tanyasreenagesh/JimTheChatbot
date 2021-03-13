import json

# create list of exercises
with open('data/howToSteps.json') as f:
    outputCategories = json.load(f)
exercisesList = outputCategories.keys()

def getName(reply):
    replyList = reply.split()
    if len(replyList) == 1:
        return reply
    elif "my name is" in reply.lower():
        return replyList[replyList.index('name')+2]
    elif "i am" in reply.lower():
        return replyList[replyList.index('am')+1]
    elif "i'm" in reply.lower():
        return replyList[replyList.index("I'm")+1]

def getLevel(reply):
    reply = reply.lower()
    if 'easy' in reply:
        return 'easy'
    elif 'medium' in reply:
        return 'medium'
    elif 'hard' in reply:
        return 'hard'
    else:
        return -1

def getDuration(reply):
    replyList = reply.split()
    if len(replyList) == 1:
        return reply
    elif "minutes" in reply.lower():
        return replyList[replyList.index('minutes')-1]
    elif "mins" in reply.lower():
        return replyList[replyList.index('mins')-1]
    else:
        return -1

def resetFlow(flow):
    for i in range(2,len(flow)):
        flow[i] = False


# Returns output category -> [category, exerciseName(opt.)]
def parseInput(reply):
    reply = reply.lower()

    # category: howTo
    if "how to" in reply or "how do i" in reply:
        for ex in exercisesList:
            if ex.lower() in reply:
                return ["howTo", ex]
    
    # category: welcome
    if "thank" in reply:
        return ["welcome"]

    # category: joke
    if "joke" in reply or "fun" in reply:
        return ["tell a joke"]

    # category: anecdote
    if "story" in reply or "anecdote" in reply:
        return ["anecdote"]
    
    # category: quote
    if "quote" in reply or "motivat" in reply or "inspir" in reply:
        return ["quote"]
    
    # category: bye
    if "bye" in reply:
        return ["bye"]
