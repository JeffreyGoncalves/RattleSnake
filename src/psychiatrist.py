# Copyright : Morgan FEURTE and Jeffrey GONCALVES © 2018
# psychiatrist.py : Second mode, Eliza-like chatbot

import random
import utilities
import re

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

dream_keywords = ["dream", "dreams", "dreaming", "night", "sleeping", "bed", "nightmare", "fantasy",
                  "oniric", "lucid", "woke"]

animals_keywords = ["animal", "animals", "pet", "pets", "dog", "dogs", "cat", "cats", "doggo",
                    "doge", "alpaca", "albatros", "rat", "mouse", "feed", "elephant", "giraffe",
                    "hamster", "pig", "horse", "pony", "monkey", "cow", "duck", "deer",
                    "rabbit", "lion", "bear"]

negation_keywords = ["not", "don't", "doesn't", "didn't", "isn't", "aren't", "wasn't", "weren't",
                     "haven't", "hasn't", "hadn't", "won't", "wouldn't", "can't", "cannot", "shouldn't"]

keywords_occurence = dict()

answers_by_category = [
    ["family",
     ["Do you have issues with your family?",
      "It's important to be able to rely on your family!",
      "Do you feel close to your family?",
      "Would you like to have children?",
      "Do you often see your family?",
      "Your mother would be proud of you!"]],

    ["depression",
     ["Do you feel depressed right now?",
      "Suicide is never the solution!",
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
      "\"Forgive your enemies\" -Lao Tseu(fake quote)"]],

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


def execute(vaporwave):
    last_answer = ""

    while(1):
        # Read input from user
        message = input("ＹＯＵ >>  ")
        # Separate commas, dots, parenthesis etc. from words with spaces
        message = re.sub('((?<![A-Z])[\.\?\!\:\,\;\"\(\)]+)', r" \1 ", message)

        # Check for politeness formulas
        # if any are found continue_answered_leave will have value "answered" (1)
        # if none are found, it will have value "continue" (0)
        # if we find a formula indicating that the user wants to leave >> "leave" (2)
        answer, continue_answered_leave = check_politeness_formulas(message, last_answer)
        if(continue_answered_leave == 1):
            last_answer = answer
        if(continue_answered_leave == 0):
        	# If no politeness formulas are found, we count the number of occurences of our
        	# different subjects then compute an appropriate answer
            count_word_occurences(message)
            answer = compute_answer(last_answer)
            last_answer = answer
        # Finally we print the answer and leave if we found any leaving intentions
        utilities.print_message(answer, 2, vaporwave)
        if(continue_answered_leave == 2):
            break


def count_word_occurences(input):
# Counting the number of occurences of each subjects and put them in the dictionnary "keywords_occurence"
    tokens = input.lower().split()
    keywords_occurence["family"] = 0
    keywords_occurence["depression"] = 0
    keywords_occurence["like"] = 0
    keywords_occurence["dislike"] = 0
    keywords_occurence["dream"] = 0
    keywords_occurence["animals"] = 0
    keywords_occurence["misunderstanding"] = 0

    for index, tkn in enumerate(tokens):
        if(tokens[index-1] not in negation_keywords):
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

    # If no keywords are found, we select "misunderstanding" as subject             
    if(keywords_occurence["family"] == 0 and keywords_occurence["depression"] == 0 and keywords_occurence["like"] == 0
        and keywords_occurence["dislike"] == 0 and keywords_occurence["dream"] == 0 and keywords_occurence["animals"] == 0):
        keywords_occurence["misunderstanding"] = 1

def compute_answer(last_answer):
# Return an answer to the subject of the message
    subjects = ["family", "depression", "like",
            "dislike", "dream", "misunderstanding", "animals"]
    max = 0
    sub = ""
    i = 0
    # Calculate which subject is the most represented
    for i in range(len(subjects)):
        if(max < keywords_occurence[subjects[i]]):
            max = keywords_occurence[subjects[i]]
            sub = subjects[i]

    # Choose a random answer different from the previous one in this subject
    toReturn = random.choice(answers_by_category[utilities.getIndex(sub, "psychiatrist")][1])
    while(toReturn == last_answer):
        toReturn = random.choice(answers_by_category[utilities.getIndex(sub, "psychiatrist")][1])
    return toReturn

def check_politeness_formulas(message, last_answer):
# Return an answer to a politeness formula and whether or not it is useful to continue parsing
    introduction_formulas = ["hi", "hello", "good morning", "good afternoon"]
    thanking_formulas = ["thank you", "thanks", "thank you very much", "cheers"]
    leaving_formulas = ["goodbye", "bye", "see you", "see you.", "goodbye.", "goodbye!", "bye!"]
    holidays_formulas = ["happy new year", "merry christmas",
                     "happy halloween", "happy easter", "happy birthday"]

    message = message.lower()
    answer = ""
    continue_answered_leave = 0

    if(message in introduction_formulas):
        answers = ["Hi!", "Hello to you.", "Great to see you:)",
               "Pleasure to meet you, I'm Dr.MoG-BOT!"]

        if(last_answer in answers):
            answers.remove(last_answer)
        answer = random.choice(answers)
        continue_answered_leave = 1

    elif(message in thanking_formulas):
        answers = ["You're welcome!", "My patients often say that.",
               "It's a pleasure to see you appreciate my hard work!"]

        if(last_answer in answers):
            answers.remove(last_answer)
        answer = random.choice(answers)
        continue_answered_leave = 1

    elif(message in leaving_formulas):
        answers = ["Goodbye!", "See you soon.", "Bye :)", "It's been nice analyzing you!"]

        if(last_answer in answers):
            answers.remove(last_answer)
        answer = random.choice(answers)
        continue_answered_leave = 2

    elif(message in holidays_formulas):
        answers = holidays_formulas

        if(last_answer in answers):
            answers.remove(last_answer)
        answer = random.choice(answers)
        continue_answered_leave = 1

    return answer, continue_answered_leave