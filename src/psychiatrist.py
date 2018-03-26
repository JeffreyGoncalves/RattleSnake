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
					"doge","alpaca", "albatros", "rat", "mouse", "feed", "elephant", "giraffe",
					"hamster", "pig", "horse", "pony", "monkey", "cow", "duck", "deer",
					"rabbit", "lion"]

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


def execute(mode):
	last_backchannel = ""
	while(1):
		# Read input from user
		message = input("YOU :  ")
		
		if(message == "exit"):
			print("Have a nice day !")
			break
		else:
			answer = be_or_not_to_be()
			last_backchannel = answer
			utilities.print_message(answer,mode)
	return

def be_or_not_to_be():

    print("Take a sit and talk me about yourself")


# check negation devant les mots et would devant like