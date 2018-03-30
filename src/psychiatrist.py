# Copyright : Morgan FEUTRE and Jeffrey GONCALVES 2018
# Psychiatrist.py : the chatbot adopt a psychiatrist's behaviour

import random
import utilities

family_keywords = ["family", "parent", "parents", "mom", "mother", "dad", "father",
                   "child", "children", "kid", "kids", "son", "daughter", "uncle",
                   "aunt", "grandmother", "grandfather", "ancestor", "husband",
                   "wife"]

depression_keywords = ["depression", "sad", "sick", "unhappy", "rejected", "miserable",
                       "down", "awful", "wrecked", "depressed", "oppressed", "desperation",
                       "worries", "sadness", "sickness", "nervous", "suicide", "anxiety"]

like_keywords = ["love", "like", "appreciate", "affection", "respect", "enjoy", "prefer",
                 "adore", "admire"]

dislike_keywords = ["dislike", "hate", "resent", "detest"]

dream_keywords = ["dream", "dreaming", "night", "sleeping", "bed", "nightmare", "fantasy",
                  "oniric", "lucid", "woke"]

animals_keywords = ["animal", "animals", "pet", "pets", "dog", "dogs", "cat", "cats", "doggo",
                    "doge", "alpaca", "albatros", "rat", "mouse", "feed", "elephant", "giraffe",
                    "hamster", "pig", "horse", "pony", "monkey", "cow", "duck", "deer",
                    "rabbit", "lion"]

negation_keywords = ["not", "don't", "doesn't", "didn't", "isn't", "aren't", "wasn't", "weren't",
                     "haven't", "hasn't", "hadn't", "won't", "wouldn't", "can't", "cannot", "shouldn't"]

keywords_occurence = dict()

answers_by_category = [
    ["family",
     ["Do you have issues with your family?",
      "It's important to be able to rely on your family!",
      "Do you feel close to your {1}?",
      "Would you like to have children?",
      "Do you often see your family?",
      "Your mother would be proud of you !"]],

    ["depression",
     ["Do you feel depressed right now ?",
      "Suicide is never the solution !",
      "The first step to feeling good is to stop feeling bad.",
      "After the rain, comes the sun.",
      "The world is cruel, it hurts me to see someone as amazing as you are in pain!",
      "The highway to happiness is steep but beautiful!"]],

    ["like",
     ["Tell me more about things you like.",
      "Does your interest in this subject reflect your personnality?",
      "You seem very passionate about that.",
      "Liking something to the fullest is a gift of life!",
      "It is interesting that you appreciate this."]],

    ["dislike",
     ["Why do you hate this?",
      "What created your dislike for this matter?",
      "Hate is to the soul what a drill is to the wood.",
      "\"Forgive your enemies\" -Lao Tseu (fake news)"]],

    ["dream",
     ["Do you dream often?",
      "What was your last dream about?",
      "In my last dream, I was a polar bear, what about you?",
      "Dreaming during the day is the mark of great people.",
      "Tell me about your dreams!",
      "Waking up during a dream hurts the soul more than a chocolate shortage at the mall."]],

    ["misunderstanding",
     ["What would you want to add about this?",
      "It is very interesting that you think that.",
      "I see.",
      "What comes to your mind when you say this?",
      "And what does that tell about you?",
      "Interesting.",
      "Beep boop biiiiiiip !!!",
      "Why would you say that?",
      "Do you truly believe in what you just said?",
      "What do you think about the percentage of aluminium in watermelons?"]],

    ["animals",
     ["You know, your love for animals make you a great person!",
      "Who does not like pets?",
      "Do you like animals?",
      "\"Woof woof\", the dog said, while his master was opening the door.",
      "A cat picture a day keeps the doctor away."]]
]

last_backchannel = ""


def execute():
    
    while(1):
        # Read input from user
        message = input("YOU :  ")

        if(message == "exit"):
            print("Have a nice day !")
            break
        else:
            reflect(message)
            answer = analyse()
            last_backchannel = answer
            utilities.print_message(answer, 2)
    return


def reflect(input):
    # spliting the input and beginning of the count of KW
    tokens = input.lower().split()
    keywords_occurence["family"] = 0
    keywords_occurence["depression"] = 0
    keywords_occurence["like"] = 0
    keywords_occurence["dislike"] = 0
    keywords_occurence["dream"] = 0
    keywords_occurence["animal"] = 0

    for tkn in enumerate(tokens):
        if(tkn in family_keywords):
            keywords_occurence["family"] += 1
        elif(tkn in depression_keywords):
            keywords_occurence["depression"] += 1
        elif(tkn in like_keywords):
            keywords_occurence["like"] += 1
        elif(tkn in dislike_keywords):
            keywords_occurence["dislike"] += 1
        elif(tkn in dream_keywords):
            keywords_occurence["dream"] += 1
        elif(tkn in animals_keywords):
            keywords_occurence["animals"] += 1
        elif (tkn in negation_keywords):
            next(tokens, None)
            continue

    if(keywords_occurence["family"] == 0 and keywords_occurence["depression"] == 0 and keywords_occurence["like"] == 0 
      and keywords_occurence["dislike"] == 0 and keywords_occurence["dream"] == 0 and keywords_occurence["animal"] == 0):
        keywords_occurence["misunderstanding"] = 1

# check negation devant les mots et would devant like

def analyse():

  subjects = ["family", "depression", "like", "dislike", "dream","misunderstanding","animals"]
  max = 0
  sub = ""
  i = 0
  for i in range(len(subjects)):
    if(max < keywords_occurence[subjects[i]]):
      max = keywords_occurence[subjects[i]]
      sub = subjects[i]
  toReturn = random.choice(answers_by_category[getIndice(sub)][1])
  while(toReturn == last_backchannel):
    toReturn = random.choice(answers_by_category[getIndice(sub)][1])
  return toReturn

def getIndice(sub):
    default = 5
    subjects = ["family", "depression", "like", "dislike", "dream","misunderstanding","animals"]
    i=0
    for i in range(len(subjects)-1):
        if(subjects[i] == sub):
            return i 
    return default #should never happen

